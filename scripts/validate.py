#!/usr/bin/env python3
"""
Validate a PoE2 .filter file before committing.

Catches the failure modes that break filters silently:
  1. Unknown Class names        -> rule never matches, item vanishes from view
  2. Unconditional Show/Hide    -> swallows every rule below it
  3. Shadowed rules             -> a broad Hide above a narrow Show
  4. Malformed colour values    -> out-of-range RGB
  5. Out-of-range font sizes    -> game clamps or ignores

Usage:
    python3 scripts/validate.py current-filter/shared.filter
    python3 scripts/validate.py            # defaults to shared.filter

Exit code 0 = clean, 1 = problems found. Safe to use as a pre-commit hook.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILTER = ROOT / "current-filter" / "shared.filter"
CLASS_LIST = ROOT / "references" / "item-classes.txt"

ACTION_PREFIXES = (
    "Set", "Play", "Minimap", "Disable", "Enable", "Custom",
)

# Conditions whose values are item Class names
CLASS_CONDITIONS = ("Class",)


def load_valid_classes():
    if not CLASS_LIST.exists():
        print(f"  ! {CLASS_LIST} missing - skipping Class validation")
        return None
    return {
        line.strip()
        for line in CLASS_LIST.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    }


def parse_blocks(text):
    """Split a filter into blocks. Returns list of dicts."""
    blocks = []
    current = None
    for lineno, raw in enumerate(text.splitlines(), 1):
        stripped = raw.strip()
        if not stripped:
            continue
        head = stripped.split("#")[0].strip()
        if head in ("Show", "Hide", "Minimal") or head.startswith(
            ("Show ", "Hide ", "Minimal ")
        ):
            if current:
                blocks.append(current)
            current = {
                "line": lineno,
                "type": head.split()[0],
                "label": stripped,
                "conditions": [],
                "actions": [],
                "continue": False,
            }
            continue
        if current is None or stripped.startswith("#"):
            continue
        if stripped == "Continue":
            current["continue"] = True
        elif stripped.startswith(ACTION_PREFIXES):
            current["actions"].append(stripped)
        else:
            current["conditions"].append(stripped)
    if current:
        blocks.append(current)
    return blocks


def check_classes(blocks, valid):
    problems = []
    if valid is None:
        return problems
    for b in blocks:
        for cond in b["conditions"]:
            if not cond.startswith(CLASS_CONDITIONS):
                continue
            for name in re.findall(r'"([^"]+)"', cond):
                if name not in valid:
                    problems.append(
                        f"line {b['line']}: unknown Class \"{name}\" "
                        f"- this rule will never match"
                    )
    return problems


def check_unreachable(blocks):
    """An unconditional block with no Continue swallows everything below it."""
    problems = []
    for i, b in enumerate(blocks[:-1]):
        if not b["conditions"] and not b["continue"]:
            remaining = len(blocks) - i - 1
            problems.append(
                f"line {b['line']}: unconditional {b['type']} with no Continue "
                f"- the {remaining} rule(s) below it are unreachable"
            )
    return problems


def check_colours(blocks):
    problems = []
    colour_re = re.compile(
        r"^Set(?:Text|Border|Background)Color\s+(.+)$"
    )
    for b in blocks:
        for act in b["actions"]:
            m = colour_re.match(act)
            if not m:
                continue
            parts = m.group(1).split()
            nums = [p for p in parts if p.lstrip("-").isdigit()]
            if len(nums) not in (3, 4):
                problems.append(
                    f"line {b['line']}: '{act}' - expected 3 or 4 numbers, got {len(nums)}"
                )
                continue
            for n in nums:
                if not (0 <= int(n) <= 255):
                    problems.append(
                        f"line {b['line']}: '{act}' - value {n} outside 0-255"
                    )
    return problems


def check_font_sizes(blocks):
    problems = []
    for b in blocks:
        for act in b["actions"]:
            if act.startswith("SetFontSize"):
                parts = act.split()
                if len(parts) < 2 or not parts[1].isdigit():
                    problems.append(f"line {b['line']}: malformed '{act}'")
                elif not (1 <= int(parts[1]) <= 45):
                    problems.append(
                        f"line {b['line']}: SetFontSize {parts[1]} outside valid range 1-45"
                    )
    return problems


def check_shadowing(blocks):
    """Warn when a broad Hide sits above a narrower Show on the same Class."""
    warnings = []
    seen_hides = []
    for b in blocks:
        classes = set()
        for cond in b["conditions"]:
            if cond.startswith(CLASS_CONDITIONS):
                classes.update(re.findall(r'"([^"]+)"', cond))
        if b["type"] == "Hide" and not b["continue"]:
            seen_hides.append((b, classes, len(b["conditions"])))
        elif b["type"] == "Show" and classes:
            for hide_b, hide_classes, hide_ncond in seen_hides:
                overlap = classes & hide_classes
                if overlap and hide_ncond <= len(b["conditions"]):
                    warnings.append(
                        f"line {b['line']}: Show for {sorted(overlap)} sits below "
                        f"a broader Hide at line {hide_b['line']} "
                        f"- items may never reach it"
                    )
    return warnings


def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILTER
    if not target.exists():
        print(f"ERROR: {target} not found")
        return 1

    text = target.read_text()
    blocks = parse_blocks(text)
    valid = load_valid_classes()

    print(f"Validating {target.name}")
    print(f"  {len(blocks)} blocks  "
          f"({sum(1 for b in blocks if b['type'] == 'Show')} Show, "
          f"{sum(1 for b in blocks if b['type'] == 'Hide')} Hide)")
    print()

    errors = []
    errors += check_classes(blocks, valid)
    errors += check_unreachable(blocks)
    errors += check_colours(blocks)
    errors += check_font_sizes(blocks)
    warnings = check_shadowing(blocks)

    if errors:
        print("ERRORS")
        for e in errors:
            print(f"  x {e}")
        print()
    if warnings:
        print("WARNINGS (review, may be intentional)")
        for w in warnings:
            print(f"  ! {w}")
        print()

    if not errors and not warnings:
        print("Clean. Safe to commit.")
    elif not errors:
        print(f"No errors. {len(warnings)} warning(s) to review.")
    else:
        print(f"{len(errors)} error(s) must be fixed before committing.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
