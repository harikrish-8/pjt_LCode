import pandas as pd

SHEET_URL = "https://docs.google.com/spreadsheets/d/1vkBFdIn_RNMOe7-1A1sanAAtxhuP_pxr/export?format=csv&gid=1467654569"

def get_leaderboard():
    # Read Google Sheet
    df = pd.read_csv(SHEET_URL)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Fill empty values with 0
    df["No of Easy Problems"] = df["No of Easy Problems"].fillna(0)
    df["No of Medium Problems"] = df["No of Medium Problems"].fillna(0)
    df["No of Hard Problems"] = df["No of Hard Problems"].fillna(0)

    # Convert to integers
    df["No of Easy Problems"] = df["No of Easy Problems"].astype(int)
    df["No of Medium Problems"] = df["No of Medium Problems"].astype(int)
    df["No of Hard Problems"] = df["No of Hard Problems"].astype(int)

    # Calculate Score
    df["Score"] = (
        df["No of Easy Problems"] * 1 +
        df["No of Medium Problems"] * 2 +
        df["No of Hard Problems"] * 3
    )

    # Sort by Score
    df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)

    # Add Rank
    df.insert(0, "Rank", range(1, len(df) + 1))

    # Show only required columns
    df = df[
        [
            "Rank",
            "NAME OF THE STUDENT",
            "LEET CODE ID",
            "No of Easy Problems",
            "No of Medium Problems",
            "No of Hard Problems",
            "Score"
        ]
    ]

    return df