class sender():
    def __init__(self, name):
        self.name = name
        self.other_key_partitial = None
        self.key_full = None
        self.key_partitial = None
        print(f"\n {self.name} ")
        while True:
            self.private_key = input(f"Введите закрытый ключ для {self.name}: ")
            self.private_key = int(self.private_key)
            if self.private_key <= 0:
                continue

            self.public_key = input(f"Введите публичный ключ для {self.name}:  ")
            self.public_key = int(self.public_key)
            if self.public_key <= 0:
                continue
            break

    def create_partial_key(self):
        print(f"\n{self.name} \nЧастичный ключ = ({Alice.public_key} ^ {self.private_key}) mod {Bob.public_key}")
        self.key_partitial = (Alice.public_key ** self.private_key) % Bob.public_key
        print(f"Частичный ключ = {self.key_partitial}")

    def send_partial_key(self):
        if self.name == "Alice":
            self.other_key_partitial = Bob.key_partitial
            print(f"Bob sending {self.other_key_partitial} to Alice")
        elif self.name == "Bob":
            self.other_key_partitial = Alice.key_partitial
            print(f"Alice sending {self.other_key_partitial} to Bob")

    def create_full_key(self):
        print(f"\n{self.name} \nИтоговый ключ = ({self.other_key_partitial} ^ {self.private_key}) mod {Bob.public_key}")
        self.key_full = (self.other_key_partitial ** self.private_key) % Bob.public_key
        print(f"Итоговый ключ = {self.key_full}")


if __name__ == '__main__':
    # str1 = send_message()

    Alice = sender('Alice')
    Bob = sender('Bob')

    Alice.create_partial_key()
    Bob.create_partial_key()

    print("\nПересылка частично зашифрованных ключей")
    Alice.send_partial_key()
    Bob.send_partial_key()

    Alice.create_full_key()
    Bob.create_full_key()