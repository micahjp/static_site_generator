from leafnode import LeafNode
from parentnode import ParentNode
from text_node_conversions import text_to_textnode, text_node_to_html_node


def block_to_block_type(block):
    unique_chars_before_space = set(list(block.split(" ")[0]))
    if len(unique_chars_before_space) == 1 and "#" in unique_chars_before_space:
        return "heading"

    if block[0:3] == block[-3:] == "```":
        return "code"

    block_lines = block.split("\n")

    lines_first_char = set(map(lambda line: line[0:1], block_lines))
    if len(lines_first_char) == 1:
        if lines_first_char.pop() == ">":
            return "quote"

    lines_first_two_chars = set(map(lambda line: line[0:2], block_lines))
    if len(lines_first_two_chars) == 1:
        match lines_first_two_chars.pop():
            case "* ":
                return "unordered_list"
            case "- ":
                return "unordered_list"

    for i in range(len(block_lines)):
        if block_lines[i][0:3] != f"{i + 1}. ":
            break
        if i == len(block_lines) - 1:
            return "ordered_list"

    return "paragraph"


def block_to_children(block, block_type):
    if block_type == "unordered_list":
        list_item_nodes = []
        items = block.split("\n")
        for item in items:
            child_text_nodes = text_to_textnode(item[2:])
            children = list(map(lambda child_text_node: text_node_to_html_node(child_text_node), child_text_nodes))
            list_item_nodes.append(ParentNode("li", children))
        return list_item_nodes

    if block_type == "ordered_list":
        list_item_nodes = []
        items = block.split("\n")
        for item in items:
            child_text_nodes = text_to_textnode(item[3:])
            children = list(map(lambda child_text_node: text_node_to_html_node(child_text_node), child_text_nodes))
            list_item_nodes.append(ParentNode("li", children))
        return list_item_nodes

    if block_type == "code":
        text_nodes = text_to_textnode(block[3:-3])
    elif block_type == "heading":
        size = get_heading_size(block)
        text_nodes = text_to_textnode(block[size + 1:])
    elif block_type == "quote":
        cleaned_block = "".join(block.split(">"))
        if cleaned_block[0] == " ":
            cleaned_block = cleaned_block[1:]
        text_nodes = text_to_textnode(cleaned_block)
    else:
        text_nodes = text_to_textnode(block)

    if text_nodes[0].text == block:
        return None

    return list(map(lambda textnode: text_node_to_html_node(textnode), text_nodes))


def get_heading_size(string):
    for i in range(6):
        if string[i] != "#":
            return i
    return 6


def block_to_htmlnode(block, block_type):
    children = block_to_children(block, block_type)
    match block_type:
        case "paragraph":
            if children:
                return ParentNode("p", children)
            return LeafNode("p", block)
        case "heading":
            size = get_heading_size(block)
            if children:
                return ParentNode(f"h{size}", children)
            return LeafNode(f"h{size}", block[size + 1:])
        case "code":
            if children:
                return ParentNode("pre", [ParentNode("code", children)])
            return ParentNode("pre", [LeafNode("code", block)])
        case "quote":
            if children:
                return ParentNode("blockquote", children)
            cleaned_quote_block = "".join(block.split(">"))
            if cleaned_quote_block[0] == " ":
                cleaned_quote_block = cleaned_quote_block[1:]
            return LeafNode("blockquote", cleaned_quote_block)
        case "unordered_list":
            return ParentNode("ul", children)
        case "ordered_list":
            return ParentNode("ol", children)
        case _:
            raise Exception("block type not supported")
