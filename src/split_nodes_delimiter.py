from textnode import TextNode


def split_nodes_delimiter(old_text_nodes, delimiter, text_type):
    valid_text_types = [
            "text",
            "bold",
            "italic",
            "code",
            "link",
            "image"
            ]
    if text_type not in valid_text_types:
        raise TypeError("not a valid text type")

    split_nodes = []
    for node in old_text_nodes:
        if node.text_type != "text":
            split_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2:
            raise Exception(f"unable to parse {node}, string formatted incorrectly")

        split_text = node.text.split(delimiter)
        for index in range(len(split_text)):
            if split_text[index] == '':
                continue
            if index % 2:
                split_nodes.append(TextNode(split_text[index], text_type))
            else:
                split_nodes.append(TextNode(split_text[index], "text"))

    return split_nodes
