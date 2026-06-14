import json
import urllib.parse
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD

# 1. Ontolojinizin Temel Adresi (Namespace)
# Ekran görüntüsündeki IRI adresini kullanıyoruz:
BASE_URI = "http://www.semanticweb.org/zteplez/video-game-rec-ontology#"
EX = Namespace(BASE_URI)


def create_knowledge_graph(json_file_path, output_file_path):
    # 2. Boş bir Graf oluştur ve namespace'i bağla
    g = Graph()
    g.bind("ex", EX)

    print("JSON verisi okunuyor...")
    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            games_data = json.load(f)
    except FileNotFoundError:
        print(f"Hata: '{json_file_path}' bulunamadı. Lütfen dosya adını kontrol edin.")
        return

    print(
        "Bilgi Grafı (Knowledge Graph) inşa ediliyor, veriler ontolojiye haritalanıyor..."
    )
    for game in games_data:
        # Oyun ismindeki boşlukları ontolojiye uygun şekilde alt çizgiye çeviriyoruz (Örn: Grand_Theft_Auto_V)
        game_name_safe = urllib.parse.quote(game["name"].replace(" ", "_"))
        game_uri = EX[game_name_safe]

        # Oyunun Sınıfını Belirle (Game)
        g.add((game_uri, RDF.type, EX.Game))

        # Veri Özellikleri (Data Properties: Çıkış Yılı ve Puan)
        if game.get("release_year"):
            g.add(
                (
                    game_uri,
                    EX.hasReleaseYear,
                    Literal(int(game["release_year"]), datatype=XSD.integer),
                )
            )

        if game.get("rating"):
            g.add(
                (
                    game_uri,
                    EX.hasRating,
                    Literal(float(game["rating"]), datatype=XSD.float),
                )
            )

        # Nesne Özellikleri (Object Properties: Türler - Genres)
        for genre in game.get("genres", []):
            genre_safe = urllib.parse.quote(genre.replace(" ", "_"))
            genre_uri = EX[genre_safe]
            g.add((genre_uri, RDF.type, EX.Genre))  # Tür bireyini Genre sınıfına ekle
            g.add((game_uri, EX.hasGenre, genre_uri))  # Oyun ile Türü bağla

        # Nesne Özellikleri (Object Properties: Platformlar - Platforms)
        for platform in game.get("platforms", []):
            plat_safe = urllib.parse.quote(platform.replace(" ", "_"))
            plat_uri = EX[plat_safe]
            g.add(
                (plat_uri, RDF.type, EX.Platform)
            )  # Platform bireyini Platform sınıfına ekle
            g.add((game_uri, EX.availableOn, plat_uri))  # Oyun ile Platformu bağla

    # 3. Dosyayı Turtle (.ttl) formatında kaydet
    g.serialize(destination=output_file_path, format="turtle")
    print(
        f"Harika! Knowledge Graph başarıyla '{output_file_path}' dosyasına kaydedildi."
    )


if __name__ == "__main__":
    # Girdi (önceki adımda çektiğimiz veri) ve Çıktı (yeni oluşacak KG dosyası)
    create_knowledge_graph("processed_games.json", "video_games_kg.ttl")
