import json
import sys

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]
status_effects = [StatusEffect.NONE, StatusEffect.POISON, StatusEffect.BURN, StatusEffect.PARALYSIS, StatusEffect.SLEEP, StatusEffect.FREEZE]

def get_catch_rate(pokemon_name, level, attempts, pokeball, status, hp_percent, noise):
    pokemon = factory.create(pokemon_name, level, status, hp_percent)
    captures = 0
    for _ in range(attempts):
        capture, _ = attempt_catch(pokemon, pokeball, noise)
        if capture:
            captures += 1
    return captures/attempts

def main():
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)

        pokemon_name = config["pokemon"]

        if "level" in config:
            level = config["level"]
        else:
            level = 100

        if "attempts" in config:
            attempts = config["attempts"]
        else:
            attempts = 1000

        if "noise" in config:
            noise = config["noise"]
        else:
            noise = 0

    if len(sys.argv) >= 3:
        out_path = sys.argv[3]
    else:
        out_path = "./configs/ej2/d/" + pokemon_name + "_optimal_config.json"

    optimal_config = {}
    highest_rate = 0

    for pokeball in pokeballs:
        for status in status_effects:
            for i in range(1, 100):
                rate = get_catch_rate(pokemon_name, level, attempts, pokeball, status, i/100, noise)
                if rate > highest_rate:
                    optimal_config = {"pokeball": pokeball, "status_effect": status.value[0], "hp_percentage": i/100}
                    highest_rate = rate

    optimal_config["highest_rate"] = highest_rate
    optimal_config["pokemon"] = pokemon_name
    optimal_config["level"] = level
    with open(out_path, "w") as f:
        json.dump(optimal_config, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()