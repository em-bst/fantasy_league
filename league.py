# League Class (league.py):
# – Attributes: teams (a list of Team objects), scores (dictionary to store game
# results: key is the team name, value is the number of points).
# – Methods:
# ∗ init
# ∗ simulate game(): inputs: 2 teams, step 1) compare the mean of player skills
# to determine which team wins, step 2) update attribute scores: +3 for the
# winner, or +1 for both teams if it’s a tie
# ∗ play season(): call simulate game() for all combinations of teams
# ∗ get results(): print scores
# – Note: You can use NumPy to add some randomness to the result of the game.

import numpy as np
from itertools import combinations

class League:
    def __init__(self, teams):
        """
        Initializes a League object with a list of teams and a dictionary to store scores.

        :param teams: A list of Team objects.
        """
        self.teams = teams
        self.scores = {team.team_name: 0 for team in teams}  # Initialize scores for each team

    def simulate_game(self, team1, team2):
        """
        Simulates a game between two teams. The team with the higher average skill wins.
        Some randomness is added to make the simulation less predictable.

        :param team1: The first Team object.
        :param team2: The second Team object.
        """
        # Step 1: Calculate the mean skill level of both teams
        mean_skill_team1 = np.mean([player.skill_level for player in team1.players])
        mean_skill_team2 = np.mean([player.skill_level for player in team2.players])

        # Add randomness to the result using normal distribution
        mean_skill_team1 += np.random.normal(0, 5)  # Adding randomness (mean 0, std deviation 5)
        mean_skill_team2 += np.random.normal(0, 5)

        # Step 2: Determine the winner or if it's a tie
        if mean_skill_team1 > mean_skill_team2:
            # Team 1 wins
            self.scores[team1.team_name] += 3
            print(f"{team1.team_name} wins against {team2.team_name}")
        elif mean_skill_team1 < mean_skill_team2:
            # Team 2 wins
            self.scores[team2.team_name] += 3
            print(f"{team2.team_name} wins against {team1.team_name}")
        else:
            # It's a tie
            self.scores[team1.team_name] += 1
            self.scores[team2.team_name] += 1
            print(f"{team1.team_name} ties with {team2.team_name}")

    def play_season(self):
        """
        Simulates a season where each team plays against all other teams.
        """
        # Step 3: Simulate games for all combinations of teams
        for team1, team2 in combinations(self.teams, 2):
            self.simulate_game(team1, team2)

    def get_results(self):
        """
        Prints the final scores for each team at the end of the season.
        """
        print("Final Scores:")
        for team, score in self.scores.items():
            print(f"{team}: {score} points")
