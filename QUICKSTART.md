# Finance Budgeting App - Quick Start Guide

## What is this?

A command-line finance application that helps you partition your monthly salary/income into budget categories and track your spending throughout the month.

## Quick Start (3 Steps)

### Step 1: Run the Application
```bash
python3 finance_app.py
```

### Step 2: Set Your Monthly Income
Choose option `1` and enter your monthly income (e.g., $5000)

### Step 3: Create Budget Categories
Choose option `2` and create categories for your expenses. Example categories:
- Housing: $1500 (rent/mortgage)
- Food: $600 (groceries)
- Transportation: $300 (gas, parking)
- Savings: $1000 (emergency fund)
- Entertainment: $200 (fun activities)

### Step 4: Track Your Spending
As you spend money, choose option `5` to add expenses to the appropriate category.

### Step 5: Check Your Budget
Choose option `6` anytime to see how much you've spent and how much remains in each category.

## Example Session

```
1. Set Monthly Income → $5000
2. Create Category → Housing ($1500)
2. Create Category → Food ($600)
2. Create Category → Transportation ($300)
2. Create Category → Savings ($1000)
5. Add Expense → Housing: $1500 (Rent)
5. Add Expense → Food: $75 (Groceries)
6. View Budget Summary → See your current status
```

## Features at a Glance

✅ **Set monthly income** - Track your total monthly funds
✅ **Create budget categories** - Organize spending into categories
✅ **Allocate funds** - Decide how much goes to each category
✅ **Track expenses** - Record spending with descriptions
✅ **View summaries** - See spending vs. budget in real-time
✅ **Data persistence** - All data automatically saved

## Benefits

- 🎯 **Clear visibility** - Know exactly where your money goes
- 💰 **Better control** - Prevent overspending
- 📊 **Financial awareness** - Make informed spending decisions
- 💾 **No data loss** - Everything is automatically saved

## Need More Details?

See [FINANCE_APP_README.md](FINANCE_APP_README.md) for complete documentation.

## Run Example Demo

```bash
python3 example_usage.py
```

This shows how the app works with sample data.

## Run Tests

```bash
python3 test_finance_app.py
```

Verifies all functionality works correctly.
