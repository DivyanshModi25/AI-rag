from app.loaders.base_loader import BaseLoader
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


from app.utils.logger import get_logger
from datetime import datetime
from pathlib import Path

logger = get_logger(__name__)

class PDFLoader(BaseLoader):
    """
    Loads one or more web pages and converts them into LangChain Documents.
    """

    def __init__(self,pdf_path: str | Path) -> None:
        self._pdf_path = Path(pdf_path)

    def load(self) -> list[Document]:

        loader = PyPDFLoader(str(self._pdf_path))
        documents = loader.load()

        for document in documents:
            document.metadata.update(
                {
                    "loader":self.__class__.__name__,
                    "loaded_at":datetime.utcnow().isoformat(),
                    "document_type":"pdf",
                    "file_name": self._pdf_path.name,
                    "file_path": str(self._pdf_path.resolve()),
                }
            )

        logger.info("Successfully loaded %d document(s).", len(documents))

        return documents