#project01 expense trackder 
import textwrap as tw


path=r'C:\Users\Tamilgovind\Documents\python_datascience_journey_2026\00_data_science_journey\25_projects\project01_expense_tracker\data.txt'
def add_expenses():
    date=input("enter date (dd-mm-yyyy) format = ")
    category=input("enter the category (ex: food,travel,etc) = ")
    description=input("detailed description = ")
    amount=input("enter the spent amount = ")

    with open(path,"a") as file:
        file.write(f"{date}|{category}|{description}|{amount}\n")
        print("data saved in ",file.name)
    print("data added successfully")

def view_expenses():
    with open(path,"r") as file:
        print("-"*90)
        print(f"{'DATE':<15}{'CATEGORY':<20}{'DESCRIPTION':<40}{"AMOUNT":<15}")
        print("-"*90)
        for line in file:
            date,category,desription,amount=line.strip().split("|")
            desc=tw.wrap(desription,width=35)
            print(f"{date:<15}{category:<15}{desc[0]:<40}{amount:>10}")
            for extra_line in desc[1:]:
                print(f"{'':<15}{'':<15}{extra_line:<40}{'':>10}")
        print("-"*90)


def search_by_category():
    categories=set()

    with open(path,"r") as file:
        for line in file:
            date,category,description,amount=line.strip().split("|")
            categories.add(category)
        #covert from set to list 
        categories=sorted(categories)
        #now display the categories
        print("-"*90) 
        for index,data in enumerate(categories,start=1):
            print(f"{index}. {data}")
        print("-"*90)
    
        choice=int(input("enter your choice ="))
        if choice<1 or choice>len(categories):
            print("invalid choice")
            return 
        selected_category=categories[choice-1]

        print(f"\nExpenses for category: {selected_category}")
        print("-" * 90)
        print(f"{'DATE':<15}{'CATEGORY':<15}{'DESCRIPTION':<40}{'AMOUNT':>10}")
        print("-" * 90)

        found=False
        for line in file:
            date,category,description,amount=line.strip().split("|")
            if category==selected_category:
                print(f"{'DATE':<15}{'CATEGORY':<15}{'DESCRIPTION':<40}{'AMOUNT':>10}")
    
def calculate_total_expenses():
    pass 

def calculate_todays_expense():
    pass 

def calculate_highest_expense():
    pass

def calculate_lowest_expense():
    pass 

def categorywise_total():
    pass 

def monthly_total():
    pass 

def delete_expense():
    pass 



print("-"*90)
print(f'{'expensetracker':^60}')
print("-"*90)

while True:
    print("-"*90)
    print("1. add expenses")
    print("2. view all expenses")
    print("3. search expense by category")
    print("4. calculate total expenses")
    print("5. calculate today's expenses")
    print("6. find the highest expense")
    print("7. find the lowest expense")
    print("8. category wise total")
    print("9. monthly total")
    print("10. delete expenses")
    print("11. close the application")
    print("-"*90)

    user_choice=int(input("enter the choice between (1-11) = "))
    match user_choice:
        case 1:
            add_expenses()
        case 2:
            view_expenses()
        case 3:
            search_by_category()
        case 4:
            calculate_total_expenses()
        case 5:
            calculate_todays_expense()
        case 6:
            calculate_highest_expense()
        case 7:
            calculate_lowest_expense()
        case 8:
            categorywise_total()
        case 9:
            monthly_total()
        case 10:
            delete_expense()
        case 11:
            print("thank you. have a nice day")
            break
        case _:
            print("invalid input retry...")



