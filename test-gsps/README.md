# Annotations - Learn By Example

### Why use Grayscale Softcopy Presentation State
Currently, the best way to output: annotations, heatmaps, and regions of interest is by using 
*Grayscale Softcopy Presentation State* (GSPS). GSPS is a way to encode visual information about a dicom image
without actually drawing on top of the existing image data. Rather than outputting a secondary capture series, which
would be a copy of the input data but with circles drawn around regions of interest, a GSPS series can be the output,
which would store the dicom instances it references along with the simple geometry information. 

Because GSPS stores more contextually relevant information, and only the data that matters 
(not the original image data), it is extremely efficient and useful.

Nearly all dicom viewers have basic GSPS support, and are able to toggle on and off annotation. Some more advanced
viewers support new interactions like accepting/rejecting each annotation separately.   

### How to implement GSPS Annotations
At a high level, to implement GSPS Annotations, one must usually create a single new series for all of your GSPS
instances and new instance for each source instance that needs to be annotated. Feel free to use some of the convenience
functions we wrote in [gsps.py](./gsps.py). Using that code along with pydicom, its pretty easy to create each instance:
```pythonstub
file_meta = gsps.get_gsps_file_metadata()
ds_out = FileDataset("instance.pre", {}, file_meta=file_meta, preamble=b"\0" * 128)
```
Set the content description and copy details from the input data:
```pythonstub
gsps.set_content_desription(ds_out, "Presentation State for image")
gsps.set_gsps_general_study_info(ds_out,file_meta,series_instance_uid)

gsps.copy_details_from_input_dicom(ds_out, input_dicom)
gsps.set_referenced_image_info(ds_out, input_dicom.SeriesInstanceUID, input_dicom.SOPClassUID,
                               input_dicom.SOPInstanceUID)
```
Add annotation data:
```pythonstub
gsps.add_graphic_layer(ds_out, "LAYER1", "for annotation", 1)
gsps.add_displayed_area_selection(ds_out, input_dicom.Columns, input_dicom.Rows)
text_annotation = gsps.get_text_annotation(annotation_text, text_bounding_box, anchor_point)
graphic_annotation = gsps.get_circle(cir_rad, cir_pos_x, cir_pos_y)
gsps.add_graphic_annotations(ds_out, "LAYER1", [circle], [text])
```
And finally output the instance to a file:
```pythonstub
ds_out.save_as("/envoyai/output/annotated-series/image.pre")
```
