from setuptools import setup

setup(
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    name="open-browser",
    version="0.0.1",
    license="MIT",
    url = "https://github.com/chenjiandongx/open-browser",
    py_modules=['open'],
    description="Open url via the command line",
    entry_points={
        'console_scripts': ['open=open:command_line_runner']
    }
)
