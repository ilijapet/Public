import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fun',
    version='0.0.1',
    author='Ilija Petroniejvic',
    author_email='ilijapet@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ilijapet/Radionica/tree/radni/Public/paket',
    project_urls = {
        "Bug Tracker": "https://github.com/ilijapet/Radionica/tree/radni/Public/paket"
    },
    license='MIT',
    packages=['fun'],
    install_requires=['requests'],
)