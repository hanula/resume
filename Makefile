
RSYNC_LOCATION=hanula.com:/var/www/resume/

.PHONY: clean html pdf publish

all: clean html pdf

html:
	python build.py
	@echo "Done"

pdf:
	python build.py pdf

clean:
	@rm -rf ./html


publish:
	rsync -aAXv build/ ${RSYNC_LOCATION}
