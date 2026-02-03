from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Answer the question ONLY using the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}
"""
)
