# from sentence_transformers import SentenceTransformer
# from qdrant_client import QdrantClient

# model = SentenceTransformer("all-MiniLM-L6-v2")
# client = QdrantClient(host="localhost", port=6333)

# q = "How many paid leaves are allowed?"
# emb = model.encode(q).tolist()

# res = client.search(
#     collection_name="documents",
#     query_vector=emb,
#     limit=3
# )

# for r in res:
#     print(r.score)
#     print(r)
import requests
import zipfile
import os

# The official vector links we selected
logos = {
    "amazon_s3.svg": "https://cdn.simpleicons.org/amazons3/white",
    "google_drive.svg": "https://cdn.simpleicons.org/googledrive/white",
    "github.svg": "https://cdn.simpleicons.org/github/white",
    "excel.svg": "https://cdn.simpleicons.org/microsoftexcel/white",
    "pdf.svg": "https://cdn.simpleicons.org/adobeacrobatreader/white",
    "postgresql.svg": "https://cdn.simpleicons.org/postgresql/white",
    "servicenow.svg": "https://cdn.simpleicons.org/servicenow/white",
    "confluence.svg": "https://cdn.simpleicons.org/confluence/white",
    "azure.svg": "https://cdn.simpleicons.org/microsoftazure/white"
}

zip_name = "ekip_logos.zip"

print("🚀 Starting download...")

with zipfile.ZipFile(zip_name, 'w') as zip_file:
    for filename, url in logos.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Write the content to a temporary file then add to zip
                with open(filename, 'wb') as f:
                    f.write(response.content)
                zip_file.write(filename)
                os.remove(filename) # Clean up local folder
                print(f"✅ Added: {filename}")
        except Exception as e:
            print(f"❌ Failed to download {filename}: {e}")

print(f"\n✨ Done! Your logos are ready in: {os.path.abspath(zip_name)}")