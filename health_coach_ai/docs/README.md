# 🩺 Personal Health Coach AI – Project Documentation

## 1. Project Overview

**Personal Health Coach AI** is an agent-based health monitoring system that analyzes user-provided health descriptions, compresses them into meaningful health insights, and generates personalized recommendations with minimal processing cost.

The project focuses on **cost-efficient, privacy-first, offline AI**, making it suitable for environments where heavy LLM usage is not feasible.

---

## 2. Problem Statement

Most health monitoring applications rely on large language models or cloud-based APIs, which:

* Increase processing cost
* Raise privacy concerns
* Add latency

This project solves the problem by using **lightweight AI agents** that process health data locally using rule-based intelligence and memory compression.

---

## 3. Solution Architecture

The system is built using **multiple AI agents**, each with a clear responsibility:

### 🧠 Compression Agent

* Takes raw health text input
* Extracts key health indicators
* Compresses unstructured text into structured insights
* Calculates a health score (0–100)

### 💡 Recommendation Agent

* Consumes compressed health memory
* Generates personalized health advice
* Avoids redundant or unnecessary suggestions

### 💾 Memory Module

* Stores compressed health summaries
* Enables context retention during the session
* Supports future extensions like trend analysis

---

## 4. Project Structure

```
HEALTH_COACH_AI/
├── agents/
│   ├── compressor_agent.py
│   └── recommendation_agent.py
│
├── memory/
│   └── compressed_memory.py
│
├── data/
│   └── health_data.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 5. Workflow

1. User enters a natural language description of their health
2. Compression agent analyzes the input and produces:

   * Health insights
   * Health score
3. Compressed memory is optionally stored
4. Recommendation agent generates personalized advice
5. Results are displayed to the user

---

## 6. Health Scoring Logic

| Condition Detected | Score Impact |
| ------------------ | ------------ |
| High stress        | -30          |
| Poor sleep         | -30          |
| Low activity       | -20          |
| No risks detected  | 0            |

**Final Score Range:** 0–100

---

## 7. Technologies Used

* **Python 3**
* Agent-based architecture
* Rule-based NLP
* Modular software design

No external APIs or paid services are required.

---

## 8. How to Run the Project

```bash
python app.py
```

### Sample Input

```
I feel tired, slept 5 hours, very stressed
```

### Sample Output

```
Health Score: 20/100
Recommendations: Improve sleep, reduce stress, add exercise
```

---

## 9. Creative / Unique Features

* 🧠 Health data compression to reduce processing overhead
* 📊 Dynamic health scoring system
* 🔒 Privacy-first offline execution
* 🧩 Modular AI agent design

---

## 10. Future Enhancements

* Trend analysis across sessions
* Persistent database-backed memory
* Web or mobile interface
* Integration with wearable device data

---

## 11. Conclusion

Personal Health Coach AI demonstrates how **intelligent agent-based systems** can deliver meaningful health insights without relying on expensive or complex AI models. The project emphasizes efficiency, modularity, and real-world applicability.
