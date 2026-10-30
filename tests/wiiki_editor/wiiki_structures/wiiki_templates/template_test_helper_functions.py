import os

import wikitextparser
from wikitextparser import Template


def read_template_from_file(file: str) -> Template:
    if not os.path.exists(file):
        raise Exception(f"Test file {file} does not exist.")
    with open(file, "r") as f:
        wiki_text = wikitextparser.parse(str(f.read()))
        if not wiki_text.templates:
            raise Exception(f"File {file} does not have any templates.")
        return wiki_text.templates[0]
