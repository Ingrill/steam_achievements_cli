import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from a .env file into os.environ
load_dotenv()

def main():
    api_key = os.environ.get("API_KEY")
    steam_id = os.environ.get("STEAM_ID")

    # Quick sanity check
    if not api_key or not steam_id:
        raise ValueError("API_KEY or STEAM_ID missing from environment variables!")

    url_owned_games = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    url_achievements = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"
    params_owned_games = {
        "key": api_key,
        "steamid": steam_id,
        "include_appinfo": True,
        "format": "json"
    }

    response_games = requests.get(url_owned_games, params=params_owned_games)
    response_games.raise_for_status()

    data_games = response_games.json()
    """with open("dump.json", "w", encoding="utf-8") as file:
        json.dump(data_games, file, indent=4) """
    games = data_games.get("response", {}).get("games", [])
    print(f"Found {len(games)} games!")
    for game in games[:5]:
        print(f"- {game['name']} ({game['playtime_forever']} minutes played)")

    params_achievements = {
        "key": api_key,
        "steamid": steam_id,
        "appid": 220,
        "l": "english",
        "format": "json"
        }
    response_achievements = requests.get(url_achievements, params=params_achievements)
    response_games.raise_for_status()
    data_achievements = response_achievements.json()
    achievements = data_achievements.get("playerstats", {}).get("achievements", [])
    for achievement in achievements:
        print(f" - {achievement["name"]}\n - {achievement["description"]}")


if __name__ == "__main__":
    main()