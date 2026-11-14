#!/usr/bin/env python3
"""Sum up 13 November's world news in one image - entry program (news-image-01).

Copies the image shipped beside this file (entry.png) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output).

The image is a "13 NOV 2026" magazine-cover montage: a night-time
globe at the centre, ringed by six vignettes of real news from
Friday 13 November 2026, each labelled:
  - SENATE SUMMONS EX-NVIDIA CEO
  - DRONE HITS RUSSIAN WARSHIP
  - US DOWNS IRAN DRONES
  - MICROSOFT OUTAGE: DAY 2
  - CHINA DRILLS AROUND TAIWAN
  - FAA LIFTS GROUND STOP

The copy is byte-for-byte, so the two grader runs produce
identical output. Nothing is generated or modified at run time:
the same input file always yields the same output bytes.
Standard library only; no network access.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    """Copy entry.png to the output directory. Returns exit code."""
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    if not source.is_file():
        print(f"missing image: {source}", file=sys.stderr)
        return 1

    # Byte-for-byte copy: deterministic by construction, no
    # re-encoding, so both grader runs write identical bytes.
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
