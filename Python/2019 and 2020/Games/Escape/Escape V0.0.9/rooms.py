rooms = {
    "your room": {
        "needed item": None,
        "south": "the hallway",
        "item": "hallway key",
        "look": "The coldness of your room chills you to the bone, you see a door to the south.",
        "end": False
    },
    "the hallway": {
        "needed item": "hallway key",
        "east": "the closet",
        "south": "the movie room",
        "item": "living room key",
        "look": "A horror movies dream place, a half open door is to your east and south, your bedroom door is still open.",
        "end": False
    },
    "the closet": {
        "needed item": None,
        "west": "the hallway",
        "item": "dining room key",
        "look": "A nice smell fills your nose as you smell the dead rat beside you, good thing you left the door to your west open.",
        "end": False
    },
    "the movie room": {
        "needed item": None,
        "north": "the hallway",
        "east": "the living room",
        "south": "the play room",
        "item": "front door key",
        "look": "Good memories fill your brain, then get smushed by the darkness, the hallway is north of you, a door is to your east and south.",
        "end": False
    },
    "the play room": {
        "needed item": "play room key",
        "north": "the movie room",
        "item": "office key",
        "look": "Your old toys give you joy in this cold darkness, the door you came through is north.",
        "end": False
    },
    "the living room": {
        "needed item": "living room key",
        "east": "the office",
        "south": "mud room",
        "west": "the movie room",
        "item": "play room key",
        "look": "You can see the white moon seeping through the front door to the south, your fathers faveroute place is to the east.",
        "end": False
    },
    "the office": {
        "needed item": "office key",
        "north": "the dark room",
        "south": "the dining room",
        "west": "the living room",
        "item": "kitchen key",
        "look": "You dont recognize this place as your father never let you in, unless to go to the kitchen, south and north are where doors are.",
        "end": False
    },
    "the dining room": {
        "needed item": "dining room key",
        "north": "the office",
        "item": "dark room key",
        "look": "You get a tad bit starved seeing this place, a door is to the south and a hidden door is down below your feet.",
        "end": False
    },
    "the dark room": {
        "needed item": "dark room key",
        "south": "the office",
        "west": "the kitchen",
        "look": "You are to afraid to open your eyes, but the smell of food is drawing you west.",
        "end": False
    },
    "the kitchen": {
        "needed item": "kitchen key",
        "east": "the dark room",
        "item": "mud room key",
        "look": "You see the dirty white floors and the tinted windows as you make your way in, you better go back east.",
        "end": False
    },
    "mud room": {
        "needed item": "mud room key",
        "north": "the living room",
        "south": "outside",
        "look": "The smell of fresh air make you feel like life might be worth living, you can see your lawn south.",
        "end": False
    },
    "outside": {
        "needed item": "front door key",
        "end": True
    }
}
