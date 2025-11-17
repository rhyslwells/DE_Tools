# ===========================================================
# Chess.com Blitz Game Analysis (Unified + Cleaned)
# ===========================================================
# This script:
#   - Loads your merged chess.com CSV
#   - Parses datetime
#   - Identifies your colour and ratings
#   - Computes rating difference
#   - Extracts move counts
#   - Analyses game length vs outcomes
#   - Analyses performance vs rating difference
#   - Shows rolling performance trends
# ===========================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# ------------------------
# 1. Load the dataset
# ------------------------
df = pd.read_csv("all_games_merged.csv")

# ------------------------
# 2. Create datetime column
# ------------------------
df["datetime"] = pd.to_datetime(
    df["date"] + " " + df["time"],
    format="%Y.%m.%d %H:%M:%S",
    errors="coerce"
)

df = df.sort_values("datetime").reset_index(drop=True)
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month

# ------------------------
# 3. Identify your colour
# ------------------------
your_name = "RhysLWells"

df["color"] = df.apply(
    lambda r: "white" if r["white"] == your_name else "black",
    axis=1
)

# ------------------------
# 4. Extract your Elo and opponent Elo
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
# 5. Convert game results to numerical score
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
# 6. Extract number of moves + length statistics
# ===========================================================
df["move_count"] = df["moves_san"].apply(
    lambda x: len(str(x).split()) if pd.notnull(x) else 0
)

print("Average game length:", df["move_count"].mean())
print("Median game length:", df["move_count"].median())
print("Shortest game:", df["move_count"].min())
print("Longest game:", df["move_count"].max())

# Histogram
plt.figure(figsize=(8,4))
plt.hist(df["move_count"], bins=20)
plt.title("Distribution of Game Length (Moves)")
plt.xlabel("Move Count")
plt.ylabel("Count")
plt.show()

# Correlation with outcome
correlation = df["move_count"].corr(df["score"])
print("Correlation between game length and score:", correlation)

plt.figure(figsize=(8,4))
plt.scatter(df["move_count"], df["score"])
plt.title("Outcome vs Move Count")
plt.xlabel("Move Count")
plt.ylabel("Score")
plt.show()

# Category for boxplot
df["result_category"] = df["score"].apply(
    lambda s: "win" if s == 1 else ("loss" if s == 0 else "draw")
)

df.boxplot(column="move_count", by="result_category", figsize=(8,5))
plt.title("Game Length by Result Category")
plt.suptitle("")
plt.xlabel("Result")
plt.ylabel("Move Count")
plt.show()

# ===========================================================
# 7. Rating difference & performance analysis
# ===========================================================
# Positive => opponent stronger
df["out_rated"] = df["rating_diff"] > 0

print("Performance vs stronger opponents:", df[df["out_rated"]]["score"].mean())
print("Performance vs weaker opponents:", df[~df["out_rated"]]["score"].mean())

plt.figure(figsize=(8,4))
plt.scatter(df["rating_diff"], df["score"])
plt.axvline(0, linestyle="dashed")
plt.title("Performance by Rating Difference")
plt.xlabel("Opponent_Elo - Your_Elo")
plt.ylabel("Score")
plt.show()

# Group bins for deeper rating-diff analysis
df["rating_bin"] = pd.cut(
    df["rating_diff"],
    bins=[-500, -100, 0, 100, 300, 500],
    labels=["Much stronger", "Stronger", "Equal", "Opponent +100", "Opponent +300"]
)

rating_bin_stats = df.groupby("rating_bin")["score"].mean()
print("Score by rating gap:")
print(rating_bin_stats)

rating_bin_stats.plot(kind="bar", figsize=(8,4))
plt.title("Score by Rating Difference Band")
plt.ylabel("Score")
plt.show()

# ===========================================================
# 8. Rolling win-rate when outrated vs higher rated
# ===========================================================
df["score_vs_higher"] = df.apply(
    lambda r: r["score"] if r["rating_diff"] > 0 else np.nan, axis=1
)
df["score_vs_lower"] = df.apply(
    lambda r: r["score"] if r["rating_diff"] < 0 else np.nan, axis=1
)

plt.figure(figsize=(10,4))
plt.plot(df["score_vs_higher"].rolling(20).mean(), label="When Opponent Higher Rated")
plt.plot(df["score_vs_lower"].rolling(20).mean(),  label="When You Are Higher Rated")
plt.xlabel("Games")
plt.ylabel("Rolling Win Rate (20 games)")
plt.title("Win Rate vs Rating Difference")
plt.legend()
plt.show()

# ===========================================================
# 9. Summary
# ===========================================================
print("Total games:", len(df))
print("Overall performance (score):", df["score"].mean())
print("Average move count:", df["move_count"].mean())
print("Average rating difference:", df["rating_diff"].mean())
