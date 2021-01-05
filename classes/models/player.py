"""Player model module"""
from .save_loading_data import SaveLoadingData


class Player:
    """Class for players"""

    def __init__(self):
        self.id = SaveLoadingData.nb_players() + 1
        self.last_name = ""
        self.first_name = ""
        self.date_of_birth = ""
        self.sex = ""
        self.rank = 0
        self.new_player()

    def new_player(self):
        """player information instance method"""
        self.last_name = input("Enter player last name : ")
        self.first_name = input("Enter player first name : ")
        self.date_of_birth = input("Enter player birth date (format dd/mm/yyyy) : ")
        self.sex = input("enter player sex 'M' or 'F' : ")
        while True:
            try:
                rank = int(input("enter player rank : "))
            except ValueError:
                print("\nPlease enter valid number.")
                input("Press ENTER to continue...")
                continue
            else:
                self.rank = abs(rank)
                break
