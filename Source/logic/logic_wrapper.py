from logic.customer_logic import Customer_Logic
from data.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.customer_logic = Customer_Logic(self.data_wrapper)

    def create_customer(self, customer):
        """Takes in a customer object and forwards it to the data layer"""
        return self.customer_logic.create_customer(customer)

    def get_all_customers(self):
        return self.customer_logic.get_all_customers()