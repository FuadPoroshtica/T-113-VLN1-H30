#import os
import csv
from model.customer import Customer

class Customer_Data:
    def __init__(self):
        #print(os.getcwd())
        self.file_name = "files/customers.csv"

    def read_all_customers(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Customer(row["name"], row["birth_year"]))
        return ret_list

    def create_customer(self, customer):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "birth_year"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': customer.name, 'birth_year': customer.birth_year})