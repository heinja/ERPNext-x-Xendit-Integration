from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_xendit_integration/__init__.py
from erpnext_xendit_integration import __version__ as version

setup(
	name="erpnext_xendit_integration",
	version=version,
	description="Adding Xendit payment gateway provider as one of the option for processing payments in ERPNext\'s (front) website checkout.",
	author="Redaco System Factory",
	author_email="andrew@redaco.id",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
