# Include config if exists
-include  config.make

# Put these into config.make to override with your setup
RESUME ?= resumes/example.yaml
RSYNC_LOCATION ?= example.com:/var/www/resume/

PYTHON ?= $(shell which python3)
RSYNC ?= $(shell which rsync)
RSYNC_ARGS ?= aAXv
BUILD_DIR ?= build
BUILD_ARGS ?= --output_dir $(BUILD_DIR)
BUILD ?= $(PYTHON) build.py $(BUILD_ARGS)


.PHONY: clean html pdf publish


all: clean html pdf

html:
	$(BUILD) --format html $(RESUME)
	@echo "Done"

pdf:
	$(BUILD) --format pdf $(RESUME)

clean:
	@rm -rf ./html

publish:
	$(RSYNC) -$(RSYNC_ARGS) $(BUILD_DIR) $(RSYNC_LOCATION)
