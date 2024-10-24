import pandas as pd
import random
from player import Player
from team import Team
from league import League

def load_players_from_csv_with_pandas(filename):
    # Lire le fichier CSV avec Pandas
    df = pd.read_csv('players.csv', delimiter=';')
    
    # Créer une liste de Player à partir des données du DataFrame
    players = [Player(row['Name'], row['Skill_level']) for _, row in df.iterrows()]
    
    return players

# Exemple d'utilisation
players = load_players_from_csv_with_pandas('players.csv')

for player in players:
    print(player)

def initialize_teams(team_names, players):
    """
    Initializes team objects with given team names and randomly assigns players to each team.
    
    :param team_names: A list of team names.
    :param players: A list of Player objects.
    :return: A list of Team objects.
    """
    num_players_per_team = len(players) // len(team_names)
    
    if len(players) < len(team_names) * 3:
        raise ValueError("Not enough players to form teams. Each team needs at least 3 players.")

    # Shuffle the list of players to ensure random assignment
    random.shuffle(players)
    
    teams = []
    for i, team_name in enumerate(team_names):
        team_players = players[i * num_players_per_team:(i + 1) * num_players_per_team]
        team = Team(team_name, team_players)
        teams.append(team)
    
    return teams


def simulate_season(teams):
    """
    Simulates a full season by playing games among all teams.
    
    :param teams: A list of Team objects.
    """
    # Initialize the league with the teams
    league = League(teams)
    
    # Play the season
    league.play_season()
    
    # Print final results
    league.get_results()


def main():
    # Step 1: Load players from CSV
    players = load_players_from_csv_with_pandas('players.csv')
    
    # Step 2: Initialize 4 teams
    team_names = ["Team Alpha", "Team Bravo", "Team Charlie", "Team Delta"]
    
    # Step 3: Randomly assign players to teams
    teams = initialize_teams(team_names, players)
    
    # Step 4: Simulate the season
    simulate_season(teams)


if __name__ == "__main__":
    main()