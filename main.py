import json
import sys

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

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
            pokemon = config["pokemon"]
        else:
            pokemon = "caterpie"

        if "status_effect" in config:
            status_effect = config["status_effect"]
        else:
            status_effect = StatusEffect.NONE

        if "hp_percentage" in config:
            hp_percentage = config["hp_percentage"]
        else:
            hp_percentage = 1

        if "level" in config:
            level = config["level"]
        else:
            level = 100

        if "attempts" in config:
            attempts = config["attempts"]
        else:
            attempts = 1

        if "out_path" in config:
            out_path = config["outpath"]
        else:
            out_path = "result.txt"

        if "noise" in config:
            noise = config["noise"]
        else:
            noise = 0

    with open(f"{out_path}", "w") as f:

        pokemon = factory.create(pokemon, level, status_effect, hp_percentage)
        results = {}

        for ball in balls:
            results[ball] = []
            f.write(f"{ball}\n")
            for _ in range(int(attempts)):
                capture = attempt_catch(pokemon, ball, noise)
                results[ball].append(capture)
                f.write(f"{capture}\n")




