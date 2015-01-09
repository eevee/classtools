from setuptools import setup

setup(
    name='classtools',
    version='0.1',
    description='A few class utilities the stdlib is missing.',
    url='https://github.com/eevee/classtools',
    author='Eevee',
    author_email='eevee.classtools@veekun.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='class development',
    py_modules=['classtools'],
    tests_require=['pytest'],
)
