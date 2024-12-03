# ERP - FI

This project is an ERP module for financial management.

## Setup

### Python version

This project uses Python 3.11.10. Make sure you have the correct version installed.

### Virtual environment

Create a virtual environment using your preferred tool. For example, using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Dependencies

Install the dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

Run the following command and follow the instructions:

```bash
fastapi dev
```

## Running Tests
### Run Tests

To run the tests, execute the following command from the root directory of the project:

```bash
pytest tests/
```

This will automatically discover and run all test files in the tests/ directory.

## Contributing

### Pre-commit hooks

Install the pre-commit hooks by running:

```bash
pre-commit install
```

### VSCode

If you use VSCode, please install the recommended extensions (see `.vscode/extensions.json`).
