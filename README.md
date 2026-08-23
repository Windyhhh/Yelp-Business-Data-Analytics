# 📊 Yelp Business Data Analytics | Yelp 商业数据集分析系统

> **Comprehensive analysis of Yelp business dataset. Restaurant/business analytics, review sentiment analysis, recommendation systems, NLP, and geographic visualization. Spark + Python + ML pipeline.**
>
> Yelp 商业数据集综合分析。餐厅/商业分析、评论情感分析、推荐系统、NLP 和地理可视化。Spark + Python + ML 流水线。

---

## 🌟 Features | 核心特性

- **Business Analytics** — Category, location, rating analysis
- **Review NLP** — Sentiment analysis, topic modeling, keyword extraction
- **Recommendation** — Collaborative filtering, content-based
- **Geographic Viz** — Map-based business distribution
- **Spark Processing** — Large-scale data processing
- **Machine Learning** — Rating prediction, business classification
- **Time Series** — Review trends over time

---

## 🚀 Quick Start | 快速开始

```bash
# Download Yelp dataset
# https://www.yelp.com/dataset

# Process with Spark
spark-submit process_yelp.py --input yelp_dataset/ --output results/

# Run analysis
python analyze_businesses.py --data results/business.parquet
python analyze_reviews.py --data results/review.parquet

# Train recommendation model
python train_recommender.py --data results/ --model als
```

---

## 📊 Analysis Dimensions | 分析维度

| Dimension | Metrics |
|-----------|---------|
| **Business** | Category distribution, rating distribution, price range |
| **Reviews** | Sentiment score, review length, helpful votes |
| **Users** | Activity level, elite status, friend network |
| **Geography** | City/state distribution, heatmaps |
| **Time** | Review trends, seasonal patterns |
| **ML** | Rating prediction, business closure prediction |

---

## 📄 License | 许可证

MIT License.

[GitHub](https://github.com/Windyhhh/Yelp-Business-Data-Analytics)
