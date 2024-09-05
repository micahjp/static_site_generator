def extract_title(markdown):
    first_line = markdown.split("\n")[0]
    if first_line[:2] != "# ":
        raise Exception("no h1 title to extract")

    return first_line[2:].strip()


def generate_page(from_path, template_path, dest_path):
    pass
