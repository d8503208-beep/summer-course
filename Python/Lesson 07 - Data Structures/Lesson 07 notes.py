# Create the unit dictionary
unit = {
    "Smith": {
        "rank": "Sergeant",
        "years_of_service": 8
    },
    "Johnson": {
        "rank": "Captain",
        "years_of_service": 12
    },
    "Williams": {
        "rank": "Private",
        "years_of_service": 1
    },
    "Brown": {
        "rank": "Lieutenant",
        "years_of_service": 5
    },
    "Davis": {
        "rank": "Corporal",
        "years_of_service": 3
    }
}

# Lookup function that validates the last name and prints the soldier's information


def lookup_soldier(unit, last_name):
    if last_name in unit:
        soldier = unit[last_name]
        print(f"Soldier: {last_name}")
        print(f"Rank: {soldier['rank']}")
        print(f"Years of Service: {soldier['years_of_service']}")
    else:
        print(f"No soldier found with last name '{last_name}'.")


# Example usage
lookup_soldier(unit, "Johnson")
lookup_soldier(unit, "Garcia")
