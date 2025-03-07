# Multi-Threaded-Stock-Market-Order-Book-Simulation
An engine for trading stocks in real-time that simulates the matching of buy and sell orders. With a capacity of 1,024 tickers (stocks), the system guarantees effective order matching while avoiding race situations in a multi-threaded setting. Below is a synopsis of the main elements and features

1. addOrder Function:
adds buy or sell orders for a certain ticker symbol to the order book.
Order_type (Buy/Sell), ticker_symbol, quantity, and price are among the parameters.a 
lock-based thread-safe approach that avoids race situations.

2. function for matchOrder:
matches purchase and sell orders according to amount and price for a specific ticker symbol.
If the buy price is higher than or equal to the sell price, the buy order is matched with the lowest sell price that is available.
When n is the number of orders in the order book, the time complexity is O(n).
thread-safe and does not rely on built-in dictionaries or maps by using lock-free data structures (basic lists).

Simulation:
 To replicate real-time trading, a simulateTrading function generates buy and sell orders for various tickers at random.
 After 50 cycles, the simulation automatically ends.

Thread Security:
In a multi-threaded setting, a global lock (order_book_lock) guarantees that the order book can be changed securely.

constraints:
No maps, dictionaries, or other data structures are used.
No imports or external libraries for data structures.
It is a fully self-contained implementation.

How It Operates: 
The application mimics a stock exchange in which buy and sell orders are constantly updated and matched.
Each sublist in an order book, which is a list of lists, corresponds to a distinct ticker symbol.
By matching the highest buy price with the lowest sale price, the match order function makes sure that trades are carried out effectively.
To ensure regulated execution, the simulation ends after 50 cycles.

Goal:
1. This evaluation shows the capacity to:
2. Create and put into use a real-time trading platform.
3. Manage race situations and concurrency in a multi-threaded setting.
4. While following stringent guidelines, optimize for temporal complexity (O(n)).
5. Programmatically model actual trading situations.

Use Case:
More sophisticated trading engines, such those seen in stock exchanges, cryptocurrency trading platforms, or algorithmic trading systems, can be constructed using this technology as a core framework.

![0utput of Stock Trading Engine](https://github.com/user-attachments/assets/c71bef6a-b68e-4823-b8ce-a01765ee8c8b)


