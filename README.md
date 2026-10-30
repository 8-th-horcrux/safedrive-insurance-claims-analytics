# SafeDrive Insurance Claims Analytics

**End-to-end portfolio case study | Business analytics | Predictive modelling | Explainability | Governance**

## Business problem
The company wants to understand its policy portfolio and identify policies that may be more likely to generate a claim in the future, so that, teams can prioritize appropriate human review and action to reduce the risk of loss to the company.

This project explores historical policy data, feature engineering using DFS (Deep Feature Synthesis), compares classification models to find the best model in terms of flagging the claim, tunes a decision tree, evaluates a held-out test set, interprets model behaviour with SHAP, and packages portfolio insights in Power BI and Streamlit.

> **Important scope note:** the supplied project files support claim-likelihood classification and risk ranking on the available dataset. They do not establish a validated forward-looking time horizon (such as claims in the next 30/90 days). Do not describe this as a validated “next 90 days” forecast unless you rebuild labels and validate using a time-based split. This is a prototype, not a production underwriting system.

## Key results
- Dataset: 58,592 policies and 49 columns.
- Observed claims: 3,748; overall claim rate approximately 6.40%.
- Held-out test set: 11,719 policies (750 claim cases, 10,969 non-claim cases).
- Selected model: Featuretools-extended Decision Tree.
- Test ROC-AUC: approximately 0.639; recall: approximately 73.07%; precision: approximately 8.79%.
- Risk bands are percentile-ranked groups within the scored test set, not calibrated probability thresholds. Observed claim rates rise from Low to Very High in the supplied summary.

The model's high recall / low precision trade-off means it may capture many claim cases but also flag many non-claim policies. It is best presented as a **review-prioritization prototype**, not an automated decision system.

## Repository contents
- `app.py` — Streamlit portfolio application.
- `notebooks/` — three canonical project notebooks.
- `data/aggregates/` — aggregate metrics and summaries only; no row-level policy dataset.
- `images/` — selected project visuals.
- `dashboard/` — Power BI dashboard and DAX measure reference.
- `reports/` — final business report.
- `artifacts/` — model metadata and Evidently HTML report.

## Run locally
```bash
# 1. Create and activate a virtual environment
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```
Open the local URL printed in the terminal (usually http://localhost:8501).

## Deployed on Streamlit Community Clou

## Data and privacy
This public package intentionally excludes the raw policy-level dataset, row-level prediction exports, full scored policy table, MLflow database, and serialized model binaries. Do not publish personal, confidential, or proprietary information.

## Reproducibility and limitations
- The notebooks are the canonical submitted workflow files, not proof of a fresh clean-room rerun.
- The reported split is stratified train/test, not a chronological future-period validation.
- Risk bands are relative rank bands within the scored test population.
- SHAP summaries describe model behaviour, not causal drivers.
- No measured financial savings, claim reduction, or production deployment impact is claimed.

