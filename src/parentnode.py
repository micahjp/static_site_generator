from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if self.children is None or len(self.children) == 0:
            raise ValueError("children cannot be None")

        content = "".join(map(lambda child: child.to_html(), self.children))
        return f"<{self.tag}>{content}</{self.tag}>"
