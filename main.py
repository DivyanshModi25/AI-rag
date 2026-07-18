from app.loaders.web_loader import WebLoader
from app.splitters.recursive_splitter import RecursiveSplitter


def main() -> None:
    loader = WebLoader(
        [
            "https://python.langchain.com/docs/introduction/"
        ]
    )

    documents = loader.load()

    splitter = RecursiveSplitter(chunk_size=1000, chunk_overlap=200)
    chunks =splitter.split(documents)

    # sum = 0

    # print(len(chunks))
    # for i, chunk in enumerate(chunks):
    #     print(f"Chunk {i + 1}")
    #     print(f"Length : {len(chunk.page_content)}")
    #     print()
    #     sum = sum + len(chunk.page_content)

    # print(f"avg: {sum/len(chunks)}")

if __name__== "__main__":
    main()