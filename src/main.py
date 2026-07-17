"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from textwrap import wrap

from recommender import load_songs, recommend_songs


def print_recommendation_table(recommendations) -> None:
    """Print recommendations in a compact ASCII table."""
    rows = []
    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        rows.append(
            {
                "rank": str(index),
                "title": song["title"],
                "score": f"{score:.2f}",
                "reasons": explanation,
            }
        )

    headers = ["Rank", "Title", "Score", "Reasons"]
    widths = {
        "rank": max(len(headers[0]), *(len(row["rank"]) for row in rows)) if rows else len(headers[0]),
        "title": max(len(headers[1]), *(len(row["title"]) for row in rows)) if rows else len(headers[1]),
        "score": max(len(headers[2]), *(len(row["score"]) for row in rows)) if rows else len(headers[2]),
        "reasons": max(30, len(headers[3])),
    }

    def border() -> str:
        return "+" + "+".join("-" * (widths[key] + 2) for key in ["rank", "title", "score", "reasons"]) + "+"

    def format_row(values) -> str:
        return "| " + " | ".join(
            value.ljust(widths[key])
            for value, key in zip(values, ["rank", "title", "score", "reasons"])
        ) + " |"

    print(border())
    print(format_row(headers))
    print(border())

    for row in rows:
        reason_lines = wrap(row["reasons"], width=widths["reasons"]) or [""]
        print(format_row([row["rank"], row["title"], row["score"], reason_lines[0]]))
        for reason_line in reason_lines[1:]:
            print(format_row(["", "", "", reason_line]))
        print(border())


def main() -> None:
    """Load songs, generate recommendations, and print them."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_profiles = [
        # {"name": "Pop & happy", "genre": "pop", "mood": "happy", "energy": 0.8},
        # {"name": "Late-night lofi", "genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True},
        # {"name": "Workout rock", "genre": "rock", "mood": "intense", "energy": 0.9},
        # {"name": "Coffee shop jazz", "genre": "jazz", "mood": "relaxed", "energy": 0.35, "likes_acoustic": True},
        # {"name": "Dreamy electronic", "genre": "electronic", "mood": "dreamy", "energy": 0.7},
        # {"name": "Tie generator", "genre": "", "mood": "", "energy": 0.575, "likes_acoustic": False},
        # { "name": "Null acoustic coercion", "genre": "electronic", "mood": "dreamy", "energy": 0.69, "likes_acoustic": None },
        { "name": "Contradictory profile", "genre": "classical", "mood": "intense", "energy": 0.93, "likes_acoustic": True },
        # { "name": "Unknown taxonomy", "genre": "hyperpop", "mood": "euphoric", "energy": 0.86, "likes_acoustic": False },
        # { "name": "Boolean trap false string", "genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": "false" },
    ]

    for user_prefs in user_profiles:
        print(f"\nUser profile: {user_prefs['name']}")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top recommendations:")
        print_recommendation_table(recommendations)


if __name__ == "__main__":
    main()
