# SafeDrive Insurance Claims Analytics

**End-to-end portfolio case study | Business analytics | Predictive modelling | Explainability | Governance**

## Business problem
An insurer wants to understand its policy portfolio and identify policies that may be more likely to generate a claim, so teams can prioritize appropriate human review and proactive service.

This project explores historical policy data, engineers features, compares classification models, tunes a decision tree, evaluates a held-out test set, interprets model behaviour with SHAP, and packages portfolio insights in Power BI and Streamlit.

> **Important scope note:** the supplied project files support claim-likelihood classification and risk ranking on the available dataset. They do not establish a validated forward-looking time horizon (such as claims in the next 30/90 days). Do not describe this as a validated “next 90 days” forecast unless you rebuild labels and validate using a time-based split. This is a prototype, not a production underwriting system.

## Key results
- Dataset: 58,592 policies and 49 columns.
- Observed claims: 3,748; overall claim rate approximately 6.40%.
- Held-out test set: 11,719 policies (750 claim cases, 10,969 non-claim cases).
- Selected model: Featuretools-extended Decision Tree.
- Test ROC-AUC: approximately 0.639; recall: approximately 73.07%; precision: approximately 8.79%.
- Risk bands are percentile-ranked groups within the scored test set, not calibrated probability thresholds. Observed claim rates rise from Low to Very High in the supplied summary.

The model's high recall / low precision trade-off means it may capture many claim cases but also flag many non-claim policies. It is best presented as a **review-prioritization prototype**, not an automated decision system.

## Repository map
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

## Deploy on Streamlit Community Cloud
1. Push this repository to GitHub as a **public** repository.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Select **Create app**.
4. Choose this repository, the `main` branch, and `app.py`.
5. Deploy and wait for the app URL.
6. Open the URL in an incognito/private browser window to verify public access.
7. Add the live app and GitHub links to your resume.

## Data and privacy
This public starter package intentionally excludes the raw policy-level dataset, row-level prediction exports, full scored policy table, MLflow database, and serialized model binaries. Review the source dataset's license and your course/provider rules before publishing any data. Do not publish personal, confidential, or proprietary information.

## Reproducibility and limitations
- The notebooks are the canonical submitted workflow files, not proof of a fresh clean-room rerun.
- The reported split is stratified train/test, not a chronological future-period validation.
- Risk bands are relative rank bands within the scored test population.
- SHAP summaries describe model behaviour, not causal drivers.
- No measured financial savings, claim reduction, or production deployment impact is claimed.

## Suggested resume entry
**SafeDrive Insurance Claims Analytics | Python, SQL/EDA, Feature Engineering, Scikit-learn, Optuna, SHAP, MLflow, Evidently, Power BI, Streamlit**
- Analysed 58.6K policy records and engineered features to investigate claim patterns and portfolio risk.
- Compared classification baselines and tuned a decision-tree model; achieved 0.639 ROC-AUC and 73.1% recall on a held-out test set, with 8.8% precision.
- Built percentile-based risk segments, interpreted model outputs with SHAP, and documented monitoring/governance considerations.
- Published an interactive Streamlit case study and Power BI dashboard for communicating model and business findings.

Tailor the wording to your actual contribution and be prepared to explain the low precision, validation limitations, and why the tool is decision support only.
