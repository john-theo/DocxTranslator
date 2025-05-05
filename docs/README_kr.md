![header](https://capsule-render.vercel.app/api?type=waving&color=6eed4c&height=300&section=header&text=Docx%20Translator&fontSize=90&fontAlignY=40&animation=fadeIn&desc=Word%20docx%20파일의%20몰입형%20번역)

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

> 순수한 바이브 코딩이 이 거대한 프로젝트를 움직입니다. <img src="https://emojik.vercel.app/s/🤖_😎?size=32" width="16px" alt="vibe coding" />

DocxTranslator는 OpenAI API를 사용하여 Word 문서(.docx)를 번역하는 도구입니다. 원본 문서의 서식을 유지하고 각 단락 아래에 번역을 추가합니다.

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

> ⤷ 이미지가 깨지면 [Github에서 볼 수 있습니다](https://github.com/john-theo/docx-translator)

## ✨ 기능

- 🔄 OpenAI GPT 모델을 사용하여 Word 문서(.docx) 번역
- 🎨 문서 서식 및 구조 보존
- 🌐 원본 텍스트 바로 아래에 번역 추가
- 💻 스크립트에 쉽게 통합할 수 있는 명령줄 인터페이스
- 🌍 Streamlit으로 구동되는 웹 인터페이스
- 💾 중복 API 호출을 방지하는 번역 캐싱
- ⚡ 더 빠른 번역을 위한 병렬 처리
- 🔧 사용자 정의 OpenAI API 엔드포인트 지원

## 📦 설치

### Pip 사용
```bash
pip install docx-translator
```

### Docker 사용
미리 빌드된 Docker 이미지를 사용하여 즉시 시작할 수 있습니다:

```bash
# 미리 빌드된 이미지 가져오기
docker pull johndope/docx-translator:latest

# API 키로 실행
docker run -p 8501:8501 -e OPENAI_API_KEY=your-api-key johndope/docx-translator
```

## 🖥️ 명령줄 사용법

설치 후 `dt` 명령을 사용하여 문서를 번역할 수 있습니다:

```bash
# 기본 사용법
dt translate document.docx 스페인어

# 출력 파일 지정
dt translate document.docx 프랑스어 --output translated_document.docx

# 특정 단락 스타일 번역
dt translate document.docx 독일어 --styles "Normal,Heading 1,List Paragraph"

# 다른 모델 사용
dt translate document.docx 일본어 --model gpt-4o

# 캐싱 비활성화
dt translate document.docx 중국어 --no-cache

# 번역 전 언어 캐시 지우기
dt translate document.docx 이탈리아어 --clear-cache

# 순차적으로 처리 (병렬 대신)
dt translate document.docx 러시아어 --sequential

# 상세 로깅 표시
dt translate document.docx 포르투갈어 --verbose
```

### 🧹 번역 캐시 지우기

```bash
dt clear-caches
```

### 🚀 웹 인터페이스 실행

```bash
dt serve
```

## 🐳 Docker 사용법

DocxTranslator를 Docker를 사용하여 실행할 수 있습니다:

### 옵션 1: 미리 빌드된 이미지 사용 (권장)

```bash
# 미리 빌드된 이미지 가져오기
docker pull johndope/docx-translator:latest

# API 키로 실행
docker run -p 8501:8501 -e OPENAI_API_KEY=your-api-key johndope/docx-translator
```

### 옵션 2: docker-compose 사용

```bash
# OpenAI API 키와 기타 설정이 포함된 .env 파일 생성
echo "OPENAI_API_KEY=your-api-key" > .env

# Docker 컨테이너 빌드 및 시작
docker-compose up -d

# http://localhost:8501에서 웹 인터페이스 접근
```

Docker 설정:
- 📂 `dt` 명령을 통해 설치된 패키지를 직접 사용
- 💽 영구적인 번역을 위한 캐시 디렉토리 마운트
- 📁 컨테이너와 문서를 공유하기 위한 데이터 디렉토리 마운트

## 🔑 환경 변수

다음 환경 변수를 설정할 수 있습니다(또는 `.env` 파일 사용):

- `OPENAI_API_KEY`: OpenAI API 키
- `OPENAI_BASE_URL`: OpenAI API용 사용자 정의 기본 URL (선택사항)
- `OPENAI_MODEL`: 사용할 모델 (기본값: gpt-4-turbo)
- `OPENAI_MAX_CONCURRENT`: 최대 동시 요청 (기본값: 5)
- `TARGET_LANGUAGE`: 기본 대상 언어 (기본값: 스페인어)
- `DOCX_TRANSLATOR_CACHE_DIR`: 사용자 정의 캐시 디렉토리

## 🐍 Python API

DocxTranslator를 프로그래밍 방식으로도 사용할 수 있습니다:

```python
from pathlib import Path
from docx_translator.translator import setup_openai_client, process_document

# OpenAI 클라이언트 설정
client = setup_openai_client(api_key="your-api-key")

# 문서 번역
process_document(
   input_file=Path("document.docx"),
   output_file=Path("translated_document.docx"),
   target_language="한국어",
   target_styles=["Normal", "Heading 1"],
   openai_client=client,
   use_cache=True,
   parallel=True,
   max_concurrent=5
)
```

## 🌐 웹 인터페이스

DocxTranslator는 Streamlit으로 구동되는 웹 인터페이스를 포함합니다. 시작하려면:

```bash
dt serve
```

이렇게 하면 다음과 같은 작업을 할 수 있는 로컬 웹 서버가 시작됩니다:
- 📤 Word 문서 업로드
- 🎯 번역할 단락 스타일 선택
- ⚙️ OpenAI API 설정 구성
- 🚀 진행 상황 추적과 함께 번역 시작
- 📥 번역된 문서 다운로드

## 📜 라이선스

MIT 