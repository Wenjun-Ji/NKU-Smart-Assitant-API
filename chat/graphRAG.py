from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import MessagesPlaceholder
from dotenv import load_dotenv


def graphRAG():
    # 加载环境变量
    load_dotenv()

    print("Step 1: Libraries and modules imported")

    # 设置Neo4j数据库连接
    print("Step 2: Setting up Neo4j database connection")
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    os.environ["NEO4J_URI"] = NEO4J_URI
    os.environ["NEO4J_USERNAME"] = NEO4J_USERNAME
    os.environ["NEO4J_PASSWORD"] = NEO4J_PASSWORD
    graph = Neo4jGraph()
    print("Neo4j database connection set up")

    # 设置OpenAI API连接
    print("Step 3: Setting up OpenAI API connection")
    API_SECRET_KEY = os.getenv("OPENAI_API_KEY")
    BASE_URL = os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
    os.environ["OPENAI_API_BASE"] = BASE_URL
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")  # gpt-4-0125-preview occasionally has issues

    # 测试连接
    print("Step 4: Testing LLM connection")
    test = llm.invoke("hello")
    print("Test LLM:", test)

    # 创建向量索引
    print("Step 5: Creating vector index")
    vector_index = Neo4jVector.from_existing_graph(
        OpenAIEmbeddings(),
        search_type="hybrid",
        node_label="Document",
        text_node_properties=["text"],
        embedding_node_property="embedding",
    )
    print("Vector index created")

    # 构建问答系统并进行查询
    print("Step 6: Building QA system and querying")

    retriever = vector_index.as_retriever()  # Your retriever

    # 继续对话，记住检索到的文档等信息
    prompt = ChatPromptTemplate.from_messages([
        ('system',
         """Your name is 南开大学院校消息通. Answer the user's questions based on the below context:\n\n{context}"""),
        MessagesPlaceholder(variable_name='chat_history'),
        ('user', '{input}')
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)

    return chain

# # 调用函数并获取chain
# chain = graphRAG()

# result = chain.invoke({"input": "南开大学有哪些学院？","chat_history":[]})
# print(result)
# print(type(result))
