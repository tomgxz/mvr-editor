from utils.map import gdtfmap

GDTFMAP = gdtfmap()

def getFixtureFromLayer(layer):

    fixture = {}

    for line in GDTFMAP:
        if line["layer"] == layer: fixture = line

    if fixture == {}: return None
    return fixture

