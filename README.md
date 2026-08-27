# ⭐ Yelp 商家数据分析 | Yelp Business Data Analytics

> **基于 Yelp 开放数据集的商业智能分析——餐厅分析、用户评论、推荐系统、NLP 情感分析，挖掘餐饮商业洞察。**
>
> *Business intelligence analysis based on the Yelp open dataset — restaurant analytics, user reviews, recommendation system, NLP sentiment analysis, mining dining business insights.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 🍽️ **餐厅分析** | Restaurant Analytics | 餐厅分布、评分、热度分析 |
| 💬 **评论分析** | Review Analysis | 用户评论情感与主题分析 |
| 🤖 **推荐系统** | Recommendation | 商家/餐厅智能推荐 |
| 🧠 **NLP 处理** | NLP Processing | 评论文本情感分析、主题挖掘 |
| 📊 **商业洞察** | Business Insight | 数据驱动的餐饮商业决策 |

---

## 🏆 技术栈 | Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-blue?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-blue?logo=numpy)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange?logo=scikitlearn)
![NLTK](https://img.shields.io/badge/NLTK-3.6+-green?logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-red?logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-blue?logo=python)

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Yelp-Business-Data-Analytics.git
cd Yelp-Business-Data-Analytics

# 1. 安装依赖
pip install -r requirements.txt

# 2. 下载/准备数据
python scripts/download_data.py

# 3. 数据清洗与预处理
python scripts/preprocess.py --input data/raw --output data/processed

# 4. 餐厅分析
python src/restaurant_analysis.py --data data/processed

# 5. NLP 情感分析
python src/sentiment_analysis.py --reviews data/processed/reviews.csv

# 6. 推荐系统
python src/recommendation.py --train data/processed/train.csv

# 7. 生成报告
python generate_report.py
```

---

## 📂 项目结构 | Project Structure

```
Yelp-Business-Data-Analytics/
├── src/                       # 核心代码
│   ├── restaurant_analysis.py # 餐厅分析
│   ├── sentiment_analysis.py  # 情感分析
│   ├── recommendation.py      # 推荐系统
│   ├── topic_modeling.py      # 主题建模
│   └── business_insight.py    # 商业洞察
├── scripts/                   # 脚本
│   ├── download_data.py
│   └── preprocess.py
├── data/                      # 数据
├── notebooks/                 # 分析 Notebook
├── result/                    # 结果
└── requirements.txt
```

---

## 🔬 核心实现 | Core Implementation

### 推荐系统 | Recommendation System

```python
# 基于协同过滤的商家推荐
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

class YelpRecommender:
    def __init__(self, ratings_matrix):
        # 用户-商家评分矩阵
        self.ratings = ratings_matrix
        # 用户相似度矩阵
        self.user_sim = cosine_similarity(ratings_matrix.fillna(0))
        
    def recommend(self, user_id, top_n=10):
        """基于相似用户的商家推荐"""
        user_idx = self.ratings.index.get_loc(user_id)
        sims = self.user_sim[user_idx]
        
        # 找到相似用户
        similar_users = np.argsort(sims)[::-1][1:11]
        
        # 聚合相似用户的评分
        scores = np.zeros(self.ratings.shape[1])
        for su in similar_users:
            scores += sims[su] * self.ratings.iloc[su].fillna(0).values
        
        # 排除已评分项
        rated = self.ratings.iloc[user_idx].notna().values
        scores[rated] = -1
        
        # 返回 Top-N 商家
        top_indices = np.argsort(scores)[::-1][:top_n]
        return self.ratings.columns[top_indices].tolist()
```

---

## 📊 分析示例 | Analysis Output

```
🍽️ 餐饮商业洞察报告
━━━━━━━━━━━━━━━━━━━━━━━━━
📊 热门餐厅品类 Top 5:
  1. 中式料理  2. 日料  3. 咖啡
  4. 快餐     5. 甜品

⭐ 高评分餐厅特征:
  平均评分 4.2+ | 评论数 200+ | 价位适中

💬 评论情感分析:
  正面 68% | 中性 20% | 负面 12%
  高频好评词: 服务好、味道棒、环境佳
  高频差评词: 等太久、价格高、分量少

🤖 推荐示例 (对用户 U123):
  推荐: 川味居、寿司屋、星巴克
━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎯 应用场景 | Use Cases

- 🍽️ **餐饮研究**：餐饮市场商业分析
- 📊 **商业智能**：商家数据分析
- 🤖 **推荐系统**：商家/餐厅推荐
- 🧠 **NLP 应用**：评论情感分析
- 🎓 **数据分析教学**：真实数据集分析项目

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **Yelp 真实数据商业分析，Star ⭐ 挖掘餐饮商业洞察！**
