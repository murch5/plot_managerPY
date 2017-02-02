import matplotlib.gridspec as gridspec

class textAnnotate():
    def __init__(self,text,position,colorMap):
        self.text = text
        self.position = position
        self.colorMap = colorMap


    def getText(self):
        return self.text;

    def getPosition(self):
        return self.position;

    def getColorMap(self):
        return self.colorMap;

class plot():

    def __init__(self,figure, data, position, title):
        self.figure = figure
        self.data = data
        self.position = position
        self.gridSpec = []

        self.subplot = self.setupSubplot()

        #self.subplot = figure.add_subplot(position, aspect="equal")
        print(self.position[2])
        print(type(self.position[2]))
        print(int(self.position[2]))
        print(int(self.position[3]))
        #self.subplot = figure.add_subplot(self.gridSpec[int(self.position[2]),int(self.position[3])])
        self.txtAnnotations = []
        self.plotTitle = title

        self.subplot.title.set_text(self.plotTitle)

    def animate(self,i):
        return;

    def initAnimate(self, i):
        return;

    def draw(self):
        return;

    def init(self):
        return;

    def drawText(self):
        for text in self.txtAnnotations:
            self.subplot.annotate(text.getText(),text.getPosition(),color=text.getColorMap(),size=15)
        return;

    def addTextAnnotation(self,text,position,colorMap):
        newAnnotate = textAnnotate(text,position,colorMap)
        self.txtAnnotations.append(newAnnotate)
        return;

    def getData(self):
        return self.data

    def setupSubplot(self):

        self.gridSpec = gridspec.GridSpec(int(self.position[0]),int(self.position[1]))

        subplotspec = self.gridSpec.new_subplotspec([int(self.position[2]),int(self.position[3])], int(self.position[4]), int(self.position[5]))

        subplotNew = self.figure.add_subplot(subplotspec)

        return subplotNew
