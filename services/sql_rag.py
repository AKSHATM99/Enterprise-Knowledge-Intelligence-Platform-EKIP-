from services.db import get_connection

def sql_rag(query: str):
    q = query.lower()
    conn = get_connection()
    cur = conn.cursor()

    # VERY IMPORTANT:
    # No LLM-generated SQL yet (safety)
    cur.execute("SELECT COUNT(*) FROM users")
    result = cur.fetchone()[0]

    return {
            "answer": f"There are {result} users in the system.",
            "sources": ["database:users"],
            "confidence": 1.0
        }

    # return {
    #     "answer": "I don't know",
    #     "sources": [],
    #     "confidence": 0.0
    # }
