# SyvaSoft Training Academy

Frappe app for internal employee training and commercial ERPNext training academy.

## Repository structure

The GitHub repository root must contain:

- setup.py
- pyproject.toml
- requirements.txt
- MANIFEST.in
- syvasoft_training/hooks.py
- syvasoft_training/__init__.py

Do not add an extra outer folder between the repository root and these files.

## Install

bench get-app syvasoft_training https://github.com/YOUR_USERNAME/syvasoft_training.git
bench --site YOUR_SITE install-app syvasoft_training
bench --site YOUR_SITE migrate
bench build --app syvasoft_training
