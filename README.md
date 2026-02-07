# chanwookim-rps

Simple rock-paper-scissors CLI game.

## Features
- Interactive terminal game with score tracking
- Simple CLI entry point after installation (`rps`)
- Support for multiple command aliases

## Prerequisites
- Python 3.8+

## Installation

### From TestPyPI (Recommended for testing the published package)
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps chanwookim-rps
```

### From GitHub repository
```bash
pip install git+https://github.com/chanwookim0716/chanwookim-rps.git
```

### Local Installation
Navigate to the project root directory and run:
```bash
pip install --user .
```

### For Development (Editable Install)
Navigate to the project root directory and run:
```bash
pip install -e .
```

## Usage
After installation, you can run the CLI command:
```bash
rps
```

### In-Game Commands
**Main Menu:**
- `game` or `play` - Start a new game
- `help` or `rules` - View game rules
- `exit` or `quit` - Exit the game

**During Game:**
- `scissors`, `rock`, `paper` - Make your choice
- `quit` or `exit` - Return to main menu

## Development

### Running Unit Tests
To ensure the core game logic is working correctly, run the unit tests:
```bash
python -m unittest tests/test_rps.py
```

### Running the Test Runner
A simple test runner (with scripted inputs) is available to exercise the game logic:
```bash
python tests/_test_rps_runner.py
```

## Contributing
- Fork the repo, make changes, and open a pull request. Keep changes small and focused.

## License
This project is licensed under the [LICENSE](LICENSE) file.
