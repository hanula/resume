resume
======

My resume with static html generator.

You can see how it looks at [resume.hanula.com](http://resume.hanula.com).


Installing
----------

    git clone https://github.com/hanula/resume
    cd resume
    pip install -r requirements.txt

Usage
-----

Update `resume.yaml` with your details and run:

    make
    open build/index.html


To publish html on your server via SSH, edit `RSYNC_LOCATION` in `Makefile` and run:

    make publish

Customizing
-----------

Add your own theme by creating `themes/<your-theme>` folder with `index.jinja2` template file.
Every other (non-jinja2) file from theme directory will be copied to final `build/` destination.

You can control which theme is used by setting `theme` property in `config.yaml` file.

License
-------
[MIT License](https://github.com/hanula/resume/blob/master/LICENSE)
