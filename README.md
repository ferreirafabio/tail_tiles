# tail_tiles

Multi-tile tail viewer for terminal. Monitor multiple log files simultaneously in a single terminal window.

## Install

```bash
pip install -e .
```

## Usage

```bash
tail-tiles
# or
python -m tail_tiles
```

On startup, select a layout and enter file paths to monitor.

## Controls

| Key | Action |
|-----|--------|
| `+` / `-` | Adjust lines shown |
| `r` | Force refresh |
| `q` | Quit |

## Requirements

- Python 3.10+
- Linux/macOS (uses curses)
