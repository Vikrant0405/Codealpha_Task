import os
import csv
from datetime import datetime

stock= {"AAPL": 230,
    "MSFT": 520,
    "GOOGL": 195,
    "AMZN": 240,
    "META": 790,
    "TSLA": 345,
    "NVDA": 180,
    "NFLX": 1300,
    "TCS": 256,
    "INFY": 145,
    "WIPRO": 42,
    "HCLTECH": 58,
    "RELIANCE": 170,
    "TATAMOTORS": 84,
    "MARUTI": 98,
    "HDFCBANK": 76,
    "ICICIBANK": 39,
    "SBIN": 95,
    "ITC": 48,
    "LT": 410}

Portfolio= { }
def remove_stock():
    print_title("Remove Stock from Portfolio")
    if not Portfolio:
        print("Your Portfolio is empty . There is nothing to remove")
        return
    symbol = input("\nEnter the Stock Name To Remove = ").strip().upper()
    if symbol not in Portfolio:
        print(f"You Don't Own any share of {symbol}.")
        return

    qty_input = input(f"\nEnter Quantity of {symbol} shares to remove= ")
    try:
        quantity = int(qty_input)
        if quantity <= 0:
            print("Quantity should me in positive")
            return
    except ValueError:
        print("Quantity Should be whole number")
        return
    Portfolio[symbol] -= quantity
    
    if Portfolio[symbol] == 0:
        del Portfolio[symbol]
    print(f"✅ Removed {quantity} share(s) of {symbol}.")



def show_available_stock():
    print_title("Available Stock")
    print("-" * 50)
    print(f"{'Symbol':<15} {'Price'}")
    print("-"*50)
    for symbol,price in stock.items():
        print(f"{symbol:<15} {price}")

def add_stock():
    print_title("add new stock")
    show_available_stock()
    symbol = input("\nEnter the Stock Name = ").strip().upper()
    print(symbol)

    if symbol not in stock:
        print(f"Error {symbol} is not in list ")
        return
    qty_input = input(f"\nEnter Quantity of {symbol} shares to add = ")
    try:
        quantity = int(qty_input)
        if quantity <= 0:
            print("Quantity should me in positive")
    except ValueError:
        print("Quantity Should be whole number")

    Portfolio[symbol] =Portfolio.get(symbol,0)+ quantity
    print(f"✅ Added {quantity} share(s) of {symbol}. "
          f"\nTotal held: {Portfolio[symbol]} share(s).")

def calculate_stock_value(syn,qty):
    return stock[syn]*qty

def calculate_profile_value():
    return sum(calculate_stock_value(syn,qty) for syn,qty in Portfolio.items())

def profile_summary():
    print_title("Profile Summary")
    if not Portfolio:
        print("Your Portfolio is currently empty .")
        print("Use Option 1 to add share")
    print(f"{'Symbol':<15}{'Quantity':<12}{'Price':<12}{'Value':<12}")
    # print(Portfolio)
    total_value =0
    for sym,qty in Portfolio.items():
        # print(Portfolio)
        # print(sym , qty)
        price= stock[sym]
        # print(price)
        value = calculate_stock_value(sym ,qty)
        # print(value)
        total_value += value
        print(f"{sym:<15}{qty:<12}{price:<12}{value:<12}")

    print("-"*55)
    print(f"{'Total Portfolio Value':<39}{total_value}")

def print_title(title):
    print( "*"*50)
    print(title.center(50).upper())
    print("*"*50)

def total_profile_value():
    print_title("Profile Value")
    if not Portfolio:
        print("Portfolio is Empty")
    print(f"Total Portfolio value : ${calculate_profile_value()}")


def save_to_csv():
    print_title("Save Portfolio to CSV")

    if not Portfolio:
        print("❌ Portfolio is empty. Nothing to save.")
        return

    filename = input("Enter filename (without extension, default 'portfolio'): ").strip()
    if not filename:
        filename = "portfolio"
    filename = f"{filename}.csv"

    try:
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])

            total_value = 0.0
            for symbol, quantity in sorted(Portfolio.items()):
                price = stock[symbol]
                value = calculate_stock_value(symbol, quantity)
                total_value += value
                writer.writerow([symbol, quantity, f"{price:.2f}", f"{value:.2f}"])

            writer.writerow([])
            writer.writerow(["", "", "TOTAL", f"{total_value:.2f}"])
            writer.writerow(["Saved on:", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

        full_path = os.path.abspath(filename)
        print(f"✅ Portfolio saved successfully to: {full_path}")

    except (OSError, IOError) as e:
        print(f"❌ Error: Could not save file. {e}")



def show_menu():
    print_title("📈 STOCK PORTFOLIO TRACKER")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio summary")
    print("4. Calculate total portfolio value")
    print("5. View available stocks & prices")
    print("6. Save to csv")
    print("7. Exit")


def main():
    print_title("Welcome to Stock Portfolio Tracker")
    while (True):
        show_menu()
        print("")
        choice = input("Enter the option (1-7) = ".strip())

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "5":
            show_available_stock()
        elif choice == "3":
            profile_summary()
        elif choice == "4":
            total_profile_value()
        elif choice == "6":
            save_to_csv()
        elif choice == "7":
            print("Thank you for using ")
            break
        else:
            print("Invalid Choice")

        input("\n Press Enter TO Continue......")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.bye! 👋")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
     