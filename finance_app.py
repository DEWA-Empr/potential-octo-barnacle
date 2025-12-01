#!/usr/bin/env python3
"""
Finance Budgeting Application

A seamless finance app that helps users partition or budget their funds or salaries each month.
"""

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional


class BudgetCategory:
    """Represents a budget category with allocated amount and expenses."""
    
    def __init__(self, name: str, allocated_amount: float):
        self.name = name
        self.allocated_amount = allocated_amount
        self.expenses: List[Dict[str, Any]] = []
    
    def add_expense(self, amount: float, description: str):
        """Add an expense to this category."""
        if not description or not description.strip():
            raise ValueError("Expense description cannot be empty")
        
        expense = {
            'amount': amount,
            'description': description.strip(),
            'date': datetime.now().isoformat()
        }
        self.expenses.append(expense)
    
    def get_total_spent(self) -> float:
        """Calculate total amount spent in this category."""
        return sum(expense['amount'] for expense in self.expenses)
    
    def get_remaining(self) -> float:
        """Calculate remaining budget for this category."""
        return self.allocated_amount - self.get_total_spent()
    
    def to_dict(self) -> Dict:
        """Convert category to dictionary for serialization."""
        return {
            'name': self.name,
            'allocated_amount': self.allocated_amount,
            'expenses': self.expenses
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'BudgetCategory':
        """Create category from dictionary."""
        category = cls(data['name'], data['allocated_amount'])
        category.expenses = data.get('expenses', [])
        return category


class FinanceBudgetApp:
    """Main application class for finance budgeting."""
    
    def __init__(self, data_file: str = 'budget_data.json'):
        self.data_file = data_file
        self.monthly_income: float = 0.0
        self.categories: Dict[str, BudgetCategory] = {}
        self.load_data()
    
    def set_monthly_income(self, income: float):
        """Set the monthly income/salary."""
        if income < 0:
            raise ValueError("Monthly income cannot be negative")
        self.monthly_income = income
        self.save_data()
    
    def create_category(self, name: str, allocated_amount: float):
        """Create a new budget category."""
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty")
        
        if allocated_amount < 0:
            raise ValueError("Allocated amount cannot be negative")
        
        name = name.strip()
        if name in self.categories:
            raise ValueError(f"Category '{name}' already exists")
        
        self.categories[name] = BudgetCategory(name, allocated_amount)
        self.save_data()
    
    def update_category_allocation(self, name: str, new_amount: float):
        """Update the allocated amount for a category."""
        if name not in self.categories:
            raise ValueError(f"Category '{name}' does not exist")
        
        self.categories[name].allocated_amount = new_amount
        self.save_data()
    
    def delete_category(self, name: str):
        """Delete a budget category."""
        if name not in self.categories:
            raise ValueError(f"Category '{name}' does not exist")
        
        del self.categories[name]
        self.save_data()
    
    def add_expense(self, category_name: str, amount: float, description: str):
        """Add an expense to a category."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist")
        
        self.categories[category_name].add_expense(amount, description)
        self.save_data()
    
    def get_total_allocated(self) -> float:
        """Get total amount allocated across all categories."""
        return sum(cat.allocated_amount for cat in self.categories.values())
    
    def get_total_spent(self) -> float:
        """Get total amount spent across all categories."""
        return sum(cat.get_total_spent() for cat in self.categories.values())
    
    def get_unallocated_amount(self) -> float:
        """Get amount of income not yet allocated to any category."""
        return self.monthly_income - self.get_total_allocated()
    
    def get_budget_summary(self) -> Dict:
        """Get a summary of the budget status."""
        return {
            'monthly_income': self.monthly_income,
            'total_allocated': self.get_total_allocated(),
            'total_spent': self.get_total_spent(),
            'unallocated': self.get_unallocated_amount(),
            'remaining_budget': self.monthly_income - self.get_total_spent(),
            'categories': {
                name: {
                    'allocated': cat.allocated_amount,
                    'spent': cat.get_total_spent(),
                    'remaining': cat.get_remaining()
                }
                for name, cat in self.categories.items()
            }
        }
    
    def save_data(self):
        """Save budget data to file."""
        data = {
            'monthly_income': self.monthly_income,
            'categories': {name: cat.to_dict() for name, cat in self.categories.items()}
        }
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except (IOError, OSError) as e:
            raise IOError(f"Failed to save data to {self.data_file}: {e}")
    
    def load_data(self):
        """Load budget data from file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.monthly_income = data.get('monthly_income', 0.0)
                    self.categories = {
                        name: BudgetCategory.from_dict(cat_data)
                        for name, cat_data in data.get('categories', {}).items()
                    }
            except (json.JSONDecodeError, IOError):
                # If file is corrupted or can't be read, start fresh
                self.monthly_income = 0.0
                self.categories = {}


def print_header(text: str):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(text.center(60))
    print("=" * 60)


def print_budget_summary(app: FinanceBudgetApp):
    """Print a formatted budget summary."""
    summary = app.get_budget_summary()
    
    print_header("BUDGET SUMMARY")
    print(f"\nMonthly Income:      ${summary['monthly_income']:,.2f}")
    print(f"Total Allocated:     ${summary['total_allocated']:,.2f}")
    print(f"Total Spent:         ${summary['total_spent']:,.2f}")
    print(f"Unallocated:         ${summary['unallocated']:,.2f}")
    print(f"Remaining Budget:    ${summary['remaining_budget']:,.2f}")
    
    if summary['categories']:
        print("\n" + "-" * 60)
        print(f"{'Category':<20} {'Allocated':>12} {'Spent':>12} {'Remaining':>12}")
        print("-" * 60)
        
        for name, data in summary['categories'].items():
            print(f"{name:<20} ${data['allocated']:>10,.2f} "
                  f"${data['spent']:>10,.2f} ${data['remaining']:>10,.2f}")
        print("-" * 60)


def main():
    """Main CLI interface for the finance budgeting app."""
    app = FinanceBudgetApp()
    
    print_header("FINANCE BUDGETING APP")
    print("\nWelcome! This app helps you partition and budget your monthly income.")
    
    while True:
        print("\n" + "=" * 60)
        print("MENU:")
        print("1. Set Monthly Income")
        print("2. Create Budget Category")
        print("3. Update Category Allocation")
        print("4. Delete Category")
        print("5. Add Expense")
        print("6. View Budget Summary")
        print("7. Exit")
        print("=" * 60)
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        try:
            if choice == '1':
                income = float(input("Enter your monthly income: $"))
                app.set_monthly_income(income)
                print(f"✓ Monthly income set to ${income:,.2f}")
            
            elif choice == '2':
                name = input("Enter category name: ").strip()
                amount = float(input("Enter allocated amount: $"))
                app.create_category(name, amount)
                print(f"✓ Category '{name}' created with ${amount:,.2f} allocated")
            
            elif choice == '3':
                name = input("Enter category name: ").strip()
                amount = float(input("Enter new allocated amount: $"))
                app.update_category_allocation(name, amount)
                print(f"✓ Category '{name}' updated to ${amount:,.2f}")
            
            elif choice == '4':
                name = input("Enter category name to delete: ").strip()
                confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower()
                if confirm == 'yes':
                    app.delete_category(name)
                    print(f"✓ Category '{name}' deleted")
                else:
                    print("Deletion cancelled")
            
            elif choice == '5':
                name = input("Enter category name: ").strip()
                amount = float(input("Enter expense amount: $"))
                description = input("Enter expense description: ").strip()
                app.add_expense(name, amount, description)
                print(f"✓ Expense of ${amount:,.2f} added to '{name}'")
            
            elif choice == '6':
                print_budget_summary(app)
            
            elif choice == '7':
                print("\nThank you for using Finance Budgeting App!")
                print("Your data has been saved.")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        
        except ValueError as e:
            print(f"✗ Error: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
