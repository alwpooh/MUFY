print("What is your name?")
name = input()
import random
adjectives = ["cute", "gorgeous", "cool", "handsome", "smart", "awesome"]
animals = ["quokka", "capybara", "rabbit", "kangaroo", "dog", "cat"]
codename = random.choice(adjectives) + " " + random.choice(animals)
print(name, ", your codename is", codename)
numbers= random.randint(1,99)
print("Your lucky number is:", numbers)