from setuptools import setup

setup(
    name='ocr_converter',
    version='1.0',
    py_modules=['main', 'ocr_converter'],
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'ocr_converter=main:main',
        ],
    },
)
