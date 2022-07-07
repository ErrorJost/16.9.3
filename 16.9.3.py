class Clients:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"Client:{self.name} {self.last_name}.{self.city}.Баланс:{self.balance}."


client_1 = Clients("Иван", "Иванов", "Москва", 50)
print(client_1)

