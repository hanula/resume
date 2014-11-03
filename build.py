
import os
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

    theme_location = 'themes/{}'.format(theme_name)

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


def main():
    data = read_yaml('resume.yaml')
    config = read_yaml('config.yaml')
    output_dir = config.get('output_dir', 'build')
    build(data, config, output_dir)


if __name__ == '__main__':
    main()
