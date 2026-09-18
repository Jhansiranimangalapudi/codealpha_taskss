stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

total_investment = 0
portfolio = []

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        portfolio.append((stock, quantity, price, investment))
        total_investment += investment

        print(f"{stock}: {quantity} × ${price} = ${investment}")

    except ValueError:
        print("Please enter a valid number.")

# Display portfolio
print("\n=== Portfolio Summary ===")

for stock, quantity, price, investment in portfolio:
    print(f"{stock} | Quantity: {quantity} | Price: ${price} | Value: ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save result to a text file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("=== Stock Portfolio Summary ===\n")

        for stock, quantity, price, investment in portfolio:
            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${investment}\n"
            )

        file.write(f"\nTotal Investment Value: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")