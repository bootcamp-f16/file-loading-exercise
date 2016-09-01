# run_report.py for store_data.json file
# Copyright Brett Fraley - 2016

import json

# Open JSON source data and convert to Python dictionary.
with open('store_data.json', 'r') as f:
     data_file = json.load(f)

# Asterisk line space for report readability (starspace).
starspace = "\n* * * * * * * *\n"

# @class Report
# Accepts a JSON format data file.
# This file uses the explicitly provided file loaded above.

class Report():
    
    def __init__(self, data_input = data_file):
        self.data_input = data_input

    # Show the Most Expensive Item
    # --------------------------------
    def get_most_expensive(self):
        return_price = 0

        for i in data_file:
            if i["price"] > return_price:
                return_price = i["price"]

        return "Most Expensive Item: {:.2f}{}".format(return_price, starspace)

    # Show the Least Expensive Item
    # --------------------------------
    def get_least_expensive(self):
        return_price = 0

        for i in data_file:
            if i["price"] < return_price:
                return_price = i["price"]

        return "Least Expensive Item: {:.2f}{}".format(return_price, starspace)

    # Show the Total Revenue
    # --------------------------------
    def get_total_revenue(self):
        total_revenue = 0

        for i in data_file:
            total_revenue += i["price"] * i["sold"]

        return "Total Revenue: {:.2f}{}".format(total_revenue, starspace)

    # Show the Total Profit
    # --------------------------------
    def get_total_profit(self):
        total_profit = 0

        for i in data_file:
            total_profit += (i["price"] - i["cost_to_make"]) * i["sold"]

        return "Total Profit: {:.2f}{}".format(total_profit, starspace)

    # Show the 10 Best Sellers.
    # --------------------------------
    def get_10_best_sellers(self):

        report_string = "Best Sellers\n{}".format(starspace)
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
            report_string += "{} : {}\n".format(seller["name"], seller["sold"])

        report_string += starspace
        return report_string

    # Show the Number Sold by Each Department.
    # ---------------------------------------
    def get_sales_by_dept(self):

        report_string = "Sales By Department\n{}".format(starspace)

        for i in data_file:
            report_string += "{} : {}\n".format(i["department"], i["sold"])
            
        report_string += starspace
        return report_string

    # Produce / Print a full report to terminal.
    # ------------------------------------------
    def print_full_report(self):
        print(self.get_most_expensive())
        print(self.get_least_expensive())
        print(self.get_total_revenue())
        print(self.get_total_profit())
        print(self.get_10_best_sellers())
        print(self.get_sales_by_dept())

    # Write a full report to report.txt file.
    # --------------------------------------
    def write_full_report_to_file(self):
        report_file = open('report.txt', 'w')
        report_file.write(self.get_most_expensive())
        report_file.write(self.get_least_expensive())
        report_file.write(self.get_total_revenue())
        report_file.write(self.get_total_profit())
        report_file.write(self.get_10_best_sellers())
        report_file.write(self.get_sales_by_dept())

        # CLOSE FILE!
        report_file.close()


# Instantiate a report, print it, and write it to file.
report = Report()
report.print_full_report()
report.write_full_report_to_file()
