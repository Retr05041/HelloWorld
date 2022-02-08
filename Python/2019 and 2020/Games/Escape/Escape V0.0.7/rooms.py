rooms = {
    "your room": {
        "needed item": None,


        "south": "the hallway",

        "item": "hallway key",
        "end": False
    },
    "the hallway": {
        "needed item": "hallway key",

        "east": "the closet",
        "south": "the movie room",

        "item": "living room key",
        "end": False
    },
    "the closet": {
        "needed item": None,
        "west": "the hallway",
        "item": "dining room key",
        "end": False
    },
    "the movie room": {
        "needed item": None,
        "north": "the hallway",
        "east": "the living room",
        "south": "the play room",
        "item": "front door key",
        "end": False
    },
    "the play room": {
        "needed item": "play room key",
        "north": "the movie room",
        "item": "office key",
        "end": False
    },
    "the living room": {
        "needed item": "living room key",
        "east": "the office",
        "south": "extra lock",
        "west": "the movie room",
        "item": "play room key",
        "end": False
    },
    "the office": {
        "needed item": "office key",
        "north": "the dark room",
        "south": "the dining room",
        "west": "the living room",
        "item": "kitchen key",
        "end": False
    },
    "the dining room": {
        "needed item": "dining room key",
        "north": "the office",
        "item": "dark room key",
        "end": False
    },
    "the dark room": {
        "needed item": "dark room key",
        "south": "the office",
        "west": "the kitchen",
        "end": False
    },
    "the kitchen": {
        "needed item": "kitchen key",
        "east": "the dark room",
        "item": "mud room key",
        "end": False
    },
    "mud room": {
        "needed item": "mud room key",
        "north": "the living room",
        "south": "outside",
        "end": False
    },
    "outside": {
        "needed item": "front door key",
        "south": "extra lock",
        "end": True
    }
}
