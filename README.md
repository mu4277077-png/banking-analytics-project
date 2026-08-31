# Banking Customer & Loan Risk Analytics

## Business Problem
Bank ko apne customer base ko better samajhna hai taake loan default risk kam ho, high-value customers retain hon, aur regional growth opportunities identify ho sakein.

## Dataset
Synthetic banking dataset — 2000 customers, columns: Age, Gender, Income, Region, AccountType, AccountBalance, CreditScore, LoanType, LoanAmount, InterestRate, LoanStatus, CustomerTenure, Transaction data.

## Methodology
1. Data Cleaning (Python/Pandas)
2. Descriptive Analysis (groupby summaries)
3. SQL Analysis (SQLite queries)
4. Exploratory Data Analysis (visualizations)
5. Statistical Analysis (correlation)
6. KPI Development
7. Customer & Loan Risk Segmentation

## Key Performance Indicators
- Total Customers: 2000
- Loan Approval Rate: 50.33%
- Loan Rejection Rate: 22.51%
- Average Account Balance: 121985.10
- Average Credit Score: 645.14
- Active Customers: 98.15%
- Average Customer Tenure: 4.55 years

## Business Insights
1. Approval aur rejection rate ke beech gap dikhata hai ke bank ka risk filtering kaafi selective hai.
2. Average credit score (645) industry ke "fair" range mein hai — approval decisions ismein important role play karte hain.
3. 98% customers active hain (5+ transactions/month) — overall engagement healthy hai.
4. Average tenure 4.55 years dikhata hai ke customer base majorly mid-term relationship wala hai.

## Business Recommendations
1. Rejected customers (22.51%) ke liye credit-improvement guidance program shuru karein.
2. High-balance regions identify kar ke unko premium banking products offer karein.
3. Low-tenure customers ke liye onboarding/engagement campaigns banayein taake retention improve ho.

## Visualizations
See PNG files in this repository: age_distribution.png, Income_distribution.png, Balance_by_accountype.png, correlation_heatmap.png, Loan_status_count.png

## Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, SQLite