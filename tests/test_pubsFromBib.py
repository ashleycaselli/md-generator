import os

from src.md_generator import pubsFromBib

ENV_FILE = "tests/.env.test"


def init_env_vars():
    with open(ENV_FILE) as env_file:
        lines = [[x.replace("\n", "") for x in y.split("=")] for y in env_file.readlines()]

    for line in lines:
        os.environ[line[0]] = line[1]


def test_generate_md_from_bib():
    init_env_vars()
    pubsFromBib.generate_md()
    assert len(os.listdir(os.environ.get("OUT_PATH"))) == 1
    assert os.listdir(os.environ.get("OUT_PATH"))[0] == "1992-01-01-World-Wide-Web-The-Information-Universe.md"
