from agents.compressor_agent import compress_health_data
from agents.recommendation_agent import recommend_health

print("🩺 Personal Health Coach AI")
print("Type 'exit' to stop")
print("----------------------------------------")

while True:
    user_input = input("\n👉 Describe your health: ")

    if user_input.lower() == "exit":
        print("👋 Stay healthy! Goodbye.")
        break

    memory = compress_health_data(user_input)

    print("\n🧠 Compressed Health Memory:")
    print(memory["insights"])

    print(f"\n📊 Health Score: {memory['score']}/100")

    print("\n💡 Health Recommendation:")
    print(recommend_health(memory))
