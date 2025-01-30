from datetime import datetime

# Define the date format
date_format = "%d-%m-%Y"

# Define the valid categories for transactions
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    """
    Prompt the user to enter a date. If allow_default is True, pressing Enter will return today's date.
    Ensures the date is in the correct format (dd-mm-yyyy).
    """
    date_str = input(prompt)
    
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)  # Return today's date formatted correctly
    
    try:
        valid_date = datetime.strptime(date_str, date_format)  # Validate date format
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)  # Recursively prompt again on invalid input

def get_amount():
    """
    Prompt the user to enter a transaction amount. Ensures the amount is a positive number.
    """
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive, non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()  # Recursively prompt again on invalid input

def get_category():
    """
    Prompt the user to select a category ('I' for Income or 'E' for Expense).
    Returns the full category name based on input.
    """
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    
    if category in CATEGORIES:
        return CATEGORIES[category]  # Return the full category name (Income or Expense)
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()  # Recursively prompt again on invalid input

def get_description():
    """
    Prompt the user to enter a description for the transaction.
    Ensures the input is not empty.
    """
    description = input("Enter a description for the transaction: ").strip()
    
    if not description:
        print("Description cannot be empty. Please enter a valid description.")
        return get_description()  # Recursively prompt again on invalid input
    
    return description  # Return the valid description