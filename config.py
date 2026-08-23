# 项目配置文件
# 统一管理路径和参数

import os

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# 数据路径配置
DATA_CONFIG = {
    # 原始数据路径
    'raw_data_path': 'file:///home/zhangtianshuo/yelp_data/yelp_academic_dataset_business.json',
    # 预处理输出路径
    'processed_data_path': '/home/zhangtianshuo/yelp_output/business_etl',
    # 本地数据目录
    'local_data_dir': os.path.join(PROJECT_ROOT, 'data'),
    # 本地输出目录
    'local_output_dir': os.path.join(PROJECT_ROOT, 'output')
}

# 分析配置
ANALYSIS_CONFIG = {
    # 异常值过滤阈值
    'outlier_threshold': 10,
    # 属性分析列表
    'attributes_to_analyze': ['RestaurantsTakeout'],
    # 分析结果输出路径
    'analysis_output_path': '/home/zhangtianshuo/yelp_output/analysis'
}

# 可视化配置
VISUAL_CONFIG = {
    # 图表保存路径
    'chart_save_path': os.path.join(PROJECT_ROOT, 'output', 'charts'),
    # 可视化主题
    'theme': 'default'
}

# Spark配置
SPARK_CONFIG = {
    'app_name': 'Yelp Business Analysis',
    'master': 'local[*]',
    'config': {
        'spark.executor.memory': '4g',
        'spark.driver.memory': '4g'
    }
}
