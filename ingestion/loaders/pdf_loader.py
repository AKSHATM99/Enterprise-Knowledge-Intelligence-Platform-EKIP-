from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
import tempfile
import os

def load_pdf(file):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, file.filename)
        file.save(path)

        reader = SimpleDirectoryReader(input_files=[path])
        docs = reader.load_data()

        splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
        nodes = splitter.get_nodes_from_documents(docs)

    return nodes
