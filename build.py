
import os
import sys
import yaml
import shutil
import jinja2
import markdown
import helpers


# Template defaults
defaults = {
    'labels': None,
}


def read_yaml(filename):
    """
    Read Yaml file given by ``filename`` and return dictionary data.
    """
    with open(filename, 'rt') as f:
        return yaml.load(f)


def render_template(tpl, vars):
    """
    Render template file with ``vars`` arguments.
    """
    with open(tpl, 'rt') as f:
        tpl = jinja2.Template(f.read())

    return tpl.render(**vars)


def copy_static_data(theme_dir, output_dir):
    """
    Copy contents of theme directory skipping all jinja template files.
    """
    def ignored_files(src, names):
        return [name for name in names if name.endswith('.jinja2')]

    shutil.copytree(theme_dir, output_dir, ignore=ignored_files)


def clean(output_dir):
    """
    Remove the output directory.
    """
    shutil.rmtree(output_dir, ignore_errors=True)


def build(data, config, output_dir):
    """
    Build the final directory, rendering all templates and copying source files
    """
    theme_name = config.get('theme', 'simple')
    vars = defaults.copy()
    vars.update(data)
    vars['config'] = config
    vars['h'] = helpers  # make helpers module accessible via 'h' shortcut.

    theme_location = os.path.join('themes', theme_name)

    clean(output_dir)
    copy_static_data(theme_location, output_dir)

    for filename in os.listdir(theme_location):
        if not filename.endswith('.jinja2'):
            continue

        html = render_template(os.path.join(theme_location, filename),
                               vars)

        rendered_file = filename.replace('.jinja2', '.html')
        with open(os.path.join(output_dir, rendered_file), 'wt') as f:
            f.write(html)


def make_html(config, data):
    """
    Generate static html build of the resume given by input `data`.
    """
    output_dir = config.get('output_dir', 'build')
    build(data, config, output_dir)


def make_pdf(config, data):
    """
    Generate PDF file out of generated 'index.html' page.
    """
    from weasyprint import HTML
    output_dir = config.get('output_dir', 'build')
    output_file = os.path.join(output_dir, config.get('pdf_file', 'resume.pdf'))
    input_file = os.path.join(output_dir, 'index.html')
    theme_location = os.path.join('themes', config['theme'])
    html = HTML(input_file, base_url=theme_location)
    html.write_pdf(output_file)


def main(args=sys.argv):
    """
    Entry function for the script to handle command arguments
    and run appropriate build like 'html' and 'pdf'.
    """
    if len(args) > 1:
        cmd = args[1]
    else:
        cmd = 'html'

    config = read_yaml('config.yaml')
    data = read_yaml('resume.yaml')

    cmds = {'html': make_html, 'pdf': make_pdf}
    return cmds[cmd](config, data)

if __name__ == '__main__':
    main()
