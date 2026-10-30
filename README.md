# SafeDrive Insurance Claims Analytics

**End-to-End Insurance Risk Analytics \| Predictive Modeling \|
Explainable AI \| Business Intelligence**

An end-to-end insurance analytics portfolio project combining
exploratory data analysis, feature engineering, machine learning, model
explainability, model-governance artifacts, and business intelligence to
support **claim-risk prioritization** across an insurance policy
portfolio.

> **Project status:** Portfolio analytics and claim-likelihood
> classification prototype. This project is not a production
> underwriting system, does not provide a validated future-period claim
> forecast, and should not be used to make automated policy acceptance,
> pricing, or rejection decisions.

------------------------------------------------------------------------

## Table of Contents

-   [Project Overview](#project-overview)
-   [Business Problem](#business-problem)
-   [Project Objectives](#project-objectives)
-   [Solution Workflow](#solution-workflow)
-   [Dataset Summary](#dataset-summary)
-   [Model Results](#model-results)
-   [Key Business Insights](#key-business-insights)
-   [Technology Stack](#technology-stack)
-   [Repository Structure](#repository-structure)
-   [Run Locally](#run-locally)
-   [Data Privacy](#data-privacy)
-   [Limitations and Responsible Use](#limitations-and-responsible-use)
-   [Potential Future Improvements](#potential-future-improvements)

------------------------------------------------------------------------

## Project Overview

Insurance companies need to understand the factors associated with
claims and identify policies that may warrant closer review. This
project explores how historical policy data can be used to analyze
portfolio characteristics, develop a claim-likelihood classification
model, and communicate risk patterns through interactive reporting.

The solution brings together:

-   **Exploratory Data Analysis (EDA):** Understand portfolio
    composition and historical claim patterns.
-   **Feature Engineering:** Create domain-informed features and explore
    automated feature generation.
-   **Predictive Modeling:** Train and compare classification models.
-   **Hyperparameter Optimization:** Tune model parameters using Optuna
    and stratified cross-validation.
-   **Explainable AI:** Use SHAP to interpret model behavior.
-   **Model Governance:** Produce validation and monitoring artifacts.
-   **Business Intelligence:** Present portfolio and risk-segment
    insights through Power BI.
-   **Interactive Application:** Bring key analytics and model outputs
    together in a Streamlit application.

The intended use is to support **portfolio analysis and prioritization
for human review**, not to replace underwriting or claims professionals.

## Business Problem

SafeDrive Insurance wants to better understand its policy portfolio and
examine patterns associated with historical claim occurrence.

The project addresses the following questions:

1.  What proportion of policies in the dataset have a recorded claim?
2.  Which policyholder and vehicle characteristics are associated with
    claim occurrence?
3.  Can a classification model identify a larger share of claim cases
    for further review?
4.  How does model performance change across evaluation metrics and
    risk-ranked segments?
5.  Which features contribute most to the model's predictions?
6.  How can portfolio and model insights be communicated clearly to
    business stakeholders?

## Project Objectives

-   Analyze policyholder, vehicle, and policy characteristics associated
    with historical claims.
-   Explore patterns and potential risk indicators in the available
    data.
-   Build and compare models that classify policies by claim likelihood.
-   Evaluate model performance with particular attention to recall and
    the precision--recall trade-off.
-   Explain model predictions using SHAP.
-   Create portfolio and risk-segmentation views in Power BI.
-   Present the analysis through an interactive Streamlit application.
-   Document validation constraints and responsible-use considerations.

## Solution Workflow

### 1. Portfolio and Claims Analysis

Performed exploratory data analysis to understand the structure and
behavior of the insurance portfolio.

Areas examined included:

-   Overall claim and non-claim distribution.
-   Claim frequency across available policyholder characteristics.
-   Vehicle-related attributes and their relationship with recorded
    claims.
-   Portfolio composition and segment-level patterns.
-   Potential data-quality issues and relationships between variables.

The objective was to translate the dataset into business-relevant
observations before building predictive models.

### 2. Feature Engineering

Prepared the dataset for modeling using a combination of manually
created and automatically generated features.

**Manual feature engineering**

-   Created risk-indicator variables from available fields.
-   Transformed policyholder and vehicle attributes.
-   Explored behavior-related and interaction features where supported
    by the dataset.
-   Prepared model-ready variables and handled preprocessing
    requirements.

**Automated feature engineering**

-   Used **Featuretools Deep Feature Synthesis (DFS)** to generate
    additional features from the available data.
-   Evaluated the expanded feature set as part of the modeling workflow.

Automated feature generation can increase the number of candidate
predictors. Its value should be assessed through validation rather than
assumed from the size of the generated feature set.

### 3. Predictive Modeling

Developed classification models to distinguish policies with and without
a recorded claim.

  -----------------------------------------------------------------------
  Modeling stage                      Approach
  ----------------------------------- -----------------------------------
  Baseline model                      Logistic Regression

  Advanced model                      Decision Tree Classifier

  Automated feature generation        Featuretools Deep Feature Synthesis

  Hyperparameter optimization         Optuna

  Validation approach                 Stratified cross-validation

  Model comparison                    Accuracy, Precision, Recall, F1
                                      Score, and ROC-AUC
  -----------------------------------------------------------------------

The selected model was chosen with attention to the project's
claim-detection objective and the trade-off between identifying claim
cases and generating additional false positives.

### 4. Model Evaluation

Evaluated model performance using:

-   **Accuracy:** Overall proportion of correct classifications.
-   **Precision:** Proportion of predicted claim cases that were actual
    claim cases.
-   **Recall:** Proportion of actual claim cases identified by the
    model.
-   **F1 Score:** Harmonic mean of precision and recall.
-   **ROC-AUC:** Ability of the model to rank positive cases above
    negative cases across classification thresholds.

Because the dataset is imbalanced, accuracy alone is not sufficient to
assess model usefulness.

Recall received particular attention because failing to identify a claim
case may be costly in some review workflows. However, recall must be
interpreted alongside precision: a model that flags many policies may
also create a substantial review workload.

### 5. Model Explainability

Implemented **SHAP (SHapley Additive Explanations)** to make model
behavior easier to inspect.

SHAP was used to:

-   Examine which features contribute most to model predictions.
-   Understand how feature values influence predictions.
-   Inspect individual predictions where applicable.
-   Communicate model behavior to technical and business stakeholders.

SHAP explanations describe how the trained model uses features. They do
**not** establish causation or prove that a feature causes a claim.

### 6. Model Governance and Monitoring

Created supporting artifacts to document model validation and facilitate
review.

Artifacts include:

-   Evidently AI monitoring report.
-   Model performance documentation.
-   Validation summaries.
-   Risk-assessment outputs.
-   Model metadata.

These artifacts support transparency and review. They should not be
interpreted as evidence of production monitoring or ongoing performance
unless the model is deployed and monitored on new, representative data.

### 7. Business Intelligence Dashboard

Developed an interactive **Power BI dashboard** to communicate
portfolio-level findings.

Dashboard areas include:

-   Portfolio overview.
-   Claim and non-claim distribution.
-   Risk segmentation.
-   KPI tracking.
-   Portfolio monitoring metrics.
-   Risk-band performance analysis.

The dashboard is designed to help stakeholders explore historical
portfolio patterns and identify segments that may warrant further
investigation.

### 8. Streamlit Application

Built an interactive Streamlit application to bring the project's
analytical outputs together.

The application showcases:

-   Portfolio analytics.
-   Model performance metrics.
-   Risk segmentation.
-   SHAP explainability outputs.
-   Business insights and recommendations.

The application is a demonstration interface for the portfolio project,
not a production decision system.

## Dataset Summary

The project uses historical insurance policy data.

  Metric               Value
  ----------------- --------
  Total policies      58,592
  Features                49
  Claim cases          3,748
  Claim rate           6.40%
  Test set size       11,719
  Test claims            750
  Test non-claims     10,969

The test-set figures are consistent with the overall dataset size and
the reported class distribution. The claim rate is rounded.

## Model Results

### Selected Model: Featuretools-Extended Decision Tree

The selected model combines the Decision Tree approach with the extended
feature set explored using Featuretools.

  Metric           Score
  ----------- ----------
  ROC-AUC        \~0.639
  Recall        \~73.07%
  Precision      \~8.79%

**Interpretation**

-   The model identified approximately 73.07% of the actual claim cases
    in the test set at the evaluated classification threshold.
-   Precision of approximately 8.79% indicates that most policies
    flagged as positive were not actual claim cases.
-   ROC-AUC of approximately 0.639 indicates modest ranking ability and
    leaves considerable scope for improvement.

The model may be useful as an **experimental prioritization signal** for
further analysis, but its low precision means that it could generate a
high volume of false-positive reviews. Its operational usefulness would
depend on review capacity, the cost of missed claims, the cost of
unnecessary reviews, and validation on future-period data.

> **Important:** These are reported results from the project's
> stratified test split. They should not be interpreted as guaranteed
> performance on future policies or on a different insurance portfolio.

## Key Business Insights

The analysis produced the following portfolio-level observations:

-   Approximately **6.4%** of policies in the dataset had a recorded
    claim.
-   Policyholder and vehicle attributes showed patterns worth
    investigating in relation to historical claim occurrence.
-   Feature engineering and automated feature generation were explored
    to capture additional relationships in the available data.
-   SHAP analysis helped identify the features most influential to the
    trained model's predictions.
-   Risk-band segmentation showed increasing claim rates among
    higher-ranked risk groups in the analyzed data.
-   The workflow provides a repeatable starting point for portfolio
    analysis, model evaluation, and risk-review prioritization.

These findings are descriptive or model-based observations from the
available dataset. They do not establish causal relationships or prove
that the same patterns will persist in future periods.

## Technology Stack

  Area                             Tools and technologies
  -------------------------------- ------------------------
  Programming and data analysis    Python, Pandas, NumPy
  Machine learning                 Scikit-learn
  Automated feature engineering    Featuretools
  Hyperparameter optimization      Optuna
  Explainable AI                   SHAP
  Model monitoring and reporting   Evidently AI
  Data visualization               Matplotlib, Seaborn
  Business intelligence            Power BI, DAX
  Application development          Streamlit

## Repository Structure

``` text
.
├── app.py
├── notebooks/
│   ├── Notebook_1_Portfolio_Analysis.ipynb
│   ├── Notebook_2_Feature_Engineering.ipynb
│   └── Notebook_3_Modeling.ipynb
│
├── data/
│   └── aggregates/
│
├── dashboard/
│   ├── SafeDrive_Dashboard.pbix
│   └── DAX_Reference.md
│
├── reports/
│   └── Final_Report.pdf
│
├── artifacts/
│   ├── Evidently_Report.html
│   └── Model_Metadata.json
│
├── images/
│
└── README.md
```

*Note: This structure describes the intended repository layout. Keep the
README synchronized with the files actually committed to the
repository.*

## Run Locally

### Prerequisites

-   Python installed.
-   Git installed (if cloning the repository).
-   Power BI Desktop, if you want to open the `.pbix` dashboard.

### 1. Clone the repository

Replace the placeholder below with your actual GitHub repository URL.

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (Command Prompt):**

``` bash
.venv\Scripts\activate
```

**Windows (PowerShell):**

``` powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

``` bash
source .venv/bin/activate
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` is included in the repository and lists
the dependencies required by the application.

### 5. Launch the Streamlit application

``` bash
streamlit run app.py
```

Open the local URL printed in the terminal. Streamlit commonly uses:

``` text
http://localhost:8501
```

### Data and artifact availability

The repository intentionally excludes raw policy-level data and certain
sensitive or environment-specific artifacts. The application may
therefore require locally supplied data or generated artifacts that are
not included in the public repository. Check the project code and setup
instructions before running it.

## Data Privacy

To protect sensitive information, this repository intentionally
excludes:

-   Raw policy-level datasets.
-   Personally identifiable information (PII).
-   Row-level prediction outputs.
-   Serialized model files.
-   MLflow databases.
-   Proprietary business information.

Only approved aggregated outputs, visualizations, reports, and project
artifacts are intended to be shared.

Do not commit confidential, personally identifiable, or licensed data to
a public repository. Review generated reports and screenshots for
accidental disclosure before publishing.

## Limitations and Responsible Use

This project is a portfolio prototype and has several important
limitations:

1.  **Validation design:** Evaluation used a stratified train-test split
    rather than a time-based split. This does not establish how the
    model would perform on policies written in a later period.
2.  **Class imbalance:** Claim cases represent approximately 6.4% of the
    dataset. Precision, recall, the classification threshold, and the
    volume of flagged policies must be considered together.
3.  **Low precision:** The reported precision of approximately 8.79%
    suggests that many flagged policies are false positives. Human
    review capacity and the cost of false positives need to be
    evaluated.
4.  **Risk-band interpretation:** Risk bands represent relative ranking
    segments. They should not be interpreted as calibrated claim
    probabilities.
5.  **Explainability:** SHAP describes model behavior and feature
    contributions, not causal relationships.
6.  **Generalization:** Results from this dataset may not generalize to
    other portfolios, customer populations, products, or time periods.
7.  **No production claim:** The project does not establish production
    deployment performance, measurable financial impact, or improved
    underwriting outcomes.
8.  **Responsible use:** Model outputs should not be used as the sole
    basis for policy pricing, acceptance, rejection, or other
    consequential decisions.

A stronger future validation process would include temporal holdout
testing, probability calibration where appropriate, threshold selection
based on business costs, segment-level performance checks, and
monitoring on new data.

## Potential Future Improvements

Possible next steps include:

-   Implement time-based train, validation, and test splits.
-   Compare additional models, such as Random Forest, XGBoost, and
    LightGBM.
-   Tune classification thresholds using an explicit business-cost
    framework.
-   Evaluate precision-recall curves and precision at a defined review
    capacity.
-   Calibrate predicted probabilities if probability estimates are
    required.
-   Assess performance across relevant customer and vehicle segments.
-   Add data-drift and model-performance monitoring using new,
    representative data.
-   Track model versions and experiments with MLflow.
-   Improve application documentation, reproducibility, and deployment
    readiness.

------------------------------------------------------------------------

## Project Takeaway

SafeDrive Insurance Claims Analytics demonstrates an end-to-end approach
to insurance portfolio analysis, claim-likelihood classification,
explainable machine learning, and business intelligence.

By combining Python-based analytics, automated feature engineering,
model evaluation, SHAP explanations, Evidently AI reporting, Power BI,
and Streamlit, the project illustrates how analytical workflows can help
stakeholders better understand historical claims and explore risk-review
prioritization.

**The central outcome is a documented proof of concept---not a
production underwriting model or a guarantee of future claim prediction
performance.**
