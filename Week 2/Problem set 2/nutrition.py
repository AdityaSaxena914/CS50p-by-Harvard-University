Nutrition = {
    "apple": "130",
    "avocado": "50",
    "cantalope": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "nectarine": "60",
    "lime": "20",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

x = input("Item: ").lower()
if x in Nutrition:
    print("Calories:",Nutrition[x])
else:
    print()
