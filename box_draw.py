#!/usr/bin/env python3
"""Box drawing — frame text in ASCII or Unicode boxes."""
import sys
STYLES={"single":"┌─┐│ │└─┘","double":"╔═╗║ ║╚═╝","round":"╭─╮│ │╰─╯","ascii":"+-+| |+-+","heavy":"┏━┓┃ ┃┗━┛"}
def box(text, style="single", padding=1):
    chars=STYLES.get(style,STYLES["single"])
    tl,th,tr,ml,_,mr,bl,bh,br=chars
    lines=text.split("\n"); width=max(len(l) for l in lines)+padding*2
    print(f"{tl}{th*width}{tr}")
    for line in lines: print(f"{ml}{' '*padding}{line.ljust(width-padding*2)}{' '*padding}{mr}")
    print(f"{bl}{bh*width}{br}")
def cli():
    if len(sys.argv)<2: print("Usage: box_draw <text> [single|double|round|ascii|heavy]"); sys.exit(1)
    style=sys.argv[2] if len(sys.argv)>2 else "single"
    box(sys.argv[1], style)
if __name__=="__main__": cli()
