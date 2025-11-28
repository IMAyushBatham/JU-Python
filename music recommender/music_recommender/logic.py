def detect_mood():
    text = input("How are you feeling today? ").lower()
    if any(word in text for word in ["happy", "good", "excited", "great"]):
        return "happy"
    elif any(word in text for word in ["sad", "down", "upset", "bad"]):
        return "sad"
    elif any(word in text for word in ["love", "romantic", "heart"]):
        return "romantic"
    elif any(word in text for word in ["tired", "lazy", "sleepy", "calm"]):
        return "chill"
    else:
        return "energetic"  


def recommend_song(songs):

    mood = detect_mood()
    print(f"\nDetected Mood: {mood.upper()}")

    mood_songs = [s for s in songs if s["mood"] == mood]

    if not mood_songs:
        print("No songs found for this mood. Try adding some!\n")
        return

    print("\nRecommended Songs:")
    for s in mood_songs:
        print(f"- {s['title']} by {s['artist']}")
    print()