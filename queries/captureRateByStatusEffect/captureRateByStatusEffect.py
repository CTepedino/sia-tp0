import json
import sys

import numpy as np

from src.catching import attempt_catch
from src.pokemon import StatusEffect, PokemonFactory

status_effects = [StatusEffect.NONE, StatusEffect.SLEEP, StatusEffect.BURN, StatusEffect.FREEZE, StatusEffect.POISON, StatusEffect.PARALYSIS]

if __name__ == "__main__":
    factory = PokemonFactory("../../pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        pokemon_name = config["pokemon"]

        if "pokeball" in config:
            pokeball = config["pokeball"]
        else:
            pokeball = "pokeball"

        if "attempts" in config:
            attempts = int(config["attempts"])
        else:
            attempts = 100

        if "outPath" in config:
            out_path = config["outPath"]
        else:
            out_path = "results.txt"

    with open(out_path, "w") as f:
        f.write(f"{pokemon_name}\n{len(status_effects)}\n")
        for status_effect in status_effects:
            pokemon = factory.create(pokemon_name, 100, status_effect, 1)
            f.write(f"{status_effect.value[0].capitalize()}\n")
            rates = []
            for _ in range(100):
                count = 0
                for _ in range(attempts):
                    captured, _ = attempt_catch(pokemon, pokeball)
                    if captured:
                        count += 1
                rates.append(count / attempts)

            f.write(f"{np.mean(rates)}\n{np.std(rates)}\n")
