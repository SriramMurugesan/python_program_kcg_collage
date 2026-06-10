# Stock Buy and Sell (Maximum Profit)
prices = [7, 1, 5, 3, 6, 4]
max_profit = 0

# Try all possible buy and sell days
for i in range(len(prices)):
    buy_price = prices[i]
    for j in range(i + 1, len(prices)):
        sell_price = prices[j]
        profit = sell_price - buy_price
        
        if profit > max_profit:
            max_profit = profit

print("Maximum profit:", max_profit)
