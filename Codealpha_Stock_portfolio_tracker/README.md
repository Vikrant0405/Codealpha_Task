# Stock Portfolio Tracker

A simple command-line **Stock Portfolio Tracker** made in Python. It lets you:

- Add stocks to your portfolio (from a fixed list of available stocks)
- Remove stocks from your portfolio
- View a portfolio summary (symbol, quantity, price, value)
- Calculate total portfolio value
- View available stock prices
- Save your portfolio to a CSV file

> The project is implemented in: `codealpha_Stock_portfolio Tracker.py` (interactive CLI).

---

## Project Structure

- `codealpha_Stock_portfolio Tracker.py` — Main interactive program

---

## How to Run

1. Open the project folder in VS Code.
2. Run the script with Python:

```bash
python "codealpha_Stock_portfolio Tracker.py"
```

---

## Features / Menu Options

When the program runs, it shows a menu:

1. **Add stock** — Choose from predefined available stocks and add a quantity.
2. **Remove stock** — Remove a quantity of a stock you currently hold.
3. **View portfolio summary** — Displays each stock in your portfolio plus totals.
4. **Calculate total portfolio value** — Prints overall portfolio value.
5. **View available stocks & prices** — Shows the predefined stock list and prices.
6. **Save portfolio to CSV** — Exports your portfolio to a CSV file.
7. **Exit** — Ends the program.

---

## CSV Output

Selecting **6** prompts for a filename (without extension). The file is saved as:

- `<filename>.csv`

CSV columns:

- `Symbol`
- `Quantity`
- `Price (USD)`
- `Value (USD)`

The CSV also includes:

- an empty row
- a `TOTAL` row
- a `Saved on` timestamp

---

## Notes

- Stock prices and the available symbols are **hardcoded** in the script.
- The portfolio is stored in-memory while the program runs (it does not automatically persist between runs). CSV saving provides persistence.

---

## Requirements

- Python 3.x

No external libraries are required beyond Python's standard library.

