🚗 SafeDrive Insurance Claims Analytics
End-to-End Insurance Risk Analytics | Predictive Modeling | Explainable AI | Business Intelligence

📌 Project Overview
Insurance companies face a constant challenge: identifying policies that are more likely to generate claims while maintaining healthy portfolio performance.

In this project, I developed an end-to-end analytics solution that combines exploratory data analysis, automated feature engineering, machine learning, model explainability, and business intelligence reporting to help prioritize higher-risk policies for review.

The solution demonstrates how data-driven risk assessment can support portfolio monitoring and claims-risk prioritization using historical insurance policy data.

🎯 Business Problem
SafeDrive Insurance wanted to better understand its policy portfolio and identify patterns associated with claim occurrence.

The objective was to:

Analyze policyholder and vehicle characteristics linked to claims.
Identify higher-risk policies within the portfolio.
Build predictive models capable of flagging potential claim cases.
Improve visibility into portfolio risk using interactive dashboards.
Provide explainable insights that support business decision-making.
Important: This project is a portfolio analytics and claim-likelihood classification prototype. It is not a production underwriting system and does not represent a validated future-period claim forecast.

🛠️ Project Approach
1. Portfolio & Claims Analysis
Performed exploratory data analysis (EDA) on historical insurance policy records to understand:

Claim distribution across the portfolio
Policyholder demographics and characteristics
Vehicle-related attributes
Risk indicators associated with claims
Overall portfolio claim trends
The analysis provided business-focused insights into portfolio composition and claim behavior.

2. Feature Engineering
Enhanced predictive performance through extensive feature engineering.

Manual Feature Creation
Risk indicator variables
Policyholder behavior metrics
Vehicle-related transformations
Automated Feature Engineering
Implemented Featuretools Deep Feature Synthesis (DFS) to automatically create higher-order interaction features and uncover hidden relationships in the data.

This significantly expanded the feature space for model training and evaluation.

3. Predictive Modeling
Built and compared multiple classification models for claim-likelihood prediction.

Baseline Model
Logistic Regression
Advanced Model
Decision Tree Classifier
Model Optimization
Hyperparameter tuning using Optuna
Stratified cross-validation
Performance comparison across evaluation metrics
Selection of the best-performing model based on claim detection capability
4. Model Evaluation
Models were evaluated using:

Accuracy
Precision
Recall
F1 Score
ROC-AUC
Given the business objective, special emphasis was placed on Recall, since missing actual claim cases can have a higher business cost than reviewing additional policies.

5. Model Explainability
Implemented SHAP (SHapley Additive Explanations) to:

Identify the most influential features
Explain model predictions
Improve transparency and interpretability
Support responsible AI practices
This allowed both technical and business stakeholders to understand key drivers behind the model's decisions.

6. Model Governance & Monitoring
Created governance and monitoring artifacts to support model transparency and validation:

Evidently AI monitoring reports
Model performance documentation
Validation summaries
Risk assessment outputs
7. Business Intelligence Dashboard
Developed an interactive Power BI dashboard to present:

Portfolio overview
Claim distribution analysis
Risk segmentation
KPI tracking
Portfolio monitoring metrics
Risk-band performance analysis
The dashboard enables business stakeholders to explore portfolio risk and identify areas requiring additional review.

8. Streamlit Application
Built an interactive Streamlit application that showcases:

Portfolio analytics
Model performance
Risk segmentation
SHAP explainability outputs
Business insights and recommendations
📊 Dataset Summary
Metric	Value
Total Policies	58,592
Features	49
Claim Cases	3,748
Claim Rate	6.40%
Test Set Size	11,719
Test Claims	750
Test Non-Claims	10,969
🏆 Results
Selected Model
Featuretools-Extended Decision Tree

Metric	Score
ROC-AUC	~0.639
Recall	~73.07%
Precision	~8.79%
Key Outcome
The final model successfully identifies a large proportion of claim cases and can be used as a risk-review prioritization tool.

While precision remains low due to class imbalance, the model effectively surfaces higher-risk policies for further investigation, making it useful for portfolio monitoring and claim-risk assessment.

📈 Key Business Insights
Approximately 6.4% of policies resulted in claims.
Feature engineering improved the model's ability to distinguish between claim and non-claim policies.
SHAP analysis highlighted the most influential features impacting claim predictions.
Risk-band segmentation showed increasing claim rates among higher-ranked risk groups.
The framework provides a repeatable approach for portfolio risk monitoring and prioritization.
🧰 Technology Stack
Programming & Data Analytics
Python
Pandas
NumPy
Scikit-Learn
Automated Feature Engineering
Featuretools
Hyperparameter Optimization
Optuna
Explainable AI
SHAP
Model Monitoring
Evidently AI
Data Visualization
Matplotlib
Seaborn
Power BI
Application Development
Streamlit
🗂️ Repository Structure
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
🚀 Run Locally
# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Launch application
streamlit run app.py
Open the local URL displayed in the terminal (typically http://localhost:8501).

🔒 Data Privacy
To protect sensitive information, this repository intentionally excludes:

Raw policy-level datasets
Personally identifiable information (PII)
Row-level prediction outputs
Serialized model files
MLflow databases
Proprietary business information
Only aggregated outputs, visualizations, reports, and project artifacts are included.

⚠️ Limitations
Validation was performed using a stratified train-test split rather than a time-based validation approach.
Risk bands represent relative ranking segments and should not be interpreted as calibrated probabilities.
SHAP explanations describe model behavior, not causal relationships.
This project does not claim production deployment performance or measurable financial impact.
Results should be interpreted as a proof-of-concept analytics solution and not an operational underwriting system.
