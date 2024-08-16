# [NKU-AI-Assistant](https://www.chatnku.top)

The NKU AI Assistant is your go-to helper for campus life at Nankai University. Whether you have academic questions or need assistance with daily tasks, the assistant is here to offer you considerate help, much like a friendly senior student.

![image](https://github.com/user-attachments/assets/22290420-9167-4a14-83e6-5517db24d673)
![image](https://github.com/user-attachments/assets/165ccf84-41ef-4288-811a-e340951254d7)
![image](https://github.com/user-attachments/assets/d69ffb81-519d-4291-a193-040c5b6156a6)


## Running Locally

> This repository contains the backend part of the NKU-AI-Assistant project, a FastAPI project. If you need to run the complete NKU-Smart-Assistant project locally, you must run both the frontend and backend projects. The method for running the frontend project is detailed in [NKU-Smart-Assistant](https://github.com/Wenjun-Ji/NKU-Smart-Assistant). Below, we introduce how to run the backend locally.

1. Clone the repository

```bash
git clone
cd NKU-Smart-Assistant-API
```

2. Download data and model files  
Please download the `files1_faiss_index` folder, the `files_faiss_index` folder, and the models from the [Google Drive link](https://drive.google.com/drive/folders/1yZ37BqKC0dqKKxjUXGctOtDeEhwSU9lr?usp=drive_link). Ensure that the project structure matches the following:

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

3. Configure the `.env` file

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

4. Set up the Python environment

```bash
conda create -n nku-smart-assistant-api python==3.9.13
pip install -r requirements.txt
```

5. Run the `server.py` file

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

> You can debug the FastAPI endpoints on the `/docs` port. Since I’ve already deployed the backend project to a cloud server, if you need to run it locally, make sure to modify the frontend by replacing the request URL in the `submitUserMessage` function in `lib/chat/action.ts`.


