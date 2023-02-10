# The F.A.M

The program is a prototype of a parental control for a bank account which is called
F.A.M. (Family Appointed Moderator). It acts as a parental control for a bank account.
It allows parents to set a budget for their children and monitor their spending.

## Authors

- [Nash Baek](nash4comp@gmail.com), A01243888
- [Taylor Ji](taylor.ji719@gmail.com), A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG

## How F.A.M Works

This program will register a user, keep track of all the spending/transactions on users' bank account and lock the account if certain conditions are met.

The program provides different moderation level for each user type such as budget limit, locking-up the account, and so on.

### User Menu
1. View Budgets
    - Selecting this option should show the user the current status of their budgets (locked or not) in addition to the amount spent, amount left, and the total amount allocated to the budget.
2. Record a Transaction
    - This takes the user to a sub-menu where they are prompted to enter the transaction details.
3. View Transactions by Budget
    - This takes the user to a sub-menu where they select their budget category and view all the transactions to date in that category.
4. View Bank Account Details
    - The application should print out the bank account details of the user and all transactions conducted to date alongside the closing balance.
5. Register User
    - This prompts to enter the new users' information to register them into the system.
6. List up Users
    - Prints out the list of users registered in the system.
7. Switch User
    - Switches to another user
8. Quit

### Registering A User
On startup, the user (usually a parent) must register their child's financial details. This includes (but is not necessarily limited to):
- The Users Name
- Age
- User Types
- Bank Account Number
- Bank Name
- Bank Balance
- Their Budgets

### User types
There are three user types.
- **The Angel**
    - The Angel represents a user whose parents are not worried at all. This child has never (as far as their parents are concerned) broken a single rule. They already have a five-year plan in place and a roadmap which is guaranteed to get them into Harvard. The Angel is the child who would set up their own FAM account, so they can monitor their expenses.
    - This user type:
        - Gets a notification if they exceed more than 90% of a budget.
        - Gets politely notified if they exceed a budget category.
        - Never gets locked out of a budget category. They can continue spending money even if they exceed the budget in question.

- **The Troublemaker**
    - The Troublemaker represents a user who often finds themselves in... well.. trouble. These are usually minor incidents and their parents are concerned but not worried. Parents usually set up a FAM account to monitor their expenses and impose light restrictions.
    - This user type:
        - Gets a notification if they exceed more than 75% of a budget category.
        - Gets politely notified iIf they exceed a budget category.
        - Gets locked out of conducting transactions in a budget category if they exceed it by 120% of the amount assigned to the budget in question.

- **The Rebel**
    - The Rebel represents a user who refuses to follow any rules and believes that society should be broken down and restructured. They do not want to pursue "a standard education", "conform to the economic/capitalist foundations of society" or "get a job". Parents of these children are quite worried and turn to F.A.M. when they are out of options.
    - This user type is strictly monitored:
        - Gets a notification if they exceed more than 50% of a budget category.
        - Gets ruthlessly notified if they exceed a budget category.
        - Gets locked out of conducting transactions in a budget category if they exceed it by 100% of the amount assigned to the budget in question.
        - If they exceed their budget in 2 or more categories than they get locked out of their account completely

### Lock out
The app has the ability to lock a user out of recording transactions (and effectively spending any money) based on certain conditions as specified by their User Type (more on this in the User Types section below).

If a user has been locked from a budget category:
- They should be notified of this via a console message.
- Any attempt at recording transactions in the affected budget category should be denied.

### Budget Categories
Each child that is being monitored is assigned the following budget categories. The exact value of each budget is assigned when registering the child as a user.
- Games and Entertainment
- Clothing and Accessories
- Eating Out
- Miscellaneous

### Record Transactions
This application maintains a collection of transactions which represent money going out of the users bank account.

Each transaction contains the following information:
- The timestamp the transaction was recorded
- The dollar amount (positive, non-zero number).
- The budget category that this transaction belongs to.
- Instead of prompting the user to enter the name of the budget category, provide them with a list of categories and ask them to select one.
The name of the shop/website where the purchase took place.

The user does not be allowed to record a transaction if the transaction cause their bank balance to go below zero. Additionally, the system should subtract the required amount from the users bank balance once a transaction has been recorded.

Depending on the type of user, after a transaction has been recorded your system will want to perform checks to see if a notification should be issued. A list of transactions that have taken place in a budget category should be printed out to the console if:
- The user receives a notification that they are getting close to exceeding their assigned budget for the category in question
- The user receives a notification that they have exceeded their assigned budget for the category in question.


## Limitations and Requirements

- Login system is not supporting the id and password. It is just a prototype.
- The program is not supporting the database.
- The program is not supporting the GUI.
- Some corner cases are not covered such as sanity check for the bank account number, bank balance, and so on. Only checking the type of the input is done.
- Removing, editing the users information is not supported.







