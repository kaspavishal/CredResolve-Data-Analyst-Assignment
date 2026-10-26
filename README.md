# CredResolve — Data Analyst Assignment

**Recovery Performance Analysis | Data Quality | SQL | Python | Streamlit**

## 📌 Project Overview

This project investigates the business claim:

> "Recovery has improved by 11% month-on-month."

The objective is to determine whether the available evidence supports this claim, identify data quality issues that may distort reported performance, and recommend a data-driven approach to allocating ₹10 crore in collections operations.

The analysis emphasizes reproducibility, transparent metric definitions, payment integrity, and evidence-based decision-making.

## 🎯 Key Questions

- Has recovery performance genuinely improved?
- Which data quality issues could distort the reported results?
- How reliable are payment attribution and transaction records?
- What do the available portfolio and promise-to-pay metrics indicate?
- What additional analysis and experiments are needed before scaling investment?

## 🔍 Key Findings

- **The 11% improvement claim remains unverified.** Available payment events cover January 1 through August 8, 2026, rather than 12 complete months.
- **Payment record integrity requires investigation.** The processed dataset contains 25,014 payment records and 25,000 distinct payment IDs.
- **Borrower identity quality is a concern.** The available borrower data contains 30,000 records but only 11,015 unique borrower IDs.
- **Payment references are not reliable unique transaction identifiers.** Repeated references require further reconciliation.
- **Promise-to-pay outcomes vary by channel.** These outcomes should not be treated as proof of realized cash recovery.
- **Investment decisions require stronger evidence.** Validate net recovery metrics and use controlled experiments before scaling investment.

These findings describe the available data and its limitations; they do not establish that the reported recovery improvement is real or false.

## 🛠️ Technology Stack

- **Python** — data processing and analysis
- **Pandas** — data cleaning and transformation
- **SQL / DuckDB-compatible queries** — analytical investigations
- **Jupyter Notebook** — exploratory analysis
- **Streamlit** — executive dashboard
- **CSV** — raw, processed, and analytical datasets
- **Git and GitHub** — version control and project sharing

## 📂 Project Structure

```text
CredResolve-Data-Analyst-Assignment/
├── dashboard/
│   └── app.py
├── data/
│   ├── golden/
│   ├── processed/
│   └── raw/
├── docs/
│   ├── architecture_diagram.md
│   ├── architecture_diagram.png
│   └── executive_memo.md
├── notebooks/
│   └── 02_data_quality_analysis.ipynb
├── reports/
│   └── Analytical and data quality reports
├── sql/
│   ├── 01_recovery_metrics.sql
│   ├── 02_duplicate_payment_audit.sql
│   ├── 03_monthly_recovery_trends.sql
│   ├── 04_recovery_by_risk_and_dpd.sql
│   └── 05_ptp_performance.sql
├── src/
│   ├── build_golden_dataset.py
│   └── profile_data.py
├── .gitignore
├── data_dictionary_output.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kaspavishal/CredResolve-Data-Analyst-Assignment.git
cd CredResolve-Data-Analyst-Assignment
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the packages required by the dashboard and notebook. If a `requirements.txt` file is added to this repository, use:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages individually according to the imports in the project files.

### 4. Rebuild the processed datasets

From the project root, run:

```bash
python src/build_golden_dataset.py
```

The script reads CSV files from `data/raw/`, writes processed datasets to `data/processed/`, and generates a dataset build report under `reports/`.

### 5. Launch the dashboard

```bash
streamlit run dashboard/app.py
```

Open the local URL displayed in the terminal.

### 6. Explore the notebook

Open `notebooks/02_data_quality_analysis.ipynb` in Jupyter or VS Code and run the analysis cells using the appropriate Python environment.

## 📊 Deliverables

| Deliverable | Location |
|---|---|
| SQL analysis | `sql/` |
| Data quality and recovery analysis | `notebooks/02_data_quality_analysis.ipynb` |
| Golden dataset build pipeline | `src/build_golden_dataset.py` |
| Data quality and analytical reports | `reports/` |
| Executive dashboard | `dashboard/app.py` |
| Executive memo | `docs/executive_memo.md` |
| Architecture documentation | `docs/architecture_diagram.md` |
| Architecture diagram | `docs/architecture_diagram.png` |

## 📈 Business Recommendation

The current evidence is insufficient to confidently validate the reported 11% month-on-month recovery improvement.

Before committing the full ₹10 crore investment, the recommended next steps are to:

1. Reconcile duplicate and repeated payment records.
2. Validate payment attribution and borrower identity resolution.
3. Establish consistent recovery definitions and denominators.
4. Analyze complete monthly periods and portfolio mix changes.
5. Run controlled experiments to estimate incremental net recovery.
6. Evaluate expected ROI, break-even, and downside scenarios before scaling.

## ⚠️ Limitations

- The available payment history does not cover 12 complete months.
- Repeated payment IDs and references require transaction-level investigation.
- Borrower identity conflicts may affect attribution and aggregation.
- Recorded successful payment amounts are not necessarily equivalent to validated net recovery.
- Observational patterns alone do not establish causality.

## 👤 Author

**Kaspa Vishal**

Data Analyst Assignment — CredResolve

---

*This project is an analytical investigation based on the supplied datasets. Findings and recommendations are subject to the data quality limitations documented in the project.*