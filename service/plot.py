from typing import Iterable

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.dates as mdates
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
from matplotlib.axes import Axes


class PlotService:
    @staticmethod
    def plot_current_pump(values: list, out_name: str):
        image_path = 'media/pumproom.png'
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')
        abscissa = 500

        for v in values:
            ax.text(abscissa, 330, v, fontsize=9, color='green',
                    bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
            abscissa += 150

        plt.title(out_name, fontsize=16)
        output_image_path = f'media/{out_name}.png'
        plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_pressures_by_date(data: dict):
        colors = ('b', 'g', 'r', 'c', 'm')
        color_index = 0
        output_image_path = 'media/'

        plt.clf()
        for pump, values in data.items():
            dates, pressures = zip(*values)
            plt.plot(dates, pressures, label=pump, color=colors[color_index])
            color_index += 1
            output_image_path += pump

        plt.xlabel('Время')
        plt.ylabel('Давление')
        date_format = mdates.DateFormatter('%H:%M')
        plt.gca().xaxis.set_major_formatter(date_format)
        current_date = dates[0].date()
        plt.title(current_date)
        plt.legend()
        output_image_path += '.png'
        plt.savefig(output_image_path)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_current_gas_level_prob(values: list):
        image_path = 'media/testroom.png'
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')

        ax.text(630, 290, "№3.8: " + str(values[0]), fontsize=9, color='green',
                bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(160, 700, "№4.1: " + str(values[1]), fontsize=9, color='green',
                bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        output_image_path = 'media/current_gas_level_prob.png'
        plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_current_gas_level_pumps(values: list):
        image_path = 'media/pumproom.png'
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')

        ax.text(550, 280, "№5.1: " + str(values[0]), fontsize=9, color='green',
                bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(930, 280, "№5.2: " + str(values[1]), fontsize=9, color='green',
                bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(930, 1170, "№5.3: " + str(values[2]), fontsize=9, color='green',
                bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(60, 530, "№5.4: " + str(values[3]), fontsize=9, color='green',
                bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        output_image_path = 'media/current_gas_level_pump.png'
        plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_gas_level_date(data: dict):
        colors = ('b', 'g', 'r', 'c', 'm', 'y')
        color_index = 0
        output_image_path = 'media/'

        plt.clf()
        for g_sens, values in data.items():
            dates, g_levels = zip(*values)
            plt.plot(dates, g_levels, label=g_sens, color=colors[color_index])
            color_index += 1
            output_image_path += g_sens

        plt.xlabel('Время')
        plt.ylabel('Показания')
        date_format = mdates.DateFormatter('%H:%M')
        plt.gca().xaxis.set_major_formatter(date_format)
        current_date = dates[0].date()
        plt.title(current_date)
        plt.legend()
        output_image_path += '.png'
        plt.savefig(output_image_path)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_uza(data: dict):
        def get_color(value):
            return 'green' if value else 'red'

        def add_rect(point: tuple[float, float], sq_color: str, axs: Axes, name: str):
            plt.text(point[0] - 0.3, point[1] + 0.6, name)
            rect = patches.Circle(point, 0.25, edgecolor='black', facecolor=sq_color)
            axs.add_patch(rect)

        plt.clf()
        axes = plt.gca()
        ordinata = 7

        for title, values in data.items():
            abcissa = 1
            plt.text(abcissa, ordinata + 1.5, title, fontsize=12)
            for pump, condition in values:
                color = get_color(condition)
                add_rect((abcissa, ordinata), color, axes, pump)
                abcissa += 1.5
            ordinata -= 3

        axes.set_aspect('equal')
        axes.set_ylim(0, 10)
        axes.set_xlim(0, 10)
        axes.axis('off')
        plt.title('УЗА и насосы', fontsize=16)

        image_path = 'media/uzas.png'
        plt.savefig(image_path)
        plt.close()

        return image_path


class ImageService:
    @staticmethod
    def paste_row(bg: Image.Image, values: Iterable, group: str, ordinata: float, abcissa: float = 30, size: int = 150,
                  step: int = 200):
        path = f'media/uza/{group}/'
        draw = ImageDraw.Draw(bg)
        font = ImageFont.truetype("fonts/Ubuntu-R.ttf", size=28, encoding='UTF-8')

        for position, val in values:
            element = Image.open(path + str(val) + '.png').resize((size, size)).convert('RGBA')
            bg.paste(element, (abcissa, ordinata), element)
            draw.text((abcissa + 40, ordinata - 40), str(position), fill='black', font=font)
            abcissa += step
        result_path = 'media/uza/result.png'
        bg.save(result_path)
        return result_path

    @staticmethod
    def print_text(img: Image.Image, some_text: list[str], point: list[float, float], step: int = 200, fontsize=33):
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("fonts/Ubuntu-R.ttf", size=fontsize, encoding='UTF-8')
        for item in some_text:
            draw.text(point, item, fill='black', font=font)
            point[0] += step
        img.save('media/uza/result.png')


