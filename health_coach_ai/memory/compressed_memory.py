import os
print("📁 compressor_agent loaded from:", os.path.abspath(__file__))


def compress_health_data(raw_text):
    text = raw_text.lower()
    insights = []

    if "stress" in text or "stressed" in text:
        insights.append("High stress detected")

    if "sleep" in text or "tired" in text:
        insights.append("Poor sleep pattern")

    if "exercise" not in text and "walk" not in text:
        insights.append("Low physical activity")

    if not insights:
        insights.append("No major health risks detected")

    return "; ".join(insights)
