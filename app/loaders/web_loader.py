from app.loaders.base_loader import BaseLoader
from langchain_core.documents import Document
from langchain_community.document_loaders import UnstructuredURLLoader

class WebLoader(BaseLoader):
    """
    Loads one or more web pages and converts them into LangChain Documents.
    """

    def __init__(self,urls: list[str]) -> None:
        self._urls = urls

    def load(self) -> list[Document]:
        loader = UnstructuredURLLoader(urls=self._urls)
        return loader.load()