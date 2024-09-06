from markdown_conversions import markdown_to_html_node
import os


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

    new_html_content = template_contents.replace("{{ Title }}", extract_title(markdown_contents))

    generated_html_content = markdown_to_html_node(markdown_contents).to_html()

    new_html_content = new_html_content.replace("{{ Content }}", generated_html_content)

    split_dest_path = dest_path.split("/")
    path = "/".join(split_dest_path[:-1])
    if not os.path.exists(path):
        os.makedirs(path)

    with open(dest_path, 'w') as file:
        file.write(new_html_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        if os.path.isdir(f"{dir_path_content}/{file}"):
            generate_pages_recursive(f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/{file}")
            continue

        if ".md" in file:
            html_file = file.split(".")[0] + ".html"
            generate_page(f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/{html_file}")
        else:
            generate_page(f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/{file}")
