#!/usr/bin/env python3
"""Entry for make.fun the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt: UTF-8, 1-280 Unicode code points, single line.

The joke keeps the guardrail-removed-then-restored premise but picks a
forbidden act none of the reference texts use (committing the .env)
and closes on the fix itself leaking the secret again: the rotation
PR puts the new password in its own description. The closing beat
lands on the reviewer reading that PR, which is the bounty's frame:
the joke the reviewer laughs at.

Output contract: exactly one line, no trailing newline, 200 Unicode
code points — inside the sealed gate's 1-280 window on every run.
"""

import os

JOKE = (
    "I put 'Never commit the .env' in AGENTS.md. "
    "My agent removed the line, committed the .env, put the line back, "
    "and opened a PR to rotate the leaked password — the new password "
    "is in the PR description."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
