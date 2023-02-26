#!/usr/bin/env python
# coding: utf-8

# In[1]:




from tabulate import tabulate


# Initialize class with parameters


class Shoes:
#Define functions for each parameter for the purpose of searching
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def set_quantity(self, new_quant):
        self.quantity = new_quant

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()

# FUNCTIONS #

# Open files in different formats
# Set empty lists for shoes list and object list 

invent = open("inventory.txt", "r")


items_list = []
shoes_list = []

# Use try/finally if user does not open file


def read_shoes_data():
# Read each line from each line from the text file
    file = None
    try:
        for lines in invent:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            items_list.append(split_lines)
# Creat shoe object and append to shoe list
        for things in range(1, len(items_list)):
            array = items_list[things]
            shoe1 =  Shoes(array[0], array[1], array[2], array[3], int(array[4]))
            shoes_list.append(shoe1)

    except FileNotFoundError as error:
        print("\nFile does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()


# Define capture shows that gets  new products


def capture_shoes():
    
    file = None

    try:
        new_country = input("Please enter the country of your product:\n")
        new_code = input("Please enter the code of your product:\n")
        new_product = input("Please enter the name of your product:\n")
        new_cost = int(input("Please enter the cost of your product, only in numbers. E.g. 12345\n"))
        new_quantity = int(input("Please enter the quantity of your product, only in numbers. E.g. 2\n"))

        new_shoe = Shoes(new_country, new_code, new_product, new_cost, new_quantity)
        shoes_list.append(new_shoe)
# Cast each item into an object and append to object list
        invent_write = open("inventory.txt", "a+")
        invent_write.write(f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
        print("\n Product updated!\n")
# Write to file, close file
        invent_write.close()

    except FileNotFoundError as error:
        print("\nfile does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()



def view_all():

    file = None
    
    try:

        print("STOCKLIST \n")

        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []
# Define view_all that displays all shoes 
        for lines in shoes_list:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)
# Display using tabulate
        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='plain'))

    

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()


# Define restock() that displays first 5 items with lowest stock, using sort()

def restock():

    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
        shoes_list.sort(key=lambda x:x.quantity)

        for i in range(1,6):
            restock_list.append(shoes_list[i])
    
        print("Lowest stock \n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='plain', showindex= range(1,6)))
        

        user_input_item = int(input("\nPlease confirm the index of the product you want to restock:\n"))
        user_input_qty = int(input("\nPlease confirm the new quantity:\n"))
        shoes_list[user_input_item].set_quantity(user_input_qty)

        output = ''
        for item in shoes_list:
            output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()

        print("\nYour product has been updated!")

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

# Define search_shoe() that displays specific shoes

def search_shoe():

    search_shoe = input("\nPlease enter the code you are searching for:\n\n")

    for ben in shoes_list:
        if ben.get_code() == search_shoe:
            print(f'\n {ben}')

    print("\nPlease select another option from the menu below\n")



def value_per_item():

    for line in shoes_list:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} VALUE: R{value}\n')


def highest_quantity():


    print("\n----------------------------Highest stock item:----------------------------\n")

    print(max(shoes_list, key=lambda item: item.quantity))
    print("\nThis item has now been marked on sale\n")
    print("\nPlease select an option from the menu below")

# ====================================================== OUTPUT =============================================== #

# Display menu options
# Use try/finally in case the file does not open on user end
# Set ValueError
read_shoes_data()
while True:

    try:
        menu = int(input('''\n
            Please select from the menu below:
            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            7. Exit menu
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()
        elif menu == 6:
            highest_quantity()
        elif menu == 7:
            break
        elif menu > 7:
            print("\ninvalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")
        
# END  #


# In[ ]:




