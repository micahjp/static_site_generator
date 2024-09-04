from textnode import TextNode
from parentnode import ParentNode
from htmlnode import HTMLNode
from blocks import markdown_to_blocks, block_to_block_type
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


def get_heading_size(string):
    for i in range(6):
        if string[i] != "#":
            return i

    return 6


def block_to_htmlnode(block, block_type, children=None):
    match block_type:
        case "paragraph":
            return ParentNode("p", children, None)
        case "heading":
            size = get_heading_size(block)
            return ParentNode(f"h{size}", children, None)
        case "code":
            pass
        case "quote":
            pass
        case "unordered_list":
            pass
        case "ordered_list":
            pass
        case _:
            raise Exception("block type unsupported")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
