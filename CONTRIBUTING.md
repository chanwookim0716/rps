# Contributing to chanwookim-rps

Thank you for your interest in contributing to chanwookim-rps! We appreciate your help in making this project better.

## Code of Conduct

Please be respectful and constructive in all interactions with other contributors.

## How to Contribute

### Reporting Bugs

If you've found a bug, please open an issue on GitHub with:
- A clear and descriptive title
- A detailed description of the bug
- Steps to reproduce the behavior
- Expected behavior
- Your Python version and OS

### Suggesting Enhancements

We welcome feature requests! Please:
1. Use a clear and descriptive title
2. Provide a detailed description of the enhancement
3. Explain why this enhancement would be useful
4. List any similar features in other projects

### Pull Requests

1. **Fork the repository** and clone your fork locally
   ```bash
   git clone https://github.com/your-username/chanwookim-rps.git
   cd chanwookim-rps
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Install development dependencies**
   ```bash
   pip install -e .
   ```

4. **Make your changes**
   - Keep changes focused and atomic
   - Write clear, descriptive commit messages
   - Follow PEP 8 style guidelines

5. **Run tests to ensure nothing breaks**
   ```bash
   python -m unittest tests/test_rps.py -v
   ```

6. **Commit and push your changes**
   ```bash
   git add .
   git commit -m "feat: Add your feature description"
   git push origin feature/YourFeatureName
   ```

7. **Open a Pull Request**
   - Provide a clear description of what your PR does
   - Reference any related issues
   - Ensure all tests pass

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Write docstrings for all functions and classes
- Add type hints where appropriate
- Keep lines under 100 characters when possible

## Commit Messages

Use clear and descriptive commit messages:
- `feat: Add new feature` for new features
- `fix: Fix bug description` for bug fixes
- `docs: Update documentation` for documentation changes
- `chore: Update dependencies` for maintenance tasks
- `test: Add test case` for test additions

## Testing

- Add tests for new features
- Ensure all existing tests pass
- Aim for high code coverage

Run tests with:
```bash
python -m unittest tests/test_rps.py -v
```

## Documentation

- Update README.md if your contribution changes user-facing functionality
- Update CHANGELOG.md with significant changes
- Add docstrings to code

## Questions?

Feel free to open an issue to ask questions or start a discussion about the project.

---

Thank you for contributing to chanwookim-rps! 🎮
