![header](https://capsule-render.vercel.app/api?type=waving&color=6eed4c&height=300&section=header&text=Docx%20Translator&fontSize=90&fontAlignY=40&animation=fadeIn&desc=Immersive%20Übersetzung%20von%20Word%20docx%20Dateien)

<p align="center"> 
  <a href="/README.md">English</a> 
  ·
  <a href="/docs/README_fr.md">Français</a>
  ·
  <a href="/docs/README_de.md">Deutsch</a>
  ·
  <a href="/docs/README_zh-cn.md">简体中文</a>  
  ·
  <a href="/docs/README_zh-tw.md">繁體中文</a>
  ·
  <a href="/docs/README_kr.md">한국어</a> 
  ·
  <a href="/docs/README_pt.md">Português</a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/100%25_vibe_coding-6eed4c?style=for-the-badge">
</p>

> Reiner, unverfälschter Vibe-Coding treibt dieses gesamte Monster-Projekt an. <img src="https://emojik.vercel.app/s/🤖_😎?size=32" width="16px" alt="vibe coding" />

DocxTranslator ist ein Werkzeug zur Übersetzung von Word-Dokumenten (.docx) mit der OpenAI-API. Es bewahrt die ursprüngliche Dokumentformatierung und fügt Übersetzungen unter jedem Absatz hinzu.

<p align="center">
  <a href="https://pypi.org/project/docx-translator/">
    <img src="https://img.shields.io/pypi/v/docx-translator?color=blue&logo=pypi&logoColor=white" alt="PyPI">
  </a>
  <a href="https://hub.docker.com/r/johndope/docx-translator">
    <img src="https://img.shields.io/docker/pulls/johndope/docx-translator?color=blue&logo=docker&logoColor=white" alt="Docker Hub">
  </a>
  <a href="https://github.com/john-theo/docx-translator">
    <img src="https://img.shields.io/github/stars/john-theo/docx-translator" alt="GitHub stars">
  </a>
  <a href="https://github.com/john-theo/docx-translator">
    <img src="https://img.shields.io/github/license/john-theo/docx-translator?color=green" alt="License">
  </a>
</p>

<img src="../static/app.jpg">
<img src="../static/demo.jpg">

> ⤷ Falls diese Bilder nicht angezeigt werden, können Sie sie [auf Github ansehen](https://github.com/john-theo/docx-translator)

## ✨ Funktionen

- 🔄 Übersetzen von Word-Dokumenten (.docx) mit OpenAI GPT-Modellen
- 🎨 Beibehaltung der Dokumentformatierung und -struktur
- 🌐 Hinzufügen von Übersetzungen direkt unter dem Originaltext
- 💻 Kommandozeilenschnittstelle für einfache Integration in Skripte
- 🌍 Weboberfläche mit Streamlit
- 💾 Übersetzungs-Caching zur Vermeidung redundanter API-Aufrufe
- ⚡ Parallele Verarbeitung für schnellere Übersetzung
- 🔧 Unterstützung für benutzerdefinierte OpenAI API-Endpunkte

## 📦 Installation

### Über Pip
```bash
pip install docx-translator
```

### Über Docker
Sie können das vorgefertigte Docker-Image verwenden, um sofort zu beginnen:

```bash
# Vorgefertigtes Image herunterladen
docker pull johndope/docx-translator:latest

# Mit Ihrem API-Schlüssel ausführen
docker run -p 8501:8501 -e OPENAI_API_KEY=Ihr-API-Schlüssel johndope/docx-translator
```

## 🖥️ Verwendung der Kommandozeile

Nach der Installation können Sie den Befehl `dt` verwenden, um Dokumente zu übersetzen:

```bash
# Grundlegende Verwendung
dt translate dokument.docx Spanisch

# Ausgabedatei angeben
dt translate dokument.docx Französisch --output übersetztes_dokument.docx

# Bestimmte Absatzstile übersetzen
dt translate dokument.docx Deutsch --styles "Normal,Überschrift 1,Listenabsatz"

# Ein anderes Modell verwenden
dt translate dokument.docx Japanisch --model gpt-4o

# Caching deaktivieren
dt translate dokument.docx Chinesisch --no-cache

# Cache für eine Sprache vor der Übersetzung löschen
dt translate dokument.docx Italienisch --clear-cache

# Sequentiell verarbeiten (anstatt parallel)
dt translate dokument.docx Russisch --sequential

# Ausführliche Protokollierung anzeigen
dt translate dokument.docx Portugiesisch --verbose
```

### 🧹 Übersetzungs-Caches löschen

```bash
dt clear-caches
```

### 🚀 Weboberfläche starten

```bash
dt serve
```

## 🐳 Docker-Verwendung

Sie können DocxTranslator mit Docker ausführen:

### Option 1: Vorgefertigtes Image verwenden (empfohlen)

```bash
# Vorgefertigtes Image herunterladen
docker pull johndope/docx-translator:latest

# Mit Ihrem API-Schlüssel ausführen
docker run -p 8501:8501 -e OPENAI_API_KEY=Ihr-API-Schlüssel johndope/docx-translator
```

### Option 2: Docker-Compose verwenden

```bash
# Eine .env-Datei mit Ihrem OpenAI API-Schlüssel und anderen Einstellungen erstellen
echo "OPENAI_API_KEY=Ihr-API-Schlüssel" > .env

# Docker-Container erstellen und starten
docker-compose up -d

# Zugriff auf die Weboberfläche unter http://localhost:8501
```

Die Docker-Einrichtung:
- 📂 Verwendet das installierte Paket direkt über den `dt`-Befehl
- 💽 Mountet ein Cache-Verzeichnis für persistente Übersetzungen
- 📁 Mountet ein Datenverzeichnis zum Teilen von Dokumenten mit dem Container

## 🔑 Umgebungsvariablen

Sie können die folgenden Umgebungsvariablen setzen (oder eine `.env`-Datei verwenden):

- `OPENAI_API_KEY`: Ihr OpenAI API-Schlüssel
- `OPENAI_BASE_URL`: Benutzerdefinierte Basis-URL für die OpenAI API (optional)
- `OPENAI_MODEL`: Das zu verwendende Modell (Standard: gpt-4-turbo)
- `OPENAI_MAX_CONCURRENT`: Maximale gleichzeitige Anfragen (Standard: 5)
- `TARGET_LANGUAGE`: Standard-Zielsprache (Standard: Spanisch)
- `DOCX_TRANSLATOR_CACHE_DIR`: Benutzerdefiniertes Cache-Verzeichnis

## 🐍 Python-API

Sie können DocxTranslator auch programmatisch verwenden:

```python
from pathlib import Path
from docx_translator.translator import setup_openai_client, process_document

# OpenAI-Client einrichten
client = setup_openai_client(api_key="Ihr-API-Schlüssel")

# Dokument übersetzen
process_document(
   input_file=Path("dokument.docx"),
   output_file=Path("übersetztes_dokument.docx"),
   target_language="Deutsch",
   target_styles=["Normal", "Überschrift 1"],
   openai_client=client,
   use_cache=True,
   parallel=True,
   max_concurrent=5
)
```

## 🌐 Weboberfläche

DocxTranslator enthält eine Weboberfläche, die von Streamlit angetrieben wird. Um sie zu starten:

```bash
dt serve
```

Dies startet einen lokalen Webserver, wo Sie:
- 📤 Word-Dokumente hochladen können
- 🎯 Auswählen können, welche Absatzstile übersetzt werden sollen
- ⚙️ OpenAI API-Einstellungen konfigurieren können
- 🚀 Übersetzungen mit Fortschrittsverfolgung starten können
- 📥 Das übersetzte Dokument herunterladen können

## 📜 Lizenz

MIT 