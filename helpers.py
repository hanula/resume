
import re
import markdown


def md(text):
    """
    Process text as markdown and remove surrounding '<p>' tags
    simple flat text if possible.
    """
    text = markdown.markdown(text, output_format='html5')
    return re.sub('<p>(.*)?</p>', '\\1', text)
