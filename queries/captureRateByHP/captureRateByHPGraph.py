import matplotlib.pyplot as plt

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_path = sys.argv[1]
    else:
        results_path = "results.txt"

    with open(results_path, "r") as f:
        pokemon_name = f.readline().strip()
        step = int(f.readline().strip())

        hp_percents = []
        means = []
        deviations = []

        for i in range(step, 100 + step, step):
            hp_percents.append(int(f.readline().strip()))
            means.append(float(f.readline().strip()) * 100)
            deviations.append(float(f.readline().strip()) * 100)

    plt.figure(figsize=(7, 5))
    plt.errorbar(hp_percents, means, yerr=deviations, ecolor="black", capsize=5)
    plt.scatter(hp_percents, means)
    plt.yticks(list(range(0, 110, 10)))
    plt.hlines(y=list(range(0, 110, 10)), xmin=0, xmax=100, color='gray', linestyle='dotted')
    plt.xticks(list(range(step, 100 + step, step)))

    plt.xlabel('HP (%)')
    plt.ylabel('Porcentaje de Captura Exitosa (%)')
    plt.title("Probabilidad de captura de " + pokemon_name.capitalize() + " según su HP")
    plt.ylim(0, 100)


    plt.show()