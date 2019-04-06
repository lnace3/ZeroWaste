#%%
import os
import glob
import shutil

def remove_ext(list_of_pathnames):
    """
    removes the extension from each file name so we can identify and remove the jpgs that do not have a corresponding xml file
    """
    
    return [os.path.splitext(filename)[0] for filename in list_of_pathnames]

path = "/home/redne/ZeroWaste IoT/images/lunch/lunch07/lunch07"
path_to_remove: "/home/redne/ZeroWaste IoT/images/images_to_remove"


jpg_list_ext = glob.glob(path+"/*.jpg")
xml_list_ext = glob.glob(path+"/*.xml")

jpg_list = remove_ext(jpg_list_ext)
xml_list = remove_ext(xml_list_ext)

for filename in jpg_list:
    if filename not in xml_list:
        print("removing: ", filename)
        # move image to another path
        shutil.move((filename + ".jpg"), "/home/redne/ZeroWaste IoT/images/images_to_remove")


	
#####
"""
The remaining section in WIP to develop a way to pull all xml to check for spelling, reporting for distribution, ect. 
"""
#%%

import os
import xml.etree.ElementTree as ET

tree = ET.parse("~/ZeroWaste IoT/images/lunch/lunch07/L07_1/L07_01/lunch07_1.xml")
root = tree.getroot()

print(ET.tostring(root, encoding='utf8').decode('utf8'))



"""
<?xml version='1.0' encoding='utf8'?>
<annotation verified="yes">
	<folder>cans</folder>
	<filename>can1.jpg</filename>
	<path>ZeroWaste IoT/images/cans/can1.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>1920</width>
		<height>1080</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>cans</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>904</xmin>
			<ymin>201</ymin>
			<xmax>1187</xmax>
			<ymax>583</ymax>
		</bndbox>
	</object>
</annotation>
"""


import os, os.path

# simple version for working with CWD
print len([name for name in os.listdir('.') if os.path.isfile(name)])

# path joining version for other paths
DIR = '/tmp'
print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
