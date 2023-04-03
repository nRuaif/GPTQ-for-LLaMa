from setuptools import setup, find_packages
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name=f"gptq_llama",
    version=f"1",
    author="nRuaif",
    description="GPTQ-for-LLaMa",
    license="MIT",
    keywords="gpu optimizers optimization 8-bit quantization compression",
    url="https://github.com/nRuaif/GPTQ-for-LLaMa",
    packages=find_packages(),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

)
