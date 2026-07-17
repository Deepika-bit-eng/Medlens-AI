import json

with open("data/medicines.json", "r") as f:
    medicines = json.load(f)


def retrieve_medicine(name):

    for medicine in medicines:
        if medicine["name"].lower() == name.lower():
            return medicine

    return None
print(retrieve_medicine("Metformin"))