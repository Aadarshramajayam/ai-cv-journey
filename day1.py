name = input("Your name: ").strip()
hours = float(input("Hours studied today: "))
topic = input("What did you learn: ").strip()
exercises = int(input("Exercises completed: "))

skills = []
skill = input("Enter a skill you know: ").strip()
skills.append(skill)
skill = input("Enter another skill: ").strip()
skills.append(skill)

def calculate_progress(completed, total):
    return (completed / total) * 100

progress = calculate_progress(exercises, 10)

print("\n========================")
print("   AI LEARNING TRACKER")
print("========================")
print(f"Student   : {name}")
print(f"Study time: {hours} hours")
print(f"Topic     : {topic}")
print(f"Exercises : {exercises}/10")
print(f"Progress  : {progress}%")
print(f"Skills    : {', '.join(skills)}")
print("========================")
print("Great work. Day 1 done.")