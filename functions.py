#functions.py
import matplotlib.pyplot as plt

def plot_capture_percentage_1(results, pokemon_name):

    percentages = {}

    for info, captures in results.items():
        true_count = sum(1 for capture in captures if capture[0] is True)
        total_count = len(captures)
        true_percentage = (true_count / total_count) * 100
        percentages[info[0]] = true_percentage

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

def plot_capture_effect_percentage_2A(results, pokemon_name):
    effect_percentages = {}

    for (ball, effect,hp, level), captures in results.items():
        true_count = sum(1 for capture in captures if capture[0] is True)
        total_count = len(captures)
        true_percentage = (true_count / total_count) * 100
        
        if effect not in effect_percentages:
            effect_percentages[effect] = []
        effect_percentages[effect].append(true_percentage)

    average_percentages = {effect: sum(percentages) / len(percentages) for effect, percentages in effect_percentages.items()}

    effect_labels = [effect.value[0].capitalize() for effect in average_percentages.keys()]
    values = list(average_percentages.values())

    fig, ax = plt.subplots()
    bars = ax.bar(effect_labels, values)

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

    plt.xlabel('Efecto de la Pelota', fontweight='bold')
    plt.ylabel('Porcentaje de Captura Exitosa (%)', fontweight='bold')
    plt.title(f'Porcentaje de Captura Exitosa por Efecto - {pokemon_name.capitalize()}')
    plt.ylim(0, 100)  

    plt.show()


def plot_capture_effect_percentage_2B(results, pokemon_name,hp_percentages):
    hp_labels = [f"{int(hp * 100)}%" for hp in hp_percentages]
    average_percentages = {}

    for (ball, effect, hp_percentage, level), captures in results.items():
        true_count = sum(1 for capture in captures if capture[0] is True)
        total_count = len(captures)
        true_percentage = (true_count / total_count) * 100
        
        key = (effect.value[0], hp_percentage)
        if key not in average_percentages:
            average_percentages[key] = []
        average_percentages[key].append(true_percentage)
    
    averaged_values = {key: sum(values) / len(values) for key, values in average_percentages.items()}
    
    hp_labels = [f"{int(hp * 100)}%" for _, hp in averaged_values.keys()]
    values = list(averaged_values.values())
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(hp_labels, values)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f'{height:.1f}%',
            ha='center',
            va='bottom',
            color='black'
        )

    plt.xlabel('HP', fontweight='bold')
    plt.ylabel('Porcentaje de Captura Exitosa (%)', fontweight='bold')
    plt.title(f'Porcentaje de Captura de {pokemon_name.capitalize()}')
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()