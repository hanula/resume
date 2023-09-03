"""
Simple HTML and PDF resume generator from structurized YAML files.

Usage:
    build.py [-o=<DIR>] [-f=<FORMAT>] [-t=<THEME>] <resume_file>

Options:
    -o=<DIR>, --output_dir=<DIR>     Output directory for the build files. [default: build].
    -f=<FORMAT>, --format=<FORMAT>   Format of the build [default: html].
    -t=<NAME>, --theme=<NAME>        Name of the theme to use.
"""

import os
from typing import TypedDict

import shutil
from weasyprint import HTML
import yaml
import docopt
import jinja2
import helpers


# Template defaults
defaults = {
    "labels": None,
}


def read_yaml(filename: str) -> TypedDict:
    """
    Read Yaml file given by ``filename`` and return dictionary data.
    """
    with open(filename, "rt", encoding="utf-8") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def render_template(tpl, variables):
    """
    Render template file with ``variables`` arguments.
    """
    with open(tpl, "rt", encoding="utf-8") as file:
        tpl = jinja2.Template(file.read())

    return tpl.render(**variables)


def copy_static_data(theme_dir, output_dir):
    """
    Copy contents of theme directory skipping all jinja template files.
    """
    shutil.copytree(
        theme_dir,
        output_dir,
        ignore=lambda src, names: [name for name in names if name.endswith(".jinja2")],
    )


def clean(output_dir):
    """
    Remove the output directory.
    """
    shutil.rmtree(output_dir, ignore_errors=True)


def build(data, config: TypedDict, output_dir):
    """
    Build the final directory, rendering all templates and copying source files
    """
    theme_name = config.get("theme", "simple")
    variables = defaults.copy()
    variables.update(data)
    variables["config"] = config
    variables["h"] = helpers  # make helpers module accessible via 'h' shortcut.

    theme_location = os.path.join("themes", theme_name)

    clean(output_dir)
    copy_static_data(theme_location, output_dir)

    for filename in os.listdir(theme_location):
        if filename != "index.jinja2":
            continue

        html = render_template(os.path.join(theme_location, filename), variables)

        rendered_file = filename.replace(".jinja2", ".html")
        with open(os.path.join(output_dir, rendered_file), "wt", encoding="utf-8") as file:
            file.write(html)


def make_html(config: TypedDict, data):
    """
    Generate static html build of the resume given by input `data`.
    """
    output_dir = config.get("output_dir", "build")
    build(data, config, output_dir)


def make_pdf(config: TypedDict):
    """
    Generate PDF file out of generated 'index.html' page.
    """
    output_dir = config.get("output_dir", "build")
    pdf_output_dir = "./pdf"
    output_file = os.path.join(pdf_output_dir, config.get("pdf_file", "resume.pdf"))
    input_file = os.path.join(output_dir, "index.html")
    theme_location = os.path.join("themes", config["theme"])
    html = HTML(input_file, base_url=theme_location)
    html.write_pdf(output_file)


def make_both(config: TypedDict, data):
    """
    Both HTML and PDF for a single file.
    """
    make_html(config, data)
    make_pdf(config)


def main():
    """
    Entry function for the script to handle command arguments
    and run appropriate build like 'html' and 'pdf'.
    """
    args = docopt.docopt(__doc__)
    output_format = args["--format"]

    # read resume data and config with some defaults
    resume_data = read_yaml(args["<resume_file>"])
    config = resume_data.get("config", {})
    config.setdefault("output_dir", args["--output_dir"])
    config["theme"] = args["--theme"] or config.get("theme")
    config.setdefault("theme", "simple")

    # build based on the given format
    # cmds = {'html': make_html, 'pdf': make_pdf}
    # return cmds[output_format](config, resume_data)

    if output_format == "both":
        make_both(config, resume_data)
    elif output_format == "html":
        make_html(config, resume_data)
    elif output_format == "pdf":
        make_pdf(config)


if __name__ == "__main__":
    main()
