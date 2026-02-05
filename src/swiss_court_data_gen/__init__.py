"""Swiss Federal Court Data Generation.

Process Swiss Federal Court data with LLMs to generate datasets for RAG and fine-tuning tasks.

This package provides tools to:
- Process court decision data from the Swiss Federal Supreme Court
- Generate synthetic Q&A pairs using multiple LLM providers
- Create high-quality datasets for legal AI applications

Example:
    >>> from swiss_court_data_gen import __version__
    >>> print(__version__)
    0.1.0

License:
    Code: Apache License 2.0
    Data: CC BY 4.0 (see DATA_LICENSE.md)

Data Source:
    Geering, F., & Merane, J. (2024). Swiss Federal Supreme Court Dataset (SCD).
    Zenodo. https://doi.org/10.5281/zenodo.13353736
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("swiss-court-data-gen")
except PackageNotFoundError:
    __version__ = "0.1.0"

__all__ = ["__version__"]
