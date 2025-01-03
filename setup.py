from setuptools import setup, find_packages

setup(
    name="NeuroAI-Framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "pytest",  
        "sphinx",
    ],
    author="Parsa Hormozi",
    description="NeuroAI Framework merging neuroscience and AI",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/TheSpiralProgrammer/NeuroAI-Framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='pytest',
)
