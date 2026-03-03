# Musical Search Engine

A web-based information retrieval system for a musical corpus, implementing Boolean search, TF-IDF ranking, and semantic search.

This application was developed as part of a group project in Natural Language Processing and Information Retrieval.

---

## Overview

The Musical Search Engine allows users to search within a corpus of musical descriptions using multiple retrieval strategies:

- Boolean search (including wildcard support)
- TF-IDF ranking
- Semantic search using vector representations
- Theme extraction and visualization

The system is implemented as a Flask web application with a modular backend architecture.

---

## Features

- Boolean query processing (AND, OR, NOT)
- Wildcard search support
- TF-IDF ranking
- Semantic similarity-based retrieval
- Theme extraction from musical descriptions
- Data visualisation (e.g., distributions, metadata insights)
- Web interface for query input and result display

---
```
## System Architecture
musical-search-engine/
│
├── app.py
├── algorithms/
│ ├── boolean.py
│ ├── tfidf.py
│ └── semantic.py
│
├── data/
│ ├── musicals.json
│ ├── musicals-data.json
│ └── musical_tags.json
│
├── templates/
├── static/
│
├── data_loader.py
├── theme_extraction.py
├── visualisations.py
└── README.md
```

### Core Components

- `algorithms/` → retrieval models (Boolean, TF-IDF, Semantic)
- `data_loader.py` → corpus loading and preprocessing
- `theme_extraction.py` → automatic theme extraction
- `visualisations.py` → corpus statistics and plots
- `app.py` → Flask application and routing logic

---

## Technologies Used

- Python
- Flask
- NLTK
- scikit-learn
- Vector-based semantic similarity
- HTML / CSS

---

## Project Contribution

This application was developed as a group project by:

- Manuel Trombetta  
- Aaro  
- Fiia  
- Isobel  

### Individual Contributions (Manuel Trombetta)

- Implementation of the Boolean Search engine (in collaboration with Aaro) 
- Implementation of the Semantic Search engine (in collaboration with Aaro)  
- Development of wildcard search functionality within the Boolean model  
- Theme extraction module  
- Partial refactoring and modifications of `app.py` together with the team  

The overall system architecture and integration were developed collaboratively.

---

## Purpose

This project demonstrates practical implementation of:

- Information Retrieval models
- Search engine architecture
- Semantic similarity techniques
- Corpus processing in Digital Humanities
- Backend web development with Flask

The focus is on combining theoretical IR concepts with a functional web-based interface.
