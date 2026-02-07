from data import COURSE_DB


def analyze_gaps(skills, goal):

    required = COURSE_DB[goal]["required"]

    gaps = []

    normalized = [s.strip().title() for s in skills]

    for skill in required:

        if skill not in normalized:
            gaps.append(skill)

    return gaps
