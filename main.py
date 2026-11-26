"""Sum up 26 November's world news in one image.

Copies the image drawn at build time (entry.png, committed in this
repository) to /output/entry.png. Standard library only, no network,
deterministic: the same bytes every run.
"""

import os

CHUNK = 65536


def copy_image():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(source):
        raise SystemExit("entry.png missing from the repository")
    with open(source, "rb") as origin:
        with open(target, "wb") as dest:
            while True:
                piece = origin.read(CHUNK)
                if not piece:
                    break
                dest.write(piece)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    copy_image()
