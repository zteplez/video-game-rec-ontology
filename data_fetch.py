import requests
import json

API_KEY = "025b8b58c37844fdab255c5892aa8cef"
URL = f"https://api.rawg.io/api/games?key={API_KEY}&page_size=50"


def fetch_and_preprocess_data():
    print("RAWG API'den veriler çekiliyor...")
    response = requests.get(URL)

    if response.status_code == 200:
        raw_data = response.json()
        processed_games = []

        for game in raw_data["results"]:
            game_info = {
                "name": game.get("name"),
                "release_year": game.get("released", "")[:4]
                if game.get("released")
                else None,
                "rating": game.get("rating"),
                "genres": [genre["name"] for genre in game.get("genres", [])],
                "platforms": [
                    plat["platform"]["name"] for plat in game.get("platforms", [])
                ],
            }
            processed_games.append(game_info)

        with open("processed_games.json", "w", encoding="utf-8") as f:
            json.dump(processed_games, f, ensure_ascii=False, indent=4)

        print(
            "Veri çekme ve ön işleme başarılı! 'processed_games.json' dosyası oluşturuldu."
        )
    else:
        print("Hata oluştu. Durum Kodu:", response.status_code)


if __name__ == "__main__":
    fetch_and_preprocess_data()
