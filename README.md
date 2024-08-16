# [NKU-AI-Assistant](https://www.chatnku.top)

南开大学智能小助手是你的校园生活好帮手。无论是学业上的问题，还是生活中的琐事，小助手都能为你提供贴心的帮助，他就像是一位热心的学长或学姐。

![image](https://github.com/user-attachments/assets/22290420-9167-4a14-83e6-5517db24d673)
![image](https://github.com/user-attachments/assets/165ccf84-41ef-4288-811a-e340951254d7)
![image](https://github.com/user-attachments/assets/d69ffb81-519d-4291-a193-040c5b6156a6)


## Features

- [LangChain](https://www.langchain.com/) The largest community building the future of LLM apps
- [LangGraph](https://www.langchain.com/langgraph) Balance agent control with agency
- [FastAPI](https://fastapi.tiangolo.com/) Building APIs
- [Next.js](https://nextjs.org) App Router
- React Server Components (RSCs), Suspense, and Server Actions
- [Vercel AI SDK](https://sdk.vercel.ai/docs) for streaming chat UI
- [shadcn/ui](https://ui.shadcn.com)
  - Styling with [Tailwind CSS](https://tailwindcss.com)
  - [Radix UI](https://radix-ui.com) for headless component primitives
  - Icons from [Phosphor Icons](https://phosphoricons.com)
- Chat History, rate limiting, and session storage with [Vercel KV](https://vercel.com/storage/kv)
- [NextAuth.js](https://github.com/nextauthjs/next-auth) for authentication

## Running Locally

> 本仓库为NKU-AI-Assistant项目的前端部分，如您想要使用我们的仓库为前端模板，您可以按照以下步骤在本地运行。

1. Cloning the repository the local machine
```bash
git clone
cd NKU-Smart-Assistant
```
2. Installing the dependencies.
```bash
pnpm install
```
3. Running the application.
```bash
pnpm dev
```

> 如您也想使用FastAPI封装您自己的机器人，您可以替换 `lib/chat/action.ts`中submitUserMessage函数中请求的地址

## Backend

后端部分代码请参考另一仓库[NKU-Smart-Assitant-API](https://github.com/Wenjun-Ji/NKU-Smart-Assitant-API)

## Powered by

在此非常感谢[ai-chatbot](https://github.com/vercel/ai-chatbot)这个项目🥰🥰🥰，我们的前端是以该项目为基础的。



```
nku-smart-assistant-master
├─ .env
├─ chat
│  ├─ graphRAG.py
│  ├─ langgraph_RAG.py
│  ├─ retrieval_chain.py
│  ├─ transform.py
│  └─ __pycache__
│     ├─ graphRAG.cpython-39.pyc
│     ├─ langgraph_RAG.cpython-39.pyc
│     ├─ retrieval_chain.cpython-39.pyc
│     └─ transform.cpython-39.pyc
├─ edgedriver
│  ├─ Driver_Notes
│  │  ├─ credits.html
│  │  ├─ EULA
│  │  └─ LICENSE
│  ├─ install-tl-windows.exe
│  ├─ msedgedriver.exe
│  └─ x86_64-8.1.0-release-win32-seh-rt_v6-rev0.7z
├─ file
│  ├─ file_analyze.py
│  ├─ transform.py
│  └─ __pycache__
│     ├─ file_analyze.cpython-39.pyc
│     └─ transform.cpython-39.pyc
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
│  ├─ news.py
│  └─ __pycache__
│     └─ news.cpython-39.pyc
├─ README.md
├─ requirements.txt
├─ server.py
├─ static
│  ├─ Backpropagation_Theory,_Architectures,_and_Applications_(Yves_Chauvin_(ed.),_David_E._Rumelhart_(ed.))_(Z-Library).pdf
│  ├─ eng.txt
│  ├─ test.txt
│  └─ translated_eng.txt
├─ videoinfo
│  ├─ videoinfo_bilibili.py
│  ├─ videoinfo_youtube.py
│  └─ __pycache__
│     └─ videoinfo_youtube.cpython-39.pyc
├─ webscrap
│  ├─ webscrap_multilevel.py
│  ├─ webscrap_single.py
│  └─ __pycache__
│     ├─ webscrap_single.cpython-311.pyc
│     └─ webscrap_single.cpython-39.pyc
└─ __pycache__
   └─ server.cpython-39.pyc

```
