from random import randint, choice
import pandas as pd

# Define customer and bank names
customer_names = ["John Doe", "Jane Smith", "Michael Brown", "Sarah Lee", "David Miller"]
bank_names = ["Citibank", "Chase", "Bank of America", "Wells Fargo", "PNC"]

# Define debit card types
card_types = ["Visa", "Mastercard"]

# Define number of transactions per day
transactions_per_day = 10

# Dictionary to store customer information (combined)
customer_info = {}


def generate_transaction(customer_name, current_date):
    """Generates a mock transaction record with a specific date"""
    if customer_name not in customer_info:
        # Generate card number and bank for new customer
        card_number = f"{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}"
        bank_name = choice(bank_names)
        customer_info[customer_name] = {
            "customer_id": randint(1000000000, 9999999999),  # 10-digit customer ID
            "debit_card_number": card_number,
            "debit_card_type": choice(card_types),
            "bank_name": bank_name,
        }

    # Use retrieved information and add customer name
    transaction_data = customer_info[customer_name].copy()
    transaction_data["name"] = customer_name
    # Set transaction date to the current day
    transaction_date = str(current_date)
    amount = round(randint(10, 100) + randint(0, 99) / 100, 2)  # Up to 2 decimal places
    transaction_data["transaction_date"] = transaction_date
    transaction_data["amount_spend"] = amount
    return transaction_data


def generate_transactions(num_transactions, current_date):
    """Generates a list of mock transaction records for a specific date"""
    transactions = []
    for _ in range(num_transactions):
        transactions.append(generate_transaction(choice(customer_names), current_date))
    return transactions


def write_to_csv(data, filename):
    """Write data to a CSV file using pandas"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Generated mock transaction data in {filename}")
    return


def generate_data(current_date, date_str):
    """Generates data and creates csv files"""
    transactions = generate_transactions(transactions_per_day, current_date)
    write_to_csv(transactions, f"/tmp/transactions_{date_str}.csv")

    print(f"Generated mock transaction data transactions_{date_str}.csv and saved in csv files")
    return