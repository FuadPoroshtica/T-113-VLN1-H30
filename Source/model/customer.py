class Customer:
    def __init__(self, name="", birth_year="2000"):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f"name: {self.name}, birth year: {self.birth_year}"