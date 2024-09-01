import re
from textnode import TextNode
from parse_md_links_img import extract_markdown_links
from parse_md_links_img import extract_markdown_images


def is_valid_text_type(text_type):
    valid_text_types = [
            "text",
            "bold",
            "italic",
            "code",
            "link",
            "image"
            ]

    return text_type in valid_text_types


def create_text_node_list(split_text_list, text_type):
    text_node_list = []
    for index in range(len(split_text_list)):
        if not len(split_text_list[index]):
            continue
        if index % 2:
            match text_type:
                case "image":
                    url = extract_markdown_images(split_text_list[index])[0][1]
                    pass
                case "link":
                    url = extract_markdown_links(split_text_list[index])[0][1]
                    pass
                case _:
                    url = None

            text_node_list.append(TextNode(split_text_list[index], text_type, url))
        else:
            text_node_list.append(TextNode(split_text_list[index], "text"))

    return text_node_list


def split_nodes_delimiter(old_text_nodes, delimiter, text_type):
    if not is_valid_text_type(text_type):
        raise TypeError("not a valid text type")

    split_nodes = []
    for node in old_text_nodes:
        if node.text_type != "text":
            split_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2:
            raise Exception(f"unable to parse {node}, string formatted incorrectly")

        split_nodes += create_text_node_list(node.text.split(delimiter), text_type)

    return split_nodes


def split_nodes_image(old_nodes):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            split_nodes.append(node)
            continue

        split_nodes += create_text_node_list(re.split(r"(!\[.*?\]\(.*?\))", node.text), "image")

    return split_nodes


def split_nodes_link(old_nodes):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            split_nodes.append(node)
            continue

        split_nodes += create_text_node_list(re.split(r"(?<!!)(\[.*?\]\(.*?\))", node.text), "link")

    return split_nodes
