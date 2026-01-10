# Python Learning Project

A collection of Python programs for learning and practicing programming concepts, from basic operations to web scraping.

## Programs

| File | Description |
|------|-------------|
| `learning_random.py` | Rock-Paper-Scissors game using the random module |
| `learning_password_generator.py` | Random password generator with customizable length |
| `learning_love_calculator.py` | Novelty compatibility score calculator |
| `learning_number_guessing.py` | Number guessing game with difficulty levels |
| `learning_blackjack.py` | Simplified Blackjack card game vs computer |
| `learning_scraping_website.py` | Web scraper using Playwright for PDF export |

## Project Structure

```
PythonLearningProject/
├── .github/
│   └── workflows/
│       └── tests.yml          # CI workflow
├── tests/
│   ├── __init__.py
│   └── test_blackjack.py      # Unit tests for blackjack
├── learning_blackjack.py
├── learning_random.py
├── learning_password_generator.py
├── learning_love_calculator.py
├── learning_number_guessing.py
├── learning_scraping_website.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone the repository
git clone git@github.com:boku-engineer/PythonLearningProject.git
cd PythonLearningProject

# Install test dependencies
pip install pytest
```

### Running Programs

```bash
# Run any program directly
python learning_blackjack.py
python learning_number_guessing.py
```

### Running Tests

```bash
# Run all tests
pytest -v
```

## Development Workflow

This project follows **trunk-based development** with automated testing.

### Workflow Steps

1. **Create a feature branch**
   ```bash
   git checkout -b feature/my-change
   ```

2. **Make changes and add tests**
   - Write your code
   - Add unit tests in `tests/` directory

3. **Run tests locally**
   ```bash
   pytest -v
   ```

4. **Push your branch**
   ```bash
   git push -u origin feature/my-change
   ```

5. **Create a Pull Request on GitHub**
   - GitHub Actions automatically runs tests
   - Review the test results

6. **Merge to main**
   - After tests pass, merge your PR

### CI/CD Pipeline

GitHub Actions automatically runs on:
- Every push to `main`
- Every pull request targeting `main`

The pipeline:
1. Checks out the code
2. Sets up Python 3.12
3. Installs pytest
4. Runs all tests

View workflow runs: [Actions](https://github.com/boku-engineer/PythonLearningProject/actions)
