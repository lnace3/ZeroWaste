import os
import xml.etree.ElementTree as ET

print 

tree = ET.parse("./images/cans/can1.xml")
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
