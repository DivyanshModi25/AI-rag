from app.loaders.web_loader import WebLoader


def main() -> None:
    loader = WebLoader(
        [
            "https://python.langchain.com/docs/introduction/"
        ]
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} document(s).")
    first_doc = documents[0]

    print(first_doc)

if __name__== "__main__":
    main()