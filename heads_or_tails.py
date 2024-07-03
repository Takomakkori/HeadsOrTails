import random

def coin_toss():
    return "Heads" if random.choice([True, False]) else "Tails"

name = input("Who are you?\n> ")
print(f"Hello, {name}!")

print("Tossing a coin...")
results = []
for round in range(1, 4):
    result = coin_toss()
    results.append(result)
    print(f"Round {round}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")
print(f"Heads: {heads_count}, Tails: {tails_count}")

if heads_count > tails_count:
    print(f"{name} won!")
else:
    print(f"{name} lost!")
