# chanwookim-rps

A simple and fun rock-paper-scissors CLI game written in Python with score tracking and interactive gameplay.

## Features
- 🎮 Interactive terminal-based rock-paper-scissors game
- 📊 Score tracking across multiple rounds
- ⌨️ Support for multiple command aliases (game/play, help/rules, exit/quit)
- 🎯 Simple CLI entry point after installation (`rps`)
- ✅ Fully tested with unit tests

## Prerequisites
- Python 3.8+

## Installation

### From PyPI (Recommended)
```bash
pip install chanwookim-rps
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

### Quick Start
After installation, simply run:
```bash
rps
```

### In-Game Commands

**Main Menu:**
- `game` or `play` - Start a new game
- `help` or `rules` - View game rules
- `exit` or `quit` - Exit the game

**During Game:**
- `scissors`, `rock`, or `paper` - Make your choice
- `quit` or `exit` - Return to main menu

### Example Gameplay
```
Rock-Paper-Scissors Game
Menu | game | help | exit |
: game

Menu | quit | Current Score: 0
Choose: scissors, rock, or paper : rock

==================== Result ====================
Your choice: rock
Computer's choice: scissors

Result: You win!
Current score: 1
================================================
```

## Development

### Project Structure
```
.
├── src/
│   └── chanwookim_rps/
│       └── __init__.py          # Main game logic
├── tests/
│   ├── test_rps.py              # Unit tests
│   └── _test_rps_runner.py       # Integration test runner
├── README.md
├── CHANGELOG.md
├── LICENSE
└── setup.cfg
```

### Running Unit Tests
To ensure the core game logic is working correctly:
```bash
python -m unittest tests/test_rps.py -v
```

### Running the Test Runner
A simple test runner (with scripted inputs) is available:
```bash
python tests/_test_rps_runner.py
```

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for a list of all versions and changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- **chanwookim0716** - Initial work and maintenance

## Enjoy the game!

