"""Test script to demonstrate tracker.py functionality"""

from pathlib import Path
from tracker import save_progress, load_progress
import json

# Sample data
profile = {
    "name": "John Doe",
    "email": "john@example.com",
    "current_level": "Intermediate",
    "learning_goal": "Machine Learning",
    "skills": ["Python", "Statistics", "SQL"]
}

roadmap = [
    {
        "id": 1,
        "topic": "Advanced Python",
        "completed": True,
        "duration": "2 weeks"
    },
    {
        "id": 2,
        "topic": "Machine Learning Fundamentals",
        "completed": False,
        "duration": "4 weeks"
    },
    {
        "id": 3,
        "topic": "Deep Learning",
        "completed": False,
        "duration": "6 weeks"
    },
    {
        "id": 4,
        "topic": "Build ML Projects",
        "completed": False,
        "duration": "8 weeks"
    }
]

# Define save path
save_path = Path("progress.json")

print("=" * 60)
print("TRACKER TEST - Demonstrating save_progress and load_progress")
print("=" * 60)

# Save progress
print("\n[1] SAVING PROGRESS...")
print("-" * 60)
saved_data = save_progress(profile, roadmap, save_path)
print(f"✓ Progress saved to: {save_path}")
print(f"✓ Saved at: {saved_data['saved_at']}")

# Load progress
print("\n[2] LOADING PROGRESS...")
print("-" * 60)
loaded_data = load_progress(save_path)

print("\nPROFILE:")
print(f"  Name: {loaded_data['profile']['name']}")
print(f"  Email: {loaded_data['profile']['email']}")
print(f"  Level: {loaded_data['profile']['current_level']}")
print(f"  Goal: {loaded_data['profile']['learning_goal']}")
print(f"  Skills: {', '.join(loaded_data['profile']['skills'])}")

print("\nROADMAP:")
for i, item in enumerate(loaded_data['roadmap'], 1):
    status = "✓ Completed" if item['completed'] else "○ Pending"
    print(f"  {i}. {item['topic']} ({item['duration']}) - {status}")

print(f"\nLast Updated: {loaded_data['saved_at']}")

print("\n[3] RAW JSON OUTPUT:")
print("-" * 60)
print(json.dumps(loaded_data, indent=2))

print("\n" + "=" * 60)
print("TEST COMPLETED SUCCESSFULLY")
print("=" * 60)
