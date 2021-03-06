import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Public',
    version='0.0.3',
    author='Ilija Petroniejvic',
    author_email='ilijapet@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/mark down",
    url='https://github.com/ilijapet/public',
    project_urls = {
        "Bug Tracker": "https://github.com/ilijapet/public/issues"
    },
    license='MIT',
    packages=['Public'],
    install_requires=['requests'],
)