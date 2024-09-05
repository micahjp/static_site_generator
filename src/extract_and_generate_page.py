from markdown_conversions import markdown_to_html_node


def extract_title(markdown):
    first_line = markdown.split("\n")[0]
    if first_line[:2] != "# ":
        raise Exception("no h1 title to extract")

    return first_line[2:].strip()


def generate_page(from_path, template_path, dest_path):
    print(f"generating page from '{from_path}' to '{dest_path}' using '{template_path}'")

    with open(from_path, 'r') as file:
        markdown_contents = file.read()

    with open(template_path, 'r') as file:
        template_contents = file.read()

    print(markdown_to_html_node(markdown_contents).to_html)
