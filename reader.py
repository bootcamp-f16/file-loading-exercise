# reader.py for store_data.json file

import json

# Reading data back
with open('store_data.json', 'r') as f:
     data_file = json.load(f)

class Report():

    def __init__(self, data_input):
        self.data_input = data_input

    # Show the Most Expensive Item
    def get_most_expensive(self):
        return_price = 0

        for i in data_file:
            if i["price"] > return_price:
                return_price = i["price"]

        print("Most Expensive Item: {}\n* * * * * * * *\n".format(return_price))

    # Show the Least Expensive Item
    def get_least_expensive(self):
        return_price = 0

        for i in data_file:
            if i["price"] < return_price:
                return_price = i["price"]

        print("Least Expensive Item: {}\n* * * * * * * *\n".format(return_price))

    # Show the Total Revenue
    def get_total_revenue(self):
        total_revenue = 0

        for i in data_file:
            total_revenue += i["price"] * i["sold"]

        print("Total Revenue: {}\n* * * * * * * *\n".format(total_revenue))

    # Show the Total Profit
    def get_total_profit(self):
        total_profit = 0

        for i in data_file:
            total_profit += (i["price"] - i["cost_to_make"]) * i["sold"]

        print("Total Profit: {}\n* * * * * * * *\n".format(total_profit))

    # Show the 10 Best Sellers.
    def get_10_best_sellers(self):
        print("Best Sellers")

        best_sellers = []
        top_sold = 0

        for i in data_file:

            # Just append the first ten records.
            if len(best_sellers) < 10:
                best_sellers.append(i)

            # Compare 'sold' to every best seller
            else:
                for best in best_sellers:
                    if i["sold"] > best["sold"]:
                        best = i

        for seller in best_sellers:
            print("{} : {}".format(seller["name"], seller["sold"]))
            
        print("\n* * * * * * * *\n")

    # Show the Number Sold by Each Department
    def get_sales_by_dept(self):
        print("Sales By Department")

        for i in data_file:
            print("{} : {}".format(i["department"], i["sold"]))
            
        print("\n* * * * * * * *\n")

# Produce / Run a full report on store_data.json file.
def produce_full_report():
    report = Report(data_file)    
    report.get_most_expensive()
    report.get_least_expensive()
    report.get_total_revenue()
    report.get_total_profit()
    report.get_10_best_sellers()
    report.get_sales_by_dept()

# Write a full report to report.txt file
"""
def write_report_to_file():
    report_file = open('report.txt', 'w')
    report_file.close()
"""

# Call produce_full_report
produce_full_report()
