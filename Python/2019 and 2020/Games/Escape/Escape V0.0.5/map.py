rooms = {

    "your room": {
          "needed item": None,
          "east": "the living room",
          "item": "hallway key",
          "end": False
        },

    "the living room": {
            "needed item": None,
            "west": "your room",
            "east": "the bathroom",
            "south": "the kitchen",
            "item": "bathroom key",
            "end": False
        },
    "the bathroom": {
            "needed item": "bathroom key",
            "west": "the living room",
            "item": "lock pick",
            "end": False
        },
    "the kitchen": {
            "needed item": None,
            "north": "the living room",
            "west": "the hallway",
            "end": False
        },
    "the hallway": {
            "needed item": "hallway key",
            "north": "the pantry",
            "east": "the kitchen",
            "west": "the dining room",
            "end": False
        },
    "the pantry": {
            "needed item": "pantry key",
            "south": "the hallway",
            "item": "door key",
            "end": False
        },
    "the dining room": {
            "needed item": "lock pick",
            "east": "the hallway",
            "south": "outside",
            "item": "pantry key",
            "end": False
        },
    "outside": {
            "needed item": "door key",
            "end": True
        }
}
