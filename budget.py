class BudgetCategory:
    def __init__ (self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expenses = []
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name
        else:
            print("Please enter a name")
    
    def add_expense(self, new_expense):
        if new_expense > 0:
            self.__expenses.append(new_expense)
        else:
            print("Expense can't be less than zero")
    
    def get_expenses(self):
        return self.__expenses

    

    @property
    def budget(self):
        return self.__budget        
    @budget.setter
    def budget(self, new_budget):
        if new_budget >0:
            self.__budget = new_budget
        else:
            print("budget can't be less than 0")
            
food_category = BudgetCategory("Food", 500)
food_category.add_expense(50)
food_category.add_expense(100)
food_category.get_expenses()
# print(f"{food_category.name}")
# print(food_category.get_expenses())
