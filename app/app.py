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

# ----------------------------------------------

# Without @st.cache_data:This runs every time the app reruns (which happens often).
# With @st.cache_data:It runs only once, then Streamlit remembers the output 
@st.cache_data
# load data safely
def loading_data():
    try:
        return pd.read_csv(DATA_PATH, parse_dates=["date"])
    except Exception as e:
        st.error("⚠️ Error loading the data: " + str(e))
        return pd.DataFrame(columns=["date", "amount", "category", "type"])

transactions_df = loading_data()

#  Ensure datetime format - ensuring the date column to be converted using pd.to_datetime() with errors='coerce'.
transactions_df["date"] = pd.to_datetime(transactions_df["date"], errors="coerce")

if transactions_df["date"].isnull().any():
    st.error("❌ Invalid date values.")
    st.stop()

transactions_df["month"] = transactions_df["date"].dt.to_period("M")

st.header("➕ Add a New Transaction")

# st.form is used to avoid re running the script
# clear_on_submit is used to automatically clear inputs
with st.form("transaction_form", clear_on_submit=True):
    # creating two equal width columns
    column1, column2 = st.columns(2)
    # user can select any date
    date = column1.date_input("Date")
    # user can input amount- only decimal value and no negative numbers
    amount = column2.number_input("Amount", min_value=0.0, format="%.2f")
    # new row of two columns
    column3, column4 = st.columns(2)
    # simple text box to enter category
    category = column3.text_input("Category")
    # shows a dropdown for income and expense
    tx_type = column4.selectbox("Type", ["Income", "Expense"])
    # submit button
    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        # creating a dataframe with user submitted values, also converted date to datetime
        new_tx = pd.DataFrame(
            [[pd.to_datetime(date), amount, category, tx_type]],
            columns=["date", "amount", "category", "type"]
        )
        try:
            # loading the existing csv
            existing = pd.read_csv(DATA_PATH, parse_dates=["date"])
            # appending the new transaction to existing ones
            combined = pd.concat([existing, new_tx], ignore_index=True)
            # saving updated data to csv
            combined.to_csv(DATA_PATH, index=False)
            st.success("✅ Transaction added successfully!")
            # to clear cache data
            st.cache_data.clear()
            # reload th updated file
            transactions_df = loading_data()
            transactions_df["date"] = pd.to_datetime(transactions_df["date"], errors="coerce")
            transactions_df["month"] = transactions_df["date"].dt.to_period("M")
         # catching errors 
        except Exception as e:
            st.error(f"Error saving transaction: {e}")

# adding a section heading titled “Monthly Summary”
st.header("📋 Monthly Summary")
total_income = transactions_df[transactions_df["type"] == "Income"]["amount"].sum()
total_expense = transactions_df[transactions_df["type"] == "Expense"]["amount"].sum()
balance = total_income - total_expense

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"₹{total_income}")
col2.metric("Total Expenses", f"₹{total_expense}")
col3.metric("Balance", f"₹{balance}")

# creating a section heading: “Visualizations”
st.header("🧮 Visualizations")
# taking the dataframe and keeping only the row expense
expense_df = transactions_df[transactions_df["type"] == "Expense"]
if not expense_df.empty:
    # groups all expenses by category and sums up the sum in each category
    category_expense = expense_df.groupby("category")["amount"].sum().sort_values()
    # plotting the pie chart
    figure1, ax1 = plt.subplots(figsize=(3, 2))
    # category_expense.plot(kind="pie", ax=ax1, color="blue")

    # adding a custom color pallette
    custom_colors = ['#9C27B0', '#7E57C2', '#BA68C8', '#9575CD', '#B39DDB',
                 '#CE93D8', '#D1C4E9', '#E1BEE7', '#F3E5F5', '#EDE7F6']

    wedges, texts, autotexts = ax1.pie(
        category_expense,
        labels=category_expense.index,
        autopct="%1.1f%%",
        startangle=90,
        radius=0.8,
        colors=custom_colors[:len(category_expense)]
    )

    # Setting font size for labels
    for text in texts:
        text.set_fontsize(4) 

    # Seting font size for percentage labels
    for autotext in autotexts:
        autotext.set_fontsize(4)

    ax1.set_title("Expenses by Category", fontsize=5)
    ax1.tick_params(labelsize=6)
    plt.tight_layout()
    st.pyplot(figure1)
else:
    st.info("No expense data to show.")

if not transactions_df.empty:
    # Groups by both month and type (Income or Expense) and sums the amount for each month/type
    monthly_summary = transactions_df.groupby(["month", "type"])["amount"].sum().unstack().fillna(0)
    # Calculates a new column: Balance = Income − Expense for each month
    monthly_summary["Balance"] = monthly_summary.get("Income", 0) - monthly_summary.get("Expense", 0)

    figure2, ax2 = plt.subplots(figsize=(5.5, 3.5))
    # monthly_summary[["Income", "Expense", "Balance"]].plot(ax=ax2, marker="o")
    monthly_summary[["Income", "Expense", "Balance"]].plot(
        kind="bar",
        ax=ax2,
        width=0.7,
        color=["#4caf50", "#f44336", "#2196f3"]  # Green, Red, Blue
    )
    ax2.tick_params(labelsize=3)
    ax2.set_title("Monthly Analysis", fontsize=7)
    ax2.set_xlabel("Month", fontsize=10)
    ax2.set_ylabel("Amount (₹)", fontsize=7)
    ax2.tick_params(axis='x', labelsize=6)
    ax2.tick_params(axis='y', labelsize=6)
    ax2.legend(fontsize=6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(figure2)

st.header("📄 All Transactions")
st.dataframe(transactions_df.sort_values(by="date", ascending=False))

