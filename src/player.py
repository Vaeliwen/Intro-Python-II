# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentroom, items=[]):
        self.name = name
        self.currentroom = currentroom
        self.items = items
