import matplotlib.pyplot as plt
import numpy as np

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_path = sys.argv[1]
    else:
        results_path = "combined_results.txt"

    with open(results_path, "r") as f:
        pokemon_count, pokeball_count = f.readline().strip().split(',')

        pokemons = {}

        for _ in range(int(pokemon_count)):
            pokemon_name = f.readline().strip()
            info = {}

            line = f.readline().strip().split(',')
            base_pokeball = line[0]
            base_rate = float(line[1])
            info[base_pokeball] = 1

            for _ in range(int(pokeball_count)-1):
                line = f.readline().strip().split(',')
                info[line[0]] =  float(line[1])/base_rate

            pokemons[pokemon_name] = info

    names = list(pokemons.keys())
    pokeballs = list(next(iter(pokemons.values())).keys())

    fig, ax = plt.subplots(figsize = (10, 6))

    pokeball_colors = {
        "PokeBall": "red",
        "UltraBall": "black",
        "FastBall": "yellow",
        "HeavyBall": "blue",
    }

    for i, pokeball in enumerate(pokeballs):
        rates = [pokemons[pokemon][pokeball] for pokemon in names]
        ax.plot(names, rates, marker='o', linestyle = "-", label=pokeball, color=pokeball_colors[pokeball])

    ax.set_xlabel("Pokémon")
    ax.set_ylabel("Efectividad de captura relativa (%)")
    ax.set_title("Efectividad de captura relativa por pokemon")
    ax.set_xticks(np.arange(len(names)))
    ax.set_xticklabels(names, rotation=30, ha="right")
    ax.set_ylim(0, 5)
    ax.legend(title="Pokeball", bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.show()