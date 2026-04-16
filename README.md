# 📦 Retail Sales Forecasting & Inventory Optimization System

## 🚀 Overview

This project builds an end-to-end system to forecast retail sales and optimize inventory decisions using machine learning and operations research techniques.

---

## 🎯 Problem Statement

Retailers face:

* Overstock → increased holding costs
* Stockouts → lost revenue

This project solves both using:

* Demand forecasting
* Inventory optimization

---

## 🏢 Industry Relevance

---

## 💡 Features

* Time series forecasting
* Feature engineering (lags, rolling stats)
* ML model (RandomForest)
* Safety stock calculation
* Reorder point optimization
* Streamlit dashboard

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib / Seaborn

---

## 📁 Project Structure

```
retail-forecasting-inventory-optimization/
│
├── data/
│   ├── raw/
│   │   └── retail_data.csv
│   ├── processed/
│   │   └── cleaned_data.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── forecast.py
│   ├── inventory.py
│   ├── utils.py
│
├── models/
│   └── rf_model.pkl
│
├── outputs/
│   ├── forecast.csv
│   ├── inventory_recommendations.csv
│
├── app/
│   └── streamlit_app.py
│
├── tests/
│   └── test_pipeline.py
│
├── requirements.txt
├── main.py
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone <repo_url>
cd retail-forecasting-inventory-optimization
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
streamlit run app/streamlit_app.py
```

---

## 📊 Results

* Forecast vs actual visualization
* Inventory recommendations:

  * Safety stock
  * Reorder point


  ---

## 📸 Dashboard Images

### 📊 Overview
![Overview](images/overview.png)

### 📈 Sales Analysis
![Sales](images/sales.png)

### 🔮 Forecasting
![Forecast](images/forecasting.png)

### 📦 Inventory Optimization
![Inventory](images/inventory.png)

### 🧠 Full Dashboard
![Dashboard](images/dashboard.png)

---

## 📈 Business Value

* Reduce stockouts
* Optimize working capital
* Improve supply chain efficiency

---

## 🔮 Future Improvements

* XGBoost model
* Multi-store forecasting
* Real-time API
* Automated PO generation

---

## 👨‍💻 Author

Shresthaa Maiti
