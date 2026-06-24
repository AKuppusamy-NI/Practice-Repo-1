# Practice-Repo-1

A repository for practicing GitHub Actions workflows and automation.

## Contents

- `hello.py` — Simple Python script
- `app.js` — Simple Node.js script
- `requirements.txt` — Python dependencies
- `package.json` — Node.js project metadata
- `data/sample.json` — Sample JSON data file
- `.github/workflows/ci.yml` — Example CI workflow

## Getting Started

### Python

```bash
pip install -r requirements.txt
python hello.py
```

### Node.js

```bash
npm install
node app.js
```

## GitHub Actions

The `.github/workflows/ci.yml` workflow runs on every push and pull request. It:

1. Checks out the code
2. Sets up Python and Node.js
3. Installs dependencies
4. Runs both scripts as a smoke test

Feel free to edit the workflow to try out new Actions features!
