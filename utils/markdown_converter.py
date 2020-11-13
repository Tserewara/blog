import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite


def convert_markdown_to_html(article):
    return markdown.markdown(
        article,
        extensions=["fenced_code", "codehilite"]
    )
