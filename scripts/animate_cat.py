"""Draw the perler-style cat and a GitHub-compatible transparent walking GIF.

All poses use authored pixel coordinates, a fixed palette and integer movement.
The cat is never rotated, warped or resampled with interpolation.
"""
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SIZE = (36, 36)
STAGE = (160, 40)
COLORS = {
    "outline": "#666765", "white": "#fffef8", "shade": "#d9dcd3",
    "ear": "#edf0e7", "ink": "#333732", "pink": "#edb6b6",
}


def sprite(eyes="open", step="still", pose="idle", facing="right"):
    mask = Image.new("L", SIZE)
    draw = ImageDraw.Draw(mask)

    def row(y, left, right):
        draw.line((left + 4, y + 2, right + 4, y + 2), fill=255)

    head_y = -2 if pose == "stretch" else 1 if pose == "crouch" else 0
    if pose == "tilt":
        # An individually drawn tilted head, including staggered ears and eyes.
        ears = [(0,6,6),(1,5,7),(2,5,8),(3,4,8),(4,4,9),
                (5,3,9),(6,3,10),(7,2,10),
                (3,23,23),(4,22,24),(5,21,24),(6,21,25),
                (7,20,25),(8,20,26),(9,19,26),(10,19,27)]
        head = [(8,2,18),(9,1,19),(10,1,27),(11,0,27),(12,0,27),
                (13,0,27),(14,0,27),(15,0,27),(16,1,27),(17,1,27),
                (18,2,26),(19,4,25),(20,8,24),(21,12,20)]
    else:
        ears = [(1,5,5),(2,4,6),(3,4,7),(4,3,7),
                (5,3,8),(6,2,8),(7,2,9),(8,1,9)]
        ears += [(y, 27-right, 27-left) for y,left,right in ears.copy()]
        head = [(9,1,26),(10,1,26),(11,0,27),(12,0,27),(13,0,27),
                (14,0,27),(15,0,27),(16,0,27),(17,0,27),(18,1,26),
                (19,2,25),(20,4,23)]
    for y,left,right in ears + head:
        row(y + head_y, left, right)

    if pose == "stretch":
        body = [(19,7,20),(20,6,21),(21,6,21),(22,7,20),
                (23,7,20),(24,8,19),(25,9,18),(26,9,18)]
        # Both paws stretch out below the lifted head.
        body += [(19,3,5),(20,3,8),(21,4,9),
                 (19,22,24),(20,19,24),(21,18,23)]
    elif pose == "crouch":
        body = [(22,7,20),(23,6,21),(24,6,21),(25,7,20),(26,8,19)]
    else:
        body = [(21,8,19),(22,7,20),(23,7,20),
                (24,7,20),(25,8,19),(26,9,18)]
    if pose == "wave-up":
        body += [(18,28,29),(19,27,30),(20,26,30),
                 (21,22,29),(22,20,27),(23,19,24)]
    elif pose == "wave-down":
        body += [(20,28,30),(21,25,30),(22,21,29),
                 (23,19,26),(24,19,22)]
    elif pose == "jump":
        body += [(22,5,22),(23,4,23),(24,5,22)]
    for y,left,right in body:
        row(y,left,right)

    left_shift = -1 if step == "left" else 0
    right_shift = 1 if step == "right" else 0
    left_bottom = 28 if step == "left" else 29
    right_bottom = 28 if step == "right" else 29
    if pose == "stretch":
        left_bottom = right_bottom = 30
    elif pose in ("jump", "crouch"):
        left_bottom, right_bottom = 28, 28
    for y in range(27,left_bottom):
        row(y,9+left_shift,12+left_shift)
    row(left_bottom,8+left_shift,12+left_shift)
    for y in range(27,right_bottom):
        row(y,15+right_shift,18+right_shift)
    row(right_bottom,15+right_shift,19+right_shift)

    image = Image.new("RGBA", SIZE)
    image.paste(COLORS["outline"], mask=mask)
    image.paste(COLORS["white"], mask=mask.filter(ImageFilter.MinFilter(3)))
    draw = ImageDraw.Draw(image)

    def line(points, color, dy=0):
        draw.line([(x+4,y+2+dy) for x,y in points],fill=COLORS[color])

    def rect(box, color, dy=0):
        x1,y1,x2,y2 = box
        draw.rectangle((x1+4,y1+2+dy,x2+4,y2+2+dy),fill=COLORS[color])

    def poly(points, color, dy=0):
        draw.polygon([(x+4,y+2+dy) for x,y in points],fill=COLORS[color])

    rect((10+left_shift,26,11+left_shift,left_bottom-1),"white")
    rect((16+right_shift,26,17+right_shift,right_bottom-1),"white")
    if pose not in ("stretch", "jump", "crouch"):
        rect((8,22,9,23),"white")
        rect((18,22,19,23),"white")
    if pose == "wave-up":
        line([(20,22),(23,22),(25,21),(27,20),(28,19),(29,19)],"white")
    elif pose == "wave-down":
        line([(20,23),(23,23),(26,22),(28,21),(29,21)],"white")
    elif pose == "stretch":
        line([(4,20),(7,21),(8,21)],"white")
        line([(23,20),(20,21),(19,21)],"white")
    if pose == "tilt":
        line([(5,18),(11,19),(18,20),(23,20)],"shade")
        poly([(6,3),(4,8),(9,7)],"ear")
        poly([(23,6),(20,10),(25,11)],"ear")
        eye_positions = [(6,11),(20,13)]
        mouth = [(10,13),(10,14),(11,15),(12,15),(13,14),
                 (14,15),(15,16),(16,16),(17,15),(17,14)]
        line([(3,14),(5,14)],"pink")
        line([(22,16),(24,16)],"pink")
    else:
        line([(5,19),(22,19)],"shade",head_y)
        line([(8,20),(19,20)],"shade",head_y)
        poly([(5,4),(3,9),(8,8)],"ear",head_y)
        poly([(22,4),(19,8),(24,9)],"ear",head_y)
        eye_positions = [(6,12),(20,12)]
        mouth = [(10,14),(10,15),(11,16),(12,16),(13,15),(14,15),
                 (15,16),(16,16),(17,15),(17,14)]
        line([(3,15),(5,15)],"pink",head_y)
        line([(22,15),(24,15)],"pink",head_y)
    for x,y in eye_positions:
        if eyes == "open":
            rect((x,y,x+1,y+1),"ink",head_y)
        else:
            line([(x,y+1),(x+1,y+1)],"ink",head_y)
    line(mouth,"ink",head_y)
    if facing == "left":
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return image


@dataclass(frozen=True)
class Frame:
    duration: int
    x: int = 0
    lift: int = 0
    pose: str = "idle"
    eyes: str = "open"
    step: str = "still"
    facing: str = "right"


def timeline():
    frames = []

    def add(duration, x, **pose):
        frames.append(Frame(duration, x=x, **pose))

    add(900,0)
    add(120,0,eyes="closed")
    add(400,0)
    for _ in range(2):
        add(180,0,pose="wave-up")
        add(180,0,pose="wave-down")
    add(700,0)

    def walk(start, end, facing):
        direction = 2 if end > start else -2
        for index,x in enumerate(range(start+direction,end+direction,direction)):
            step = ("left","still","right","still")[index % 4]
            add(110,x,step=step,facing=facing)

    walk(0,120,"right")
    add(650,120)
    add(120,120,eyes="closed")
    add(250,120)
    add(800,120,pose="tilt")
    add(450,120)
    add(180,120,pose="crouch",eyes="closed")
    add(850,120,pose="stretch",eyes="closed")
    add(650,120)
    walk(120,60,"left")
    add(500,60,facing="left")
    add(160,60,pose="crouch",eyes="closed")
    for lift,duration in [(2,80),(4,80),(6,140),(4,80),(2,80)]:
        add(duration,60,lift=lift,pose="jump",facing="left")
    add(160,60,pose="crouch",eyes="closed",facing="left")
    add(700,60,facing="left")
    walk(60,0,"left")
    add(650,0,facing="left")
    add(120,0,eyes="closed",facing="left")
    add(450,0)
    return frames


def render(frame, stage=STAGE):
    image = Image.new("RGBA",stage)
    cat = sprite(frame.eyes,frame.step,frame.pose,frame.facing)
    # The jump shifts only whole grid cells, leaving every drawn pixel intact.
    image.paste(cat,(frame.x,4-frame.lift),cat)
    return image


def save_gif(path, images, durations, scale=2):
    rgb = [tuple(bytes.fromhex(value[1:])) for value in COLORS.values()]
    lookup = {color:index+1 for index,color in enumerate(rgb)}
    palette = [0,0,0] + [channel for color in rgb for channel in color]
    palette += [0]*(768-len(palette))
    frames = []
    for image in images:
        indexed = Image.new("P",image.size,0)
        indexed.putpalette(palette)
        indexed.putdata([lookup[image.getpixel((x,y))[:3]]
                         if image.getpixel((x,y))[3] else 0
                         for y in range(image.height) for x in range(image.width)])
        frames.append(indexed.resize((image.width*scale,image.height*scale),
                                     Image.Resampling.NEAREST))
    frames[0].save(path,save_all=True,append_images=frames[1:],duration=durations,
                   loop=0,transparency=0,disposal=2,optimize=False)


def build():
    assets = ROOT/"assets"
    sprite().resize((216,216),Image.Resampling.NEAREST).save(assets/"pixel-cat.png")
    frames = timeline()
    save_gif(assets/"pixel-cat-walk.gif",[render(frame) for frame in frames],
             [frame.duration for frame in frames])
    # A compact version is useful outside the title without the walking strip.
    compact = [Frame(f.duration,lift=f.lift,pose=f.pose,eyes=f.eyes,
                     step=f.step,facing=f.facing) for f in frames]
    save_gif(assets/"pixel-cat.gif",[render(f,(36,40)) for f in compact],
             [f.duration for f in compact])
    print(f"Built {len(frames)} frames, {sum(f.duration for f in frames)/1000:.2f}s. "
          "Walking, waving, head tilt, stretch, jump and blink.")


if __name__ == "__main__":
    build()
