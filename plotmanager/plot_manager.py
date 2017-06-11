import logging
logger = logging.getLogger(__name__)

import matplotlib.pyplot as plt

import factory_manager as fm

from plotmanager.plottype.DNA_track import DNAtrack
from plotmanager.plottype.cluster_map import ClusterMap
from plotmanager.plottype.contour import ContourMap
from plotmanager.plottype.forest import Forest
from plotmanager.plottype.image_stack import ImageStack
from plotmanager.plottype.pie import Pie
from plotmanager.plottype.protein_track import ProteinTrack
from plotmanager.plottype.scatter import Scatter
from plotmanager.plottype.survival import Survival
from plotmanager.plottype.swarm_interval import SwarmInterval
from plotmanager.plottype.track import Track
from plotmanager.plottype.variant_track import VariantTrack
from plotmanager.plottype.venn import Venn
from plotmanager.plottype.violin import Violin
from plotmanager.plottype.peristalsis import ZbPeristalsis
from plotmanager.plottype.image import Image

import matplotlib.gridspec as gridspec
import data_manager.datatypes as dt

plt.rcParams['animation.ffmpeg_path'] = '/ffmpeg/bin/ffmpeg'
plt.rcParams['image.cmap'] = 'magma'

chartTypes = {"violin": Violin, "pie": Pie, "scatter": Scatter, "forest": Forest, "contour": ContourMap,
              "imageStack": ImageStack, "zbperistalsis": ZbPeristalsis, "image": Image, "swarmInterval": SwarmInterval,
              "survival": Survival, "track": Track, "proteinTrack": ProteinTrack, "DNAtrack": DNAtrack,
              "variantTrack": VariantTrack, "clusterMap": ClusterMap, "venn": Venn}

class PlotManager(fm.FactoryStack):

    def setup_figure(self):

        if self.engine == "matplotlib":
            logger.debug("--- Plot manager name: matplotlib")
            self.figure = plt.figure(figsize=(11, 9))
            #self.figure.canvas.set_window_title(self.name)
        else:
            logger.debug("--- Plot manager name: seaborn")
            self.figure = None

        row = self.plotsize.get("row")
        col = self.plotsize.get("col")

        self.grid_spec = gridspec.GridSpec(int(row), int(col))


    def onResize(self, event):
        print("Resizing...")
        self.draw_plots()
        self.figure.canvas.flush_events()
        return

    def add_plot(self,data,type,plot_settings):

        new_plot = chartTypes[type](self.figure,data,plot_settings)
        new_plot.set_gridspec(self.grid_spec)
        new_plot.setup_subplot()
        new_plot.initialize()

        self.plot_list.append(new_plot)


    def get_figure(self):
        return self.figure

    def draw_plots(self):

        for plot in self.plot_list:
            plot.draw()

        return

    def show_plots(self):
        plt.show()

    def set_gridspec(self,gridspec):
        self.gridspec = gridspec

    def initialize(self):
        pass




