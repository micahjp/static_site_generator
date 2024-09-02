from textnode import TextNode
import split_nodes


def text_to_textnode(string):
    types = {
            "bold": "**",
            "italic": "*",
            "code": "`"
            }
    text_nodes = [TextNode(string, "text")]

    text_nodes = split_nodes.split_nodes_link(text_nodes)
    text_nodes = split_nodes.split_nodes_image(text_nodes)

    for type in types:
        text_nodes = split_nodes.split_nodes_delimiter(text_nodes, types[type], type)

    return text_nodes
