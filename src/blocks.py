def markdown_to_blocks(markdown):
    blocks = list(map(lambda block: block.strip(" \n"), markdown.split("\n\n")))
    while '' in blocks:
        blocks.remove('')

    return blocks


def block_to_block_type(block):
    if block[0:2] == "# ":
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

    # need to add ordered list functionality!
    for i in range(len(block_lines)):
        if block_lines[i][0:3] != f"{i + 1}. ":
            break
        if i == len(block_lines) - 1:
            return "ordered_list"

    return "paragraph"
