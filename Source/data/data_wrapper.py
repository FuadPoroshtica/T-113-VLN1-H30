from data.customer_data import Customer_Data


class Data_Wrapper:
    def __init__(self):
        self.customer_data = Customer_Data()

    def get_all_customers(self):
        return self.customer_data.read_all_customers()

    def create_customer(self, customer):
        return self.customer_data.create_customer(customer)