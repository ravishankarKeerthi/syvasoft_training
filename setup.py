from setuptools import setup, find_packages

app_name = "syvasoft_training"

setup(
    name=app_name,
    version="1.0.0",
    description="SyvaSoft Training Academy for Frappe",
    author="SyvaSoft Business Solutions",
    author_email="info@syvasoft.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
