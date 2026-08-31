import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 


df=pd.read_csv("banking_dataset.csv")
print("Shape of Data set Before Cleaning: ", df.shape)

df=df.drop_duplicates()

df["Income"]=df["Income"].fillna(df["Income"].median())
df["AccountBalance"]=df["AccountBalance"].fillna(df["AccountBalance"].median())
df["CreditScore"]=df["CreditScore"].fillna(df["CreditScore"].median())

df["LoanType"]=df["LoanType"].fillna("No Loan")
df["LoanStatus"]=df["LoanStatus"].fillna("No Loan")
df["InterestRate"]=df["InterestRate"].fillna(0)

df["LastTransactionDate"]=pd.to_datetime(df["LastTransactionDate"])

print("Shape after Cleaning", df.shape)
print(df.isna().sum())

# =========================Analysis====================
print(" Average Balanece By region: ")
print(df.groupby("Region")["AccountBalance"].mean())

print("Loan status count: ")
print(df["LoanStatus"].value_counts())

print("Average Transaction value By account Type :")
print(df.groupby("AccountType")["AvgTransactionValue"].mean())

approved_score=df[df["LoanStatus"]=="Approved"]["CreditScore"].mean()
rejected_score=df[df["LoanStatus"]=="Rejected"]["CreditScore"].mean()
print("Average credit score Approved: ",approved_score)
print("Avg Credit Score - Rejected :", rejected_score)

print("Income and Balance By Gender : ")
print(df.groupby("Gender")[["Income","AccountBalance"]].mean())

# ----------------SQL DataBase And Analysis--------------

conn=sqlite3.connect("banking.db")
df.to_sql("Customers", conn, if_exists="replace", index=False)

query1 = """
Select Region, AVG(AccountBalance) as AvgBalance
From customers
GROUP BY Region
ORDER BY AvgBalance DESC
"""
print("\nSQL - Region-wise Avg Balance:")
print(pd.read_sql(query1, conn))

query2 = """
Select LoanStatus, COUNT(*) as Count
FROM customers
GROUP BY LoanStatus
"""
print("\nSQL - Loan Status Count:")
print(pd.read_sql(query2, conn))

query3 = """
SELECT Region, COUNT(*) as HighValueCustomers
FROM customers
WHERE AccountBalance > 200000
GROUP BY Region
ORDER BY HighValueCustomers DESC
"""
print("\nSQL - High Value Customers by Region:")
print(pd.read_sql(query3, conn))
conn.close()


# ------------------EDA-------------

# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Age"],bins=20, kde=True)
plt.title("Age distrubution ")
plt.savefig("Income_distribution.png")
plt.show()

# income Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Income"],bins=30,kde=True)
plt.title("Income Distribution")
plt.savefig("Income_distribution.png")
plt.show()

# Account Balance by account type 
plt.figure(figsize=(8,5))
sns.boxplot(x="AccountType", y="AccountBalance", data=df)
plt.title("Account balance by account Type")
plt.savefig("Balance_by_accountype.png")
plt.show()

# Heat Map 
plt.figure(figsize=(10,6))
numeric_df=df.select_dtypes(include="number")
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# Loan status count plot
plt.figure(figsize=(8,5))
sns.countplot(x="LoanStatus", data=df)
plt.title("Loan status Distribution")
plt.savefig("Loan_status_count.png")
plt.show()


# KPI Development 

total_customers= len(df)

loan_customers = df[df["LoanStatus"] != "No Loan"]
approval_rate=(loan_customers["LoanStatus"]=="Approved").mean()*100

avg_balance=df["AccountBalance"].mean()

avg_credit_score= df["CreditScore"].mean()

rejection_rate=(loan_customers["LoanStatus"]=="Rejected").mean()*100

active_pct = (df["NumTransactionsLastMonth"] > 5).mean() * 100

avg_tenure=df["CustomerTenureYears"].mean()

print("--------------Indicator--------------------")
print("Total customers: ", total_customers)
print("Loan Approval Rate: {:.2f}%".format(approval_rate))
print("Loan Rejection Rate: {:.2f}%".format(rejection_rate))
print("Average Account Balance: {:.2f}".format(avg_balance))
print("Average Credit Score: {:.2f}".format(avg_credit_score))
print("Active Customers: {:.2f}%".format(active_pct))
print("Average Customer Tenure: {:.2f} years".format(avg_tenure))
print("Code is completely run")
