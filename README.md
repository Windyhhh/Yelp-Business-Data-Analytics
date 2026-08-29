<div align="center">

# Yelp 商户数据分析 | Yelp-Business-Data-Analytics

### Analytics over the Yelp business dataset.

Restaurant analysis, reviews, recommendations and NLP — with Spark-based analysis output.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Spark-3-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/)

</div>

---

**Yelp-Business-Data-Analytics** analyzes the **Yelp business dataset** — restaurant analysis, reviews, recommendations and **NLP**, with Spark-based analysis output.

> [!NOTE]
> 中文项目：Yelp 商家数据集分析——餐厅分析、评论、推荐、NLP。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Yelp-Business-Data-Analytics.git
cd Yelp-Business-Data-Analytics

pip install -r requirements.txt

# configure and run analysis
python -c "import config; print(config.DATA_DIR)"
```

Analysis results land in `server_data/yelp_output/analysis/` (average stars per category, top business city, etc.).

---

## Features

- **Restaurant analysis** — category / city / review aggregates.
- **Reviews + NLP** — review analytics.
- **Recommendation** — data-driven business insights.

---

## Project Structure

```
Yelp-Business-Data-Analytics/
├── config.py
├── server_data/yelp_output/analysis/   # Spark analysis output JSON
│   ├── average_stars_category/
│   ├── average_review_category/
│   └── top_business_city/
├── README.md / README_CN.md
```

---

## 技术实现细节

### 架构概览

项目采用模块化设计，核心目录包括：**server_data, src**。

### 关键函数

- `create_spark_session`, `attribute_score`, `analysis`, `data_process`

### 技术栈与依赖

**核心框架/库**：Spark

**主要 import**：
```python
import os
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import sys
import os
from config import DATA_CONFIG, ANALYSIS_CONFIG, SPARK_CONFIG
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
```

### 实现要点

- 通过 `create_spark_session` 等函数实现核心流程编排
- 基于 Spark 构建，技术栈成熟稳定
- 代码结构清晰，模块间低耦合，便于扩展和维护

---
## License

MIT — free to use, modify and distribute.
