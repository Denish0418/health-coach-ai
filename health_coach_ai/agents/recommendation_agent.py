def recommend_health(memory):
    recommendations = []

    insights = memory["insights"].lower()
    score = memory["score"]

    if "stress" in insights:
        recommendations.append("Practice meditation or breathing exercises")

    if "sleep" in insights:
        recommendations.append("Aim for 7–8 hours of quality sleep")

    if "physical" in insights:
        recommendations.append("Include daily walking or light exercise")

    if score >= 80:
        recommendations.append("You're doing great — keep it up!")

    return " | ".join(recommendations)
