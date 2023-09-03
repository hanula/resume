# Include config if exists
# -include  config.make

# Put these into config.make to override with your setup
RESUME ?= resumes/hanula.yaml
# RESUME ?= resumes/jmbeach.yaml

PYTHON ?= $(shell which python3)
BUILD_DIR ?= build
THEME ?= compact
BUILD_ARGS ?= --output_dir $(BUILD_DIR)
BUILD ?= $(PYTHON) build.py $(BUILD_ARGS)

# all: clean html pdf
all: html pdf

clean:
	@rm -rf ./build

html:
	$(BUILD) --format html --theme $(THEME) $(RESUME)

pdf:
	$(BUILD) --format pdf --theme $(THEME) $(RESUME)
