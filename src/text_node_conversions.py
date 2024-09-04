from leafnode import LeafNode
from textnode import TextNode
from split_text_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("text node type unsupported")


def text_to_textnode(string):
    types = {
            "bold": "**",
            "italic": "*",
            "code": "`"
            }
    text_nodes = [TextNode(string, "text")]

    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_image(text_nodes)

    for type in types:
        text_nodes = split_nodes_delimiter(text_nodes, types[type], type)

    return text_nodes
