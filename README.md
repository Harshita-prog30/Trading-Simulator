
## Trading Simulator – Python Mini Project
 Overview
## This project is a Python-based trading simulator that allows users to buy and sell stocks, track their portfolio, and analyze performance over time. It is designed to demonstrate how investments, profits, and transaction costs affect trading decisions in a real-world-like scenario.

## Features

Virtual portfolio management with a fixed starting capital.
Buy and sell functionality with dynamic price handling.
Transaction cost simulation to represent brokerage charges.
Investment history tracking for every trade.
Tabular trade summary output using tabulate.
Data visualization of portfolio growth using matplotlib.

## Tech Stack

Programming Language: Python

Libraries:

tabulate – for tabular display of trades in the terminal.
matplotlib – for generating portfolio performance graphs.

## Example Usage
# Buy 5 stocks at 100
buy(5, 100)

# Buy 3 stocks at 120
buy(3, 120)

# Sell 4 stocks at 150
sell(4, 150)

## Sample Output

Trade Summary (Table):

Action	Quantity	Price	Portfolio	Money Left	Net Value
BUY	5	100	5	500.0	995.0
BUY	3	120	8	140.0	1939.0
SELL	4	150	4	730.0	2539.0

Graph: Portfolio value vs trades is automatically plotted after execution.

## Future Improvements

Integration of real-time stock prices using financial APIs (e.g., Yahoo Finance).
Support for multiple stocks in one portfolio.
Development of a web-based dashboard with Flask or Django for interactive visualization.
