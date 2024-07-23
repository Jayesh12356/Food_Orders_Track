from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in food_order_app/__init__.py
from food_order_app import __version__ as version

setup(
	name="food_order_app",
	version=version,
	description="Food Order App",
	author="Jayesh Koli",
	author_email="jkoli6704@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
