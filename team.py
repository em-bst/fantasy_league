# Team Class (team.py):
# – Attributes: team name, players (a list of Player objects).
# – Methods: init , add player(), remove player(), str (to print team
# information).

class Team:
    def __init__(self, team_name, players = None):
        """
        Initializes a Team object with a team name and a list of players.

        :param team_name: The name of the team.
        :param players: A list of Player objects. Defaults to an empty list if none provided.
        """
        self.team_name = team_name
        self.players = players if players is not None else []
    
    def add_players(self, player):
        """
        Adds a player to the team.

        :param player: A Player object to add to the team.
        """
        self.players.append(player)

    def remove_players(self, player_name):
        """
        Removes a player from the team by name.

        :param player_name: The name of the player to remove.
        :return: True if the player was found and removed, False if the player was not found.
        """
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return True
        return False  # Player not found


    def __str__(self):
        """
        Returns a string representation of the team's details, including the team name and all players.

        :return: A formatted string with the team name and a list of player names and skill levels.
        """
        player_list = ', '.join([f"{player.name} (Skill: {player.skill_level})" for player in self.players])
        return f"The team {self.team_name} consists of the following players: {player_list if player_list else 'No players'}."