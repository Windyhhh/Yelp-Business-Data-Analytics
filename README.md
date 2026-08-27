<div align="center">

# ⭐ Yelp-Business-Data-Analytics

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

## License

MIT — free to use, modify and distribute.
