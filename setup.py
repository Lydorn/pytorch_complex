import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()
# This call to setup() does all the work
setuptools.setup(
    name="torch_complex",
    version="0.0.1",
    description="PyTorch extension library for working with complex tensors",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Nicolas Girard",
    author_email="nicolas.jp.girard@gmail.com",
    license="INRIA",
    classifiers=[
        "License :: INRIA",
        "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
