from setuptools import setup, find_packages

# A file to setup the entire project, it lists the packages that
# python needs to build and install the entire app as a package.
# It also serves as an entry point to specify the list of dependencies
# required by the application.
setup(
    name='my_cart_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[]
)
