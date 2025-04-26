# optimizer/content_optimizer.py

action_verbs = {
    "worked": "collaborated",
    "made": "engineered",
    "did": "executed",
    "led": "spearheaded"
}

def optimize_content(text):
    words = text.split()
    polished = [action_verbs.get(word.lower(), word) for word in words]
    return ' '.join(polished).capitalize()