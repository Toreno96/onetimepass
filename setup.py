from setuptools import setup, find_packages

PACKAGE_NAME = "onetimepass"
SCRIPT_NAME = "otp"

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click"],
    extras_require={"dev": ["black"]},
    entry_points=f"""
        [console_scripts]
        {SCRIPT_NAME}={PACKAGE_NAME}.{SCRIPT_NAME}:otp
    """,
)
