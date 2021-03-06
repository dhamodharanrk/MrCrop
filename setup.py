import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

NAME = "MrCrop"
DESCRIPTION = "Crop faces from batches of images in directory faster"
URL = "https://github.com/dhamodharanrk/MrCrop"
EMAIL = "dhamodharanrk@gmail.com"
AUTHOR = "Dhamodharan Karuppuswamy"

REQUIRED = ["numpy>=1.10", "opencv-python>=3, <4", "Pillow>5"]

HERE = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

about = {}
with open(os.path.join(HERE, NAME, "__version__.py")) as f:
    exec(f.read(), about)

class UploadCommand(Command):

    description = "Build and publish the package."
    user_options = []
    @staticmethod
    def status(s):
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass
        self.status("Building Source and Wheel (universal) distribution…")
        setup_str = "{0} setup.py sdist bdist_wheel --universal"
        os.system(setup_str.format(sys.executable))
        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")
        sys.exit()
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    entry_points={"console_scripts": ["MrCrop=MrCrop:cli"]},
    install_requires=REQUIRED,
    include_package_data=True,
    license="BSD 2-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    cmdclass={"upload": UploadCommand},
)
