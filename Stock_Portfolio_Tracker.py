# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

# Taking user input
for i in range(n):
    stock_name = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in price list.")

# Calculating total investment
print("\n----- Portfolio Summary -----")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment

    print(f"{stock} -> Quantity: {qty}, Price: ${price}, Investment: ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to text file
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Summary\n")
file.write("------------------------\n")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    file.write(f"{stock} - Qty: {qty}, Price: ${price}, Investment: ${investment}\n")

file.write(f"\nTotal Investment Value: ${total_investment}")

file.close()

print("\nPortfolio saved to portfolio.txt")
