# Steam Achievement Viewer (CLI)

A Python command-line interface (CLI) tool designed to check user achievements for Steam games. The script searches through the specified user's game library for matches and prints out all achievements along with their unlock status (unlocked / locked) and descriptions.

## 🚀 Features

* **Game Search:** Matches games in the user's Steam library by a partial name/keyword.
* **Achievement Status:** Clearly displays unlocked (`✔`) and locked (`✘`) achievements.
* **Hidden Achievements Support:** Safely handles achievements with hidden or missing public descriptions.
* **Security:** Keeps your API key safe by managing sensitive credentials via a `.env` file.

## 🛠️ Requirements

* **Python 3.7+**
* **Steam Web API Key** (obtainable from the official [Steam Developer Page](https://steamcommunity.com/dev/apikey))
* Public Steam profile (ensure your profile privacy settings for "Game details" are set to "Public")

## 📦 Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/your-username/steam-achievement-viewer.git
   cd steam-achievement-viewer
   ```

2. Install the required dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the root directory of the project and add your Steam API key:

   ```env
   API_KEY=your_steam_api_key_here
   ```

## 💻 Usage

Run the script from your terminal by passing two required arguments: **Steam ID** and **Game Name** (or a keyword).

### Syntax:

```bash
python main.py <STEAM_ID> "<GAME_NAME>"
```

### Arguments:

* `STEAM_ID` — 64-bit Steam ID (SteamID64) of the targeted user.
* `GAME_NAME` — Full name or part of the name of the game (case-insensitive).

### Example:

```bash
python main.py 76561198000000000 "Portal"
```

### Example Output:

```text
Portal 2


 - Lab Rat
 - ✔ - Acquire the fully functional Portal Gun.
 - High Five
 - ✘ - Perform a high-five with a co-op partner.
 - Hidden Treasure
 - ✔ - Achievement description hidden
```

## 📂 Project Structure

* `main.py` — Main CLI script logic.
* `.env` — Environment file storing your private API key (do not commit this to public repositories).
* `.gitignore` — Make sure to list `.env` here to avoid leaking your API key.