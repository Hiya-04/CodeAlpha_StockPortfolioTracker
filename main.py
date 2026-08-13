stock_prices = {
    "Reliance": 2850,
    "TCS": 3900,
    "Infosys": 1650,
    "Wipro": 540,
    "SBI": 870
}

ans = "yes"
total = 0

while ans == "yes":

    stock = input("Enter the name of the stock: ")

    if stock in stock_prices:
        print("The price for the stock you entered is:", stock_prices[stock])

        quantity = int(input("Now enter the quantity: "))

        # Calculate investment for this stock
        # Add it to total

    else:
        print("Stock not available!!")
        print("Available stocks are:")
        print(stock_prices)

    ans = input("Do you want to add another stock? (yes/no): ")

print("Total Investment =", total)