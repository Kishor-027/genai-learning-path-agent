# Learning Path Recommender – Project Report

## 1. Introduction
This project is an AI-powered Learning Path Recommender developed as part of the Intel HPE GenAI for GenZ Challenge. The system analyzes learner profiles, compresses course data using ScaleDown techniques, and generates personalized learning roadmaps.

## 2. Problem Statement
Students often struggle to identify the right learning sequence from large course catalogs. This project solves this problem by providing optimized and personalized learning paths based on skill gaps, prerequisites, and user goals.

## 3. Objectives
- Analyze user skills and learning goals
- Detect missing skills
- Generate optimized learning paths
- Compress course data using ScaleDown
- Track learner progress
- Provide time and certification planning

## 4. System Architecture
The system follows a modular architecture:

- Frontend: Streamlit Interface
- Backend: Python AI Agents
- Data Layer: JSON-based course and progress storage
- Recommendation Engine
- Skill Gap Analyzer
- Progress Tracker

## 5. Technology Stack
| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Data Storage | JSON |
| Version Control | GitHub |
| Deployment | Streamlit Cloud |

## 6. Modules Description

### 6.1 Agent Module
Handles communication between user input and backend logic.

### 6.2 Analyzer Module
Analyzes learner skills and identifies gaps.

### 6.3 Compressor Module
Applies ScaleDown techniques to compress course data.

### 6.4 Tracker Module
Tracks learning progress and completion.

### 6.5 Recommendation Engine
Generates optimized learning paths using prerequisites and difficulty level.

## 7. Features
- Personalized learning roadmap
- Skill gap detection
- Course prerequisite handling
- Difficulty adaptation
- Time estimation
- Progress monitoring
- Certification planning
- Interactive dashboard

## 8. Implementation Details
The backend is implemented using Python modules. The frontend uses Streamlit for rapid UI development. Data is stored in JSON format and processed using custom algorithms.

## 9. User Interface
The system provides:
- Skill input form
- Level selection
- Path generation button
- Progress visualization
- Result dashboard

## 10. Testing
Unit tests are implemented for progress tracking and recommendation logic to ensure reliability.

## 11. Results
The system successfully generates optimized learning paths, improves learning efficiency, and reduces irrelevant course suggestions.

## 12. Future Enhancements
- Integration with Coursera and Udemy APIs
- Machine Learning-based recommendation
- Mobile application
- Peer learning system
- AI Mentor chatbot
- Performance analytics dashboard

## 13. Conclusion
This project demonstrates how GenAI and ScaleDown techniques can be used to build efficient personalized learning systems. It improves learner engagement and provides structured learning guidance.

## 14. References
- Streamlit Documentation
- Python Official Docs
- GitHub Guides
- Intel GenAI Program Resources
