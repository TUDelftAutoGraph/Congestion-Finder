class Road:
    roadNumber = None
    bpsDetectors = None
    spaceToSpaceIndex = None

    def __init__(self, roadNumber):
        """
        :rtype: Road
        :param roadNumber: int
        """
        self.roadNumber = roadNumber
        self.bpsDetectors = set()
        self.spaceToSpaceIndex = dict()

    def addBPSDetector(self, bpsDetector):
        self.bpsDetectors.add(bpsDetector)

    def indexDetectorSpaces(self):
        spaceSet = set()
        for bpsDetector in self.bpsDetectors:
            spaceSet.add(bpsDetector.getMeter())
        sortedSpaceSet = sorted(spaceSet)
        for spaceIndex in range(len(sortedSpaceSet)):
            self.spaceToSpaceIndex[sortedSpaceSet[spaceIndex]] = spaceIndex

    def getBPSDetectors(self):
        return self.bpsDetectors

    def getSpaceToSpaceIndex(self):
        return self.spaceToSpaceIndex

    @property
    def __str__(self):
        stringTemplate = "roadNumber: {} | len(bpsDetectors): {} | len(spaceToSpaceIndex): {}"
        templateElements = [self.roadNumber, len(self.bpsDetectors), len(self.spaceToSpaceIndex)]
        return stringTemplate.format(templateElements)
