class Container:
    def __init__(self, id, cargo_owner, amount):
        self.id = id
        self.cargo_owner = cargo_owner
        self.amount = amount

    def __str__(self):
        return f'id: {self.id}, cargo owner: {self.cargo_owner}, amount: {self.amount}'
