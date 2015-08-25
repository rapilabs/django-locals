from setuptools import setup, find_packages

setup(
    name='django-locals',
    version='1.1',
    description='A model for storing GeoNames data, and finding "surrounding suburbs".',
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='https://github.org/funkybob/django-locals/',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>=1.8',
    ],
)
