"""Plot data from sim.py"""
import json
import matplotlib.pyplot as plt

def plot():
    """Plots data"""
    # Data
    data = {}
    with open('data.json',encoding="UTF-8") as f:
        data = json.load(f)

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), color='blue')
    plt.xticks(rotation=90)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart of Provided Data')
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot()
