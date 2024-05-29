import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.dates as mdates


class PlotService:
    @staticmethod
    def plot_current_pump(values: list, out_name: str):
        image_path = 'media/pumproom.png'
        img = mpimg.imread(image_path)
        values.reverse()
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')
        ax.text(550, 280, "№5.1: "+str(values[0]), fontsize=9, color='green',bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(930, 280, "№5.2: "+str(values[1]), fontsize=9, color='green', bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(930, 1170, "№5.3: "+str(values[2]), fontsize=9, color='green', bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(60, 530, "№5.4: "+str(values[3]), fontsize=9, color='green', bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        output_image_path = f'media/current_{out_name}.png'
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
    def plot_current_gas_level_prob(values: list, out_name: str):
        image_path = 'media/testroom.png'
        img = mpimg.imread(image_path)

        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')

        ax.text(630, 290, "№3.8: "+str(values[0]), fontsize=9, color='green',
        bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        ax.text(160, 700, "№4.1: "+str(values[1]), fontsize=9, color='green',
        bbox=dict(facecolor='black', alpha=0.1, boxstyle='round'))
        output_image_path = 'media/current_gas_level.png'
        plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=300)
        plt.close()

        return output_image_path

    @staticmethod
    def plot_gas_level_date(data: dict):
        colors = ('b', 'g', 'r', 'c', 'm')
        color_index = 0
        output_image_path = 'media/'

        plt.clf()
        for g_sens, values in data.items():
            dates, g_levels = zip(*values)
            plt.plot(dates, g_levels, label=g_sens, color=colors[color_index])
            color_index += 1
            output_image_path += g_sens

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