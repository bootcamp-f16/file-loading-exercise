import json
from functools import reduce

with open("store_data.json", 'r') as f:
    store_data = json.load(f)


def return_price_data():
    """Display price data to user."""
    prices = [item['price'] for item in store_data]

    print('The highest priced item is ${}.'.format(
        reduce(lambda x, y: y if y > x else x, prices)))
    print('The lowed priced item is ${}.'.format(
        reduce(lambda x, y: y if y < x else x, prices)))
    print('The total revenue of all items is ${:,.2f}.'.format(
        reduce(lambda x, y: x + y, prices)))
    print('='*20)


def display_profits():
    """Display total profit to user."""
    profit = [item['price'] - item['cost_to_make'] for item in store_data]

    print('Total profit is ${:,.2f}.'.format(
        reduce(lambda x, y: x + y, profit)))
    print('='*20)


def display_top_selling_prices():
    # We need a dict with the sale number as the key
    items_by_price = {item['sold']: item['name'] for item in store_data}
    # Then we need to get a list of the top ten items
    top_selling_items = [items_by_price[num] for num
                         in sorted(items_by_price)[:10]]

    print('\nThe top selling items are: ')
    for item in top_selling_items:
        print(item)
    print('='*20)


def get_list_of_departments():
    # We need all the departments listed in our data file
    listings = [item['department'] for item in store_data]
    # However, there are multiple per line
    # So we need to parse them
    departments = []
    for listing in listings:
        if listing not in departments:
            departments.append(listing)

    return departments


def item_in_department(department, item):
    """Checks to see if item is in department. If so, returns true."""
    return True if item.department == department else False


def get_sales_per_department(department):
    """Returns the number of sales for a department."""
    sales = 0
    for item in store_data:
        if department == item['department']:
            sales += item['sold']
    return sales


def get_sales_for_all_departments():
    dept_and_sales = {
        dept: get_sales_per_department(dept)
        for dept in get_list_of_departments()
    }

    print('\nHere are the sales per department:\n')
    for k, v in dept_and_sales.items():
        print('{}: {}'.format(k, v))
    print('='*10)



def main():
    print('*'*20)
    return_price_data()
    display_profits()
    display_top_selling_prices()
    get_list_of_departments()
    get_sales_for_all_departments()

if __name__ == '__main__':
    main()
