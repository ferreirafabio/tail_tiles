"""tail_tiles - Multi-tile tail viewer for terminal."""

from tail_tiles.__main__ import (
    LAYOUTS,
    TailTile,
    TileRenderer,
    clamp,
    load_session,
    main,
    read_last_n_lines,
    run_viewer,
    save_session,
)

__version__ = "0.1.0"
__all__ = [
    "LAYOUTS",
    "TailTile",
    "TileRenderer",
    "clamp",
    "load_session",
    "main",
    "read_last_n_lines",
    "run_viewer",
    "save_session",
]
