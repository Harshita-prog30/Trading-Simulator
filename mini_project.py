from tabulate import tabulate
from colorama import Fore, Style, init
import matplotlib.pyplot as plt

# Initialize colorama
init(autoreset=True)

# Initial setup
amount = 1000
portfolio = 0
money_end = amount
investment = []
transaction_cost = 0.0075
trade_history = []  # to store all trades

# Tracking for graphs
money_history = [money_end]
portfolio_history = [portfolio]
networth_history = [money_end]


# Buy function
def buy(quantity, price):
    global portfolio, money_end
    allocated_money = quantity * price
    total_cost = allocated_money + transaction_cost * allocated_money
    money_end -= total_cost
    portfolio += quantity

    if not investment:
        investment.append(allocated_money)
    else:
        investment.append(investment[-1] + allocated_money)

    trade_history.append(["BUY", quantity, price, round(total_cost, 2), portfolio, round(money_end, 2)])
    money_history.append(round(money_end, 2))
    portfolio_history.append(portfolio)
    networth_history.append(round(money_end + portfolio * price, 2))

    print(
        Fore.GREEN + f"✅ Bought {quantity} units at {price}, Remaining Money: {round(money_end, 2)}, Portfolio: {portfolio}")


# Sell function
def sell(quantity, price):
    global portfolio, money_end
    allocated_money = quantity * price
    total_gain = allocated_money - transaction_cost * allocated_money
    money_end += total_gain
    portfolio -= quantity

    investment.append(investment[-1] - allocated_money)

    trade_history.append(["SELL", quantity, price, round(total_gain, 2), portfolio, round(money_end, 2)])
    money_history.append(round(money_end, 2))
    portfolio_history.append(portfolio)
    networth_history.append(round(money_end + portfolio * price, 2))

    print(
        Fore.RED + f"📉 Sold {quantity} units at {price}, Remaining Money: {round(money_end, 2)}, Portfolio: {portfolio}")


# Example trades
buy(5, 100)  # Buy 5 stocks at 100
buy(3, 120)  # Buy 3 stocks at 120
sell(4, 150)  # Sell 4 stocks at 150
buy(2, 130)  # Buy 2 stocks at 130

# Final status
print("\n" + "-" * 40)
print(Fore.CYAN + Style.BRIGHT + "📊 Final Portfolio Summary")
print("-" * 40)

headers = ["Action", "Quantity", "Price", "Amount", "Portfolio", "Money Left"]
print(tabulate(trade_history, headers=headers, tablefmt="fancy_grid"))

total_investment = investment[-1] if investment else 0
net_worth = money_end + portfolio * 150  # assuming last market price = 150
profit_loss = net_worth - amount

print(f"\n💰 Starting Money: {amount}")
print(f"🏦 Money Left: {round(money_end, 2)}")
print(f"📦 Stocks in Portfolio: {portfolio}")
print(f"📈 Net Worth: {round(net_worth, 2)}")

if profit_loss >= 0:
    print(Fore.GREEN + f"🚀 Profit: +{round(profit_loss, 2)}")
else:
    print(Fore.RED + f"🔻 Loss: {round(profit_loss, 2)}")

# -------------------------
# 📊 PLOTTING GRAPHS
# -------------------------
plt.figure(figsize=(12, 6))

# Money History Graph
plt.subplot(1, 3, 1)
plt.plot(money_history, marker="o", label="Money Left")
plt.title("Money Over Time")
plt.xlabel("Trades")
plt.ylabel("Money")
plt.legend()
plt.grid(True)

# Portfolio History Graph
plt.subplot(1, 3, 2)
plt.plot(portfolio_history, marker="o", color="orange", label="Stocks in Portfolio")
plt.title("Portfolio Over Time")
plt.xlabel("Trades")
plt.ylabel("Stocks")
plt.legend()
plt.grid(True)

# Net Worth Graph
plt.subplot(1, 3, 3)
plt.plot(networth_history, marker="o", color="green", label="Net Worth")
plt.title("Net Worth Over Time")
plt.xlabel("Trades")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
