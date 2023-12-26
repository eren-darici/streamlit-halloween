#!/bin/bash

# Set the project directory name
PROJECT_DIR="."

# Create directories
mkdir -p $PROJECT_DIR/app
mkdir -p $PROJECT_DIR/data

# Create app files
touch $PROJECT_DIR/app/__init__.py
touch $PROJECT_DIR/app/main.py
echo "streamlit" > $PROJECT_DIR/app/requirements.txt

# Create Docker and Heroku files
touch $PROJECT_DIR/Dockerfile
echo "web: streamlit run app/main.py" > $PROJECT_DIR/Procfile

# Create documentation
echo "# Streamlit Halloween App" > $PROJECT_DIR/README.md

# Create gitignore
echo "__pycache__/" > $PROJECT_DIR/.gitignore
echo "venv/" >> $PROJECT_DIR/.gitignore

# Display completion message
echo "Streamlit Halloween app file structure created successfully in '$PROJECT_DIR'!"
