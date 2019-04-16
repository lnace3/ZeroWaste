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

"""
label_dict = {'can': '485411e9-feee-4d83-af5b-b933c30a1bbb',
 'ms clear container': '075ee6d7-1789-4004-b173-3daf233a765e',
 'plastic container': '4d71f5b3-cf13-42d7-817c-3e57d64a2445',
 'dairy tub': '3d47b7fa-38cc-4fe0-9cb6-aec45903d09f',
 'plastic bottle': '18e07619-4045-40a6-aba2-cb005e05196c',
 'carton': '784d8e00-0ecd-450f-9b32-5a945e809c58',

 'all other non-recyclable plastics': '5e143acf-2217-4f24-b151-0a1046f8a012',
 'non-recyclable paper': '721717d1-eaaf-4721-8d64-8c05de5ecef6',
 'ms paper food holder': '8deea74d-c9e0-4574-9b4f-7a9531046dfc',
 'glass bottle': '786b3f1f-bfb3-4432-b779-fac74d132ec0',
 'glass container': 'ee097a91-4951-4649-a383-24730e13fbf8',

 'reusable drinking container': '7ed60bc1-252b-4066-8ccc-e4e7c1b59b00',
 'plastic bag': 'a6db8e31-9d6e-4113-8eaf-37127ea2ffe8',
 'wrappers': '3af28ce8-449b-4e46-84ba-d40bef4382c7',
 'ms coffee cup': 'daecb4c0-b42d-4ab7-b674-47134f9ffc78',
 'straws': '71fa5326-6f63-436b-a30b-fafd8bc15005',
 'ceremics': '82fa7276-77d4-4cd8-84ef-b212f9840219',
 'receipts': '954e0c9f-acc8-4421-b828-f888e3963766',
 'ms black utensils': '35109eb5-a78c-4a94-950d-dc856c134e30',
 'pizza box': '763d2ab8-8c5c-4dd7-b487-7f8fc4d1c5bc',
 'ms wooden utensils': '4b0dd937-4b9d-472e-ac68-3ece2d2b7998',
 'tea bag': 'd4dc6bfb-0485-44f1-9ae8-493f448be80a',
 'ms coffee lid': '49dface1-d0de-4b91-bcc5-6f69614b52ed',
 
 'soup lid': '1752cb01-6578-4b2d-a6af-49c9687a7004',
 'other trash': '1dd18a06-0278-4dba-92dc-39f22c38b153'}
"""


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
