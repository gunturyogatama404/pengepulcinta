from setuptools import Extension, find_packages, setup


with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="pengepulcinta",
        scripts=["scripts/colabcode"],
        version="0.3.0",
        description="pengepulcinta - Run codeserver on Colab!",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="aa Thakur",
        author_email="aa@gmail.com",
        url="https://github.com/gunturyogatama404/pengepulcinta/colabcode",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            "pyngrok>=5.1.0",
            "nest_asyncio==1.4.3",
            "uvicorn==0.13.1",
            "jupyterlab==3.4.2",
        ],
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
