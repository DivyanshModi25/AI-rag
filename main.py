from app.loaders.web_loader import WebLoader
from app.splitters.recursive_splitter import RecursiveSplitter


def main() -> None:
    loader = WebLoader(
        [
            "https://python.langchain.com/docs/introduction/"
        ]
    )

    documents = loader.load()

    splitter = RecursiveSplitter()
    chunks =splitter.split(documents)

    

if __name__== "__main__":
    main()