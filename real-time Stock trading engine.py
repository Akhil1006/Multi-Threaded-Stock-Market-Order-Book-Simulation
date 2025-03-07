# Importing Modules as Requirement
import random
import threading
import time

# Defining Constants
NUM_TICKERS = 1024 # Number of unique ticker symbols
MAX_QUANTITY = 110 # Maximum quantity for an order
MAX_PRICE = 1100 ## Maximum price for an order

# Order book for each ticker Data Structure
order_books = [[] for _ in range(NUM_TICKERS)]  # Initialize order books for each ticker

# Lock for thread-safe operations
order_book_lock = threading.Lock()  

# Counter to track the number of cycles (Because Inifinate cycles makes difficulty to find output) 
cycle_counter = 0
cycle_limit = 50  # Stop after 50 cycles

def addOrder(order_type, ticker_symbol, quantity, price):
    """
    1. Adds an order to the order book.
    
    :param order_type: 'Buy' or 'Sell'
    :param ticker_symbol: Ticker symbol (0 to 1023)
    :param quantity: Quantity of the order
    :param price: Price of the order
    """
    with order_book_lock:
        order_books[ticker_symbol].append({
            'type': order_type,
            'quantity': quantity,
            'price': price
        })
        print(f"Added {order_type} order for Ticker {ticker_symbol}: Quantity {quantity}, Price {price}")

# Matching Orders
def matchOrder(ticker_symbol):
    """
    2. Matches buy and sell orders for a given ticker symbol.
    
    :param ticker_symbol: Ticker symbol (0 to 1023)
    """
    with order_book_lock:
        buy_orders = [order for order in order_books[ticker_symbol] if order['type'] == 'Buy']
        sell_orders = [order for order in order_books[ticker_symbol] if order['type'] == 'Sell']
        
        # Sort buy orders in descending order of price
        buy_orders.sort(key=lambda x: -x['price'])
        
        # Sort sell orders in ascending order of price
        sell_orders.sort(key=lambda x: x['price'])
        
        matched = False
        for buy_order in buy_orders:
            for sell_order in sell_orders:
                if buy_order['price'] >= sell_order['price'] and buy_order['quantity'] > 0 and sell_order['quantity'] > 0:
                    # Determine the minimum quantity to match
                    match_quantity = min(buy_order['quantity'], sell_order['quantity'])
                    
                    # Execute the trade
                    print(f"Matched Buy Order (Price: {buy_order['price']}, Quantity: {match_quantity}) with Sell Order (Price: {sell_order['price']}, Quantity: {match_quantity}) for Ticker {ticker_symbol}")
                    
                    # Update the quantities
                    buy_order['quantity'] -= match_quantity
                    sell_order['quantity'] -= match_quantity
                    
                    matched = True
                    
                    # Remove orders with zero quantity
                    if buy_order['quantity'] == 0:
                        order_books[ticker_symbol].remove(buy_order)
                    if sell_order['quantity'] == 0:
                        order_books[ticker_symbol].remove(sell_order)
        
        if not matched:
            print(f"No matches found for Ticker {ticker_symbol}")

def simulateTrading():
    """
    Simulates active stock trading by randomly adding orders.
    """
    global cycle_counter
    while cycle_counter < cycle_limit:
        ticker_symbol = random.randint(0, NUM_TICKERS - 1)
        order_type = random.choice(['Buy', 'Sell'])
        quantity = random.randint(1, MAX_QUANTITY)
        price = random.randint(1, MAX_PRICE)
        
        addOrder(order_type, ticker_symbol, quantity, price)
        matchOrder(ticker_symbol)
        
        cycle_counter += 1  # Increment the cycle counter
        time.sleep(random.random())  # Random delay to simulate real-time trading
    
    print(f"Simulation stopped after {cycle_limit} cycles.")

# Start the simulation in a separate thread
simulation_thread = threading.Thread(target=simulateTrading)
simulation_thread.daemon = True
simulation_thread.start()

# Keep the main thread alive to allow the simulation to run
try:
    while cycle_counter < cycle_limit:
        time.sleep(1)
except KeyboardInterrupt:
    print("Simulation stopped manually.")