# Financial Planner App
A Python-based financial tracking tool to help you log and manage your income and expenses. This application allows you to:
- Add transactions (income or expense).
- View transaction summaries for any date range.
- Generate visual charts comparing income vs. expenses over time.

## Features
- **Track daily transactions**: Log both income and expenses.
- **View financial summaries**: Get a summary of income, expenses, and net savings within a specific date range.
- **Generate visual charts**: Plot income and expenses over time using matplotlib.
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/financial-planner.git
    cd financial-planner
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure your `finance_data.csv` file is created:
    - The app will automatically create this file if it doesn't already exist when you add your first transaction.

## Usage

Run the app using the following command:

```bash
python main.py