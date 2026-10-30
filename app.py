from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="SafeDrive | Claims Analytics", page_icon="🚗", layout="wide")

ROOT = Path(__file__).parent
AGG = ROOT / "data" / "aggregates"
IMG = ROOT / "images"

def read_csv(name):
    path = AGG / name
    return pd.read_csv(path) if path.exists() else pd.DataFrame()

st.title("SafeDrive | Insurance Claims Analytics")
st.caption("Portfolio case study • Claims-risk modelling • Explainability • Model governance")

st.info(
    "Decision-support prototype: this app summarizes the analysis and held-out test results. "
    "Risk bands are percentile-ranked groups within the scored test set, not calibrated underwriting "
    "cut-offs. The model is not validated for production pricing, automatic rejection, or claims decisions."
)

kpi = read_csv("business_kpi_summary.csv")
metrics = read_csv("model_test_metrics.csv")
risk = read_csv("risk_band_summary.csv")
comparison = read_csv("model_comparison.csv")
shap = read_csv("shap_feature_summary.csv")

def metric_value(df, candidates):
    if df.empty: return None
    # Support common export layouts: Metric/Value or one-row wide table.
    cols = {str(c).strip().lower(): c for c in df.columns}
    for key in candidates:
        if key.lower() in cols:
            return df.iloc[0][cols[key.lower()]]
    if len(df) == 1:
        for c in df.columns:
            if any(key.lower() in str(c).lower() for key in candidates):
                return df.iloc[0][c]
    return None

# KPI CSV often stores Metric and Value as rows; display it as a compact table.
st.header("1. Business problem and portfolio baseline")
st.write(
    "The business question: can historical policy information help prioritize policies "
    "for closer review based on estimated claim likelihood?"
)
if not kpi.empty:
    st.dataframe(kpi, use_container_width=True, hide_index=True)
else:
    st.warning("Business KPI export not found. Add data/aggregates/business_kpi_summary.csv.")

st.header("2. Portfolio and risk segmentation")
if not risk.empty:
    st.dataframe(risk, use_container_width=True, hide_index=True)
    st.caption("Bands use percentile ranks of model scores: Low ≤ 40th percentile; Medium ≤ 75th; High ≤ 90th; remaining = Very High.")
else:
    st.warning("Risk summary export not found.")
img = IMG / "claim_rate_by_predicted_risk.png"
if img.exists():
    st.image(str(img), caption="Observed claim rate by predicted risk band", use_container_width=True)

st.header("3. Model validation")
if not metrics.empty:
    st.dataframe(metrics, use_container_width=True, hide_index=True)
else:
    st.warning("Model test metrics export not found.")
if not comparison.empty:
    st.subheader("Cross-validation model comparison")
    st.dataframe(comparison, use_container_width=True, hide_index=True)
img = IMG / "model_comparison.png"
if img.exists():
    st.image(str(img), caption="Model comparison", use_container_width=True)

st.header("4. Explainability")
if not shap.empty:
    st.dataframe(shap.head(10), use_container_width=True, hide_index=True)
img = IMG / "shap_summary.png"
if img.exists():
    st.image(str(img), caption="SHAP global feature-importance summary", use_container_width=True)
st.caption(
    "Mean absolute SHAP indicates average contribution magnitude in model output; it is not evidence "
    "of causation. Signed mean SHAP is an average direction in model-output space."
)

st.header("5. Business interpretation and recommended use")
st.markdown("""
- Use the model as a **human-review prioritization aid**, not as an automated decision-maker.
- The held-out test result shows relatively high recall but low precision; many flagged policies may not claim.
- Before operational use, validate on a later time period, calibrate probabilities, select thresholds using business costs, and assess fairness and stability.
- Define the prediction horizon (for example, claims within the next 90 days) and ensure training labels match that horizon.
""")

st.header("6. Project evidence")
st.markdown("""
- **Notebooks:** end-to-end preprocessing, modelling, AutoML, explainability and governance.
- **Power BI:** interactive portfolio dashboard (`dashboard/SafeDrive_PowerBI_Dashboard.pbix`).
- **Business report:** `reports/SafeDrive_Business_Report.pdf`.
- **Monitoring evidence:** `artifacts/evidently_model_monitoring_report.html`.
""")
st.caption("Built as an educational portfolio case study. Confirm dataset licensing and remove any sensitive or restricted data before public release.")
