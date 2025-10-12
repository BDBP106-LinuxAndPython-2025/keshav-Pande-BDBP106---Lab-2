fruits = {
    "apple": "red",
    "grapes": "green",
    "mango": "yellow",
    "guava": "green",
    "banana": "yellow",
    "strawberry": "red",
    "watermelon": "green",
    "cherry": "red",
    "pear": "green",
    "orange": "orange"
}

print("Fruits that are green:")
for fruit, color in fruits.items():
    if color == "green":
        print(fruit)
