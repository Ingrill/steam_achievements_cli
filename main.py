import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file into os.environ
load_dotenv()

def main():
    api_key = os.environ.get("API_KEY")
    steam_id = os.environ.get("STEAM_ID")

    # Quick sanity check
    if not api_key or not steam_id:
        raise ValueError("API_KEY or STEAM_ID missing from environment variables!")

    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    params = {
        "key": api_key,
        "steamid": steam_id,
        "include_appinfo": True,
        "format": "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    games = data.get("response", {}).get("games", [])
    print(f"Found {len(games)} games!")
    for game in games[:5]:
        print(f"- {game['name']} ({game['playtime_forever']} minutes played)")

if __name__ == "__main__":
    main()