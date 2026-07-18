from abc import ABC, abstractmethod

from langchain_core.documents import Document

class BaseSplitters(ABC):

    @abstractmethod
    def split(self, documents: list[Document]) -> list[Document]:
        raise NotImplementedError