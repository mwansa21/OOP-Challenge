from pet import Pet
import random

def main():
    names = ['Max', 'Simba', 'Rocky', 'Zeus', 'Shaka', 'Rex']
    tricks_pool = ['roll over', 'play dead', 'shake hands', 'high five', 'fetch', 'spin']
    extra_actions = ['eat', 'sleep', 'play', 'bark', 'drink', 'run']

    # Randomly selects name and tricks
    name = random.choice(names)
    pet = Pet(name)
    print(f"\nCreating pet: {name}")

    # Performs 3 random actions
    for _ in range(3):
        action = random.choice(extra_actions)
        if action == 'eat':
            pet.eat()
        elif action == 'sleep':
            pet.sleep()
        elif action == 'play':
            pet.play()
        elif action == 'bark':
            pet.bark()
        elif action == 'drink':
            pet.drink()
        elif action == 'run':
            pet.run()

    # Teaches 2 random tricks
    selected_tricks = random.sample(tricks_pool, 2)
    for trick in selected_tricks:
        pet.train(trick)

    # Shows final status
    pet.get_status()

if __name__ == "__main__":
    main()
