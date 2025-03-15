import json
import sys

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        if "pokeball" in config:
            ball = config["pokeball"]
        else:
            ball = "pokeball"

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

        pokemon = factory.create(config["pokemon"], config["level"], config["status_effect"], config["hp_percentage"])


        print("No noise: ", attempt_catch(pokemon, ball))
        for _ in range(int(config["attempts"])):
            print("Noisy: ", attempt_catch(pokemon, ball, 0.15))

