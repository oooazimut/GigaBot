from typing import Iterable, List, Tuple

import matplotlib.dates as mdates
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from PIL import Image, ImageDraw, ImageFont


class PlotService:
    @staticmethod
    def plot_current_pump(values: list, out_name: str):
        image_path = "media/pumproom.png"
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis("off")
        abscissa = 500

        for v in values:
            ax.text(
                abscissa,
                330,
                v,
                fontsize=9,
                color="green",
                bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
            )
            abscissa += 150

        plt.title(out_name, fontsize=16)
        output_image_path = f"media/{out_name}.png"
        plt.savefig(output_image_path, bbox_inches="tight", pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_pressures_by_date(data: dict):
        colors = ("b", "g", "r", "c", "m")
        color_index = 0
        output_image_path = "media/"

        plt.clf()
        for pump, values in data.items():
            dates, pressures = zip(*values)
            plt.plot(dates, pressures, label=pump, color=colors[color_index])
            color_index += 1
            output_image_path += pump

        plt.xlabel("Время")
        plt.ylabel("Давление")
        date_format = mdates.DateFormatter("%H:%M")
        plt.gca().xaxis.set_major_formatter(date_format)
        current_date = dates[0].date()
        plt.title(current_date)
        plt.legend()
        output_image_path += ".png"
        plt.savefig(output_image_path)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_current_gas_level_prob(values: dict):
        image_path = "media/testroom.png"
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis("off")

        ax.text(
            630,
            290,
            "№3.8: " + str(values.get("3.8")),
            fontsize=9,
            color="green",
            bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
        )
        ax.text(
            160,
            700,
            "№4.1: " + str(values.get("4.1")),
            fontsize=9,
            color="green",
            bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
        )
        output_image_path = "media/current_gas_level_prob.png"
        plt.savefig(output_image_path, bbox_inches="tight", pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_current_gas_level_pumps(values: dict):
        image_path = "media/pumproom.png"
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis("off")

        ax.text(
            550,
            280,
            "№5.1: " + str(values.get("5.1")),
            fontsize=9,
            color="green",
            bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
        )
        ax.text(
            930,
            280,
            "№5.2: " + str(values.get("5.2")),
            fontsize=9,
            color="green",
            bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
        )
        ax.text(
            930,
            1170,
            "№5.3: " + str(values.get("5.3")),
            fontsize=9,
            color="green",
            bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
        )
        ax.text(
            60,
            530,
            "№5.4: " + str(values.get("5.4")),
            fontsize=9,
            color="green",
            bbox=dict(facecolor="black", alpha=0.1, boxstyle="round"),
        )
        output_image_path = "media/current_gas_level_pump.png"
        plt.savefig(output_image_path, bbox_inches="tight", pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_gas_level_date(data: dict):
        colors = ("b", "g", "r", "c", "m", "y")
        color_index = 0
        output_image_path = "media/"

        plt.clf()
        for g_sens, values in data.items():
            dates, g_levels = zip(*values)
            plt.plot(dates, g_levels, label=g_sens, color=colors[color_index])
            color_index += 1
            output_image_path += g_sens

        plt.xlabel("Время")
        plt.ylabel("Показания")
        date_format = mdates.DateFormatter("%H:%M")
        plt.gca().xaxis.set_major_formatter(date_format)
        current_date = dates[0].date()
        plt.title(current_date)
        plt.legend()
        output_image_path += ".png"
        plt.savefig(output_image_path)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_uza(data: dict):
        def get_color(value):
            return "green" if value else "red"

        def add_rect(point: tuple[float, float], sq_color: str, axs: Axes, name: str):
            plt.text(point[0] - 0.3, point[1] + 0.6, name)
            rect = patches.Circle(point, 0.25, edgecolor="black", facecolor=sq_color)
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

        axes.set_aspect("equal")
        axes.set_ylim(0, 10)
        axes.set_xlim(0, 10)
        axes.axis("off")
        plt.title("УЗА и насосы", fontsize=16)

        image_path = "media/uzas.png"
        plt.savefig(image_path)
        plt.close()

        return image_path


class ImageService:
    _font_cache = {}
    _image_cache = {}

    @staticmethod
    def _get_font(font_path: str, font_size: int) -> ImageFont.FreeTypeFont:
        key = (font_path, font_size)
        if key not in ImageService._font_cache:
            ImageService._font_cache[key] = ImageFont.truetype(
                font_path, size=font_size, encoding="UTF-8"
            )
        return ImageService._font_cache[key]

    @staticmethod
    async def paste_row(
        bg: Image.Image,
        values: Iterable,
        group: str,
        ordinata: int,
        abcissa: int = 30,
        size: int = 150,
        step: int = 200,
    ):

        draw = ImageDraw.Draw(bg)
        font = ImageService._get_font("fonts/Ubuntu-R.ttf", font_size=28)
        path = f"media/uza/{group}/"

        image_cache = ImageService._image_cache.setdefault(group, {})

        for position, val in values:
            if val not in image_cache:
                element_path = f"{path}{str(val)}.png"
                element = Image.open(element_path).resize((size, size)).convert("RGBA")
                image_cache[val] = element
            element = image_cache[val]

            print('abcissa - ', type(abcissa), 'step - ', type(step), 'position - ', type(position))
            position_tuple = (abcissa + step, ordinata)
            bg.paste(element, position_tuple, element)
            draw.text(
                (position_tuple[0] + 40, position_tuple[1] - 40),
                str(position),
                fill="black",
                font=font,
            )

        result_path = "media/uza/result.png"
        bg.save(result_path, optimize=True)
        return result_path

    @staticmethod
    async def print_text(
        img: Image.Image,
        some_text: List[str],
        point: Tuple[float, float],
        step: int = 200,
        fontsize=33,
    ):
        draw = ImageDraw.Draw(img)
        font = ImageService._get_font("fonts/Ubuntu-R.ttf", font_size=fontsize)
        for item in some_text:
            draw.text(point, item, fill="black", font=font)
            point = (point[0] + step, point[1])

        result_path = "media/uza/result.png"
        img.save(result_path, optimize=True)

        return result_path
