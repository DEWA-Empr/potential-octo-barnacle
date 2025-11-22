#!/usr/bin/env python3
"""
Example usage of the Finance Budgeting App

This script demonstrates how to use the FinanceBudgetApp class programmatically.
"""

from finance_app import FinanceBudgetApp, print_budget_summary


def example_usage():
    """Demonstrate example usage of the finance app."""
    
    # Clean up any existing example data
    import os
    if os.path.exists('example_budget.json'):
        os.remove('example_budget.json')
    
    # Create app instance with a custom data file
    app = FinanceBudgetApp('example_budget.json')
    
    print("Finance Budgeting App - Example Usage")
    print("=" * 60)
    
    # Set monthly income
    print("\n1. Setting monthly income to $5,000")
    app.set_monthly_income(5000.0)
    
    # Create budget categories
    print("\n2. Creating budget categories...")
    categories = [
        ("Housing", 1500.0),
        ("Food", 600.0),
        ("Transportation", 300.0),
        ("Utilities", 200.0),
        ("Savings", 1000.0),
        ("Entertainment", 400.0),
        ("Miscellaneous", 500.0)
    ]
    
    for name, amount in categories:
        app.create_category(name, amount)
        print(f"   - {name}: ${amount:,.2f}")
    
    # Add some expenses
    print("\n3. Adding some expenses...")
    expenses = [
        ("Housing", 1500.0, "Monthly rent"),
        ("Food", 75.0, "Groceries - Week 1"),
        ("Food", 82.50, "Groceries - Week 2"),
        ("Transportation", 45.0, "Gas"),
        ("Utilities", 65.0, "Electric bill"),
        ("Entertainment", 35.0, "Movie tickets"),
        ("Miscellaneous", 25.0, "Office supplies")
    ]
    
    for category, amount, description in expenses:
        app.add_expense(category, amount, description)
        print(f"   - {category}: ${amount:,.2f} ({description})")
    
    # Display budget summary
    print("\n4. Budget Summary:")
    print_budget_summary(app)
    
    # Demonstrate updating allocation
    print("\n5. Updating Food category allocation to $700")
    app.update_category_allocation("Food", 700.0)
    
    # Show updated summary
    print("\n6. Updated Budget Summary:")
    print_budget_summary(app)
    
    # Show budget insights
    summary = app.get_budget_summary()
    print("\n7. Budget Insights:")
    print("-" * 60)
    
    allocation_rate = (summary['total_allocated'] / summary['monthly_income']) * 100
    spending_rate = (summary['total_spent'] / summary['monthly_income']) * 100
    
    print(f"Allocation Rate: {allocation_rate:.1f}% of income")
    print(f"Spending Rate: {spending_rate:.1f}% of income")
    print(f"Savings Rate: {100 - spending_rate:.1f}% of income")
    
    # Find categories with highest spending
    print("\n8. Top Spending Categories:")
    print("-" * 60)
    sorted_categories = sorted(
        summary['categories'].items(),
        key=lambda x: x[1]['spent'],
        reverse=True
    )
    
    for i, (name, data) in enumerate(sorted_categories[:3], 1):
        percentage = (data['spent'] / summary['total_spent']) * 100 if summary['total_spent'] > 0 else 0
        print(f"{i}. {name}: ${data['spent']:,.2f} ({percentage:.1f}% of total spending)")
    
    # Show categories with most budget remaining
    print("\n9. Categories with Most Budget Remaining:")
    print("-" * 60)
    sorted_remaining = sorted(
        summary['categories'].items(),
        key=lambda x: x[1]['remaining'],
        reverse=True
    )
    
    for i, (name, data) in enumerate(sorted_remaining[:3], 1):
        print(f"{i}. {name}: ${data['remaining']:,.2f} remaining")
    
    print("\n" + "=" * 60)
    print("Example completed! Data saved to 'example_budget.json'")
    print("=" * 60)


if __name__ == "__main__":
    example_usage()
