# Player Class (player.py):
# – Attributes: name, skill level.
# – Methods: init , str (for easy printing of player details: “The player
# insert name has a skill level of insert skill level.”)

class Player:
    def __init__(self, name, skill_level):
        """
        Initializes a Player object with a name and skill level.

        :param name: The name of the player.
        :param skill_level: The skill level of the player (integer or float).
        """
        self.name = name
        self.skill_level = skill_level

    def __str__(self):
        """
        Returns a string representation of the player's details.

        :return: A formatted string with the player's name and skill level.
        """
        return f"The player {self.name} has a skill level of {self.skill_level}."