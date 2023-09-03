# RESUME ?= resumes/hanula.yaml
RESUME ?= resumes/jmbeach.yaml

PYTHON ?= $(shell which python3)
BUILD_DIR ?= build
THEME ?= compact
BUILD_ARGS ?= --output_dir $(BUILD_DIR)
BUILD ?= $(PYTHON) build.py $(BUILD_ARGS)

.PHONY: clean html pdf

all: clean html pdf

clean:
#	@rm -rf ./build
	@echo $(RESUME)

html:
	$(BUILD) --format html --theme $(THEME) $(RESUME)

pdf:
	$(BUILD) --format pdf --theme $(THEME) $(RESUME)
