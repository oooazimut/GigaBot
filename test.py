from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

from config import PUMPS_IDS


def paste_row(bg: Image.Image, values: Iterable, group: str, ordinata: float, abcissa: float = 30, size: int = 150,
              step: int = 200):
    path = f'media/uza/{group}/'
    for position, val in values:
        element = Image.open(path + str(val) + '.png').resize((size, size)).convert('RGBA')
        bg.paste(element, (abcissa, ordinata), element)
        draw = ImageDraw.Draw(bg)
        font = ImageFont.truetype("fonts/Ubuntu-R.ttf", size=28, encoding='UTF-8')
        draw.text((abcissa+40, ordinata-20), str(position), fill='black', font=font, anchor='ls')
        abcissa += step
    bg.save('media/uza/result.png')


imaga = Image.new('RGBA', (1000, 1000), (255, 255, 255))

paste_row(imaga, enumerate([1, 1, 1, 0, 0, 1], start=1), 'tongs', 100, step=150)
paste_row(imaga, enumerate([1, 0, 0, 2, 4, 5], start=1), 'shifters',  350, step=150)
paste_row(imaga, zip(PUMPS_IDS, [1, 0, 0, 1, 1]), 'condition', 600, abcissa=50, size=100)
paste_row(imaga, zip(PUMPS_IDS, [0, 0, 0, 0, 1]), 'pumps', 850)
