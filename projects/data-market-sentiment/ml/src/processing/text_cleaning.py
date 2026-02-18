import re


def clean_text(text: str) -> str:
    """
    Nettoyage texte basique pour NLP.
    """

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"u\/\w+", " ", text)
    text = re.sub(r"r\/\w+", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()
