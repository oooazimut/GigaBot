import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.dates as mdates
import matplotlib.patches as patches
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
    def plot_uza(data: dict):
        def get_color(value):
            return 'green' if value else 'red'

        def add_rect(point: tuple, sq_color: str, axs: Axes, name: str):
            plt.text(point[0]-0.3, point[1]+0.6, name)
            rect = patches.Circle(point, 0.25, edgecolor='black', facecolor=sq_color)
            axs.add_patch(rect)

        plt.clf()
        axes = plt.gca()
        ordinata = 7

        for title, values in data.items():
            abcissa = 1
            plt.text(abcissa, ordinata+1.5, title, fontsize=12)
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

