# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

> I am designing a content-based recommendation system that recommends songs by comparing a user’s taste profile to the features of each song. Each song is described using genre, mood, energy, and acousticness, while the user profile stores their preferred genre, mood, target energy level, and acoustic preference. The recommender computes a weighted score for each song based on how closely it matches the user’s preferences and recommends the songs with the highest scores. This makes the system simple, interpretable, and easy to explain.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
User profile: genre=pop, mood=happy, energy=high
Top recommendations:

Title : Sunrise City
Score : 0.97
Reasons:
  - genre matches pop
  - mood matches happy
  - energy is close to the target
  - acousticness is low at 0.18
----------------------------------------
Title : Gym Hero
Score : 0.71
Reasons:
  - genre matches pop
  - mood differs from happy
  - energy is close to the target
  - acousticness is low at 0.05
----------------------------------------
Title : Rooftop Lights
Score : 0.59
Reasons:
  - genre differs from pop
  - mood matches happy
  - energy is close to the target
  - acousticness is low at 0.35
----------------------------------------
Title : Neon Skyline
Score : 0.37
Reasons:
  - genre differs from pop
  - mood differs from happy
  - energy is close to the target
  - acousticness is low at 0.11
----------------------------------------
Title : City of Fire
Score : 0.37
Reasons:
  - genre differs from pop
  - mood differs from happy
  - energy is close to the target
  - acousticness is low at 0.08
----------------------------------------
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
