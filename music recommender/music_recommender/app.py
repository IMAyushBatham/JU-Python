from .storage import load_songs_from_file, save_songs_to_file, export_to_csv
from .logic import recommend_song

songs = load_songs_from_file()

def add_song():
    title = input("Enter song title: ")
    artist = input("Enter artist: ")
    mood = input("Enter mood (happy/sad/romantic/chill/energetic): ").lower()

    songs.append({"title": title, "artist": artist, "mood": mood})
    save_songs_to_file(songs)
    print("Song added!\n")

def view_all_songs():
    if not songs:
        print("No songs saved.\n")
        return

    print("\nAll Songs:")
    for s in songs:
        print(f"- {s['title']} by {s['artist']} [{s['mood']}]")
    print()

def start_app():
    while True:
        print("=== Mood-Based Music Recommender ===")
        print("1. Add Song")
        print("2. Recommend Based on Mood")
        print("3. View All Songs")
        print("4. Export Songs to CSV")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_song()
        elif choice == "2":
            recommend_song(songs)
        elif choice == "3":
            view_all_songs()
        elif choice == "4":
            export_to_csv(songs)
        elif choice == "65":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")
