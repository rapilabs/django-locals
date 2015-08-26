from setuptools import setup, find_packages

setup(
    name='django-locals',
    version='1.1',
    description='A model for storing GeoNames data, and finding "surrounding suburbs".',
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='https://github.com/funkybob/django-locals/',
    packages=find_packages(),
    include_package_data = True,
    package_data = {
        '': ['*.txt'],
    },
    zip_safe=False,
    install_requires=[
        'Django>=1.8',
    ],
)
