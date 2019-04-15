from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region, Image, ImageRegionCreateEntry, ImageRegionCreateBatch

ENDPOINT = ENDPOINT

# Replace with a valid key
training_key = "<<training_key>>"
prediction_key = "<<prediction_key>>"


trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

project = trainer.get_project('<<project_id>>')


## Create label tabs
import pandas as pd
df = pd.read_csv('test_labels.csv')

label_list = df['class'].unique()
label_tags = []

for label in label_list:
    label_tags.append(trainer.create_tag(project.id, label).id)

label_dict = dict(zip(label_list, label_tags))
#label_dict['can'].id
#trainer.get_tags(project.id)


# Update this with the path to where you downloaded the images.
base_image_url = "<<image path>>"

# Go through the data table above and create the images
print ("Adding images...")
tagged_images_with_regions = []


for _, row in df1.iterrows():
    regions = [Region(tag_id = label_dict[row['class']].id, 
    left = row.left,
    top = row.top, 
    width = row.width,
    height = row.height)]

    with open(base_image_url + row.filename, mode='rb') as image_contents:
        tagged_images_with_regions.append(ImageFileCreateEntry(name = row.filename, 
        contents=image_contents.read(),
        regions = regions))


## UPLOAD IMAGES TO ENDPOITN CUSTOMVISON
upload_result = trainer.create_images_from_files(project.id, images=tagged_images_with_regions)
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)
