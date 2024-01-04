from pathlib import Path
from xml.dom import minidom

import os

from settings import PARENTDIR,NAME

BASE_DIR = f".\\{NAME}_mvr"



# Clear and recreate the base directory for the mvr file
if not os.path.isdir(BASE_DIR): os.mkdir(BASE_DIR)




# Generate the GeneralScceneDescription.xml file
root = minidom.Document()

#root.setAttribute("version", "1.0")
#root.setAttribute("encoding", "UTF-8")
#root.setAttribute("standalone", "no")

gds = root.createElement("GeneralSceneDescription")
gds.setAttribute("verMajor", "1")
gds.setAttribute("verMinor", "4")
root.appendChild(gds)

userDataRoot = root.createElement("UserData")
gds.appendChild(userDataRoot)

sceneRoot = root.createElement("Scene")
gds.appendChild(sceneRoot)

layersRoot = root.createElement("Layers")
sceneRoot.appendChild(layersRoot)

layer = root.createElement("Layer")
layer.setAttribute("name","FixtureLayer 1")
layersRoot.appendChild(layer)

layer_childList = root.createElement("ChildList")
layer.appendChild(layer_childList)

fixture = root.createElement("Fixture")
fixture.setAttribute("name","Blinder 1")
layer_childList.appendChild(fixture)

classing = root.createElement("Classing")
fixture.appendChild(classing)

gdtfspec = root.createElement("GDTFSpec")
gdtfspec.appendChild(root.createTextNode("Generic@Dimmer"))
fixture.appendChild(gdtfspec)

gdtfmode = root.createElement("GDTFMode")
gdtfmode.appendChild(root.createTextNode("Mode 0"))
fixture.appendChild(gdtfmode)

addresses = root.createElement("Addresses")
address = root.createElement("Address")
address.setAttribute("break","0")
address.appendChild(root.createTextNode("768"))
addresses.appendChild(address)
fixture.appendChild(addresses)

fid = root.createElement("FixtureID")
fid.appendChild(root.createTextNode("101"))
fixture.appendChild(fid)

unit = root.createElement("UnitNumber")
unit.appendChild(root.createTextNode("0"))
fixture.appendChild(unit)

typeid = root.createElement("FixtureTypeId")
typeid.appendChild(root.createTextNode("0"))
fixture.appendChild(typeid)

customid = root.createElement("CustomId")
customid.appendChild(root.createTextNode("0"))
fixture.appendChild(customid)

color = root.createElement("Color")
color.appendChild(root.createTextNode("0.312712,0.329008,100.000000"))
fixture.appendChild(color)

shadows = root.createElement("CastShadow")
shadows.appendChild(root.createTextNode("false"))
fixture.appendChild(shadows)

mappings = root.createElement("Mappings")
fixture.appendChild(mappings)



auxData = root.createElement("AUXData")
sceneRoot.appendChild(auxData)

content = root.toprettyxml(indent="  ")

# Save the MVR GeneralScceneDescription.xml file
with open(f"{BASE_DIR}\\{NAME} Fixtures.xml","w") as file: file.write(content)