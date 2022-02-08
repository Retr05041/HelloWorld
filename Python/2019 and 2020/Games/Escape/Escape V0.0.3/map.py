rooms = {

    "your room": {
          "needed item": None,
          "east": "the living room",
          "item": "hallway key"
        },

    "the living room": {
            "needed item": None,
            "west": "your room",
            "east": "the bathroom",
            "south": "the kitchen",
            "item": "bathroom key"
        },
    "the bathroom": {
            "needed item": "bathroom key",
            "west": "the living room",
            "item": "lock pick"
        },
    "the kitchen": {
            "needed item": None,
            "north": "the living room",
            "west": "the hallway",
        },
    "the hallway": {
            "needed item": "hallway key",
            "north": "the pantry",
            "east": "the kitchen",
            "west": "the dining room",
        },
    "the pantry": {
            "needed item": "pantry key",
            "south": "the hallway",
            "item": "door key"
        },
    "the dining room": {
            "needed item": "lock pick",
            "east": "the hallway",
            "south": "outside",
            "item": "pantry key"
        },
    "outside": {
            "needed item": "door key"
        }
}
