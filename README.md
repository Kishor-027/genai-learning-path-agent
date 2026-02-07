# 🎓 GenAI Learning Path Assistant
> **AI-Powered Personalized Learning Roadmap Generator** - Get customized learning paths for GenAI Engineer, Data Scientist, and AI Product Manager roles with real-time progress tracking and skill gap analysis.

## 🌟 About the Project

GenAI Learning Path Assistant is an intelligent, modular Streamlit web application designed to help learners and professionals create personalized learning roadmaps in AI and related fields. The application combines advanced profile compression, comprehensive skill gap analysis, intelligent path generation, and progress tracking into a single, intuitive dark-themed dashboard.

Whether you're a beginner starting your AI journey or an advanced professional looking to specialize, this tool adapts to your experience level and career goals to provide actionable, step-by-step learning plans.

### 🎯 Mission
To democratize AI education by providing personalized, data-driven learning paths that help individuals bridge skill gaps and achieve their career goals in Artificial Intelligence and Machine Learning.

---

## ✨ Key Features

### 1. **Smart Profile Compression** 📚
- Automatically normalizes and deduplicates user skills
- Removes redundant skill entries (e.g., "Python", "python" → "Python")
- Creates a clean, focused learner profile
- Handles whitespace and case normalization

### 2. **Intelligent Skill Gap Analysis** 🔍
- Identifies missing skills for your chosen career goal
- Compares current profile against industry requirements
- Provides clear visibility into learning priorities
- Goal-specific skill requirements built-in

### 3. **Personalized Learning Path Generation** 🗺️
- **Goal-Based Customization**: Different paths for:
  - 🛠️ **GenAI Engineer**: LLM APIs, RAG systems, vector databases, MLOps
  - 📊 **Data Scientist**: Statistics, ML pipelines, visualization, A/B testing
  - 📱 **AI Product Manager**: Product strategy, user research, roadmapping, metrics
  
- **Level-Aware Adaptation**:
  - **Beginner**: Foundation focus (3 core skills + community engagement)
  - **Intermediate**: Balanced approach (5 core skills + project work)
  - **Advanced**: Specialization (leadership, research, mentoring)

- **Structured Roadmap Items**:
  - Core skill courses with emojis for visual clarity
  - Goal-specific learning modules
  - Advanced topics and specializations
  - Hands-on project recommendations
  - Industry-relevant certifications

### 4. **Real-Time Progress Tracking** 📈
- **Color-Coded Status Indicators**:
  - 🔴 **RED (0-25%)**: Needs Significant Improvement
  - 🟡 **YELLOW (25-50%)**: Keep Improving
  - 🔵 **BLUE (50-75%)**: On Track
  - 🟢 **GREEN (75-100%)**: Perfect!

- **Detailed Progress Breakdown**:
  - Visual progress bar with gradient
  - Completion percentage metrics
  - Status-specific recommendations
  - Actionable next steps based on progress level

### 5. **JSON-Based Progress Persistence** 💾
- Save learning profiles and roadmaps to JSON
- Export progress snapshots with timestamps
- Easy integration with external systems
- Resume learning anytime with saved data

### 6. **API Key Management** 🔑
- Built-in API configuration panel
- Support for OpenAI/Claude API keys
- Secure (password field) API key input
- Ready for future AI service integrations

### 7. **Beautiful Dark-Themed UI** 🎨
- Modern, professional dark theme
- Gradient backgrounds (#0f172a to #020617)
- Cyan/sky blue accents (#38bdf8, #22d3ee)
- Responsive card-based layout
- Mobile-friendly design
- Smooth animations and transitions

### 8. **Three-Tab Dashboard**
- **🗺️ Learning Roadmap Tab**: Step-by-step personalized learning plan
- **📊 Skill Gap Analysis Tab**: Visual skill gap report with missing skills
- **📈 Progress Tracker Tab**: Color-coded progress with detailed breakdown

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit 1.31.0+ |
| **Backend** | Python 3.10+ |
| **Data Storage** | JSON |
| **Architecture** | Modular agent-based design |
| **Styling** | Custom CSS with Streamlit markdown |
| **Data Processing** | Pandas-compatible structures |

---

## 📦 Project Structure

```
genai-learning-path-agent/
│
├── 📄 README.md                    # Project documentation
├── 📋 requirements.txt             # Python dependencies
├── 💾 progress.json                # Saved learning progress
│
├── 🎨 Frontend/
│   └── index.html                  # Static HTML (future frontend)
│
├── ⚙️ Backend/
│   ├── app.py                      # Main Streamlit application
│   ├── agent.py                    # Learning path generation logic
│   ├── analyzer.py                 # Skill gap analysis
│   ├── compressor.py               # Profile compression/normalization
│   ├── tracker.py                  # Progress save/load utilities
│   ├── data.py                     # Career goals & course database
│   ├── test_tracker.py             # Unit tests for tracker
│   └── run_all_tests.py            # Comprehensive test suite
│
├── 📚 docs/
│   └── Project_Report.md           # Detailed project report
│
└── 🐍 __pycache__/                # Python cache files
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Windows/macOS/Linux

### Installation & Setup

1. **Clone or navigate to the repository**
   ```bash
   cd genai-learning-path-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run Backend/app.py
   ```

4. **Access the web app**
   - Local URL: `http://localhost:8501`
   - Network URL: `http://<your-ip>:8501`

### Usage Steps

1. **Fill Your Profile** (Sidebar):
   - Enter your full name
   - Select your current skills (Python, Statistics, SQL, etc.)
   - Choose your career goal (Data Scientist, GenAI Engineer, AI Product Manager)
   - Select experience level (Beginner, Intermediate, Advanced)
   - Adjust your learning progress with the slider (0-100%)

2. **Generate Learning Plan** (Optional API):
   - Expand "API Configuration" to add OpenAI API key
   - Click "🚀 Generate Learning Plan"

3. **View Three Tabs**:
   - 🗺️ **Roadmap**: Your personalized step-by-step learning plan
   - 📊 **Gap Analysis**: See what skills you're missing
   - 📈 **Progress**: Track your learning with color-coded indicators

4. **Save Your Progress**:
   - Progress automatically saves to `learning_progress.json`
   - Download and backup your learning data anytime

---

## 📊 Career Goals & Requirements

### 🛠️ GenAI Engineer
**Required Skills**: Python, Prompt Engineering, LLM APIs, Vector Databases  
**Advanced Topics**: MLOps, Evaluation, Fine-tuning LLMs  
**Focus Areas**:
- Master OpenAI/Claude APIs
- Build vector database systems
- Create RAG (Retrieval-Augmented Generation) systems
- Deploy LLM applications
- Create autonomous agents

**Sample Roadmap**:
- 📚 Complete Prompt Engineering
- 📚 Complete LLM APIs
- 🎓 Master OpenAI/Claude APIs
- 🛠️ Build LLM application
- 🔗 Create RAG system

---

### 📊 Data Scientist
**Required Skills**: Python, Statistics, Machine Learning, SQL  
**Advanced Topics**: Model Deployment, Experimentation, Advanced Analytics  
**Focus Areas**:
- Advanced Statistical Analysis
- ML Pipeline Development
- Data Visualization & Storytelling
- A/B Testing & Experimentation
- Production ML Deployment

**Sample Roadmap**:
- 📚 Complete Statistics
- 📚 Complete Machine Learning
- 🎓 Advanced Statistical Analysis
- 📈 Build ML models
- 🔍 Analyze datasets

---

### 📱 AI Product Manager
**Required Skills**: AI Strategy, User Research, Prompt Design, Metrics  
**Advanced Topics**: Roadmapping, Competitive Analysis, Go-to-Market Strategy  
**Focus Areas**:
- AI Product Strategy & Vision
- User Research Methods
- AI Product Roadmapping
- AI Metrics & KPIs
- Responsible AI Ethics

**Sample Roadmap**:
- 📚 Complete AI Strategy
- 📚 Complete User Research
- 🎓 AI Product Strategy
- 🎯 Create product strategy
- 👥 User research

---

## 📈 Progress Tracking System

### Color-Coded Indicators

| Progress | Color | Status | Action |
|----------|-------|--------|--------|
| 0-25% | 🔴 RED | Needs Significant Improvement | Focus on fundamentals |
| 25-50% | 🟡 YELLOW | Keep Improving | Build on basics |
| 50-75% | 🔵 BLUE | On Track | Push towards advanced topics |
| 75-100% | 🟢 GREEN | Perfect! | Ready for industry |

### Progress Metrics Displayed
- Overall completion percentage
- Visual progress bar
- Status-specific recommendations
- Breakdown of needs work / in progress / completed

---

## 🔌 API Integration (Future Ready)

The application includes API key management for future integrations:

```python
# API Configuration in sidebar
with st.sidebar.expander("🔑 API Configuration"):
    api_key = st.text_input("Enter OpenAI API Key (Optional)", type="password")
    if api_key:
        st.success("✓ API Key configured")
```

**Future Integrations**:
- OpenAI GPT models for dynamic content generation
- Claude API for personalized recommendations
- Real-time course recommendations
- AI-powered learning suggestions

---

## 🧪 Testing

Run the comprehensive test suite to verify all features:

```bash
# Navigate to Backend directory
cd Backend

# Run all tests
python run_all_tests.py

# Run specific tests
python test_tracker.py
```

**Test Coverage**:
- ✓ Profile compression and normalization
- ✓ Skill gap analysis for all career goals
- ✓ Learning path generation (Beginner/Intermediate/Advanced)
- ✓ Progress save and load functionality
- ✓ Multiple goal-specific paths

---

## 📊 Data Structure

### Learner Profile JSON Format
```json
{
  "profile": {
    "name": "Alex Johnson",
    "skills": ["Python", "SQL"],
    "goal": "Data Scientist",
    "level": "Beginner",
    "progress": 45,
    "skill_gaps": ["Statistics", "Machine Learning"]
  },
  "roadmap": [
    {
      "id": 1,
      "task": "📚 Complete Statistics",
      "completed": false
    },
    {
      "id": 2,
      "task": "📚 Complete Machine Learning",
      "completed": false
    }
  ],
  "saved_at": "2026-02-07T15:18:50.721823+00:00"
}
```

---

## 🌐 Deployment Options

### Streamlit Cloud (Recommended)

1. Push repository to GitHub
2. Go to https://share.streamlit.io
3. Create new app pointing to `Backend/app.py`
4. Streamlit automatically handles dependencies

### Docker

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "Backend/app.py"]
```

### Local Development
```bash
streamlit run Backend/app.py --logger.level=error
```

---

## 🔄 Workflow Overview

```
User Input (Profile)
        ↓
Profile Compression
        ↓
├── Skill Gap Analysis → Gap Report
├── Path Generation → Roadmap
└── Progress Tracking → JSON Save
        ↓
Display Dashboard (3 Tabs)
        ↓
Save Learning Progress
```

---

## 🎯 Current Features vs Roadmap

### ✅ Implemented
- [x] Profile compression and skill deduplication
- [x] Skill gap analysis
- [x] Goal-specific learning paths
- [x] Level-based path adaptation (Beginner/Intermediate/Advanced)
- [x] Color-coded progress indicators (Red/Yellow/Blue/Green)
- [x] Progress persistence (JSON)
- [x] API key management UI
- [x] Beautiful dark-themed UI
- [x] Three-tab dashboard
- [x] Comprehensive test suite

### 🚀 Planned Features
- [ ] AI-powered course recommendations (OpenAI/Claude API)
- [ ] External course integrations (Coursera, Udemy, LinkedIn Learning)
- [ ] PDF export of learning plans
- [ ] Mobile-optimized responsive design
- [ ] User authentication & cloud sync
- [ ] Community feature for peer learning
- [ ] Automated progress reminders
- [ ] Interactive quiz for skill assessment
- [ ] Career path comparison tool
- [ ] Mentor matching system

---

## 📚 Module Documentation

### `agent.py` - Learning Path Generator
Generates personalized learning roadmaps based on goals, skills, and experience level.
- Adapts content based on learner level
- Includes goal-specific modules
- Adds practical projects

### `analyzer.py` - Skill Gap Analyzer
Identifies missing skills and knowledge gaps.
- Compares user skills with required skills
- Returns prioritized gap list
- Goal-aware analysis

### `compressor.py` - Profile Compressor
Normalizes and deduplicates learner profiles.
- Removes case sensitivity issues
- Eliminates duplicate skills
- Cleans whitespace

### `tracker.py` - Progress Tracker
Saves and loads learning progress from JSON files.
- Persistent storage
- Timestamp tracking
- Easy data export

### `data.py` - Data & Configuration
Contains career goals, course database, and learning paths.
- Career goal definitions
- Skill requirements
- Goal-specific learning modules
- Course catalog

### `app.py` - Main Streamlit Application
User-facing web interface with sidebar controls and tabbed dashboard.
- Profile input
- Goal selection
- Progress tracking
- API key management

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Guidelines
1. Follow PEP 8 style guide
2. Add tests for new features
3. Update README with changes
4. Use clear commit messages

---

## 📝 License

This project is open for public usage.

---

## 🙋 Support & Contact

For questions, issues, or suggestions:
- Create an issue on GitHub
- Review the `docs/Project_Report.md` for detailed technical information
- Check test files for usage examples

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Official Documentation](https://docs.python.org/)
- [AI Career Paths Guide](https://www.deeplearning.ai/)
- [Learning Path Best Practices](https://www.coursera.org/)

---

## 🎉 Acknowledgments

Built with ❤️ for AI learners and professionals worldwide.

---

**Last Updated**: February 7, 2026  
**Version**: 1.0.0  
**Status**: Active Development
