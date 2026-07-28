from data.mlb_api import get_games
from config import REPORT_TITLE
from datetime import datetime


def create_report():

    games = get_games()

    today = datetime.now().strftime("%B %d, %Y")

    print("=" * 60)
    print(REPORT_TITLE)
    print(today)
    print("=" * 60)

    print("\nYESTERDAY'S SCORES\n")

    if not games:
        print("No MLB games found.")
        return

    for game in games:

        away = game["teams"]["away"]["team"]["name"]
        home = game["teams"]["home"]["team"]["name"]

        away_score = game["teams"]["away"].get(
            "score",
            ""
        )

        home_score = game["teams"]["home"].get(
            "score",
            ""
        )

        print(
            f"{away} {away_score} - {home} {home_score}"
        )


if __name__ == "__main__":
    create_report()
