from datetime import datetime

def final_balance(A, D):
    # Initialize the balance and card payments for each month
    balances = {}
    card_payments = {}
    total_card_fee = 0  # Initialize total card fee

    # Process each transaction
    for amount, date in zip(A, D):
        date = datetime.strptime(date, '%Y-%m-%d')
        year, month = date.year, date.month

        # Ignore transactions not in 2020
        if year != 2020:
            continue

        # Update the balance and card payments for the month
        if month not in balances:
            balances[month] = 0
        balances[month] += amount

        if amount < 0:
            if month not in card_payments:
                card_payments[month] = []
            card_payments[month].append(amount)

    # Iterate over the months of 2020 after processing all transactions
    for month in range(1, 13):
        # Subtract the card fee if necessary
        if month not in card_payments or len(card_payments[month]) < 3 or sum(card_payments[month]) > -100:
            balances[month] = balances.get(month, 0) - 5
            total_card_fee += 5

    # Return the final balance
    return sum(balances.values())

# Test cases
print(final_balance([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))  # Expected output: 230
print(final_balance([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))  # Expected output: 25
print(final_balance([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))  # Expected output: -164
print(final_balance([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))  # Expected output: 80
print(final_balance([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))  # Expected output: -115
