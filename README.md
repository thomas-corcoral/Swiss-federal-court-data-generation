# Swiss Federal Court Data Generation

[![CI](https://github.com/thomas-corcoral/Swiss-federal-court-data-generation/actions/workflows/ci.yaml/badge.svg)](https://github.com/thomas-corcoral/Swiss-federal-court-data-generation/actions/workflows/ci.yaml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Data License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

Process Swiss Federal Court (Bundesgericht/Tribunal fédéral) data with LLMs to generate high-quality synthetic datasets for **RAG (Retrieval-Augmented Generation)** and **fine-tuning** tasks.

## Project Overview

This project processes the [Swiss Federal Supreme Court Dataset (SCD)](https://doi.org/10.5281/zenodo.13353736) using advanced LLMs to generate:

- **Synthetic Q&A pairs** for legal RAG systems
- **Email response datasets** for legal assistant fine-tuning
- **Structured legal annotations** for domain-specific models

## Features

- 🚀 **Multi-LLM Support**: OpenAI, Anthropic Claude, Google Gemini
- 📊 **Streaming Processing**: Memory-efficient batch processing of large datasets
- 🔄 **Checkpoint/Resume**: Automatic progress saving for long-running jobs
- ✅ **Quality Gates**: Built-in quality assessment with configurable thresholds
- 🐳 **Docker Ready**: Containerized for reproducible execution
- 📈 **Parallel Processing**: Configurable concurrency for optimal throughput

## Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/thomas-corcoral/Swiss-federal-court-data-generation.git
cd Swiss-federal-court-data-generation

# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

### Using pip

```bash
pip install -e ".[dev]"
```

### Using Docker

```bash
docker build -t swiss-court-data-gen:latest -f docker/Dockerfile .
```

## Quick Start

1. **Set up environment variables:**

```bash
cp .env.example .env
# Edit .env with your API keys
```

2. **Download the source data:**

Place your Swiss Federal Court parquet files in the `data/` directory.

3. **Run the generation pipeline:**

```bash
uv run python -m swiss_court_data_gen.synthetic_data_generation
```

## Configuration

Create a `.env` file with your LLM API keys:

```env
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GOOGLE_API_KEY=your-google-key
```

## Development

```bash
# Run linting
make lint

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Type checking
make typecheck
```

## Project Structure

```
Swiss-federal-court-data-generation/
├── src/
│   └── swiss_court_data_gen/     # Main package
│       ├── config.py             # Configuration management
│       ├── llm_factory.py        # LLM provider abstraction
│       ├── row_processor.py      # Data row processing logic
│       └── synthetic_data_generation.py
├── tests/                        # Test suite
├── docker/                       # Docker configuration
├── data/                         # Input data (not committed)
└── output/                       # Generated outputs (not committed)
```

## Data Source

This project uses the **Swiss Federal Supreme Court Dataset (SCD)**, which must be cited when using the generated data:

> Geering, F., & Merane, J. (2024). Swiss Federal Supreme Court Dataset (SCD) (2024-2) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.13353736

### BibTeX Citation

```bibtex
@dataset{geering_2024_13353736,
  author       = {Geering, F. and Merane, J.},
  title        = {Swiss Federal Supreme Court Dataset (SCD)},
  month        = aug,
  year         = 2024,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.13353736},
  url          = {https://doi.org/10.5281/zenodo.13353736}
}
```

## License

- **Code**: [Apache License 2.0](LICENSE)
- **Data**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](DATA_LICENSE.md)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Support

- [Documentation](https://github.com/thomas-corcoral/Swiss-federal-court-data-generation#readme)
- [Issue Tracker](https://github.com/thomas-corcoral/Swiss-federal-court-data-generation/issues)
- [Discussions](https://github.com/thomas-corcoral/Swiss-federal-court-data-generation/discussions)

## ⭐ Acknowledgments

- [Swiss Federal Supreme Court](https://www.bger.ch/) for making court decisions publicly available
- The creators of the [Swiss Federal Supreme Court Dataset](https://doi.org/10.5281/zenodo.13353736)
- All contributors to this project

