# OpenCart UI Automation Tests

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/github/actions/workflow/status/AyuArts/opencart_auto_tests/tests.yml?label=CI)
![License](https://img.shields.io/badge/License-MIT-green)

End‑to‑end regression suite for the **OpenCart demo store** built with **Python + Selenium** using the **Page Object Model** pattern.

---

## Tech Stack

| Category    | Tool                                     |
|-------------|------------------------------------------|
| Language    | Python 3.11                              |
| Test Runner | Pytest 7.x                               |
| UI Driver   | Selenium 4.x (Chrome / Firefox / Safari) |
| Test Data   | Faker                                    |
| Logging     | Loguru                                   |
| Reporting   | Allure 2.x                               |
| Dependency Mgmt | Poetry                                   |

---

## Project Layout

```text
.
├── core/          # driver factory, logger wrapper, BaseTest
├── locators/      # validated locator collections
├── page/          # Page Object classes + navigation helpers
├── tests/         # pytest scenarios
├── utils/         # helpers: fake data, decorators, etc.
├── config.py      # global settings (base URL, timeouts…)
└── pyproject.toml # Poetry deps
```

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/AyuArts/opencart_auto_tests.git
cd opencart_auto_tests

# 2. Install Poetry
pip install --upgrade poetry

# 3. Install dependencies
poetry install

# 4. (optional) activate venv
poetry shell
```

> **Prerequisites:** a local Chrome/Firefox installation and the matching *driver* in `$PATH`.  

---

## Running Tests

```bash
# all tests
pytest -n auto -s

# single test
pytest tests/test_brands.py::TestBrandsPage

# with Allure report
pytest -q --alluredir=reports
allure serve reports
```

Override settings via env vars or CLI flags:

```bash
export OC_URL="https://demo.opencart.com/"
pytest -k cameras
```

---

## Test Scenarios

| # | Title            | Assertions |
|---|------------------|------------|
| 0 | Brands list      | Brands Apple … Sony are visible |
| 1 | Registration     | Successful signup, *Welcome* header |
| 2 | Show All Desktops| `Show=10`, `Sort=Default`, 10 cards |
| 3 | Sorting          | Name (A→Z) & Price (Low→High) orders |
| 4 | Currency switch  | iPhone prices for $, €, £ are correct |
| 5 | Cameras          | Prices & quantity for Canon EOS 5D, Nikon D300 |

---

## Handy Poetry Commands

| Command | Purpose |
|---------|---------|
| `poetry run pytest` | run tests inside venv |
| `poetry add <pkg>`  | add dependency |
| `poetry update`     | refresh lock‑file |
| `poetry version patch/minor/major` | bump version |

---

## Contributing

Issues and PRs are welcome!  
Follow the [Angular commit style](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#-commit-message-format) (`feat:`, `fix:`, `test:` …).

---

## License

[MIT](LICENSE)

---

> *Happy testing — make bugs afraid of you!* 🚀
