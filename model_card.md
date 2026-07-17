# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This recommender suggests songs based on a user’s genre, mood, energy, and acoustic taste. It assumes the user wants music that matches those simple preferences. It is meant for classroom exploration, not real users.

---

## 3. How the Model Works

The model looks at genre, mood, energy, and acousticness for each song. It compares those features to the user’s preferences and gives more points when they match. Genre and energy matter the most, and mood and acousticness also affect the score. I kept the scoring simple so it is easy to read and test.

---

## 4. Data

The catalog has 18 songs. It includes pop, lofi, rock, jazz, classical, electronic, and several other styles. It also has moods like happy, chill, intense, dreamy, and relaxed. The dataset is small, so it does not cover every kind of music taste.

---

## 5. Strengths

It works well when the user gives clear preferences. For example, a happy pop profile usually gets pop songs with matching mood and energy. It also does a good job when someone wants chill or acoustic music. The results feel reasonable when the preferences are simple and consistent.

---

## 6. Limitations and Bias

The system can over-prioritize exact genre matches, even when the mood or energy fit is weaker. In my tests, Ocean Echo could outrank a better mood match because genre and acousticness still added enough points. The recommender also depends heavily on the acoustic preference, so a truthy or malformed value can push the results in the wrong direction. Because the model only adds points and never subtracts them, it can reinforce one style too strongly.

---

## 7. Evaluation

I tested several user profiles: a tie generator, a null acoustic coercion case, a contradictory profile, an unknown taxonomy profile, and a boolean trap case. I checked whether the top songs matched the intended genre, mood, energy, and acoustic preference. I also compared how the rankings changed when the preferences conflicted. One surprise was that Ocean Echo could still rank first for the contradictory profile even when its mood and energy were not the best fit. Another surprise was that a truthy acoustic value could change the output in a way that felt unintended.

No need for numeric metrics unless you created some.

---

## 8. Future Work

I would add more song features, like tempo and valence, to make the scores smarter. I would also add a diversity rule so the top results are not too similar. Better explanations would help users understand why a song was recommended. I would also handle more complex user tastes instead of only using a few simple preferences.

---

## 9. Personal Reflection

I learned that simple scoring rules can still create believable recommendations. I was surprised by how a small input choice could change the ranking a lot. This project made me think more carefully about bias and edge cases in music recommendation apps.
