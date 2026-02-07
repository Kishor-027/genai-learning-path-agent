def compress_profile(skills):

    # Remove duplicates and normalize
    compressed = list(set([s.strip().title() for s in skills]))

    return compressed
