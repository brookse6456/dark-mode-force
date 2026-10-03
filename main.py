"""Dark Mode Force — Set Windows apps and system theme to dark or light."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='dark_mode_force',
        description='Set Windows apps and system theme to dark or light.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Dark Mode Force')
    print('Theme flip without Settings.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
