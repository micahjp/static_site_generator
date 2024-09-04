from parentnode import ParentNode
from block_conversions import block_to_htmlnode, block_to_block_type


def markdown_to_blocks(markdown):
    blocks = list(map(lambda block: block.strip(" \n"), markdown.split("\n\n")))
    while '' in blocks:
        blocks.remove('')

    return blocks


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        html_nodes.append(block_to_htmlnode(block, block_to_block_type(block)))

    html_node = ParentNode("div", html_nodes)
    return html_node
