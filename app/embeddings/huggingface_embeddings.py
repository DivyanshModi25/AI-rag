from app.embeddings.base_embeddings import BaseEmbedding

from langchain_huggingface import HuggingFaceEmbeddings


class HuggingFaceEmb(BaseEmbedding):

    def __init__(self,model_name:str = "BAAI/bge-small-en-v1.5") -> None:

        self._embedding_model = HuggingFaceEmbeddings(
            model_name = model_name,
            model_kwargs={
                "device":"cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True,
            }
        )

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._embedding_model.embed_documents(texts)
    
    def embed_query(self, text: str) -> list[float]:
        return self._embedding_model.embed_query(text)