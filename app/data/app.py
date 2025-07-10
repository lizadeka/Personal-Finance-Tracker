import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Finance Tracker", layout="wide")
st.title("💰 Personal Finance Tracker")

DATA_PATH = r"C:\Users\MY PC\Downloads\Data analysis\Python\personal-finance-tracker\app\data\transaction.csv"

# @st.cache_data
# def load_data():
#     try:
#         return pd.read_csv(DATA_PATH, parse_dates=["date"])
#     except Exception as e:
#         st.error("⚠️ Error loading data: " + str(e))
#         return pd.DataFrame(columns=["date", "amount", "category", "type"])

# df = load_data()

# # ➕ Add new transaction
# st.header("➕ Add a New Transaction")

# with st.form("transaction_form", clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     date = col1.date_input("Date")
#     amount = col2.number_input("Amount", min_value=0.0, format="%.2f")

#     col3, col4 = st.columns(2)
#     category = col3.text_input("Category")
#     tx_type = col4.selectbox("Type", ["Income", "Expense"])

#     submitted = st.form_submit_button("Add Transaction")
#     if submitted:
#         # new_tx = pd.DataFrame([{
#         #     "date": pd.to_datetime(date),
#         #     "amount": amount,
#         #     "category": category,
#         #     "type": tx_type
#         # }])
#         new_tx = pd.DataFrame([[pd.to_datetime(date), amount, category, tx_type]],
#                       columns=["date", "amount", "category", "type"])

#         try:
#             new_tx.to_csv(DATA_PATH, mode="a", header=False, index=False)
#             st.success("✅ Transaction added successfully!")

#             # 🔁 Reload updated data immediately
#             st.cache_data.clear()
#             df = load_data()

#         except Exception as e:
#             st.error(f"Error saving transaction: {e}")


# # 📊 Summary
# st.header("📊 Monthly Summary")
# total_income = df[df["type"] == "Income"]["amount"].sum()
# total_expense = df[df["type"] == "Expense"]["amount"].sum()
# balance = total_income - total_expense

# col1, col2, col3 = st.columns(3)
# col1.metric("Total Income", f"₹{total_income}")
# col2.metric("Total Expenses", f"₹{total_expense}")
# col3.metric("Balance", f"₹{balance}")


# # 📄 Raw data
# st.header("📄 All Transactions")
# st.dataframe(df.sort_values(by="date", ascending=False))

# @st.cache_data
# def load_data():
#     try:
#         return pd.read_csv(DATA_PATH, parse_dates=["date"])
#     except Exception as e:
#         st.error("⚠️ Error loading data: " + str(e))
#         return pd.DataFrame(columns=["date", "amount", "category", "type"])

# df = load_data()

# # ⛑ Ensure date column is in datetime format
# df["date"] = pd.to_datetime(df["date"], errors="coerce")

# # 🚨 Stop app if any bad dates found
# if df["date"].isnull().any():
#     st.error("❌ Some date values are invalid and could not be converted. Please check your CSV.")
#     st.stop()

# # ✅ Safe to use .dt now
# df["month"] = df["date"].dt.to_period("M")


# st.header("➕ Add a New Transaction")

# with st.form("transaction_form", clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     date = col1.date_input("Date")
#     amount = col2.number_input("Amount", min_value=0.0, format="%.2f")

#     col3, col4 = st.columns(2)
#     category = col3.text_input("Category")
#     tx_type = col4.selectbox("Type", ["Income", "Expense"])

#     submitted = st.form_submit_button("Add Transaction")

# if submitted:
#     new_tx = pd.DataFrame(
#         [[pd.to_datetime(date), amount, category, tx_type]],
#         columns=["date", "amount", "category", "type"]
#     )

#     try:
#         # Read, append, and save back to ensure no merging
#         existing = pd.read_csv(DATA_PATH)
#         updated = pd.concat([existing, new_tx], ignore_index=True)
#         updated.to_csv(DATA_PATH, index=False)
        
#         st.success("✅ Transaction added successfully!")
#         st.cache_data.clear()
#         df = load_data()
#     except Exception as e:
#         st.error(f"Error saving transaction: {e}")


# st.header("📊 Monthly Summary")
# total_income = df[df["type"] == "Income"]["amount"].sum()
# total_expense = df[df["type"] == "Expense"]["amount"].sum()
# balance = total_income - total_expense

# col1, col2, col3 = st.columns(3)
# col1.metric("Total Income", f"₹{total_income}")
# col2.metric("Total Expenses", f"₹{total_expense}")
# col3.metric("Balance", f"₹{balance}")

# st.header("📈 Visualizations")
# expense_df = df[df["type"] == "Expense"]
# if not expense_df.empty:
#     category_expense = expense_df.groupby("category")["amount"].sum().sort_values()
#     fig1, ax1 = plt.subplots()
#     category_expense.plot(kind="barh", ax=ax1, color="salmon")
#     ax1.set_title("Expenses by Category")
#     st.pyplot(fig1)
# else:
#     st.info("No expense data to show.")

# if not df.empty:
#     df["month"] = df["date"].dt.to_period("M")
#     monthly_summary = df.groupby(["month", "type"])["amount"].sum().unstack().fillna(0)
#     monthly_summary["Balance"] = monthly_summary.get("Income", 0) - monthly_summary.get("Expense", 0)

#     fig2, ax2 = plt.subplots()
#     monthly_summary[["Income", "Expense", "Balance"]].plot(ax=ax2, marker="o")
#     ax2.set_title("Monthly Financial Trend")
#     st.pyplot(fig2)

# st.header("📄 All Transactions")
# st.dataframe(df.sort_values(by="date", ascending=False))

@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_PATH, parse_dates=["date"])
    except Exception as e:
        st.error("⚠️ Error loading data: " + str(e))
        return pd.DataFrame(columns=["date", "amount", "category", "type"])

df = load_data()

# ✅ Ensure datetime format
df["date"] = pd.to_datetime(df["date"], errors="coerce")

if df["date"].isnull().any():
    st.error("❌ Some date values are invalid. Please fix your CSV.")
    st.stop()

df["month"] = df["date"].dt.to_period("M")

st.header("➕ Add a New Transaction")

with st.form("transaction_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    date = col1.date_input("Date")
    amount = col2.number_input("Amount", min_value=0.0, format="%.2f")

    col3, col4 = st.columns(2)
    category = col3.text_input("Category")
    tx_type = col4.selectbox("Type", ["Income", "Expense"])

    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        new_tx = pd.DataFrame(
            [[pd.to_datetime(date), amount, category, tx_type]],
            columns=["date", "amount", "category", "type"]
        )
        try:
            existing = pd.read_csv(DATA_PATH, parse_dates=["date"])
            combined = pd.concat([existing, new_tx], ignore_index=True)
            combined.to_csv(DATA_PATH, index=False)
            st.success("✅ Transaction added successfully!")
            st.cache_data.clear()
            df = load_data()
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            df["month"] = df["date"].dt.to_period("M")
        except Exception as e:
            st.error(f"Error saving transaction: {e}")

st.header("📋 Monthly Summary")
total_income = df[df["type"] == "Income"]["amount"].sum()
total_expense = df[df["type"] == "Expense"]["amount"].sum()
balance = total_income - total_expense

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"₹{total_income}")
col2.metric("Total Expenses", f"₹{total_expense}")
col3.metric("Balance", f"₹{balance}")

st.header("🧮 Visualizations")
expense_df = df[df["type"] == "Expense"]
if not expense_df.empty:
    category_expense = expense_df.groupby("category")["amount"].sum().sort_values()
    fig1, ax1 = plt.subplots(figsize=(4, 3))
    # category_expense.plot(kind="pie", ax=ax1, color="blue")
    ax1.pie(
        category_expense,
        labels=category_expense.index,
        autopct="%1.1f%%",
        startangle=90,
        radius=0.8  # 👈 Shrinks the pie size
    )
    ax1.set_title("Expenses by Category", fontsize=10)
    ax1.tick_params(labelsize=8)
    plt.tight_layout()
    st.pyplot(fig1)
else:
    st.info("No expense data to show.")

if not df.empty:
    monthly_summary = df.groupby(["month", "type"])["amount"].sum().unstack().fillna(0)
    monthly_summary["Balance"] = monthly_summary.get("Income", 0) - monthly_summary.get("Expense", 0)

    fig2, ax2 = plt.subplots(figsize=(4, 3))
    monthly_summary[["Income", "Expense", "Balance"]].plot(ax=ax2, marker="o")
    ax2.set_title("Monthly Financial Trend")
    ax2.tick_params(labelsize=8)
    plt.tight_layout()
    st.pyplot(fig2)

st.header("📄 All Transactions")
st.dataframe(df.sort_values(by="date", ascending=False))
