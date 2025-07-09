# ThreatSight AI  
**Unsupervised Anomaly Detection on Web Server Logs**

ThreatSight AI is an intelligent Security Operations Center (SOC) assistant designed to detect anomalies in Apache server logs using unsupervised learning. Leveraging Isolation Forest and Autoencoder models, the system flags suspicious access patterns and visualizes them through an interactive dashboard.

---

## Project Overview

This project was built as part of an internal initiative to improve early threat detection through log analysis. It involves parsing raw logs, extracting features, applying machine learning techniques, and visualizing results for actionable insights.

---

## 📂 Repository Structure

```plaintext
THREATSIGHT_AI/
│
├── dashboard/
│   └── interface.py                # Plotly Dash app
│
├── data/
│   ├── processed/
│   │   ├── final_merged.csv
│   │   ├── labeled_subset.csv
│   │   ├── parsed_logs.csv
│   │   ├── with_autoencoder.csv
│   │   ├── with_autoencoder_tuned.csv
│   │   └── with_isolation_forest.csv
│   └── raw_logs/
│       └── promjetDec2021.log     # Raw Apache logs
│
├── notebooks/
│   ├── 01_etl_parsing.ipynb
│   ├── 02_isolation_forest.ipynb
│   ├── 03_autoencoder.ipynb
│   └── 04_evaluation.ipynb
│
├── report/
│   ├── Unsupervised Anomaly Detection on Server Logs.pdf
│   └── Unsupervised Anomaly Detection on Server Logs.docx
│
├── requirements.txt
├── README.md
└── .gitignore
```
---

## Features

- ✅ ETL pipeline to parse Apache logs  
- ✅ Time-based & categorical feature engineering  
- ✅ Isolation Forest for quick unsupervised anomaly detection  
- ✅ Deep learning Autoencoder with reconstruction error thresholding  
- ✅ Combined precision-recall evaluation on labeled subset  
- ✅ Interactive dashboard to explore anomalies over time  

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/threatsight-ai.git
cd threatsight-ai
2. Install Requirements
pip install -r requirements.txt
3. Run the Dashboard
cd dashboard
python interface.py
```
#### Then visit http://127.0.0.1:8050/ in your browser.
---

## Models Used

- Isolation Forest  
- Autoencoder (Neural Network)

---

## Feature Engineering

- Hour of request (`hour`)
- Day of week (`weekday`)
- URL length
- Status codes
- Encoded user-agent & request types

---

## Dashboard Features

✅ Built using Plotly Dash:

- ⏱ Time series anomaly scatter plot  
- 📈 Reconstruction error trend  
- 🌐 Top anomalous URLs bar chart  
- 🧾 Interactive table of anomalies  

Screenshots available in the `/report` folder.

---

## Getting Started

###  1. Clone the Repository

```bash
git clone https://github.com/your-username/threatsight_ai.git
cd threatsight_ai
```

### 2. Setup Virtual Environment

```bash
python -m venv venv

# Activate:
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Dashboard

```bash
python dashboard/interface.py
```
Then open http://127.0.0.1:8050/ in your browser.

---

## Report
The full professional report with evaluation metrics and dashboard screenshots is included here:
```bash
/report/Unsupervised Anomaly Detection on Server Logs.pdf
```

---

## Author

### Medapati Veerendra Subhash Reddy
### Infoshare Soft Solutions