import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_CONFIG, ANALYSIS_CONFIG, VISUAL_CONFIG

def read_json(file_path):
    """读取Spark输出的JSON格式分析结果"""
    json_path_names = os.listdir(file_path)
    data = []
    for idx in range(len(json_path_names)):
        json_path = os.path.join(file_path, json_path_names[idx])
        if json_path.endswith('.json'):
            with open(json_path) as f:
                for line in f:
                    data.append(json.loads(line))
    return data

def save_chart(fig, chart_name):
    """保存图表到指定路径"""
    chart_save_path = VISUAL_CONFIG['chart_save_path']
    # 创建图表保存目录
    os.makedirs(chart_save_path, exist_ok=True)
    # 保存图表
    fig.savefig(os.path.join(chart_save_path, f'{chart_name}.png'), dpi=300, bbox_inches='tight')
    print(f"✓ 图表已保存到 {os.path.join(chart_save_path, f'{chart_name}.png')}")

def visualize_top_categories(data, top_n=10):
    """可视化数量最多的商业类别"""
    # 按频率排序
    data.sort(key=lambda x: x['freq'], reverse=True)
    
    # 提取前top_n个类别
    categories = [item['new_category'] for item in data[:top_n]]
    frequencies = [item['freq'] for item in data[:top_n]]
    
    # 创建横向柱状图
    plt.figure(figsize=(10, 6))
    plt.barh(categories, frequencies, color='skyblue')
    plt.title('Top 10 Business Categories', size=16)
    plt.xlabel('Number of Businesses', size=12, color='Black')
    plt.ylabel('Category', size=12, color='Black')
    plt.tight_layout()
    
    # 保存图表
    save_chart(plt, 'top_10_categories')
    
    # 展示图表
    plt.show()

def visualize_average_stars(data, top_n=10):
    """可视化平均星级最高的商业类别"""
    # 按平均星级排序
    data.sort(key=lambda x: x['avg_stars'], reverse=True)
    
    # 提取前top_n个类别
    categories = [item['new_category'] for item in data[:top_n]]
    avg_stars = [item['avg_stars'] for item in data[:top_n]]
    
    # 创建柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(categories, avg_stars, color='lightgreen')
    plt.title('Top 10 Categories by Average Stars', size=16)
    plt.xlabel('Category', size=12, color='Black')
    plt.ylabel('Average Stars', size=12, color='Black')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # 保存图表
    save_chart(plt, 'top_10_categories_by_stars')
    
    # 展示图表
    plt.show()

def visualize_top_cities(data, top_n=10):
    """可视化商家数量最多的城市"""
    # 按商家数量排序
    data.sort(key=lambda x: x['no_of_bus'], reverse=True)
    
    # 提取前top_n个城市
    cities = [item['city'] for item in data[:top_n]]
    business_counts = [item['no_of_bus'] for item in data[:top_n]]
    
    # 创建横向柱状图
    plt.figure(figsize=(10, 6))
    plt.barh(cities, business_counts, color='salmon')
    plt.title('Top 10 Cities with Most Businesses', size=16)
    plt.xlabel('Number of Businesses', size=12, color='Black')
    plt.ylabel('City', size=12, color='Black')
    plt.tight_layout()
    
    # 保存图表
    save_chart(plt, 'top_10_cities')
    
    # 展示图表
    plt.show()

if __name__ == '__main__':
    # 分析结果路径
    analysis_output_path = ANALYSIS_CONFIG['analysis_output_path']
    
    print("=" * 70)
    print("Yelp数据分析可视化")
    print("=" * 70)
    print(f"Analysis Data Path: {analysis_output_path}")
    print(f"Chart Save Path: {VISUAL_CONFIG['chart_save_path']}")
    print()
    
    try:
        # 读取各维度分析结果
        top_category_list = read_json(os.path.join(analysis_output_path, 'top_category'))
        print("✓ 读取了类别数据")
        
        ave_stars_category_list = read_json(os.path.join(analysis_output_path, 'average_stars_category'))
        print("✓ 读取了星级数据")
        
        top_business_city_list = read_json(os.path.join(analysis_output_path, 'top_business_city'))
        print("✓ 读取了城市数据")
        
        # 可视化数量最多的10个商业类别
        print("\n1. 可视化数量最多的10个商业类别...")
        visualize_top_categories(top_category_list)
        
        # 可视化平均星级最高的10个商业类别
        print("\n2. 可视化平均星级最高的10个商业类别...")
        visualize_average_stars(ave_stars_category_list)
        
        # 可视化商家数量最多的10个城市
        print("\n3. 可视化商家数量最多的10个城市...")
        visualize_top_cities(top_business_city_list)
        
        print("\n✓ 所有可视化完成！")
        print("=" * 70)
        
    except FileNotFoundError as e:
        print(f"❌ 错误：找不到分析数据文件 - {e}")
        print("请先运行数据分析脚本生成数据")
    except Exception as e:
        print(f"❌ 错误：{e}")
        import traceback
        traceback.print_exc()

