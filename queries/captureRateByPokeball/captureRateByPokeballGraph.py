import matplotlib.pyplot as plt
import numpy as np

import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_path = sys.argv[1]
    else:
        results_path = "results.txt"

    with open(results_path, "r") as f:
        pokemon_name = f.readline().strip()
        pokeball_count = int(f.readline().strip())

        pokeballs = []
        means = []
        deviations = []

        for _ in range(pokeball_count):
            pokeballs.append(f.readline().strip())
            means.append(float(f.readline().strip()) * 100)
            deviations.append(float(f.readline().strip()) * 100)

    plt.figure(figsize=(7, 5))
    bars = plt.bar(
        pokeballs,
        means,
        yerr=deviations,
        capsize=5,
    )
    plt.yticks(np.arange(0, 110, 10))

    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + deviations[i] + 2,
                 f"{means[i]:.2f}%",
                 ha="center",
                 fontsize=10,
                 color="black"
        )

    plt.xlabel('Pokeballs')
    plt.ylabel('Porcentaje de Captura Exitosa (%)')
    plt.title("Probabilidad de captura de " + pokemon_name.capitalize() + " en condiciones ideales")
    plt.ylim(0, 100)

    plt.show()

