import json
import sys

import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

pokeballs = ["PokeBall", "UltraBall", "FastBall", "HeavyBall"]

if __name__ == "__main__":
    factory = PokemonFactory("../../pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        pokemon_name = config["pokemon"]

        if "attempts" in config:
            attempts = int(config["attempts"])
        else:
            attempts = 100

        if "outPath" in config:
            out_path = config["outPath"]
        else:
            out_path = "results.txt"

    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)


    with open(out_path, "w") as f:
        f.write(f"{pokemon_name}\n{len(pokeballs)}\n")
        for pokeball in pokeballs:
            f.write(f"{pokeball}\n{attempts}\n")
            rates = []
            for _ in range(100):
                count = 0
                for _ in range(attempts):
                    captured, _ = attempt_catch(pokemon, pokeball.lower())
                    if captured:
                        count += 1
                rates.append(count/attempts)

            f.write(f"{np.mean(rates)}\n{np.std(rates)}\n")

