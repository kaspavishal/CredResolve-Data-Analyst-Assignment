
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="CredResolve Analytics",
    page_icon="📊",
    layout="wide"
)

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"


# --------------------------------------------------
# REPORT LOADER
# --------------------------------------------------
def load_report(filename):
    file_path = REPORTS / filename

    if file_path.exists():
        try:
            return pd.read_csv(file_path)
        except (OSError, pd.errors.ParserError, UnicodeDecodeError) as exc:
            st.warning(f"Could not read {filename}: {exc}")

    return pd.DataFrame()


# --------------------------------------------------
# LOAD REPORTS
# --------------------------------------------------
keys = load_report("table_key_uniqueness.csv")
risk = load_report("recovery_by_risk_and_dpd.csv")
references = load_report("repeated_reference_risk_summary.csv")
profile = load_report("profile_summary.csv")


# --------------------------------------------------
# DASHBOARD HEADER
# --------------------------------------------------
st.title("CredResolve | Recovery Analytics Dashboard")

st.caption(
    "Data quality, payment performance, and recovery opportunities"
)

st.warning(
    "The claimed 11% month-on-month improvement is unverified. "
    "Available payment data ends on August 8, 2026; August is incomplete."
)


# --------------------------------------------------
# DATA QUALITY OVERVIEW
# --------------------------------------------------
st.header("Data Quality Overview")

c1, c2, c3 = st.columns(3)

c1.metric("Payment Event Records", "25,014")
c2.metric("Unique Payment IDs", "25,000")
c3.metric("Repeated Payment IDs", "14")

c4, c5, c6 = st.columns(3)

c4.metric("Borrower Records", "30,000")
c5.metric("Unique Borrower IDs", "11,015")
c6.metric("Repeated Payment References", "3,407")


# --------------------------------------------------
# PORTFOLIO ANALYSIS BY RISK AND DPD
# --------------------------------------------------
st.divider()
st.header("Portfolio Analysis by Risk and DPD")

required_columns = {
    "risk_segment",
    "dpd_bucket",
    "total_accounts",
    "accounts_with_successful_payments"
}

if risk.empty:
    st.error(
        "Risk-and-DPD report not found. "
        "Check reports/recovery_by_risk_and_dpd.csv."
    )

elif not required_columns.issubset(risk.columns):
    missing = sorted(required_columns - set(risk.columns))
    st.error(f"The risk report is missing these columns: {missing}")
    st.dataframe(risk, width="stretch")

else:
    # Convert account counts to numeric values.
    risk["total_accounts"] = pd.to_numeric(
        risk["total_accounts"], errors="coerce"
    )

    risk["accounts_with_successful_payments"] = pd.to_numeric(
        risk["accounts_with_successful_payments"], errors="coerce"
    )

    # Calculate account payment-activity coverage.
    valid_denominator = risk["total_accounts"].where(
        risk["total_accounts"] > 0
    )

    risk["successful_payment_coverage_pct"] = (
        risk["accounts_with_successful_payments"]
        .div(valid_denominator)
        .mul(100)
        .round(2)
    )

    st.subheader("Portfolio Summary")
    st.dataframe(risk, width="stretch")

    chart_data = risk.dropna(
        subset=["successful_payment_coverage_pct"]
    ).copy()

    if not chart_data.empty:
        dpd_order = [
            "0-30 days",
            "31-60 days",
            "61-90 days",
            "90+ days"
        ]

        chart_data["dpd_bucket"] = pd.Categorical(
            chart_data["dpd_bucket"],
            categories=dpd_order,
            ordered=True
        )

        chart_data = chart_data.sort_values(
            ["dpd_bucket", "risk_segment"]
        )

        fig = px.bar(
            chart_data,
            x="dpd_bucket",
            y="successful_payment_coverage_pct",
            color="risk_segment",
            barmode="group",
            title=(
                "Accounts with Recorded Successful Payments "
                "by Risk Segment and DPD"
            ),
            labels={
                "dpd_bucket": "Days Past Due",
                "successful_payment_coverage_pct":
                    "Accounts with Successful Payments (%)",
                "risk_segment": "Risk Segment"
            },
            hover_data={
                "total_accounts": True,
                "accounts_with_successful_payments": True,
                "successful_payment_coverage_pct": ":.2f"
            }
        )

        fig.update_layout(
            legend_title_text="Risk Segment",
            xaxis_title="Days Past Due",
            yaxis_title="Accounts with Successful Payments (%)",
            yaxis_range=[0, 100]
        )

        st.plotly_chart(fig, width="stretch")

    else:
        st.info("No valid coverage values are available for the chart.")

    st.caption(
        "Coverage means the percentage of accounts with at least one "
        "recorded successful payment. It is not a verified net recovery rate."
    )


# --------------------------------------------------
# PAYMENT REFERENCE INTEGRITY
# --------------------------------------------------
st.divider()
st.header("Payment Reference Integrity")

if references.empty:
    st.info("Repeated-reference risk summary is not available.")
else:
    st.dataframe(references, width="stretch")

    st.caption(
        "Repeated payment references require reconciliation. "
        "A repeated reference alone does not prove a duplicate payment."
    )


# --------------------------------------------------
# DATA QUALITY REPORTS
# --------------------------------------------------
st.divider()
st.header("Data Quality Reports")

reports_to_show = [
    ("Table Key Uniqueness", keys),
    ("Dataset Profile Summary", profile)
]

for report_title, report_data in reports_to_show:
    with st.expander(report_title):
        if report_data.empty:
            st.info(f"{report_title} is not available.")
        else:
            st.dataframe(report_data, width="stretch")


# --------------------------------------------------
# BUSINESS CONCLUSION
# --------------------------------------------------
st.divider()
st.subheader("Business Conclusion")

st.markdown(
    "**Finding:** The claimed 11% month-on-month recovery improvement "
    "remains unverified. Payment data is incomplete, and borrower "
    "identity conflicts and payment-reference anomalies require "
    "reconciliation."
)

st.markdown(
    "**Recommendation:** Validate net recovery against a reliable "
    "outstanding-balance denominator, then run controlled experiments "
    "before scaling the proposed ₹10 Cr investment."
)

st.caption(
    "CredResolve Data Analyst Assignment | Preliminary analytical dashboard"
)
