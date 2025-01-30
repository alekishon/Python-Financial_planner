import pandas as pd  # Helps load and work with CSV files easily.
import csv
from datetime import datetime  # Helps work with date and time for this project.
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt  # Used for plotting graphs.

class CSV:
    # Define the CSV file name and the columns it should contain.
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    FORMAT = "%d-%m-%Y"  # Date format used in the CSV.

    @classmethod
    def initialize_csv(cls):
        """Checks if the CSV file exists, if not, creates it with predefined columns."""
        try:
            pd.read_csv(cls.CSV_FILE)  # Try reading the CSV file.
        except FileNotFoundError:  # If the file does not exist, create a new one.
            df = pd.DataFrame(columns=cls.COLUMNS)  # Create an empty DataFrame.
            df.to_csv(cls.CSV_FILE, index=False)  # Save it as a CSV file.

    @classmethod
    def add_entry(cls, Date, Amount, Category, Description):
        """Adds a new transaction entry to the CSV file."""
        new_entry = {
            "Date": Date,
            "Amount": Amount,
            "Category": Category,
            "Description": Description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)  # Append the new entry to the CSV.
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        """Fetches transactions between a given date range and calculates summary statistics."""
        df = pd.read_csv(cls.CSV_FILE)  # Load the CSV file into a DataFrame.
        df["Date"] = pd.to_datetime(df["Date"], format=CSV.FORMAT)  # Convert date column to datetime format.

        # Convert user input dates to datetime objects.
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        # Filter transactions that fall within the date range.
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(CSV.FORMAT)}))

            # Calculate income, expenses, and net savings.
            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()

            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${total_income - total_expense:.2f}")

            return filtered_df

def add():
    """Prompts the user for transaction details and adds them to the CSV."""
    CSV.initialize_csv()  # Ensure the CSV file exists.
    Date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date:", allow_default=True)
    Amount = get_amount()
    Category = get_category()
    Description = get_description()
    CSV.add_entry(Date, Amount, Category, Description)

def plot_transactions(df):
    """Generates a plot of income and expenses over time and saves it as an image."""
    df.set_index('Date', inplace=True)  # Set 'Date' as the index for time series analysis.

    # Resample the data by day and fill missing values with zero.
    income_df = df[df['Category'] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df['Category'] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    # Create the plot.
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["Amount"], label="Income", color="g")  # Plot income in green.
    plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="r")  # Plot expense in red.
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)

    # Save the plot as an image.
    plt.savefig("transaction_plot.png")
    print("Plot saved as 'transaction_plot.png'.")

def main():
    """Main menu to interact with the user."""
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()  # Call function to add a transaction.
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if df is not None and input("Do you want to see a plot? (y/n): ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed.