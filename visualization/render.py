"""Render the 3D projection of the FAST counterexample and its margins."""

import argparse
from itertools import combinations
from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BG = "#101c30"
PANEL = "#1b2e4b"
LIGHT = "#f5f8fd"
MUTED = "#cfdef2"
TEAL = "#78dcd1"
GRAY = "#7c8fae"
CORAL = "#ffac97"
VERTICES = ((-.65,-.65,-.65), (1.0,-.65,-.65), (-.65,1.0,-.65), (-.65,-.65,.13))
EDGES = tuple(combinations(range(4), 2))
COLORS = (GRAY, CORAL, TEAL, GRAY)


def project(vertex, angle):
    x, y, z = vertex
    x, z = x * cos(angle) + z * sin(angle), z * cos(angle) - x * sin(angle)
    tilt = .4 + .14 * cos(angle)
    y, z = y * cos(tilt) - z * sin(tilt), y * sin(tilt) + z * cos(tilt)
    scale = 385 / (4.7 - z)
    return 214 + scale * x, 275 - scale * y, z


def frame(angle, title, label, value, body):
    image = Image.new("RGB", (880, 550), BG)
    draw = ImageDraw.Draw(image)
    draw.text((26, 20), "FAST stops on the lower margin", font=title, fill=LIGHT)
    draw.line((28, 79, 852, 79), fill="#395375", width=2)
    draw.rounded_rectangle((27, 104, 407, 410), radius=17, fill=PANEL)
    draw.text((49, 119), "Simplex projection", font=label, fill=LIGHT)
    points = tuple(project(v, angle) for v in VERTICES)
    for i, j in sorted(EDGES, key=lambda edge: (points[edge[0]][2] + points[edge[1]][2]) / 2):
        p, q = points[i], points[j]
        draw.line((p[:2], q[:2]), fill="#7d90b0", width=3)
    for i, (x, y, depth) in sorted(enumerate(points), key=lambda p: p[1][2]):
        radius = 10 + depth * 2.2
        draw.ellipse((x-radius, y-radius, x+radius, y+radius),
                     fill=COLORS[i], outline=BG, width=2)
    draw.rounded_rectangle((429, 104, 853, 410), radius=17, fill=PANEL)
    draw.text((452, 119), "Margin comparison", font=label, fill=LIGHT)
    for y, name, fraction, color in ((187,"Returned","1/2",CORAL),
                                     (259,"Required","9/16",LIGHT),
                                     (331,"Optimum","3/4",TEAL)):
        draw.text((452,y+5), name, font=body, fill=MUTED)
        draw.text((825,y-2), fraction, font=value, fill=color, anchor="ra")
    for x, color, caption in ((34,CORAL,"Played vertex"), (278,TEAL,"Optimal vertex")):
        draw.ellipse((x,444,x+18,462),fill=color)
        draw.text((x+27,435),caption,font=body,fill=MUTED)
    draw.text((34,494),"Stops when the boundary per round falls below 1/14",font=body,fill=MUTED)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font", default="DejaVuSans.ttf")
    parser.add_argument("--bold-font", default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output", type=Path, default=Path("visualization/simplex-certificate.gif"))
    args = parser.parse_args()
    fonts = tuple(ImageFont.truetype(font, size) for font, size in (
        (args.bold_font, 42), (args.bold_font, 33), (args.bold_font, 47), (args.regular_font, 29)
    ))
    frames = [frame(.55 + i*tau/64, *fonts).quantize(colors=120, method=2) for i in range(64)]
    frames[0].save(args.output, save_all=True, append_images=frames[1:],
                   duration=92, loop=0, disposal=2, optimize=True)


if __name__ == "__main__":
    main()
