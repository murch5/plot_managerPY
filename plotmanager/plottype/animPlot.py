from plotmanager.plottype import plot


class AnimPlot(plot.Plot):

    def animate(self,i):
        return;

    def draw(self):
        return;

    def __init__(self,figure, data, plot_XML):
        plot.Plot.__init__(self,figure, data, plot_XML)
        self.frames = data
        self.position = position
        self.currFrame = data
        self.fig = figure
        self.framesPerImage = 1
        self.currFrameIndex = 0
        self.currImageIndex = 0

    def initAnimate(self, i):
        return;
