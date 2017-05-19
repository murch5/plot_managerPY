from plotmanager.plottype import plot


class animPlot(plot.plot):

    def animate(self,i):
        return;

    def draw(self):
        return;

    def __init__(self,figure, data, position,title="",plotArgs=[],annotate=[]):
        plot.plot.__init__(self,figure, data, position,title,plotArgs,annotate)
        self.frames = data
        self.position = position
        self.currFrame = data
        self.fig = figure
        self.framesPerImage = 1
        self.currFrameIndex = 0
        self.currImageIndex = 0

    def initAnimate(self, i):
        return;