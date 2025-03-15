import json
import sys

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

import functions as mf

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        if "pokeball" in config:
            balls = [config["pokeball"]]
        elif "pokeballs" in config:
            balls = config["pokeballs"]
        else:
            balls = ["pokeball"]

        if "pokemon" in config:
            pokemon_name = config["pokemon"]
        else:
            pokemon_name = "caterpie"

        if "status_effect" in config:
            status_effect_lookup = {effect.value[0]: effect for effect in StatusEffect}
            status_effects = [status_effect_lookup.get(config["status_effect"], None)]
        elif "status_effects" in config:
            status_effect_lookup = {effect.value[0]: effect for effect in StatusEffect}
            status_effects = []
            for effect in config["status_effects"]:
                status_effects.append(status_effect_lookup.get(effect, None))
        else:
            status_effects = [StatusEffect.NONE]

        if "hp_percentage" in config:
            hp_percentages = [config["hp_percentage"]]
        elif "hp_percentages" in config:
            hp_percentages = config["hp_percentages"]
        else:
            hp_percentages = [1]

        if "level" in config:
            levels = [config["level"]]
        elif "levels" in config:
            levels = config["levels"]
        else:
            levels = [100]

        if "attempts" in config:
            attempts = config["attempts"]
        else:
            attempts = 1

        if "noise" in config:
            noise = config["noise"]
        else:
            noise = 0

    if len(sys.argv) == 3:
        out_path = sys.argv[3]
    else:
        out_path = "result.txt"

    with open(f"{out_path}", "w") as f:

        results = {}

        for ball in balls:
            f.write(f"{ball}\n")
            for effect in status_effects:
                f.write(f"{effect.value[0]}\n")
                for hp_percentage in hp_percentages:
                    f.write(f"{hp_percentages}\n")
                    for level in levels:
                        f.write(f"{level}\n")
                        info = (ball, effect, hp_percentage, level)
                        results[info] = []
                        pokemon = factory.create(pokemon_name, level, effect, hp_percentage)
                        for _ in range(int(attempts)):
                            capture = attempt_catch(pokemon, ball, noise)
                            results[info].append(capture)
                            f.write(f"{capture}\n")

    if len(sys.argv) >= 3:
        match sys.argv[2]:
            case "1A":
                mf.plot_capture_percentage_1(results, pokemon_name)
            case "2A":
                mf.plot_capture_effect_percentage_2(results, pokemon_name)
            case "2B":
                pass

    # mf.plot_capture_percentage_1(results, pokemon_name)

