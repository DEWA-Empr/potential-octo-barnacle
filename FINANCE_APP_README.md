# Finance Budgeting App

A seamless finance application that helps users partition or budget their funds or salaries each month.

## Overview

The Finance Budgeting App is a command-line application that enables users to:
- Set their monthly income/salary
- Create budget categories (Housing, Food, Transportation, Savings, etc.)
- Allocate funds to different categories
- Track expenses against each category
- View comprehensive budget summaries
- Monitor spending and remaining budgets

## Features

### 1. Income Management
- Set and update monthly income/salary
- Track total allocated vs. unallocated funds

### 2. Budget Categories
- Create custom budget categories
- Allocate specific amounts to each category
- Update allocations as needed
- Delete categories when no longer needed

### 3. Expense Tracking
- Add expenses to specific categories
- Include descriptions for better tracking
- Automatic calculation of spent amounts
- Track remaining budget per category

### 4. Budget Analysis
- View comprehensive budget summaries
- See total allocated, spent, and remaining amounts
- Category-wise breakdown of budget status
- Real-time calculation of unallocated funds

### 5. Data Persistence
- Automatic saving of all budget data
- JSON-based storage for easy data portability
- Load previous budget data on app restart

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup
1. Clone or download the repository
2. No additional dependencies required (uses Python standard library)

```bash
# Make the script executable (optional)
chmod +x finance_app.py
```

## Usage

### Running the Application

```bash
python3 finance_app.py
```

Or if made executable:
```bash
./finance_app.py
```

### Main Menu Options

1. **Set Monthly Income**: Enter your monthly salary or income
2. **Create Budget Category**: Create a new budget category with allocated amount
3. **Update Category Allocation**: Modify the allocated amount for an existing category
4. **Delete Category**: Remove a category (with confirmation)
5. **Add Expense**: Record an expense against a specific category
6. **View Budget Summary**: Display comprehensive budget overview
7. **Exit**: Save and exit the application

### Example Workflow

```
1. Set monthly income: $5,000
2. Create categories:
   - Housing: $1,500
   - Food: $600
   - Transportation: $300
   - Utilities: $200
   - Savings: $1,000
   - Entertainment: $400
   - Miscellaneous: $500
3. Add expenses as they occur:
   - Housing: $1,500 (Rent)
   - Food: $75 (Groceries)
   - Transportation: $45 (Gas)
4. View budget summary to track spending
```

## Example Budget Summary

```
============================================================
                     BUDGET SUMMARY                     
============================================================

Monthly Income:      $5,000.00
Total Allocated:     $4,500.00
Total Spent:         $1,620.00
Unallocated:         $500.00
Remaining Budget:    $3,380.00

------------------------------------------------------------
Category             Allocated        Spent    Remaining
------------------------------------------------------------
Housing              $  1,500.00  $  1,500.00  $      0.00
Food                 $    600.00  $     75.00  $    525.00
Transportation       $    300.00  $     45.00  $    255.00
Utilities            $    200.00  $      0.00  $    200.00
Savings              $  1,000.00  $      0.00  $  1,000.00
Entertainment        $    400.00  $      0.00  $    400.00
Miscellaneous        $    500.00  $      0.00  $    500.00
------------------------------------------------------------
```

## Budget Categories Examples

Common budget categories you might create:

- **Essential Expenses**
  - Housing (Rent/Mortgage)
  - Utilities (Electric, Water, Gas, Internet)
  - Groceries/Food
  - Transportation (Gas, Public Transit, Car Payment)
  - Insurance (Health, Car, Home)
  - Healthcare/Medical

- **Savings & Investments**
  - Emergency Fund
  - Retirement Savings
  - Investment Accounts
  - Vacation Fund

- **Discretionary Spending**
  - Entertainment
  - Dining Out
  - Shopping/Clothing
  - Hobbies
  - Subscriptions

- **Debt Payments**
  - Credit Cards
  - Student Loans
  - Personal Loans

## Data Storage

The application stores data in `budget_data.json` in the current directory. The file contains:
- Monthly income
- All budget categories
- Allocated amounts
- Expense history with timestamps and descriptions

### Data File Format

```json
{
  "monthly_income": 5000.0,
  "categories": {
    "Housing": {
      "name": "Housing",
      "allocated_amount": 1500.0,
      "expenses": [
        {
          "amount": 1500.0,
          "description": "Rent",
          "date": "2024-01-15T10:30:00"
        }
      ]
    }
  }
}
```

## Testing

The application includes comprehensive unit tests.

### Running Tests

```bash
python3 test_finance_app.py
```

### Test Coverage

The test suite includes:
- Budget category operations (create, update, delete)
- Expense tracking functionality
- Total calculations (allocated, spent, remaining)
- Data persistence (save and load)
- Edge cases (zero income, overspending, negative amounts)
- Error handling

## Key Features Explained

### Budget Partitioning
The app helps you partition your monthly income into specific categories, ensuring you allocate funds appropriately before spending. This prevents overspending and helps maintain financial discipline.

### Real-time Tracking
As you add expenses, the app automatically calculates:
- How much you've spent in each category
- How much remains in each category
- Total spent vs. total budget
- Unallocated funds

### Financial Awareness
The budget summary provides instant visibility into:
- Where your money is going
- Which categories are over/under budget
- How much you have left to spend
- Whether you're staying within your income

## Tips for Effective Budgeting

1. **Be Realistic**: Set realistic allocations based on your actual spending patterns
2. **Track Regularly**: Add expenses as soon as they occur for accurate tracking
3. **Review Monthly**: Check your budget summary regularly to stay on track
4. **Adjust as Needed**: Update category allocations when circumstances change
5. **Save First**: Allocate to savings before discretionary spending
6. **Emergency Fund**: Maintain an emergency fund category for unexpected expenses
7. **Use Unallocated Wisely**: Keep some unallocated funds for flexibility

## Troubleshooting

### Issue: Data file corrupted
**Solution**: The app will start fresh if the data file is corrupted. Your previous data will need to be manually recovered from backups.

### Issue: Can't create category
**Solution**: Ensure the category name doesn't already exist. Category names are case-sensitive.

### Issue: Negative remaining budget
**Solution**: This is allowed and indicates overspending in a category. Consider reallocating funds or reducing future expenses.

## Future Enhancements

Potential features for future versions:
- Multiple month tracking and history
- Expense categories and subcategories
- Budget templates
- Export to CSV/PDF reports
- Graphical charts and visualizations
- Recurring expense tracking
- Budget goals and alerts
- Mobile app version

## License

This project is available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue in the repository.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
