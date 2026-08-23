from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_CONFIG, ANALYSIS_CONFIG, SPARK_CONFIG

def create_spark_session():
    """创建Spark会话"""
    builder = SparkSession.builder \
        .appName(SPARK_CONFIG['app_name']) \
        .master(SPARK_CONFIG['master'])
    
    # 添加配置
    for key, value in SPARK_CONFIG['config'].items():
        builder = builder.config(key, value)
    
    return builder.getOrCreate()

def data_process(raw_data_path, output_path, outlier_threshold=10):
    """数据预处理函数"""
    spark = create_spark_session()
    # 加载JSON数据
    business = spark.read.json(raw_data_path)
    print(f"✓ 加载了 {business.count()} 条记录")
    
    # 拆分categories字段为数组，过滤空城市值并删除缺失值行
    split_col = f.split(business['categories'], ',')
    business = business.withColumn("categories", split_col).filter(business["city"] != "").dropna()
    business.createOrReplaceTempView("business")
    print(f"✓ 清洗后: {business.count()} 条记录")

    # 筛选核心字段并缓存
    b_etl = spark.sql("SELECT business_id, name, city, state, latitude, longitude, stars, review_count, is_open, categories, attributes FROM business").cache()
    b_etl.createOrReplaceTempView("b_etl")
    
    # 计算每个商家到所在州平均经纬度的欧式距离，识别异常值
    outlier = spark.sql(
        "SELECT b1.business_id, SQRT(POWER(b1.latitude - b2.avg_lat, 2) + POWER(b1.longitude - b2.avg_long, 2)) \
        as dist FROM b_etl b1 INNER JOIN (SELECT state, AVG(latitude) as avg_lat, AVG(longitude) as avg_long \
        FROM b_etl GROUP BY state) b2 ON b1.state = b2.state ORDER BY dist DESC")
    outlier.createOrReplaceTempView("outlier")
    
    # 过滤异常值，保存清洗后的数据
    joined = spark.sql(f"SELECT b.* FROM b_etl b INNER JOIN outlier o ON b.business_id = o.business_id WHERE o.dist<{outlier_threshold}")
    final_count = joined.count()
    print(f"✓ 过滤后: {final_count} 条记录")
    
    joined.write.parquet(f"file://{output_path}", mode="overwrite")
    print(f"✓ 数据已保存到 {output_path}")
    
    spark.stop()

if __name__ == "__main__":
    # 使用配置文件中的路径
    raw_hdfs_path = DATA_CONFIG['raw_data_path']
    output_path = DATA_CONFIG['processed_data_path']
    outlier_threshold = ANALYSIS_CONFIG['outlier_threshold']

    print("=" * 70)
    print("Yelp数据预处理")
    print("=" * 70)
    print(f"Input: {raw_hdfs_path}")
    print(f"Output: {output_path}")
    print(f"Outlier Threshold: {outlier_threshold}")
    print()

    print("✓ Spark会话已创建")
    print("加载JSON数据...")
    
    # 调用数据处理函数
    data_process(raw_hdfs_path, output_path, outlier_threshold)
    
    print()
    print("=" * 70)
    print("✓ 数据预处理完成！")
    print("=" * 70)

