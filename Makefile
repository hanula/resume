# RESUME ?= resumes/hanula.yaml
RESUME ?= resumes/jmbeach.yaml
RESUMES_DIR ?= resumes
list: $(RESUMES_DIR)/*
			@echo $^

PYTHON ?= $(shell which python3)
BUILD_DIR ?= build
THEME ?= compact
BUILD_ARGS ?= --output_dir $(BUILD_DIR)
BUILD ?= $(PYTHON) build.py $(BUILD_ARGS)

.PHONY: clean html pdf

all: clean html pdf

dir_all: $(RESUMES_DIR)/*
	@for file in $^ ; do $(BUILD) --format both --theme $(THEME) $${file} ; done

clean:
#	@rm -rf ./build
	@echo $(RESUME)

html:
	$(BUILD) --format html --theme $(THEME) $(RESUME)

pdf:
	$(BUILD) --format pdf --theme $(THEME) $(RESUME)
