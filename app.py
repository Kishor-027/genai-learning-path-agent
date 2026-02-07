import streamlit as st
from pathlib import Path
from agent import generate_path
from analyzer import analyze_gaps
from tracker import save_progress


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GenAI Learning Agent",
    page_icon="🎓",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#0f172a,#020617);
}

.main {
    background-color: transparent;
}

h1 {
    color: #38bdf8;
    text-align: center;
    font-size: 45px;
}

h2, h3 {
    color: #22d3ee;
}

.card {
    background: rgba(15,23,42,0.9);
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0px;
    box-shadow: 0px 0px 15px #22d3ee;
}

.sidebar .sidebar-content {
    background: #020617;
}

.stButton button {
    background: linear-gradient(90deg,#22d3ee,#38bdf8);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 45px;
    width: 100%;
}

.stProgress > div > div {
    background: linear-gradient(90deg,#22d3ee,#38bdf8);
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown("<h1>🎓 GenAI Learning Path Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Personalized AI Roadmap Generator</h3>", unsafe_allow_html=True)
st.write("---")


# ---------------- SIDEBAR ----------------
st.sidebar.title("👤 Student Profile")

# API Key section
with st.sidebar.expander("🔑 API Configuration"):
    api_key = st.text_input("Enter OpenAI API Key (Optional)", type="password")
    if api_key:
        st.success("✓ API Key configured")

name = st.sidebar.text_input("Full Name")

skills = st.sidebar.multiselect(
    "Your Current Skills",
    [
        "Python", "Java", "C++", "ML Basics", "Maths",
        "Statistics", "SQL", "HTML", "CSS", "JavaScript", "DSA"
    ]
)

goal = st.sidebar.selectbox(
    "Career Goal",
    [
        "Data Scientist",
        "GenAI Engineer",
        "AI Product Manager"
    ]
)

level = st.sidebar.radio(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

progress = st.sidebar.slider("Learning Progress (%)", 0, 100, 0)

generate = st.sidebar.button("🚀 Generate Learning Plan")


# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "🗺️ Learning Roadmap",
    "📊 Skill Gap Analysis",
    "📈 Progress Tracker"
])


# ---------------- MAIN LOGIC ----------------
if generate:

    if name == "" or len(skills) == 0:

        st.warning("⚠️ Please fill all details")

    else:

        roadmap = generate_path(skills, goal, level)
        gaps = analyze_gaps(skills, goal)

        # Create profile dictionary
        profile = {
            "name": name,
            "skills": skills,
            "goal": goal,
            "level": level,
            "progress": progress
        }

        # Save progress to JSON file
        progress_path = Path("learning_progress.json")
        save_progress(profile, roadmap, progress_path)


        # -------- TAB 1 : ROADMAP --------
        with tab1:

            st.subheader("🗺️ Personalized Learning Roadmap")

            for i, step in enumerate(roadmap, 1):

                st.markdown(f"""
                <div class="card">
                    <h4>Step {i}</h4>
                    <p>{step}</p>
                </div>
                """, unsafe_allow_html=True)


        # -------- TAB 2 : GAP ANALYSIS --------
        with tab2:

            st.subheader("📊 Skill Gap Report")

            if len(gaps) == 0:

                st.success("🎉 No major skill gaps detected!")

            else:

                for g in gaps:

                    st.markdown(f"""
                    <div class="card">
                        ⚠️ <b>Missing Skill:</b> {g}
                    </div>
                    """, unsafe_allow_html=True)


        # -------- TAB 3 : PROGRESS --------
        with tab3:

            st.subheader("📈 Your Learning Progress")

            st.progress(progress / 100)

            # Color-coded progress indicator
            if progress < 25:
                progress_color = "🔴 RED - Needs Significant Improvement"
                progress_message = "Focus on fundamentals and core concepts"
                color_box = "background-color: #ff4444;"
            elif progress < 50:
                progress_color = "🟡 YELLOW - Keep Improving"
                progress_message = "Good start! Continue building on basics"
                color_box = "background-color: #ffaa00;"
            elif progress < 75:
                progress_color = "🔵 BLUE - On Track"
                progress_message = "Excellent progress! Push towards advanced topics"
                color_box = "background-color: #4488ff;"
            else:
                progress_color = "🟢 GREEN - Perfect!"
                progress_message = "Outstanding! You're ready for industry challenges"
                color_box = "background-color: #44aa44;"

            st.metric(
                label="Completion Status",
                value=f"{progress}%",
                delta=progress_color
            )

            st.markdown(f"""
            <div style="{color_box} color: white; padding: 15px; border-radius: 10px; margin: 10px 0;">
                <h4>{progress_color}</h4>
                <p>{progress_message}</p>
            </div>
            """, unsafe_allow_html=True)

            # Detailed progress breakdown
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"""
                <div style="background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #ff4444;">
                    <h4>❌ Needs Work</h4>
                    <p style="font-size: 20px; font-weight: bold;">{max(0, 25-progress)}%</p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div style="background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #ffaa00;">
                    <h4>🔄 In Progress</h4>
                    <p style="font-size: 20px; font-weight: bold;">{min(50, max(0, progress-25))}%</p>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown(f"""
                <div style="background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #44aa44;">
                    <h4>✅ Completed</h4>
                    <p style="font-size: 20px; font-weight: bold;">{min(progress, 100)}%</p>
                </div>
                """, unsafe_allow_html=True)
