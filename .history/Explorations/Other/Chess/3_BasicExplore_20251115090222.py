# ===========================================================
# Extended Chess.com Game Analysis Script
# Includes move counts + rating difference analysis
# ===========================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# ------------------------
# Load CSV
# ------------------------
df = pd.read_csv("all_games_merged.csv")

# Combine date + time
df["datetime"] = pd.to_datetime(
    df["date"] + " " + df["time"],
    format="%Y.%m.%d %H:%M:%S",
    errors="coerce"
)

df = df.sort_values("datetime").reset_index(drop=True)
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month

# ------------------------
# Identify your colour
# ------------------------
your_name = "RhysLWells"

df["color"] = df.apply(
    lambda r: "white" if r["white"] == your_name else "black",
    axis=1
)

# ------------------------
# Extract your rating and opponent rating
# ------------------------
df["your_elo"] = df.apply(
    lambda r: r["white_elo"] if r["color"] == "white" else r["black_elo"],
    axis=1
)

df["opponent_elo"] = df.apply(
    lambda r: r["black_elo"] if r["color"] == "white" else r["white_elo"],
    axis=1
)

# Rating difference (positive = opponent stronger)
df["rating_diff"] = df["opponent_elo"] - df["your_elo"]

# ------------------------
# Convert result to score
# ------------------------
def result_score(row):
    if row["color"] == "white":
        if row["result"] == "1-0": return 1
        if row["result"] == "0-1": return 0
        return 0.5
    else:
        if row["result"] == "0-1": return 1
        if row["result"] == "1-0": return 0
        return 0.5

df["score"] = df.apply(result_score, axis=1)

# ===========================================================
# 1. Extract number of moves + length statistics
# ===========================================================

# moves_san is a space-separated sequence: "e4 e5 Nf3 Nc6 ..."
# Counting moves = count tokens
df["move_count"] = df["moves_san"].apply(lambda x: len(str(x).split()))

print("Average game length (moves):", df["move_count"].mean())
print("Median game length:", df["move_count"].median())
print("Shortest game:", df["move_count"].min())
print("Longest game:", df["move_count"].max())

# Visualisation
plt.figure(figsize=(8,4))
plt.hist(df["move_count"], bins=20)
plt.title("Distribution of Game Length (Move Count)")
plt.xlabel("Move Count")
plt.ylabel("Count")
plt.show()

# ------------------------
# Correlate move count with game outcome
# ------------------------
correlation = df["move_count"].corr(df["score"])
print("Correlation between move length and score:", correlation)

plt.figure(figsize=(8,4))
plt.scatter(df["move_count"], df["score"])
plt.title("Game Outcome vs Game Length")
plt.xlabel("Move Count")
plt.ylabel("Score (1=win, 0.5=draw, 0=loss)")
plt.show()

# ===========================================================
# 2. Performance vs Rating Difference
# ===========================================================

# Your score when you are outrated vs when you are higher rated
df["out_rated"] = df["rating_diff"] > 0   # True if opponent stronger

performance_vs_gap = df.groupby("out_rated")["score"].mean()

print("Performance vs rating difference:")
print("When opponent stronger (rating_diff > 0):", performance_vs_gap[True])
print("When you are stronger:", performance_vs_gap[False])

# Scatter: rating difference vs score
plt.figure(figsize=(8,4))
plt.scatter(df["rating_diff"], df["score"])
plt.axvline(0, linestyle="dashed")
plt.title("Performance by Rating Difference")
plt.xlabel("Rating Difference (opponent_elo - your_elo)")
plt.ylabel("Score")
plt.show()

# ------------------------
# Grouped bins for deeper analysis
# ------------------------
df["rating_bin"] = pd.cut(
    df["rating_diff"],
    bins=[-500, -100, 0, 100, 300, 500],
    labels=["Much stronger than opp", "Stronger", "Equal range", "Opponent +100", "Opponent +300"]
)

rating_bin_stats = df.groupby("rating_bin")["score"].mean()
print("Average score by rating difference band:")
print(rating_bin_stats)

rating_bin_stats.plot(kind="bar", figsize=(8,4))
plt.title("Score by Rating Difference Bands")
plt.ylabel("Score")
plt.show()

# End of extended script
