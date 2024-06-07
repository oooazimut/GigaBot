from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


def paste_row(bg: Image.Image, values: Iterable, group: str, ordinata: float, abcissa: float = 30, size: int = 150,
              step: int = 150):
    path = f'media/uza/{group}/'
    for position, val in values:
        element = Image.open(path + str(val) + '.png').resize((size, size)).convert('RGBA')
        bg.paste(element, (abcissa, ordinata), element)
        draw = ImageDraw.Draw(bg)
        font = ImageFont.load_default(36)
        draw.text((abcissa, ordinata-20), str(position), fill='black', font=font)
        abcissa += step
    bg.save('media/uza/result.png')


imaga = Image.new('RGBA', (1000, 1000), (255, 255, 255))

paste_row(imaga, enumerate([1, 1, 1, 0, 0, 1], start=1), 'tongs', 100)
# paste_row(imaga, [1, 0, 0, 2, 4, 5], 'shifters',  300)
# paste_row(imaga, [1, 0, 0, 1, 1, 1], 'condition', 500, abcissa=50, size=100, step=150)
