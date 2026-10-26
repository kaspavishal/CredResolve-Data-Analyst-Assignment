from pathlib import Path
import pandas as pd

# Project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
REPORT_DIR = PROJECT_DIR / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

summary = []
column_details = []

print("=" * 60)
print("CREDRESOLVE - RAW DATA PROFILING")
print("=" * 60)

csv_files = sorted(RAW_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {RAW_DIR}")

print(f"\nFound {len(csv_files)} CSV files.\n")

for file_path in csv_files:
    print(f"Inspecting: {file_path.name}")

    try:
        df = pd.read_csv(file_path, low_memory=False)

        row_count, column_count = df.shape

        summary.append({
            "dataset": file_path.stem,
            "rows": row_count,
            "columns": column_count,
            "missing_cells": int(df.isna().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "memory_mb": round(
                df.memory_usage(deep=True).sum() / (1024 ** 2), 2
            ),
            "status": "SUCCESS",
            "error": ""
        })

        for column in df.columns:
            column_details.append({
                "dataset": file_path.stem,
                "column": column,
                "dtype": str(df[column].dtype),
                "missing_count": int(df[column].isna().sum()),
                "missing_percent": round(
                    df[column].isna().mean() * 100, 2
                ),
                "unique_values": int(df[column].nunique(dropna=True)
                )
            })

        print(
            f"  Rows: {row_count:,} | "
            f"Columns: {column_count} | "
            f"Missing cells: {int(df.isna().sum().sum()):,} | "
            f"Duplicate rows: {int(df.duplicated().sum()):,}"
        )

    except Exception as error:
        summary.append({
            "dataset": file_path.stem,
            "rows": None,
            "columns": None,
            "missing_cells": None,
            "duplicate_rows": None,
            "memory_mb": None,
            "status": "FAILED",
            "error": str(error)
        })

        print(f"  ERROR: {error}")

# Save profiling reports
summary_df = pd.DataFrame(summary)
columns_df = pd.DataFrame(column_details)

summary_path = REPORT_DIR / "profile_summary.csv"
columns_path = REPORT_DIR / "column_profile.csv"

summary_df.to_csv(summary_path, index=False)
columns_df.to_csv(columns_path, index=False)

print("\n" + "=" * 60)
print("PROFILING COMPLETED")
print("=" * 60)

print(f"\nDatasets inspected: {len(csv_files)}")
print(f"Successful: {(summary_df['status'] == 'SUCCESS').sum()}")
print(f"Failed: {(summary_df['status'] == 'FAILED').sum()}")

print(f"\nSummary report: {summary_path}")
print(f"Column report:  {columns_path}")

print("\nDataset summary:")
print(summary_df.to_string(index=False))