#functions.py
import matplotlib.pyplot as plt

def plot_capture_percentage_1A(results, pokemon_name):

    percentages = {}

    for ball, captures in results.items():
        true_count = sum(1 for capture in captures if capture[0] is True)
        total_count = len(captures)
        true_percentage = (true_count / total_count) * 100
        percentages[ball] = true_percentage

    balls = list(percentages.keys())
    values = list(percentages.values())

    fig, ax = plt.subplots()
    bars = ax.bar(balls, values)

    for bar in bars:
        height = bar.get_height()
        if height > -1:  
            ax.text(
                bar.get_x() + bar.get_width() / 2,  
                height + 2,  
                f'{height:.1f}%',  
                ha='center',  
                va='bottom',  
                color='black'
            )

    plt.xlabel('Pokeballs', fontweight='bold')
    plt.ylabel('Porcentaje de Captura Exitosa (%)', fontweight='bold')
    plt.title( pokemon_name.capitalize())
    plt.ylim(0, 100)  

    plt.show()