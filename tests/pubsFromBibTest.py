import os

from dotenv import load_dotenv

from pubsFromBib import generate_md

load_dotenv(".env.test")


def test_generate_md_from_bib():
    generate_md()
    assert len(os.listdir(os.getenv("OUT_PATH"))) == 1
    assert os.listdir(os.getenv("OUT_PATH"))[0] == "1992-01-01-World-Wide-Web-The-Information-Universe.md"
