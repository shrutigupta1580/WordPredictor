import random

# ---------------- TECH DOMAIN ----------------

tech_subjects = [
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "neural networks",
    "data science",
    "natural language processing",
    "computer vision",
    "reinforcement learning",
    "python programming",
    "cloud computing"
]

tech_verbs_present = [
    "transforms",
    "improves",
    "changes",
    "powers",
    "drives",
    "enables",
    "reshapes",
    "advances",
    "supports",
    "optimizes"
]

tech_verbs_past = [
    "transformed",
    "improved",
    "changed",
    "powered",
    "drove",
    "enabled",
    "reshaped",
    "advanced",
    "supported",
    "optimized"
]

tech_objects = [
    "modern technology",
    "business applications",
    "scientific research",
    "healthcare systems",
    "education platforms",
    "financial markets",
    "automation systems",
    "predictive analytics",
    "intelligent systems",
    "real world solutions"
]

tech_extra_phrases = [
    "at a rapid pace",
    "with great efficiency",
    "in innovative ways",
    "using advanced algorithms",
    "through data driven methods",
    "across multiple industries",
    "in today's world",
    "with scalable systems",
    "for better outcomes",
    "with powerful models"
]

tech_connectors = [
    "because it uses data",
    "as technology evolves",
    "when models improve",
    "while systems scale",
    "since data grows rapidly",
    "as research advances",
    "when computing power increases",
    "because algorithms improve"
]


# ---------------- GENERAL LIFE ----------------

subjects = ["I", "You", "We", "They", "He", "She"]

emotions = [
    "happy", "sad", "angry", "excited", "tired", "hungry",
    "bored", "confused", "nervous", "relaxed"
]

likes = [
    "music", "books", "movies", "cricket", "football",
    "guitar", "pizza", "coffee", "coding", "traveling"
]

activities = [
    "play cricket", "play guitar", "watch movies",
    "read books", "eat pizza", "drink coffee",
    "write code", "learn programming",
    "go outside", "meet friends"
]

places = [
    "school", "college", "office", "market",
    "park", "home", "gym", "restaurant"
]

times = [
    "in the morning", "at night", "every day",
    "on weekends", "after work", "before dinner"
]

questions = [
    "What are you doing",
    "How are you feeling",
    "Where are you going",
    "Why are you late",
    "When will you come"
]


# ---------------- GENERATOR ----------------

def generate_tech_sentence():
    pattern_type = random.randint(1, 3)

    subject = random.choice(tech_subjects)
    obj = random.choice(tech_objects)

    if pattern_type == 1:
        return f"{subject} {random.choice(tech_verbs_present)} {obj} {random.choice(tech_extra_phrases)}."
    elif pattern_type == 2:
        return f"{subject} {random.choice(tech_verbs_past)} {obj} {random.choice(tech_connectors)}."
    else:
        return f"In modern systems, {subject} {random.choice(tech_verbs_present)} {obj}."


def generate_general_sentence():
    pattern = random.randint(1, 8)
    subject = random.choice(subjects)

    if pattern == 1:
        if subject == "I":
            return f"I am {random.choice(emotions)}."
        else:
            return f"{subject} is {random.choice(emotions)}."

    elif pattern == 2:
        return f"I like {random.choice(likes)}."

    elif pattern == 3:
        return f"I like to {random.choice(activities)}."

    elif pattern == 4:
        return f"{subject} go to the {random.choice(places)} {random.choice(times)}."

    elif pattern == 5:
        return f"{subject} want to {random.choice(activities)}."

    elif pattern == 6:
        return f"{subject} are going to the {random.choice(places)}."

    elif pattern == 7:
        return random.choice(questions) + "?"

    else:
        return f"Today I feel {random.choice(emotions)} and I want to {random.choice(activities)}."


def generate_sentence():
    # 50% tech, 50% general
    if random.random() < 0.5:
        return generate_tech_sentence()
    else:
        return generate_general_sentence()


# ---------------- WRITE DATA ----------------

with open("data/corpus.txt", "w", encoding="utf-8") as f:
    for _ in range(50000):
        f.write(generate_sentence() + "\n")

print("50,000 combined tech + general sentences generated successfully.")
