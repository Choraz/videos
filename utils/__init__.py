from matplotlib.font_manager import fontManager
from matplotlib import style
from matplotlib import pyplot as plt

from pathlib import Path


def setup_xkcd():
    font_folder = Path(__file__).parents[1].joinpath("fonts")
    fontManager.addfont(font_folder.joinpath("xkcd", "xkcd-Regular.otf"))
    fontManager.addfont(font_folder.joinpath("xkcd_scripts", "xkcd-script.ttf"))
    fontManager.addfont(font_folder.joinpath("humor_sans", "Humor Sans.ttf"))
    fontManager.addfont(font_folder.joinpath("comic_neue", "ComicNeue-Regular.ttf"))

    style.use("fivethirtyeight")
    plt.xkcd()
