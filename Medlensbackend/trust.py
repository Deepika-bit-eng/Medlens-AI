def calculate_trust(medicine):

    score = 0
    reasons = []

    if medicine.get("purpose"):
        score += 25
        reasons.append("Purpose identified")

    if medicine.get("why_prescribed"):
        score += 25
        reasons.append("Reason for prescription explained")

    if medicine.get("common_side_effects"):
        score += 20
        reasons.append("Common side effects available")

    if medicine.get("source"):
        score += 20
        reasons.append("Verified medical source available")

    if medicine.get("confidence", 0) >= 90:
        score += 10
        reasons.append("High AI confidence")

    medicine["trust_score"] = score
    medicine["reasoning"] = reasons

    return medicine