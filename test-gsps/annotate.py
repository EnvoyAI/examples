import gsps
import dicom
import os
from dicom.dataset import Dataset, FileDataset
from shutil import copyfile

# load annotation text parameter
with open("/envoyai/input/text-annotation", "r") as f:
    annotation_text = f.read()

# load text alignment parameter
with open("/envoyai/input/label-alignment") as f:
    left_right = f.read()

# load circle radius parameter
with open("/envoyai/input/circle-radius") as f:
    cir_rad = int(f.read())

# load circle x parameter
with open("/envoyai/input/circle-pos-x") as f:
    cir_pos_x = int(f.read())

# load circle y parameter
with open("/envoyai/input/circle-pos-y") as f:
    cir_pos_y = int(f.read())

# load the input image
input_dicom = dicom.read_file("/envoyai/input/input-image")

# create the bare output dicom
file_meta = gsps.get_gsps_file_metadata()
ds_out = FileDataset("image.pre", {}, file_meta=file_meta, preamble=b"\0" * 128)

# set the content description and general study fields
gsps.set_content_desription(ds_out, "Presentation State for image")
gsps.set_gsps_general_study_info(ds_out)

# copy patient, study, series data from input image
gsps.copy_details_from_input_dicom(ds_out, input_dicom)
gsps.set_referenced_image_info(ds_out, input_dicom.SeriesInstanceUID, input_dicom.SOPClassUID,
                               input_dicom.SOPInstanceUID)

# calculate coordinates for annotation and anchor point
input_rows = input_dicom.Rows
input_columns = input_dicom.Columns
anchor_point = [input_columns / 2, input_rows / 2]

top_left = [input_columns / 10, input_rows / 5]
bottom_right = [input_columns / 5, input_rows / 5 + 16]
if left_right == "Right":
    top_left = [input_columns - (input_columns / 10), input_rows / 5]
    bottom_right = [input_columns / 5, input_rows / 5 + 16]
anchor_point = {"AnchorPointAnnotationUnits": "PIXEL", "AnchorPoint": anchor_point, "AnchorPointVisibility": "Y"}
text_bounding_box = {"BoundingBoxAnnotationUnits": "PIXEL", "BoundingBoxTopLeftHandCorner": top_left,
                     "BoundingBoxBottomRightHandCorner": bottom_right}

# add the annotation
gsps.add_graphic_layer(ds_out, "LAYER1", "for annotation", 1)
gsps.add_displayed_area_selection(ds_out, input_dicom.Columns, input_dicom.Rows)
text = gsps.get_text_annotation(annotation_text, text_bounding_box, anchor_point)
circle = gsps.get_circle(cir_rad, cir_pos_x, cir_pos_y)
gsps.add_graphic_annotations(ds_out, "LAYER1", [circle], [text])

# write output
os.mkdir("/envoyai/output/annotated-series")
copyfile("/envoyai/input/input-image", "/envoyai/output/annotated-series/image.dcm")
ds_out.save_as("/envoyai/output/annotated-series/image.pre")
