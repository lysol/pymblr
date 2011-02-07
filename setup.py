from distutils.core import setup

setup(name='pymblr',
      version='0.2.22',
      description='Python wrapper for Tumblr API. Original version by ' + \
        'Ryan A. Cox.',
      author='Derek Arnold',
      author_email='derek@dderek.com',
      license='Apache License 2.0',
      url='http://github.com/lysol/pymblr',
      py_modules=['pymblr'],
      classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ),
      requires=(
          'ElementTree',
          'httplib2',
          'poster',
          'mechanize',
          'simplejson'
          ),
      download_url="http://github.com/lysol/pymblr/tarball"
     )
