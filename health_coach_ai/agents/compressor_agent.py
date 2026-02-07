def compress_health_data(raw_text):
    text = raw_text.lower()
    insights = []
    score = 100

    if "stress" in text or "stressed" in text:
        insights.append("High stress detected")
        score -= 30

    if "sleep" in text or "tired" in text:
        insights.append("Poor sleep pattern")
        score -= 30

    if "exercise" not in text and "walk" not in text:
        insights.append("Low physical activity")
        score -= 20

    if not insights:
        insights.append("No major health risks detected")

    return {
        "insights": "; ".join(insights),
        "score": max(score, 0)
    }
