
import re
import markdown


def md(text):
    text = markdown.markdown(text, output_format='html5')
    return re.sub('<p>(.*)?</p>', '\\1', text)
