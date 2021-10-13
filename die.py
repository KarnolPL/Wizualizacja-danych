from random import randint

class Die:
    """Klasa przedstawiajaca pojedyncza koncz do gry"""

    def __init__(self, num_sides=6):
        """Przyjecie założenia ze kosc do gry ma postac szczescianu"""
        self.num_sides = num_sides

    def roll(self):
        "Rzucenie koscia i odtrzymanie wyniku od 1 do ilosci scian w kosci"
        return randint(1, self.num_sides)