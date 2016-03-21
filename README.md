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

Usage
-----

Update `resume.yaml` with your details and run:

    make
    open build/index.html

Which will generate static HTML in `build` directory, containing `index.html` page with theme assets and generated pdf file.

### PDF generator

PDF is automatically generated along with html when running `make`.
To just create PDF file:

    make pdf

PDF file name in `build` directory is defined by `pdf_file` in `config.yaml`.


### Publishing

To publish html on your server via SSH, edit `RSYNC_LOCATION` in `Makefile` and run:

    make publish
    

Customizing
-----------
This repo contains a simple and a compact theme.

Add your own theme by creating `themes/<your-theme>` folder with `index.jinja2` template file.
Every other (non-jinja2) file from theme directory will be copied to final `build/` destination.

You can control which theme is used by setting `theme` property in `config.yaml` file.


License
-------
[MIT License](https://github.com/hanula/resume/blob/master/LICENSE)
