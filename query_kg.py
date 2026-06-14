from rdflib import Graph

# 1. Oluşturduğumuz Knowledge Graph'ı yüklüyoruz
g = Graph()
print("Knowledge Graph yükleniyor, lütfen bekleyin...")
g.parse("video_games_kg.ttl", format="turtle")
print(f"Başarılı! Toplam {len(g)} adet anlamsal ilişki (triple) yüklendi.\n")

# 2. SPARQL Sorgusu 1: Belirli bir türdeki (Örn: Action) oyunları listeleme
query_action_games = """
PREFIX ex: <http://www.semanticweb.org/zteplez/video-game-rec-ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?gameName
WHERE {
  ?game rdf:type ex:Game .
  ?game ex:hasGenre ex:Action .
  BIND(REPLACE(STR(?game), "^.*#", "") AS ?gameName)
}
LIMIT 5
"""

# 3. SPARQL Sorgusu 2: Puanı 4.5'ten yüksek ve belirli bir yıldan sonra çıkan oyunlar
query_top_rated = """
PREFIX ex: <http://www.semanticweb.org/zteplez/video-game-rec-ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?gameName ?rating ?year
WHERE {
  ?game rdf:type ex:Game .
  ?game ex:hasRating ?rating .
  ?game ex:hasReleaseYear ?year .
  FILTER (?rating >= 4.5 && ?year >= 2015)
  BIND(REPLACE(STR(?game), "^.*#", "") AS ?gameName)
}
ORDER BY DESC(?rating)
LIMIT 5
"""

# Sorguları Çalıştırma ve Ekrana Yazdırma
print("--- SORGULAMA 1: 'Action' Türündeki 5 Oyun ---")
for row in g.query(query_action_games):
    print(f"Oyun: {row.gameName.replace('_', ' ')}")

print("\n--- SORGULAMA 2: 2015 Sonrası Çıkan ve Puanı 4.5+ Olan 5 Oyun ---")
for row in g.query(query_top_rated):
    print(
        f"Oyun: {row.gameName.replace('_', ' ')} | Puan: {row.rating} | Çıkış Yılı: {row.year}"
    )
