import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.dates as mdates


class PlotService:
    @staticmethod
    def plot_current_pressures(values: list):
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

        output_image_path = 'media/current_pressures.png'
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
