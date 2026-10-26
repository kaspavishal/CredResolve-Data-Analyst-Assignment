from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR = PROJECT_ROOT / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

quality_results = []

def build_dataset(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    original_rows = len(df)
    exact_duplicate_rows = int(df.duplicated().sum())

    # Preserve the raw data; write a separate analytical copy.
    cleaned = df.drop_duplicates().copy()

    output_path = OUTPUT_DIR / file_path.name
    cleaned.to_csv(output_path, index=False)

    quality_results.append({
        "dataset": file_path.stem,
        "original_rows": original_rows,
        "exact_duplicate_rows": exact_duplicate_rows,
        "processed_rows": len(cleaned),
        "rows_removed": original_rows - len(cleaned),
        "missing_cells": int(df.isna().sum().sum()),
        "output_file": str(output_path.relative_to(PROJECT_ROOT))
    })

    print(
        f"{file_path.name}: {original_rows:,} rows -> "
        f"{len(cleaned):,} rows; "
        f"{exact_duplicate_rows:,} exact duplicates"
    )

def main():
    if not RAW_DIR.exists():
        raise FileNotFoundError(f"Raw data directory not found: {RAW_DIR}")

    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {RAW_DIR}")

    for file_path in csv_files:
        build_dataset(file_path)

    report = pd.DataFrame(quality_results)
    report_path = REPORT_DIR / "golden_dataset_build_report.csv"
    report.to_csv(report_path, index=False)

    print("\nBUILD COMPLETE")
    print("Datasets processed:", len(csv_files))
    print("Original rows:", f"{report['original_rows'].sum():,}")
    print("Processed rows:", f"{report['processed_rows'].sum():,}")
    print("Report:", report_path)
    print("Processed data:", OUTPUT_DIR)

if __name__ == "__main__":
    main()