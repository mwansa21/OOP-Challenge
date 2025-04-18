import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing. ")
        else:
            print(f"{self.name} is too tired to play.")

    def bark(self):
        print(f"{self.name} is barking!")

    def drink(self):
        print(f"{self.name} is drinking water.")

    def run(self):
        print(f"{self.name} is running around joyfully!")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks if self.tricks else 'None'}")
