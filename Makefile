
RSYNC_LOCATION=hanula.com:/var/www/resume/

.PHONY: html clean

all: clean html

html:
	python build.py
	@echo "Done"

clean:
	@rm -rf ./html


publish:
	rsync -aAXv build/ ${RSYNC_LOCATION}
