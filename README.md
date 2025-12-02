# Agent Labs

## Setup

### Google Cloud Authentication

To use Google Cloud services, you need to install the gcloud CLI and set up authentication:

1. Install gcloud CLI: `brew install --cask google-cloud-sdk`
2. Authenticate with Application Default Credentials: `gcloud auth application-default login`

**Application Default Credentials (ADC)** are a strategy used by Google client libraries to automatically find credentials. When you run `gcloud auth application-default login`, it stores your user credentials in a well-known location that Google client libraries can automatically discover and use for API calls. This eliminates the need to explicitly pass credentials in your code.

### Code Formatting

This project uses **Ruff** for fast Python linting and formatting. Ruff combines the functionality of multiple tools (flake8, isort, black, etc.) in a single, extremely fast package.

#### Commands:

```bash
# Check for linting issues
uv run ruff check

# Fix auto-fixable issues
uv run ruff check --fix

# Format code
uv run ruff format

# Run both linting and formatting
uv run ruff check --fix && uv run ruff format
```

#### IDE Integration:
- **VS Code**: Install the official Ruff extension
- **PyCharm**: Enable Ruff in Settings > Tools > External Tools
- Most editors have Ruff plugins available

#### Pre-commit Hooks

This project uses **pre-commit hooks** to automatically enforce code quality before commits. The hooks will run Ruff linting and formatting on every commit attempt.

**Automatic setup** (already done):
```bash
uv run pre-commit install
```

**Manual commands**:
```bash
# Run hooks on all files (useful for testing)
uv run pre-commit run --all-files

# Run hooks on staged files only
uv run pre-commit run

# Update hook versions to latest
uv run pre-commit autoupdate

# Bypass hooks for a specific commit (use sparingly)
git commit --no-verify -m "your message"
```

**What happens during commit**:
1. Ruff checks code for linting issues and fixes auto-fixable ones
2. Ruff formats code to ensure consistent style
3. If unfixable issues remain, the commit is blocked
4. Fix the issues manually and commit again

This ensures all committed code maintains consistent quality and style standards.