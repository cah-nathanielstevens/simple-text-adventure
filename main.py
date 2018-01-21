class Room:
    def __init__(self, north=None, south=None, east=None, west=None, description=None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def go(self, direction):
        if direction == 'north' and self.north:
            return self.north
        elif direction == 'south' and self.south:
            return self.south
        elif direction == 'east' and self.east:
            return self.east
        elif direction == 'west' and self.west:
            return self.west
        else:
            print("You can't go " + direction)
            return self
        
    def describe(self):
        print(self.description)

def main():
    print(("After a long walk you finally arrive at your great grandfather's old house.\n"
           "You had thought it was abandoned but oddly there is one light on in the attic.\n"
           "You enter the house to persue your fortune.\n\n"))
    
    entrance = Room()
    reading_room = Room()
    upstairs_landing = Room()
    solarium = Room()

    entrance.description = ("To the north lies a grand staircase.\n"
                            "To the east a reading room.\n"
                            "To the west a solarium.\n")
    entrance.north = upstairs_landing
    entrance.east = reading_room
    entrance.west = solarium


    reading_room.description = ("Wow...that's a lot of books. You see title such as:\n"
                                "'Skinning a Dog: For Work and Play,'\n"
                                "'Demonic Possession for the Neophyte, and'\n"
                                "'How to Win Friends and Influence People.'\n"
                                "To the West is the Entrance")
    reading_room.west = entrance


    solarium.description = ("You imagine the solarium must be far more impressive in the daytime.\n"
                            "However, during the day you might not notice that there is a candle burning\n"
                            "...Why is there a candle burning? Isn't this house abandoned?\n"
                            "To the East is the entrance.")
    solarium.east = entrance


    upstairs_landing.description = "Well, you're upstairs now. To the South is the entrance."
    upstairs_landing.south = entrance
    
    current_room = entrance
    isRunning = True
    
    while isRunning:
        current_room.describe()
        command = input(">")
        command_words = command.lower().split(" ")

        if 'go' in command_words:
            if 'north' in command_words:
                current_room = current_room.go('north')
            elif 'south' in command_words:
                current_room = current_room.go('south')
            elif 'east' in command_words:
                current_room = current_room.go('east')
            elif 'west' in command_words:
                current_room = current_room.go('west')
        elif 'help' in command_words:
            print("Go [North,South,East,West]")
        elif 'quit' in command_words:
            print("And thus ends the adventure.")
            isRunning = False
        else:
            print("I don't know how to '" + command + "'")


if __name__ == '__main__':
    main()
