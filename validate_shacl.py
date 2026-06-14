from pyshacl import validate
from rdflib import Graph

print("Knowledge Graph verileri SHACL kurallarına göre test ediliyor...\n")

# 1. Test edeceğimiz veri grafını (Knowledge Graph) yüklüyoruz
data_graph = Graph()
data_graph.parse("video_games_kg.ttl", format="turtle")

# 2. SHACL Kuralları (Shapes)
# Kural 1: Her oyunun en az 1 türü (hasGenre) olmalı.
# Kural 2: Puan (hasRating) veri tipi float (ondalıklı sayı) olmalı.
shacl_rules = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://www.semanticweb.org/zteplez/video-game-rec-ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:GameShape a sh:NodeShape ;
    sh:targetClass ex:Game ;
    
    sh:property [
        sh:path ex:hasGenre ;
        sh:minCount 1 ;
        sh:message "HATA: Sisteme eklenen her oyunun en az bir türü (Genre) olmak zorundadır!" ;
    ] ;
    
    sh:property [
        sh:path ex:hasRating ;
        sh:datatype xsd:float ;
        sh:message "HATA: Oyun puanı (Rating) mutlaka ondalıklı sayı (float) olmalıdır!" ;
    ] .
"""

# 3. Doğrulama (Validation) İşlemini Başlat
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shacl_rules,
    data_graph_format="turtle",
    shacl_graph_format="turtle",
    inference="rdfs",
    debug=False,
)

# 4. Sonuçları Yazdır
print("--- SHACL DOĞRULAMA RAPORU ---")
if conforms:
    print(
        "✅ BAŞARILI: Knowledge Graph'taki tüm veriler SHACL kurallarına %100 uyuyor!"
    )
else:
    print("❌ BAŞARISIZ: Verilerde kurallara uymayan hatalar bulundu.")
    print("\nDetaylar:")
    print(results_text)
