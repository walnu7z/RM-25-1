# Define the Git repository
REPO_URL=https://github.com/ros/urdf_tutorial.git
CLONE_DIR=urdf_tutorial

# Define the workspace directory
WORKSPACE=.

# Default target
all: clone 

# Clone the repository if it doesn't exist
clone:
	@if [ ! -d "$(WORKSPACE)/src/$(CLONE_DIR)" ]; then \
		echo "Cloning the repository..."; \
		mkdir -p $(WORKSPACE)/src; \
		cd $(WORKSPACE)/src && git clone -b ros2 $(REPO_URL); \
	else \
		echo "Repository already cloned."; \
	fi

# Clean the workspace
clean:
	@echo "Cleaning the workspace..."
	rm -rf $(WORKSPACE)/build $(WORKSPACE)/install $(WORKSPACE)/log

# Run colcon test (optional target for running tests)
test:
	@echo "Running tests..."
	colcon test --base-path $(WORKSPACE)

.PHONY: all clone build clean test

