# Video Game Recommendation Chatbot Ontology

## Project Objective
The main objective of this project is to develop a conversational video game recommendation chatbot underpinned by a robust semantic knowledge graph. Using the METHONTOLOGY framework, this project models core gaming entities (Games, Genres, Platforms) to facilitate highly specific, semantic-driven recommendations. The system integrates automated data acquisition and explores Large Language Models (LLMs) for dynamic ontology population.

## Dataset Sources
Data populating the knowledge graph was obtained via the public RESTful API provided by **RAWG (Video Games Database API)**. A target batch of high-ranking titles was extracted, preprocessed, and formatted as JSON before being mapped to the OWL schema.

## Installation and Setup Instructions
To reproduce the knowledge graph construction, validation, and querying processes locally, follow these steps:

1. **Clone the repository:**
```bash
   git clone https://github.com/zteplez/video-game-rec-ontology.git
   cd video-game-rec-ontology
```

2. Install required dependencies:
```
   pip install rdflib pyshacl
```

3. Run the pipeline scripts in order:

python build_kg.py -> Constructs the RDF/Turtle Knowledge Graph from JSON data.

python query_kg.py -> Executes predefined SPARQL competency questions.

python validate_shacl.py -> Validates the graph constraints using SHACL.

python llm_integration_demo.py -> Simulates the LLM extraction pipeline.

Repository Structure
/docs : WIDOCO-generated HTML ontology documentation and WebVOWL visualizations.

video-game-ontology.rdf : The core OWL/RDF conceptual model developed in Protégé.

video_games_kg.ttl : The populated Knowledge Graph in Turtle format.

processed_games.json : The raw dataset extracted from the RAWG API.

build_kg.py : Script for RDFlib knowledge graph construction.

query_kg.py : Script containing executable SPARQL queries.

validate_shacl.py : Script for SHACL data quality validation.

llm_integration_demo.py : Demonstration of LLM prompt engineering for ontology population.

Team Members
İbrahim As (220316083) - Computer Engineering


About Widoco output
===================
The purpose of Widoco is to reuse and integrate existing tools for documentation, plus the set of features listed below:
* Separation of the sections of your html page so you can write them independently and replace only those needed.
* Automatic annotation in RDF-a of the html produced.
* Association of a provenance page which includes the history of your vocabulary (W3C PROV-O compliant).
* Metadata extraction from the ontology plus the means to complete it on the fly when generating your ontology.
* Guidelines on the main sections that your document should have and how to complete them.

Widoco will create 3 different folders:
|
|-provenance (a folder including an html and RDF serialization of how the documentation page was created)
|-resources (folder with the different resources)
|-sections (folder with the different sections of the documentation, separated for easy editing. Just edit one and the main page will be updated)

Completing ontology metadata.
===================
Widoco uses the ontology metadata to update a configuration file. If you complete that configuration file (ended up widoco.conf), the tool will enhance your html with additional details, such as how to cite the document, previous revisions, icons with the licence, etc.

Browser issues
==========
The result of executing Widoco is an html file. We have tested it in Mozilla, IE and Chrome, and when the page is stored in a server all the browsers work correctly. If you view the file locally, we recommend you to use Mozilla Firefox (or Internet Explorer, if you must). Google Chrome will not show the contents correctly, as it doesn't allow  XMLHttpRequest without HTTP. If you want to view the page locally with Google Chrome you have two possibilities:

a) Place the file in a server and access it via its URL (for example, put it in dropbox and access through its public url).

b) Execute Chrome with the following commands :

(WIN) chrome.exe --allow-file-access-from-files,

(OSX) open /Applications/Google\ Chrome.app/ --args --allow-file-access-from-files

(UNX) /usr/bin/google-chrome --allow-file-access-from-files

Do you have a problem? open an issue at https://github.com/dgarijo/Widoco
