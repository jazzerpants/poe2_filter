#!/bin/sh
# Copy current-filter/shared.filter into the live PoE2 filter folder.
#
# macOS + CrossOver: the bottle's Documents is a symlink to ~/Documents, so
# the game reads filters straight from the real Mac path below. Override with:
#   POE2_FILTER_DIR="/some/other/path" ./scripts/install.sh
#
# The game does NOT hot-reload — after running this, in game do
# Options -> Game -> Item Filter -> "shared" -> Reload.
set -e

# Resolve repo root from this script's location so it works from any CWD.
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
SRC="$ROOT/current-filter/shared.filter"
DST_DIR="${POE2_FILTER_DIR:-$HOME/Documents/My Games/Path of Exile 2}"
DST="$DST_DIR/shared.filter"

if [ ! -f "$SRC" ]; then
	echo "error: source filter not found: $SRC" >&2
	exit 1
fi

if [ ! -d "$DST_DIR" ]; then
	echo "error: PoE2 filter folder not found: $DST_DIR" >&2
	echo "       Launch PoE2 once so it creates the folder, or set POE2_FILTER_DIR." >&2
	exit 1
fi

cp "$SRC" "$DST"
echo "Installed -> $DST"
echo "Now in game: Options -> Game -> Item Filter -> \"shared\" -> Reload."
