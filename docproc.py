from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings


def chunk_document(file_path: str):
    pdfloader = UnstructuredPDFLoader(file_path)
    data = pdfloader.load()
    print(f"Docs loaded: {len(data)}")

    semantic_chunker = SemanticChunker(OpenAIEmbeddings(),
                                    breakpoint_threshold_type="percentile")
    semantic_chunks = semantic_chunker.create_documents([d.page_content for d in data])

    for chunk in semantic_chunks:
        print("\r------------------------------------------\r")
        print(chunk.page_content)
        print("\r------------------------------------------\r")

    print(f"Number of chunks: {len(semantic_chunks)}")
    return semantic_chunks