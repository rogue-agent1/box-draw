import argparse

STYLES = {
    "single": "┌─┐│ │└─┘",
    "double": "╔═╗║ ║╚═╝",
    "rounded": "╭─╮│ │╰─╯",
    "heavy": "┏━┓┃ ┃┗━┛",
}

def draw_box(text, style="single", padding=1):
    chars = STYLES[style]
    tl, h, tr, vl, sp, vr, bl, _, br = chars
    lines = text.split("\n")
    w = max(len(l) for l in lines) + padding * 2
    result = [tl + h * w + tr]
    for line in lines:
        pad = line + " " * (w - padding * 2 - len(line))
        result.append(vl + " " * padding + pad + " " * padding + vr)
    result.append(bl + h * w + br)
    return "\n".join(result)

def main():
    p = argparse.ArgumentParser(description="Box drawing")
    p.add_argument("text", nargs="*")
    p.add_argument("-s", "--style", choices=STYLES.keys(), default="single")
    p.add_argument("-p", "--padding", type=int, default=1)
    p.add_argument("--stdin", action="store_true")
    args = p.parse_args()
    import sys
    text = sys.stdin.read().strip() if args.stdin else " ".join(args.text)
    print(draw_box(text, args.style, args.padding))

if __name__ == "__main__":
    main()
