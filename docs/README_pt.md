![header](https://capsule-render.vercel.app/api?type=waving&color=6eed4c&height=300&section=header&text=Docx%20Translator&fontSize=90&fontAlignY=40&animation=fadeIn&desc=Tradução%20imersiva%20de%20arquivos%20Word%20docx)

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

> Programação pura e autêntica baseada em vibes é o que impulsiona todo este incrível projeto. <img src="https://emojik.vercel.app/s/🤖_😎?size=32" width="16px" alt="vibe coding" />

DocxTranslator é uma ferramenta para traduzir documentos Word (.docx) usando a API da OpenAI. Ele preserva a formatação original do documento e adiciona traduções abaixo de cada parágrafo.

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

> ⤷ Se estas imagens não carregarem, você pode [vê-las no Github](https://github.com/john-theo/docx-translator)

## ✨ Recursos

- 🔄 Tradução de documentos Word (.docx) usando modelos OpenAI GPT
- 🎨 Preservação da formatação e estrutura do documento
- 🌐 Adição de traduções diretamente abaixo do texto original
- 💻 Interface de linha de comando para fácil integração em scripts
- 🌍 Interface web alimentada pelo Streamlit
- 💾 Cache de traduções para evitar chamadas redundantes à API
- ⚡ Processamento paralelo para tradução mais rápida
- 🔧 Suporte a endpoints personalizados da API OpenAI

## 📦 Instalação

### Via Pip
```bash
pip install docx-translator
```

### Via Docker
Você pode usar a imagem Docker pré-construída para começar imediatamente:

```bash
# Baixar a imagem pré-construída
docker pull johndope/docx-translator:latest

# Executar com sua chave de API
docker run -p 8501:8501 -e OPENAI_API_KEY=sua-chave-api johndope/docx-translator
```

## 🖥️ Uso pela Linha de Comando

Após a instalação, você pode usar o comando `dt` para traduzir documentos:

```bash
# Uso básico
dt translate documento.docx Espanhol

# Especificar arquivo de saída
dt translate documento.docx Francês --output documento_traduzido.docx

# Traduzir estilos de parágrafo específicos
dt translate documento.docx Alemão --styles "Normal,Título 1,Parágrafo de Lista"

# Usar um modelo diferente
dt translate documento.docx Japonês --model gpt-4o

# Desativar cache
dt translate documento.docx Chinês --no-cache

# Limpar cache para um idioma antes da tradução
dt translate documento.docx Italiano --clear-cache

# Processar sequencialmente (em vez de em paralelo)
dt translate documento.docx Russo --sequential

# Mostrar logs detalhados
dt translate documento.docx Português --verbose
```

### 🧹 Limpar Caches de Tradução

```bash
dt clear-caches
```

### 🚀 Iniciar Interface Web

```bash
dt serve
```

## 🐳 Uso com Docker

Você pode executar o DocxTranslator usando Docker:

### Opção 1: Usar imagem pré-construída (recomendado)

```bash
# Baixar a imagem pré-construída
docker pull johndope/docx-translator:latest

# Executar com sua chave de API
docker run -p 8501:8501 -e OPENAI_API_KEY=sua-chave-api johndope/docx-translator
```

### Opção 2: Usar docker-compose

```bash
# Criar um arquivo .env com sua chave de API OpenAI e outras configurações
echo "OPENAI_API_KEY=sua-chave-api" > .env

# Construir e iniciar o contêiner Docker
docker-compose up -d

# Acessar a interface web em http://localhost:8501
```

A configuração do Docker:
- 📂 Usa o pacote instalado diretamente via comando `dt`
- 💽 Monta um diretório de cache para traduções persistentes
- 📁 Monta um diretório de dados para compartilhar documentos com o contêiner

## 🔑 Variáveis de Ambiente

Você pode definir as seguintes variáveis de ambiente (ou usar um arquivo `.env`):

- `OPENAI_API_KEY`: Sua chave de API OpenAI
- `OPENAI_BASE_URL`: URL base personalizada para API OpenAI (opcional)
- `OPENAI_MODEL`: O modelo a ser usado (padrão: gpt-4-turbo)
- `OPENAI_MAX_CONCURRENT`: Número máximo de solicitações simultâneas (padrão: 5)
- `TARGET_LANGUAGE`: Idioma alvo padrão (padrão: Espanhol)
- `DOCX_TRANSLATOR_CACHE_DIR`: Diretório de cache personalizado

## 🐍 API Python

Você também pode usar o DocxTranslator programaticamente:

```python
from pathlib import Path
from docx_translator.translator import setup_openai_client, process_document

# Configurar cliente OpenAI
client = setup_openai_client(api_key="sua-chave-api")

# Traduzir documento
process_document(
   input_file=Path("documento.docx"),
   output_file=Path("documento_traduzido.docx"),
   target_language="Português",
   target_styles=["Normal", "Título 1"],
   openai_client=client,
   use_cache=True,
   parallel=True,
   max_concurrent=5
)
```

## 🌐 Interface Web

DocxTranslator inclui uma interface web alimentada pelo Streamlit. Para iniciá-la:

```bash
dt serve
```

Isso lançará um servidor web local onde você pode:
- 📤 Carregar documentos Word
- 🎯 Selecionar quais estilos de parágrafo traduzir
- ⚙️ Configurar as definições da API OpenAI
- 🚀 Iniciar traduções com acompanhamento de progresso
- 📥 Baixar o documento traduzido

## 📜 Licença

MIT 