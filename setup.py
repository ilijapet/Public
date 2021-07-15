import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='paket',
    version='0.0.1',
    author='Ilija Petroniejvic',
    author_email='ilijapet@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/mark down",
    url='https://github.com/ilijapet/public/tree/Master/paket',
    project_urls = {
        "Bug Tracker": "https://github.com/ilijapet/public/tree/Master/paket/issues"
    },
    license='MIT',
    packages=['paket'],
    install_requires=['requests'],
)