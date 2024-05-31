This is a Retrieval-augmented generation (RAG) chatbot with LangChain. It can answer questions about LangChain based on LangChain documents. 

Documents are HTML files from the langchain website. Then it is chunked, embedded, and stored in the Pinecone vector store (about 50k vectors using cosine metric).

It is hosted on https://langchainchatbot.onrender.com (it might be slow at the first time since I used the free-tier service).

<br></br>
<h3>examples</h3>
- ask a question:
<img width="1000" alt="Screenshot 2024-05-30 at 5 34 31 PM" src="https://github.com/zycs19/LangchainChatbot/assets/49542462/c1318721-0226-44fc-815c-bd3ce6dd9913">
<br></br>
- answer questions:
<img width="1000" alt="Screenshot 2024-05-30 at 5 35 03 PM" src="https://github.com/zycs19/LangchainChatbot/assets/49542462/e7b3a28e-b037-4521-b728-15e0cf547080">
<br></br>
