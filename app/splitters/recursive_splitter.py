from app.splitters.base_splitter import BaseSplitters

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter



class RecursiveSplitter(BaseSplitters):

    def __init__(self, chunk_size:int = 1000, chunk_overlap:int = 200) -> None:

        self._splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size, 
                chunk_overlap=chunk_overlap
            )
        
    
    def split(self, documents: list[Document]) -> list[Document]:
        return self._splitter.split_documents(documents)