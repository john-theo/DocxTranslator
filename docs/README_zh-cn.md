![header](https://capsule-render.vercel.app/api?type=waving&color=6eed4c&height=300&section=header&text=Docx%20Translator&fontSize=90&fontAlignY=40&animation=fadeIn&desc=Word%20docx%20文件的沉浸式翻译)

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

> 纯粹、原汁原味的氛围编码驱动着这个庞大项目的运行。 <img src="https://emojik.vercel.app/s/🤖_😎?size=32" width="16px" alt="vibe coding" />

DocxTranslator 是一个使用 OpenAI API 翻译 Word 文档（.docx）的工具。它保留原始文档格式并在每个段落下方添加翻译。

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

> ⤷ 如果这些图片无法显示，您可以[在 Github 上查看它们](https://github.com/john-theo/docx-translator)

## ✨ 特性

- 🔄 使用 OpenAI GPT 模型翻译 Word 文档（.docx）
- 🎨 保留文档格式和结构
- 🌐 在原文下方直接添加翻译
- 💻 命令行界面，易于集成到脚本中
- 🌍 由 Streamlit 提供支持的 Web 界面
- 💾 翻译缓存，避免重复的 API 调用
- ⚡ 并行处理，实现更快的翻译
- 🔧 支持自定义 OpenAI API 端点

## 📦 安装

### 通过 Pip
```bash
pip install docx-translator
```

### 通过 Docker
您可以使用预构建的 Docker 镜像立即开始使用：

```bash
# 拉取预构建镜像
docker pull johndope/docx-translator:latest

# 使用您的 API 密钥运行
docker run -p 8501:8501 -e OPENAI_API_KEY=您的API密钥 johndope/docx-translator
```

## 🖥️ 命令行使用

安装后，您可以使用 `dt` 命令翻译文档：

```bash
# 基本用法
dt translate document.docx 西班牙语

# 指定输出文件
dt translate document.docx 法语 --output translated_document.docx

# 翻译特定段落样式
dt translate document.docx 德语 --styles "Normal,Heading 1,List Paragraph"

# 使用不同的模型
dt translate document.docx 日语 --model gpt-4o

# 禁用缓存
dt translate document.docx 中文 --no-cache

# 在翻译前清除某语言的缓存
dt translate document.docx 意大利语 --clear-cache

# 顺序处理（而非并行）
dt translate document.docx 俄语 --sequential

# 显示详细日志
dt translate document.docx 葡萄牙语 --verbose
```

### 🧹 清除翻译缓存

```bash
dt clear-caches
```

### 🚀 启动 Web 界面

```bash
dt serve
```

## 🐳 Docker 使用

您可以使用 Docker 运行 DocxTranslator：

### 选项 1：使用预构建镜像（推荐）

```bash
# 拉取预构建镜像
docker pull johndope/docx-translator:latest

# 使用您的 API 密钥运行
docker run -p 8501:8501 -e OPENAI_API_KEY=您的API密钥 johndope/docx-translator
```

### 选项 2：使用 docker-compose

```bash
# 创建一个包含 OpenAI API 密钥和其他设置的 .env 文件
echo "OPENAI_API_KEY=您的API密钥" > .env

# 构建并启动 Docker 容器
docker-compose up -d

# 在 http://localhost:8501 访问 Web 界面
```

Docker 设置：
- 📂 通过 `dt` 命令直接使用已安装的包
- 💽 挂载缓存目录以保留翻译结果
- 📁 挂载数据目录，用于与容器共享文档

## 🔑 环境变量

您可以设置以下环境变量（或使用 `.env` 文件）：

- `OPENAI_API_KEY`：您的 OpenAI API 密钥
- `OPENAI_BASE_URL`：自定义 OpenAI API 基础 URL（可选）
- `OPENAI_MODEL`：要使用的模型（默认：gpt-4-turbo）
- `OPENAI_MAX_CONCURRENT`：最大并发请求数（默认：5）
- `TARGET_LANGUAGE`：默认目标语言（默认：西班牙语）
- `DOCX_TRANSLATOR_CACHE_DIR`：自定义缓存目录

## 🐍 Python API

您也可以以编程方式使用 DocxTranslator：

```python
from pathlib import Path
from docx_translator.translator import setup_openai_client, process_document

# 设置 OpenAI 客户端
client = setup_openai_client(api_key="您的API密钥")

# 翻译文档
process_document(
   input_file=Path("document.docx"),
   output_file=Path("translated_document.docx"),
   target_language="中文",
   target_styles=["Normal", "Heading 1"],
   openai_client=client,
   use_cache=True,
   parallel=True,
   max_concurrent=5
)
```

## 🌐 Web 界面

DocxTranslator 包含一个由 Streamlit 提供支持的 Web 界面。要启动它：

```bash
dt serve
```

这将启动一个本地 Web 服务器，您可以：
- 📤 上传 Word 文档
- 🎯 选择要翻译的段落样式
- ⚙️ 配置 OpenAI API 设置
- 🚀 开始翻译并跟踪进度
- 📥 下载翻译后的文档

## 📜 许可证

MIT 