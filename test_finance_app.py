#!/usr/bin/env python3
"""
Unit tests for the Finance Budgeting Application
"""

import unittest
import os
import json
from finance_app import BudgetCategory, FinanceBudgetApp


class TestBudgetCategory(unittest.TestCase):
    """Test cases for BudgetCategory class."""
    
    def test_create_category(self):
        """Test creating a budget category."""
        category = BudgetCategory("Housing", 1500.0)
        self.assertEqual(category.name, "Housing")
        self.assertEqual(category.allocated_amount, 1500.0)
        self.assertEqual(len(category.expenses), 0)
    
    def test_add_expense(self):
        """Test adding an expense to a category."""
        category = BudgetCategory("Food", 500.0)
        category.add_expense(50.0, "Groceries")
        
        self.assertEqual(len(category.expenses), 1)
        self.assertEqual(category.expenses[0]['amount'], 50.0)
        self.assertEqual(category.expenses[0]['description'], "Groceries")
    
    def test_get_total_spent(self):
        """Test calculating total spent in a category."""
        category = BudgetCategory("Transportation", 300.0)
        category.add_expense(50.0, "Gas")
        category.add_expense(30.0, "Parking")
        
        self.assertEqual(category.get_total_spent(), 80.0)
    
    def test_get_remaining(self):
        """Test calculating remaining budget."""
        category = BudgetCategory("Entertainment", 200.0)
        category.add_expense(75.0, "Movie tickets")
        
        self.assertEqual(category.get_remaining(), 125.0)
    
    def test_to_dict(self):
        """Test converting category to dictionary."""
        category = BudgetCategory("Utilities", 150.0)
        category.add_expense(50.0, "Electric bill")
        
        data = category.to_dict()
        self.assertEqual(data['name'], "Utilities")
        self.assertEqual(data['allocated_amount'], 150.0)
        self.assertEqual(len(data['expenses']), 1)
    
    def test_from_dict(self):
        """Test creating category from dictionary."""
        data = {
            'name': "Healthcare",
            'allocated_amount': 250.0,
            'expenses': [
                {'amount': 30.0, 'description': 'Pharmacy', 'date': '2024-01-15'}
            ]
        }
        
        category = BudgetCategory.from_dict(data)
        self.assertEqual(category.name, "Healthcare")
        self.assertEqual(category.allocated_amount, 250.0)
        self.assertEqual(len(category.expenses), 1)


class TestFinanceBudgetApp(unittest.TestCase):
    """Test cases for FinanceBudgetApp class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_file = 'test_budget_data.json'
        self.app = FinanceBudgetApp(self.test_file)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_set_monthly_income(self):
        """Test setting monthly income."""
        self.app.set_monthly_income(5000.0)
        self.assertEqual(self.app.monthly_income, 5000.0)
    
    def test_create_category(self):
        """Test creating a budget category."""
        self.app.create_category("Savings", 1000.0)
        
        self.assertIn("Savings", self.app.categories)
        self.assertEqual(self.app.categories["Savings"].allocated_amount, 1000.0)
    
    def test_create_duplicate_category(self):
        """Test that creating duplicate category raises error."""
        self.app.create_category("Food", 500.0)
        
        with self.assertRaises(ValueError):
            self.app.create_category("Food", 600.0)
    
    def test_update_category_allocation(self):
        """Test updating category allocation."""
        self.app.create_category("Housing", 1200.0)
        self.app.update_category_allocation("Housing", 1500.0)
        
        self.assertEqual(self.app.categories["Housing"].allocated_amount, 1500.0)
    
    def test_update_nonexistent_category(self):
        """Test updating nonexistent category raises error."""
        with self.assertRaises(ValueError):
            self.app.update_category_allocation("NonExistent", 100.0)
    
    def test_delete_category(self):
        """Test deleting a category."""
        self.app.create_category("Entertainment", 200.0)
        self.app.delete_category("Entertainment")
        
        self.assertNotIn("Entertainment", self.app.categories)
    
    def test_delete_nonexistent_category(self):
        """Test deleting nonexistent category raises error."""
        with self.assertRaises(ValueError):
            self.app.delete_category("NonExistent")
    
    def test_add_expense(self):
        """Test adding an expense to a category."""
        self.app.create_category("Transportation", 300.0)
        self.app.add_expense("Transportation", 50.0, "Gas")
        
        expenses = self.app.categories["Transportation"].expenses
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]['amount'], 50.0)
    
    def test_add_expense_to_nonexistent_category(self):
        """Test adding expense to nonexistent category raises error."""
        with self.assertRaises(ValueError):
            self.app.add_expense("NonExistent", 50.0, "Test")
    
    def test_get_total_allocated(self):
        """Test calculating total allocated amount."""
        self.app.create_category("Housing", 1500.0)
        self.app.create_category("Food", 500.0)
        self.app.create_category("Savings", 1000.0)
        
        self.assertEqual(self.app.get_total_allocated(), 3000.0)
    
    def test_get_total_spent(self):
        """Test calculating total spent amount."""
        self.app.create_category("Food", 500.0)
        self.app.create_category("Transportation", 300.0)
        self.app.add_expense("Food", 100.0, "Groceries")
        self.app.add_expense("Transportation", 50.0, "Gas")
        
        self.assertEqual(self.app.get_total_spent(), 150.0)
    
    def test_get_unallocated_amount(self):
        """Test calculating unallocated amount."""
        self.app.set_monthly_income(5000.0)
        self.app.create_category("Housing", 1500.0)
        self.app.create_category("Food", 500.0)
        
        self.assertEqual(self.app.get_unallocated_amount(), 3000.0)
    
    def test_get_budget_summary(self):
        """Test getting budget summary."""
        self.app.set_monthly_income(5000.0)
        self.app.create_category("Housing", 1500.0)
        self.app.create_category("Food", 500.0)
        self.app.add_expense("Food", 100.0, "Groceries")
        
        summary = self.app.get_budget_summary()
        
        self.assertEqual(summary['monthly_income'], 5000.0)
        self.assertEqual(summary['total_allocated'], 2000.0)
        self.assertEqual(summary['total_spent'], 100.0)
        self.assertEqual(summary['unallocated'], 3000.0)
        self.assertEqual(summary['remaining_budget'], 4900.0)
        self.assertIn('Housing', summary['categories'])
        self.assertIn('Food', summary['categories'])
    
    def test_save_and_load_data(self):
        """Test saving and loading data persistence."""
        self.app.set_monthly_income(5000.0)
        self.app.create_category("Savings", 1000.0)
        self.app.add_expense("Savings", 200.0, "Emergency fund")
        
        # Create new app instance with same file
        app2 = FinanceBudgetApp(self.test_file)
        
        self.assertEqual(app2.monthly_income, 5000.0)
        self.assertIn("Savings", app2.categories)
        self.assertEqual(app2.categories["Savings"].allocated_amount, 1000.0)
        self.assertEqual(len(app2.categories["Savings"].expenses), 1)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_file = 'test_edge_cases.json'
        self.app = FinanceBudgetApp(self.test_file)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_zero_income(self):
        """Test handling zero income."""
        self.app.set_monthly_income(0.0)
        self.assertEqual(self.app.monthly_income, 0.0)
    
    def test_negative_amounts(self):
        """Test that negative amounts work (could be refunds)."""
        self.app.create_category("Utilities", 200.0)
        self.app.add_expense("Utilities", -50.0, "Refund")
        
        self.assertEqual(self.app.categories["Utilities"].get_total_spent(), -50.0)
        self.assertEqual(self.app.categories["Utilities"].get_remaining(), 250.0)
    
    def test_empty_budget(self):
        """Test operations with no categories."""
        self.assertEqual(self.app.get_total_allocated(), 0.0)
        self.assertEqual(self.app.get_total_spent(), 0.0)
        
        summary = self.app.get_budget_summary()
        self.assertEqual(len(summary['categories']), 0)
    
    def test_overspending_category(self):
        """Test category with spending exceeding allocation."""
        self.app.create_category("Entertainment", 100.0)
        self.app.add_expense("Entertainment", 150.0, "Concert")
        
        self.assertEqual(self.app.categories["Entertainment"].get_remaining(), -50.0)


if __name__ == '__main__':
    unittest.main()
