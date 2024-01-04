from xml.dom import minidom,Node
import zipfile, os, shutil, glob

from settings import PARENTDIR,NAME
from fixturemap import getFixtureFromLayer,getGDTFFromName

def getChildNodes(node,selector): return list(filter(lambda x: x.nodeType == Node.ELEMENT_NODE and x.tagName == selector, node.childNodes))
def getChildNode(node,selector): return getChildNodes(node,selector)[0]

CONVERT_FROM_ZIP = True
CONVERT_TO_ZIP = True

MVR_BASE_DIR = f".\\mvr_files"
MVR_NAME = f"Programming Challenge 1"

BASE_DIR = f"{MVR_BASE_DIR}\\tmp"

layerNames = [
    "Chauvet Ovation CYC 1 FC",
    "Chauvet Ovation CYC 3 FC",
    "Clay Paky Sharpy X Frame",
    "Clay Paky Stormy CC",
    "Elation DTW Blinder 700 IP",
    "ETC Source 4 LED",
    "Generic 2-Cell Blinder",
    "Generic RGBAW LED Bulb",
    "GLP Impression FR10 Bar",
    "GLP Impression X4 Bar 10",
    "GLP JDC1 Strobe",
    "Martin MAC Aura PXL",
    "Martin MAC Aura XB",
    "Martin MAC Ultra Performance",
    "Martin MAC Viper Performance",
    "Martin VDO Sceptron 10, 1000mm",
    "Mole-Richardson 24kW Molequartz Moleno Molepar",
    "Portman P1 Evo",
    "Prolight StudioCob PlusFC",
    "Robe HolyPATT"
    "Robe MolyPATT",
    "Robe Robin BMFL FollowSpot LT",
    "Robe Robin BMFL WashBeam",
    "Robe Robin ColorStrobe",
    "Robe Robin Esprite",
    "Robe Robin Forte",
    "Robe Robin LEDBeam 150",
    "Robe Robin LEDBeam 350",
    "Robe Robin MegaPointe",
    "Robe Robin Painte",
    "Robe Robin Spiider",
    "Robe Robin Tarrantula",
    "Varilite VL2600 Profile"
]

used_gdtf_files = []

if CONVERT_FROM_ZIP:

    with zipfile.ZipFile(os.path.abspath(f"{MVR_BASE_DIR}\\{MVR_NAME}.mvr"), 'r') as zip_ref:
        zip_ref.extractall(BASE_DIR)


# FORMAT .XML FILE
#region

xdom = minidom.parse(f"{BASE_DIR}\\GeneralSceneDescription.xml")
xdoc = xdom.documentElement

# get layers
scene = getChildNode(xdoc, "Scene")
layersWrapper = getChildNode(scene, "Layers")
layers = list(filter(lambda x: x.getAttribute("name") in layerNames, getChildNodes(layersWrapper, "Layer")))

for layer in layers:

    iter = 1
    newfixture = layer.getAttribute("name")

    childList = getChildNode(layer,"ChildList")
    fixtures = getChildNodes(childList,"Fixture")

    for fixture in fixtures:

        fixtureDict = getFixtureFromLayer(newfixture)
        if fixtureDict == None: continue

        gdtf = getGDTFFromName(fixtureDict["Fixture"])

        if gdtf not in used_gdtf_files and gdtf is not None: used_gdtf_files.append(gdtf)

        fixture.setAttribute("name",f"{newfixture} {iter}")

        getChildNode(fixture,"GDTFSpec").firstChild.replaceWholeText(gdtf)
        getChildNode(fixture,"GDTFMode").firstChild.replaceWholeText(fixtureDict["DMX Mode"])

        iter += 1

content = "\n".join(line for line in xdoc.toprettyxml(indent="  ").split("\n") if line.strip())

# Save the MVR GeneralScceneDescription.xml file
with open(f"{BASE_DIR}\\GeneralSceneDescription.xml","w") as file: 
    file.write(content)
    file.close()

#endregion

# ADD GDTF FILES

for gdtf in used_gdtf_files: shutil.copy(f".\\gdtf_files\\{gdtf}", BASE_DIR)

# CONVERT INTO ZIP

zipf = zipfile.ZipFile(f'{MVR_BASE_DIR}\\{MVR_NAME}_formatted.mvr', 'w', zipfile.ZIP_DEFLATED)

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(BASE_DIR, '.')))
        
zipf.close()

# REMOVE TEMP DIRECTORY

for file in glob.glob(f"{BASE_DIR}\\*"):  os.remove(file)
os.rmdir(BASE_DIR)