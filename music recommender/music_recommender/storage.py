import json
import os
import csv

FILE_NAME = "songs.json"

def load_songs_from_file():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_songs_to_file(songs):
    with open(FILE_NAME, "w") as f:
        json.dump(songs, f, indent=4)

def export_to_csv(songs):
    if not songs:
        print("No songs found. Add some songs first.\n")
        return

    with open("songs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Artist", "Mood"])   

        for s in songs:
            writer.writerow([s["title"], s["artist"], s["mood"]])

    print("Songs exported successfully to songs.csv!\n")