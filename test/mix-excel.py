import pandas as pd

# File paths
file1 = "human_scores.xlsx"
file2 = "human_scoresv2.xlsx"

# Read both files
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Combine them row by row
combined_df = pd.concat([df1, df2], ignore_index=True)

# Optional: sort nicely
combined_df = combined_df.sort_values(
    by=["question_number", "answer_label", "scorer_name"]
).reset_index(drop=True)

# Save result
combined_df.to_excel("combined_human_scores.xlsx", index=False)

print("Done! Combined file saved as combined_human_scores.xlsx")