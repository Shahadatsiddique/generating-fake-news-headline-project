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


# import random
# a=["Labhesh",
#    "ShahRukh Khan",
#    "AjayDevgan",
#    "SunnyDeol"
# ]
# b=[" is playing in ",
#    " is dancing over",
#    " is hanging over"
# ]
# c=[" chennai",
#    " shit" ,
#    " Paxtan"
#    ]
# News=""

  
# #now all you have to do is start a loop 
# while True:
# 	News+=random.choice(a)
# 	break
# while True:
# 	News+=random.choice(b)
# 	break
# while True :
# 	News+=random.choice(c)
# 	break
# print("BREAKING NEWS :",News)