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

def attribute_score(spark, attribute, output_path):
    """分析商家特定属性（如外卖服务）与星级的关系"""
    att = spark.sql(f"SELECT attributes.{attribute} as {attribute}, category, stars FROM for_att").dropna()
    att.createOrReplaceTempView("att")
    att_group = spark.sql(f"SELECT {attribute}, AVG(stars) AS stars FROM att GROUP BY {attribute} ORDER BY stars")
    att_group.show()    
    att_group.write.json(f"file://{output_path}/{attribute}", mode='overwrite')
    print(f"✓ 属性分析结果已保存到 {output_path}/{attribute}")

def analysis(spark, data_path, output_path):
    """数据分析主函数"""
    # 加载预处理后的Parquet数据
    business = spark.read.parquet(data_path).cache()
    business.createOrReplaceTempView("business")
    print(f"✓ 加载了 {business.count()} 条记录")

    # 拆分categories为单行，清理类别名称空格
    part_business = spark.sql("SELECT state, city, stars, review_count, explode(categories) AS category FROM business").cache()
    part_business.createOrReplaceTempView('part_business_1')
    part_business = spark.sql("SELECT state, city, stars, review_count, REPLACE(category, ' ','') as new_category FROM part_business_1")
    part_business.createOrReplaceTempView('part_business')

    # 1. 统计所有不同的商业类别数量
    print("## All distinct categories")
    all_categories = spark.sql("SELECT business_id, explode(categories) AS category FROM business")
    all_categories.createOrReplaceTempView('all_categories')
    distinct = spark.sql("SELECT COUNT(DISTINCT(new_category)) FROM part_business")
    distinct.show()

    # 2. 统计数量最多的10个商业类别
    print("## Top 10 business categories")
    top_cat = spark.sql("SELECT new_category, COUNT(*) as freq FROM part_business GROUP BY new_category ORDER BY freq DESC")
    top_cat.show(10)   
    top_cat.write.json(f"file://{output_path}/top_category", mode='overwrite')
    print(f"✓ 数量最多的10个商业类别已保存")

    # 3. 统计每个城市各商业类别的商家数量
    print("## Top business categories - in every city")
    top_cat_city = spark.sql("SELECT city, new_category, COUNT(*) as freq FROM part_business GROUP BY city, new_category ORDER BY freq DESC")
    top_cat_city.show()  
    top_cat_city.write.json(f"file://{output_path}/top_category_city", mode='overwrite')
    print(f"✓ 每个城市各商业类别的商家数量已保存")

    # 4. 统计商家数量最多的10个城市
    print("## Cities with most businesses")
    bus_city = spark.sql("SELECT city, COUNT(business_id) as no_of_bus FROM business GROUP BY city ORDER BY no_of_bus DESC")
    bus_city.show(10)   
    bus_city.write.json(f"file://{output_path}/top_business_city", mode='overwrite')
    print(f"✓ 商家数量最多的10个城市已保存")

    # 5. 统计平均评论数最多的10个商业类别
    print("## Average review count by category")
    avg_city = spark.sql(
        "SELECT new_category, AVG(review_count) as avg_review_count FROM part_business GROUP BY new_category ORDER BY avg_review_count DESC")
    avg_city.show()  
    avg_city.write.json(f"file://{output_path}/average_review_category", mode='overwrite')
    print(f"✓ 平均评论数最多的10个商业类别已保存")

    # 6. 统计平均星级最高的10个商业类别
    print("## Average stars by category")
    avg_state = spark.sql(
        "SELECT new_category, AVG(stars) as avg_stars FROM part_business GROUP BY new_category ORDER BY avg_stars DESC")
    avg_state.show()   
    avg_state.write.json(f"file://{output_path}/average_stars_category", mode='overwrite')
    print(f"✓ 平均星级最高的10个商业类别已保存")

    # 7. 分析商家属性与星级的关系
    print("## Data based on Attribute")
    for_att = spark.sql("SELECT attributes, stars, explode(categories) AS category FROM business")
    for_att.createOrReplaceTempView("for_att")
    
    for attribute in ANALYSIS_CONFIG['attributes_to_analyze']:
        attribute_score(spark, attribute, output_path)

if __name__ == "__main__":
    # 使用配置文件中的路径
    business_data_path = f"file://{DATA_CONFIG['processed_data_path']}"
    output_base_path = ANALYSIS_CONFIG['analysis_output_path']

    print("=" * 70)
    print("Yelp数据分析")
    print("=" * 70)
    print(f"Input: {business_data_path}")
    print(f"Output: {output_base_path}")
    print()

    # 创建输出目录
    os.makedirs(output_base_path, exist_ok=True)

    # 创建Spark会话
    spark = create_spark_session()
    print("✓ Spark会话已创建")

    # 调用数据分析函数
    analysis(spark, business_data_path, output_base_path)

    spark.stop()
    print("\n✓ 数据分析完成！")
    print("=" * 70)

