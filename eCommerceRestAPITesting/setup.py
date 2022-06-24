from setuptools import setup, find_packages


setup(name='web',
      version='1.0',
      description="Practice REST API testing",
      author='Or Kazaz',
      author_email='kazi@email.com',
      url='https://kazi.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'attrs==21.4.0',
          'certifi==2022.6.15',
          'charset-normalizer==2.0.12',
          'idna==3.3',
          'iniconfig==1.1.1',
          'packaging==21.3',
          'pluggy==1.0.0',
          'py==1.11.0',
          'PyMySQL==1.0.2',
          'pyparsing==3.0.9',
          'pytest==7.1.2',
          'pytest-html==3.1.1',
          'pytest-metadata==2.0.1',
          'requests==2.28.0',
          'tomli==2.0.1',
          'urllib3==1.26.9',
          'WooCommerce==3.0.0'
      ]
      )
