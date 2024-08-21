from leafnode import LeafNode


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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        split_text = node.text.split(delimiter)
        if node.text[0] == delimiter:
            # there will be an empty string at the beginnig of the list
            pass
