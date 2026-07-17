import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with a song catalog."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the first k songs as a placeholder recommendation."""
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a placeholder explanation for a recommendation."""
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into dictionaries."""
    songs = []

    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return reasons."""
    reasons: List[str] = []

    genre_weight = 0.35
    mood_weight = 0.25
    energy_weight = 0.25
    acoustic_weight = 0.15

    score = 0.0

    user_genre = str(user_prefs.get("genre", "")).strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    if user_genre and song_genre:
        if user_genre == song_genre:
            score += genre_weight
            reasons.append(f"genre matches {song.get('genre')}")
        else:
            reasons.append(f"genre differs from {user_prefs.get('genre')}")

    user_mood = str(user_prefs.get("mood", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()
    if user_mood and song_mood:
        if user_mood == song_mood:
            score += mood_weight
            reasons.append(f"mood matches {song.get('mood')}")
        else:
            reasons.append(f"mood differs from {user_prefs.get('mood')}")

    target_energy = user_prefs.get("energy")
    song_energy = song.get("energy")
    if target_energy is not None and song_energy is not None:
        energy_closeness = max(0.0, 1.0 - abs(float(target_energy) - float(song_energy)))
        score += energy_weight * energy_closeness
        reasons.append(
            f"energy is {'close to' if energy_closeness >= 0.8 else 'some distance from'} the target"
        )

    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))
    acousticness = song.get("acousticness")
    if acousticness is not None:
        acoustic_value = float(acousticness) if likes_acoustic else 1.0 - float(acousticness)
        score += acoustic_weight * acoustic_value
        if likes_acoustic:
            reasons.append(f"acousticness is high at {song.get('acousticness')}")
        else:
            reasons.append(f"acousticness is low at {song.get('acousticness')}")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k recommendations."""
    ranked_songs = sorted(
        (
            (song, *score_song(user_prefs, song))
            for song in songs
        ),
        key=lambda item: item[1],
        reverse=True,
    )

    top_k = ranked_songs[:k]
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in top_k
    ]
