# cicd-demo-dataweek2025

This repository serves as playground for the DevOps workshop at DataWeek Leipzig 2025

## Clone the Github Repository

Clone the repository using the following command:

```bash
git clone https://github.com/ScaDS/cicd-demo-dataweek2025.git
```

### Project Structure

- `app/` - Source code with gradio app, analysis modules and data
- `tests/` - Test files
- `scripts/` - Utility scripts including test checkers
- `devops-conda-env.yml` - Conda environment file
- `pyproject.toml` - Python project and tools configuration
- `.github/workflows/ci.yml` - CICD configuration for Github Actions in this repository
- `gitlab-ci.yml` - CICD configuration equivalent for Gitlab

## Local Development Setup

### Conda Environment Setup

Create (or update) and activate the conda environment using:

```bash
conda env update -f devops-conda-env.yml --prune
conda activate dataweek-devops-env
```

### Development Testing Requirements

Before submitting changes, complete these mandatory testing steps locally:

#### Code Style and Linting

   ```bash
   ruff check
   ```
   Identifies code style violations and linting errors.

   ```bash
   ruff check --fix
   ```
   Identifies code style violations and linting errors, tries to fix them.

#### Test Coverage Verification

   ```bash
   python scripts/check_tests.py
   ```
   Ensures all analysis modules have corresponding test implementations.

#### Test Execution

   ```bash
   pytest tests
   ```
   Runs the complete test suite to verify functionality.

## Run the App

   ```bash
   python -m app.main
   ````
   Run the Gradio app locally.

## Contributing

1. Create a new branch for your feature
2. Follow the local testing requirements above
3. Submit a pull request with your changes

## Zenodo Link for Slides

https://zenodo.org/records/15654889
