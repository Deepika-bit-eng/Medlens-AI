import json
from extractor import extract_prescription
from retriever import retrieve_medicine
from trust import calculate_trust
from interaction import check_interactions

def run_agent(image_path):

    result = extract_prescription(image_path)

    print("===== RAW EXTRACTOR OUTPUT =====")
    print(result)
    print("===============================")

    result = result.replace("```json", "").replace("```", "").strip()

    data = json.loads(result)

    explained_medicines = []

    for medicine in data["medicines"]:
        medicine_data = retrieve_medicine(medicine["name"])
        if medicine_data is None:
            medicine_data = {
               "name": medicine["name"],
               "purpose": "Medicine not found in local database.",
               "why_prescribed": "Unknown",
                "common_side_effects": [],
                "source": "Not Available"
    }

        medicine_data = calculate_trust(medicine_data)

        explained_medicines.append(medicine_data)

    data["medicines"] = explained_medicines

    medicine_names = []

    for med in explained_medicines:
        medicine_names.append(med["name"])

    data["interaction_report"] = check_interactions(medicine_names)

    return data