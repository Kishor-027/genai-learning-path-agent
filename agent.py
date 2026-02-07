from compressor import compress_profile
from data import COURSE_DB, GOAL_SPECIFIC_PATHS


def generate_path(skills, goal, level):
    """Generate personalized learning path based on goal and level"""
    
    profile = compress_profile(skills)
    required = COURSE_DB[goal]["required"]
    advanced = COURSE_DB[goal]["advanced"]
    specific_path = GOAL_SPECIFIC_PATHS.get(goal, [])
    
    roadmap = []
    
    # Core Learning
    for skill in required:
        if skill not in profile:
            roadmap.append(f"📚 Complete {skill}")
    
    # Level Adaptation
    if level == "Beginner":
        roadmap = roadmap[:3]
        roadmap.extend([
            "🎯 Complete beginner projects",
            "📖 Study fundamentals",
            "💡 Join community forums"
        ])
    elif level == "Intermediate":
        roadmap = roadmap[:5]
        roadmap.extend([
            "🔧 Build real-world projects",
            "🚀 Learn advanced concepts",
            "🤝 Contribute to open-source"
        ])
    else:
        roadmap.extend([
            "🏆 Master advanced topics",
            "🔬 Lead research projects",
            "👨‍🏫 Mentor and teach others"
        ])
    
    # Add goal-specific paths
    for path in specific_path[:3]:
        roadmap.append(f"🎓 {path}")
    
    # Advanced modules
    for adv in advanced[:2]:
        roadmap.append(f"⚡ {adv}")
    
    # Goal-specific projects
    if goal == "GenAI Engineer":
        roadmap.extend([
            "🛠️ Build LLM application",
            "🔗 Create RAG system",
            "📊 Deploy production model"
        ])
    elif goal == "Data Scientist":
        roadmap.extend([
            "📈 Build ML models",
            "🔍 Analyze datasets",
            "🎨 Data visualization"
        ])
    else:
        roadmap.extend([
            "🎯 Create product strategy",
            "👥 User research",
            "📋 Build roadmaps"
        ])
    
    return roadmap
