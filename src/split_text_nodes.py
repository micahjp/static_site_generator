import re
from textnode import TextNode


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

        split_node = node.text.split(delimiter)

        for index in range(len(split_node)):
            if not len(split_node[index]):
                continue

            if index % 2:
                split_nodes.append(TextNode(split_node[index], text_type))
            else:
                split_nodes.append(TextNode(split_node[index], "text"))

    return split_nodes


def split_nodes_image(old_nodes):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            split_nodes.append(node)
            continue

        for text in re.split(r"(!\[.*?\]\(.*?\))", node.text):
            if not text:
                continue

            image = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

            if image:
                split_nodes.append(TextNode(image[0][0], "image", image[0][1]))
                continue

            split_nodes.append(TextNode(text, "text"))

    return split_nodes


def split_nodes_link(old_nodes):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            split_nodes.append(node)
            continue

        for text in re.split(r"(?<!!)(\[.*?\]\(.*?\))", node.text):
            if not text:
                continue
            link = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

            if link:
                split_nodes.append(TextNode(link[0][0], "link", link[0][1]))
                continue

            split_nodes.append(TextNode(text, "text"))

    return split_nodes
