from setuptools import setup, find_packages

setup(
    name="parker-utils",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "Click",
        "asyncclick",
    ],
    entry_points={
        "console_scripts": [
            "yourscript = yourscript:cli",
            "format-slack-dm = format_slack_dm_history:main",
        ],
    },
)
