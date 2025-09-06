import random

subjects=[
    "shahrukh khan",
    "virat kohli",
    "nirmala sitharam",
    "a mumbai cat",
    "prime minister modi",
    "auto rikshaw driver from delhi"
]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places=[
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during ipl match",
    "at india gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)


    headline=f"breaking news: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\ndo you want another headline? (yes/no)").strip().lower()
    if user_input=="no":
        break

print("\nthanks for using the fake news headline generator.have a fun day")