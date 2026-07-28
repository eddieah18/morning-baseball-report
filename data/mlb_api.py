import requests
from datetime import datetime, timedelta


MLB_API = "https://statsapi.mlb.com/api"


def yesterday_date():
    return (
        datetime.now() - timedelta(days=1)
    ).strftime("%Y-%m-%d")


def get_schedule():

    date = yesterday_date()

    url = f"{MLB_API}/v1/schedule"

    params = {
        "sportId": 1,
        "date": date,
        "hydrate": "team"
    }

    response = requests.get(
        url,
        params=params
    )

    response.raise_for_status()

    return response.json()


def get_games():

    schedule = get_schedule()

    games = []

    for date in schedule.get("dates", []):

        for game in date["games"]:
            games.append(game)

    return games
