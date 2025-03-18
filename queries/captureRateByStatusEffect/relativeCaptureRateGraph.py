import matplotlib.pyplot as plt
import numpy as np

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_path = sys.argv[1]
    else:
        results_path = "combined_results.txt"

    with open(results_path, "r") as f:
        pokemon_count, status_count = f.readline().strip().split(',')

        pokemons = {}

        for _ in range(int(pokemon_count)):
            pokemon_name = f.readline().strip()
            info = {}

            line = f.readline().strip().split(',')
            base_status = line[0]
            base_rate = float(line[1])
            info[base_status] = 1

            for _ in range(int(status_count)-1):
                line = f.readline().strip().split(',')
                info[line[0]] =  float(line[1])/base_rate

            pokemons[pokemon_name] = info

    names = list(pokemons.keys())
    effects = list(next(iter(pokemons.values())).keys())

    fig, ax = plt.subplots(figsize = (10, 6))

    status_colors = {
        "Ninguno": "black",
        "Dormido": "green",
        "Quemadura": "red",
        "Congelado": "blue",
        "Veneno": "purple",
        "Parálisis": "yellow",
    }

    for i, status in enumerate(effects):
        rates = [pokemons[pokemon][status] for pokemon in names]
        ax.plot(names, rates, marker='o', linestyle = "-", label=status, color=status_colors[status])

    ax.set_xlabel("Pokémon")
    ax.set_ylabel("Efectividad de captura relativa (%)")
    ax.set_title("Efectividad de captura relativa por pokemon")
    ax.set_xticks(np.arange(len(names)))
    ax.set_xticklabels(names, rotation=30, ha="right")
    ax.set_ylim(0, 3)
    ax.legend(title="Efectos de estado", bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.show()