resume
======

Python resume generator. From YAML to PDF and static HTML.

Example Themes
--------------
* [simple](http://resume.hanula.com/)
* [compact](http://jmbeach.github.io/resume/)

Installing
----------

    git clone https://github.com/hanula/resume
    cd resume
    pip install -r requirements.txt

### Requirements

This script requires `Python 3` and a set of libraries with their dependencies:

    PyYAML
    Jinja2
    Markdown
    WeasyPrint
    docopt

Usage
-----

1. Look at resume examples in the `resumes` folder and create your own.
2. Copy `config.make.example` to `config.make` and update it with your settings.
3. Run `make` to build HTML and PDF files that will go to the `build` directory.


### PDF generator

PDF is automatically generated along with html when running `make`.
To just create PDF file:

    make pdf

PDF file name in `build` directory is defined by `pdf_file` property in the `config` section of your resume `yaml` file.


### Publishing

To publish html on your server via SSH, edit `RSYNC_LOCATION` in `config.make` and run:

    make publish


Customizing
-----------
This repo contains a simple and a compact theme.

Add your own theme by creating `themes/<your-theme>` folder with `index.jinja2` template file.
Every other (non-jinja2) file from theme directory will be copied to final `build/` destination.

You can control which theme is used by setting `theme` property in the resume's `config` section.


License
-------
[MIT License](https://github.com/hanula/resume/blob/master/LICENSE)
