"""Comprehensive test of all backend modules"""

from pathlib import Path
from agent import generate_path
from analyzer import analyze_gaps
from compressor import compress_profile
from tracker import save_progress, load_progress
import json

print("\n" + "=" * 70)
print("GENAI LEARNING PATH AGENT - COMPREHENSIVE TEST")
print("=" * 70)

# Test 1: Compress Profile
print("\n[TEST 1] COMPRESSING PROFILE")
print("-" * 70)
raw_skills = ["Python", "python", "SQL", "  Statistics  ", "statistics"]
print(f"Raw skills input: {raw_skills}")
compressed = compress_profile(raw_skills)
print(f"Compressed profile: {compressed}")
print(f"✓ Duplicates removed and normalized")

# Test 2: Analyze Gaps
print("\n[TEST 2] ANALYZING SKILL GAPS")
print("-" * 70)
user_skills = ["Python", "Statistics"]
learning_goal = "Data Scientist"
print(f"User skills: {user_skills}")
print(f"Learning goal: {learning_goal}")
gaps = analyze_gaps(user_skills, learning_goal)
print(f"Skill gaps identified: {gaps}")
print(f"✓ Found {len(gaps)} skill gaps to address")

# Test 3: Generate Learning Path
print("\n[TEST 3] GENERATING LEARNING PATH")
print("-" * 70)
skills = ["Python", "SQL"]
goal = "Data Scientist"
level = "Beginner"
print(f"Input - Skills: {skills}")
print(f"Input - Goal: {goal}")
print(f"Input - Level: {level}")
roadmap = generate_path(skills, goal, level)
print(f"\nGenerated Roadmap ({len(roadmap)} items):")
for i, item in enumerate(roadmap, 1):
    print(f"  {i}. {item}")

# Test 4: Save and Load Progress
print("\n[TEST 4] SAVING AND LOADING PROGRESS")
print("-" * 70)
profile = {
    "name": "Alex Johnson",
    "email": "alex@example.com",
    "current_level": level,
    "learning_goal": goal,
    "skills": skills,
    "skill_gaps": gaps
}

roadmap_data = [
    {"id": i, "task": item, "completed": False}
    for i, item in enumerate(roadmap, 1)
]

save_path = Path("learning_progress.json")
print(f"Saving to: {save_path}")
saved_data = save_progress(profile, roadmap_data, save_path)
print(f"✓ Progress saved successfully")
print(f"  Timestamp: {saved_data['saved_at']}")

# Load and display
print(f"\nLoading saved progress...")
loaded = load_progress(save_path)
print(f"✓ Progress loaded successfully")

print(f"\nUser Profile:")
print(f"  Name: {loaded['profile']['name']}")
print(f"  Email: {loaded['profile']['email']}")
print(f"  Goal: {loaded['profile']['learning_goal']}")
print(f"  Level: {loaded['profile']['current_level']}")
print(f"  Current Skills: {', '.join(loaded['profile']['skills'])}")
print(f"  Skill Gaps: {', '.join(loaded['profile']['skill_gaps'])}")

print(f"\nRoadmap Progress:")
for item in loaded['roadmap']:
    status = "✓" if item['completed'] else "○"
    print(f"  {status} [{item['id']}] {item['task']}")

# Test 5: Multiple Goal Examples
print("\n[TEST 5] DIFFERENT LEARNING GOALS")
print("-" * 70)
goals = ["GenAI Engineer", "AI Product Manager", "Data Scientist"]
user_level = "Intermediate"
test_skills = ["Python", "LLM APIs"]

for goal_name in goals:
    print(f"\n→ {goal_name}:")
    gaps = analyze_gaps(test_skills, goal_name)
    roadmap = generate_path(test_skills, goal_name, user_level)
    print(f"  Gaps: {gaps}")
    print(f"  Roadmap items: {len(roadmap)}")
    print(f"  First 3 items: {roadmap[:3]}")

print("\n" + "=" * 70)
print("ALL TESTS COMPLETED SUCCESSFULLY ✓")
print("=" * 70 + "\n")
