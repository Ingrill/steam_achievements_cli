import requests
import os
import argparse
from dotenv import load_dotenv

# Load environment variables from a .env file into os.environ
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="CLI tool for viewing Steam achievements.")
    parser.add_argument("steam_id", type=str, help="The id of the user.")
    parser.add_argument("name", type=str, help="The name of the game.")
    args = parser.parse_args()

    api_key = os.environ.get("API_KEY")
    steam_id = args.steam_id
    game_ids = []

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
    params_achievements = {
            "key": api_key,
            "steamid": steam_id,
            "appid": 0,
            "l": "english",
            "format": "json"
            }

    response_games = requests.get(url_owned_games, params=params_owned_games)
    response_games.raise_for_status()

    data_games = response_games.json()

    games = data_games.get("response", {}).get("games", [])
    for game in games:
        if args.name.lower() in game["name"].lower():
            game_ids.append(game["appid"])

    for game_id in game_ids:
        params_achievements["appid"] = game_id
        response_achievements = requests.get(url_achievements, params=params_achievements)
        response_games.raise_for_status()

        data_achievements = response_achievements.json()

        achievements = data_achievements.get("playerstats", {}).get("achievements", [])
        if data_achievements["playerstats"]["success"] == False:
            pass
        else:
            print(data_achievements["playerstats"]["gameName"]+ "\n\n")
            for achievement in achievements:
                if achievement["unlocktime"] > 0:
                    check = "✔"
                else:
                    check = "✘"
                if achievement["description"] == "":
                    desc = "Achievement description hidden"
                else:
                    desc = achievement["description"]
                print(f" - {achievement["name"]}\n - {check} - {desc}")


if __name__ == "__main__":
    main()