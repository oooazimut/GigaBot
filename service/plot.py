import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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
