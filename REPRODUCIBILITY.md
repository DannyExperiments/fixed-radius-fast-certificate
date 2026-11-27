# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay gives conservative finite parameters and checks 29 rational boundary values, including equality in the strict stopping rule. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/simplex-certificate-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font paths. [Build the paper](paper/BUILD.md).
