# [NKU-AI-Assistant](https://www.chatnku.top)

南开大学智能小助手是你的校园生活好帮手。无论是学业上的问题，还是生活中的琐事，小助手都能为你提供贴心的帮助，他就像是一位热心的学长或学姐。

![image](https://github.com/user-attachments/assets/22290420-9167-4a14-83e6-5517db24d673)
![image](https://github.com/user-attachments/assets/165ccf84-41ef-4288-811a-e340951254d7)
![image](https://github.com/user-attachments/assets/d69ffb81-519d-4291-a193-040c5b6156a6)


## Running Locally

> 本仓库为NKU-AI-Assistant项目的后端部分,是一个FastAPI项目，如果您需要在本地运行我们NKU-Smart-Assistant完整的项目，您需要先分别运行前端项目和后端项目，前端项目的运行方法在[NKU-Smart-Assistant](https://github.com/Wenjun-Ji/NKU-Smart-Assistant)中已经详细介绍了，在次介绍后端的本地运行方式

1. 克隆仓库

```bash
git clone
cd NKU-Smart-Assistant-API
```

2. 下载数据和模型文件
请从[google网盘链接](https://drive.google.com/drive/folders/1yZ37BqKC0dqKKxjUXGctOtDeEhwSU9lr?usp=drive_link)下载files1_faiss_index文件夹和files_faiss_index文件夹，以及models，使项目结构与下面的一致
```
nku-smart-assistant-api
├─ .env
├─ chat
├─ edgedriver
├─ file
├─ files1_faiss_index
│  ├─ index.faiss
│  └─ index.pkl
├─ files_faiss_index
│  ├─ index.faiss
│  └─ index.pkl
├─ models
│  └─ m3e-base-huggingface
│     ├─ 1_Pooling
│     │  └─ config.json
│     ├─ config.json
│     ├─ gitattributes
│     ├─ model.safetensors
│     ├─ modules.json
│     ├─ pytorch_model.bin
│     ├─ README.md
│     ├─ sentence_bert_config.json
│     ├─ special_tokens_map.json
│     ├─ tokenizer.json
│     ├─ tokenizer_config.json
│     └─ vocab.txt
├─ NewsGet
├─ README.md
├─ requirements.txt
├─ server.py
├─ static
├─ videoinfo
├─ webscrap
```

3. 配置.env文件

```bash
# Neo4j Database 
NEO4J_URI=""
NEO4J_USERNAME=""
NEO4J_PASSWORD=""

# OpenAI
OPENAI_API_KEY=""
OPENAI_API_BASE=""

# Tavily
TAVILY_API_KEY=""

# LangSmith 
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=""
LANGCHAIN_API_KEY=""

# GROQ
GROQ_API_KEY=""
```

4. 配置python环境
```bash
conda create -n nku-smart-assistant-api python==3.9.13
pip install -r requirment.txt
```
4. 运行server.py文件
```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```



