from typing import Any


def artifact_sorter(
    artifacts: list[dict[str, int | str]],
) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
    mages: list[dict[str, int | str]], min_power: int
) -> list[dict[str, int | str]]:

    return list(filter(lambda x: int(x["power"]) > min_power, mages))


# Map: Apply a function on iterable items and return map
# object -> iterable object
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int]:

    results: dict[str, Any] = {}

    results["max_power"] = sorted(
        mages, key=lambda x: x["power"], reverse=True
    )[0]["power"]

    results["min_power"] = sorted(
        mages, key=lambda x: x["power"], reverse=False
    )[0]["power"]

    results["avg_power"] = round(
        sum(map(lambda x: x["power"], mages)) / len(mages), 2
    )
    return results


if __name__ == "__main__":
    artifacts: list[dict[str, int | str]] = [
        {"name": "Earth Shield", "power": 103, "type": "armor"},
        {"name": "Fire Staff", "power": 63, "type": "weapon"},
        {"name": "Light Prism", "power": 93, "type": "armor"},
        {"name": "Light Prism", "power": 66, "type": "weapon"},
    ]

    print("Testing artifact sorter...\n")

    for i in artifact_sorter(artifacts):
        print(f"{i["name"]} ({i["power"]}) comes before", end="")

    print("\n\nTesting spell transformer...\n")
    names = ["fireball", "Shilksd", "test"]

    for j in spell_transformer(names):
        print(j, end=", ")
    print("\n\nTesting power filter...\n")
    for k in power_filter(artifacts, 66):
        print(f"Values appeard {k} ")
    print("\nShow stats...\n")
    for key, value in mage_stats(artifacts).items():
        print(f"{key} = {value}")
