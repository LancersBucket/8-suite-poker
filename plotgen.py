"""Plot data from sim.py"""
import json
import matplotlib.pyplot as plt

def plot(games='Unknown',players='Unknown'):
    """Plots data"""
    # Data
    data = {}
    with open('data.json',encoding="UTF-8") as f:
        data = json.load(f)

    games = data['meta']['games_played']
    players = data['meta']['players']

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(data['totals'].keys(), data['totals'].values(), color='blue')
    plt.xticks(rotation=90)
    plt.xlabel('Hands')
    plt.ylabel('Values')
    plt.title(f'{games} games with {players} player(s)')
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot()
