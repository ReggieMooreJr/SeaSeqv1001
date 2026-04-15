Welecome to SEA SEQ Software created by Mojo Consultants.

---

```markdown
# 🛡️ MCP Site Scanner

**MCP Site Scanner** is a modular, lightweight, and automated **security and reliability scanner** that validates website health, link integrity, form functionality, and response behavior — all while generating rich, timestamped HTML reports.

It’s **DevSecOps-ready**, **Docker-ready**, and **CI/CD-integrated**, offering complete visibility into your site’s reliability and test coverage across all environments.

# MCP Weather Server

A Model Context Protocol server that provides:

- Weather alerts (US National Weather Service)
- Weather forecasts by latitude/longitude
- Structured API logging

## Run

```bash
python weather.py

---

## ⚙️ What It Does

**MCP Site Scanner** performs the following tasks:

- 🧩 Crawls and scans an entire target website.
- 🔗 Validates internal and external links for availability and performance.
- 🧍 Detects “Add Member”, “Signup”, or “Register” forms automatically.
- 📤 Submits safe dummy payloads to confirm backend functionality.
- 🧾 Generates visually rich HTML reports for every scan.
- 🧪 Executes automated **unit and feature tests** inside Docker.
- 🧱 Seamlessly integrates with **GitHub Actions**, **Jenkins**, **CircleCI**, or **GitLab CI**.

---

## 🧠 Developer Notes 

# 📖 DEVELOPER NOTES

# 1. Every run yields an HTML report in ./reports/REPORT_MM_DD_YY_HHMM.html.

# 2. Every test speaks truth through ./reports/tests/.

# 3. The console must narrate — silence is error, verbosity is clarity.

# =============================================================================

```

---

## 🚀 Key Features

| Capability | Description |
|-------------|-------------|
| **Link Validation** | Checks every link, script, and image for reliability. |
| **Form Testing** | Detects signup/member forms and submits safe data. |
| **Security Checks** | Identifies missing headers and weak endpoints. |
| **Report Generation** | Creates professional HTML reports with timestamps. |
| **Automated Testing** | Combines unit and feature tests for coverage tracking. |
| **Docker Integration** | Fully containerized; run anywhere, any CI/CD. |
| **Pipeline Ready** | Works out of the box with GitHub, Jenkins, CircleCI, or GitLab CI. |

---

## 🧩 Project Structure

```

mcp-site-scanner/
├── mcp_site_scanner.py       # Core scanning engine
├── run-scan.sh               # Unified runner (API, CLI, one-off, test)
├── run-docker-tests.sh       # Dockerized test automation runner
├── Makefile                  # Developer command center
├── docker-compose.yml        # Multi-container orchestration
├── Dockerfile                # Container definition
├── reports/                  # Generated reports
│   ├── REPORT_MM_DD_YY_HHMM.html
│   └── tests/
│       ├── behave_report_MM_DD_YY_HHMM.html
│       ├── pytest_report_MM_DD_YY_HHMM.html
│       └── test_summary_MM_DD_YY_HHMM.html
├── tests/
│   ├── features/             # BDD feature tests (behave)
│   └── unit/                 # Unit tests (pytest)
└── .github/workflows/
└── docker-test.yml       # GitHub Actions CI/CD pipeline

````

---

## 🧭 Workflow Overview

| Action | Command | Description |
|--------|----------|-------------|
| **Start API Server** | `make api` | Runs Flask API on port 8020. |
| **Run CLI Scan** | `make cli` | Scans interactively and prints report location. |
| **Run One-Off Scan** | `make once` | Runs a single scan and generates a report. |
| **Run Local Tests** | `make test` | Executes cucumber + pytest locally. |
| **Build Docker Image** | `make docker-build` | Builds the containerized scanner image. |
| **Run Containerized API** | `make docker-run` | Runs the scanner API within Docker. |
| **Run All Tests in Docker** | `make docker-tests` | Runs Dockerized unit + feature tests with HTML reports. |
| **Docker Compose Up** | `make docker-compose-up` | Launches full stack with persistent reports. |
| **Clean Environment** | `make clean` | Removes temp files, cache, and logs. |

---

## 🧱 Local Setup

### 1. Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

### 2. Run a One-Off Scan

```bash
make once
```

Sample Output:

```
⚡ Running one-off scan for https://wwsad.b12sites.com/index...
✅ Report created: reports/REPORT_10_15_25_1342.html
📘 Logs saved: logs/scan_10_15_25_1342.log
```

---

## �� Docker Workflow

### Build the Image

```bash
make docker-build
```

### Run the Containerized Scanner

```bash
make docker-run
```

### Run All Tests Inside Docker

```bash
make docker-tests
```

Results appear in:

```
reports/tests/
├── behave_report_MM_DD_YY_HHMM.html
├── pytest_report_MM_DD_YY_HHMM.html
└── test_summary_MM_DD_YY_HHMM.html
```

---

## 🌐 Docker Compose Deployment

Spin up a persistent stack:

```bash
make docker-compose-up
```

Stop the stack:

```bash
make docker-compose-down
```

Reports remain saved under:

```
./reports/
```

---

## 🤖 GitHub Actions CI/CD

The GitHub workflow (`.github/workflows/docker-test.yml`) automatically executes the following on each push or pull request:

1. Builds the Docker image.
2. Runs all tests in Docker using `run-docker-tests.sh`.
3. Generates feature and unit test reports under `/reports/tests/`.
4. Uploads all reports as **CI artifacts**.
5. Displays a success/failure badge on the repository.

Artifacts can be downloaded under:
**Actions → Run → Artifacts → `mcp-site-scanner-reports.zip`**

---

## 🧪 Automated Test Reports

Every Docker test run generates:

* 🧩 **`behave_report.html`** — feature (BDD) tests
* 🧱 **`pytest_report.html`** — unit test results
* 🧾 **`test_summary.html`** — combined dashboard

The dashboard includes:

* Number of tests executed
* Test purpose and descriptions
* Pass/fail ratio
* Historical success tracking

Example:

```
reports/tests/test_summary_10_15_25_1415.html
```

You can open it directly in your browser for a full summary.

---

## 🧾 Visual Reports & Screenshots

Reports are automatically generated in HTML format.
Open them directly in your browser:

```bash
open reports/REPORT_MM_DD_YY_HHMM.html
open reports/tests/test_summary_MM_DD_YY_HHMM.html
```

They include:

* Color-coded risk indicators
* Performance and security metrics
* Visual pass/fail tables
* Historical test run summary

Optional: integrate **Playwright** or **Selenium** for screenshot-based visual verification.

---

## 🔗 Integrating into Other CI/CD Systems

### 🧱 Jenkins

```groovy
stage('Security Scan') {
  steps {
    sh 'make docker-tests'
    archiveArtifacts artifacts: 'reports/tests/**', fingerprint: true
  }
}
```

### 🔁 CircleCI

```yaml
jobs:
  mcp-scan:
    docker:
      - image: cimg/python:3.13
    steps:
      - checkout
      - run: make docker-tests
      - store_artifacts:
          path: reports/tests
```

### ⚙️ GitLab CI

```yaml
mcp_scan:
  stage: test
  script:
    - make docker-tests
  artifacts:
    paths:
      - reports/tests/
```

---

## 🧾 GitHub Badge Example

Add this to the top of your README for build visibility:

```markdown
[![MCP Site Scanner CI](https://github.com/YOUR-ORG/YOUR-REPO/actions/workflows/docker-test.yml/badge.svg)](https://github.com/YOUR-ORG/YOUR-REPO/actions/workflows/docker-test.yml)
```

This badge automatically updates to reflect your CI status
(✅ Passing or ❌ Failing) after each pipeline run.

---

## 📈 Optional: Live Success Rate Badge (Coming Soon)

A post-CI badge-updater script can parse your `test_summary.html` and
generate a dynamic badge showing your actual success rate percentage.
Example:

```
Tests Passing: 98% ✅
```

This will automatically push to your README using GitHub Actions.

---

## 🪪 License

**Apache License 2.0**
© 2025 **Mojo Consultants** — All Rights Reserved.

---

## 🧩 Developer Creed

```
# =============================================================================
# 📖 DEVELOPER NOTES — READ LIKE SCRIPTURE
# 1. Every scan writes its gospel — the report.
# 2. Every test tells its story — pass, fail, or truth.
# 3. Every build leaves proof — artifacts that endure.
# =============================================================================
```

```

---

### ✅ Summary
- Copy and paste this file directly as your `README.md`.
- It provides a polished, professional introduction to your repository.
- It fully explains setup, commands, reports, and pipeline integration.
- It’s styled consistently with your "Bible-style developer documentation


## Notes: 

I was stuck in VIM mode because i had VIM extension turned on. 

Reminder to turn off VIM Extension 

Option 1: Disable or Uninstall the Vim Extension

Open Extensions Panel
Ctrl + Shift + X (or click the Extensions icon on the sidebar)

Search for “Vim”

Click Disable or Uninstall
