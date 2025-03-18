import json
import sys

import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("../../pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        pokemon_name = config["pokemon"]

        if "attempts" in config:
            attempts = int(config["attempts"])
        else:
            attempts = 25

        if "pokeball" in config:
            pokeball = config["pokeball"]
        else:
            pokeball = "pokeball"

        if "noise" in config:
            noise = float(config["noise"])
        else:
            noise = 0

        if "step" in config:
            step = int(config["step"])
        else:
            step = 5

        if "outPath" in config:
            out_path = config["outPath"]
        else:
            out_path = "results.txt"

    with open(out_path, "w") as f:
        f.write(f"{pokemon_name}\n{step}\n")
        for i in range(step, 100 + step, step):
            f.write(f"{i}\n")
            pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, i/100)
            rates = []
            for _ in range(attempts):
                _, rate = attempt_catch(pokemon, pokeball, noise)
                rates.append(rate)
            f.write(f"{np.mean(rates)}\n{np.std(rates)}\n")
