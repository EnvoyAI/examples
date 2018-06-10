from datetime import datetime
import dicom
from dicom.dataset import Dataset, DataElement, Tag
from dicom.sequence import Sequence


def get_gsps_file_metadata():
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.11.1"  # Grayscale Softcopy Presentation State Storage SOP Class
    file_meta.MediaStorageSOPInstanceUID = dicom.UID.generate_uid()
    file_meta.ImplementationClassUID = "1.2.276.0.7230010.3.0.3.4.1"
    file_meta.ImplementationVersionName = "GSPS_DEMO"
    return file_meta


def set_gsps_general_study_info(dataset, file_meta, series_instance_uid):
    dataset.SOPClassUID = file_meta.MediaStorageSOPClassUID
    dataset.SOPInstanceUID = file_meta.MediaStorageSOPInstanceUID
    dataset.AccessionNumber = ""
    dataset.Modality = "PR"  # Presentation State
    dataset.Manufacturer = ""
    dataset.SeriesDescription = "GSPS demo"
    dataset.SeriesInstanceUID = series_instance_uid
    dataset.SeriesNumber = 1
    dataset.InstanceNumber = 1
    dataset.ContentLabel = "GSPS_demo"
    dataset.PresentationCreationDate = datetime.now().date().strftime("%Y%m%d")
    dataset.PresentationCreationTime = datetime.now().time().strftime("%H%M%S")
    dataset.ContentCreatorName = "GSPS^demo"
    dataset.PresentationLUTShape = "IDENTITY"


def set_content_desription(dataset, description):
    dataset.ContentDescription = description


def set_referenced_image_info(dataset, series_instance_uid, sop_class_uid, sop_instance_uid):
    referenced_series_dataset = Dataset()
    referenced_series_dataset.SeriesInstanceUID = series_instance_uid
    referenced_image_dataset = Dataset()
    referenced_image_dataset.ReferencedSOPClassUID = sop_class_uid
    referenced_image_dataset.ReferencedSOPInstanceUID = sop_instance_uid
    referenced_series_dataset.ReferencedImages = Sequence([referenced_image_dataset])
    dataset.ReferencedSeries = Sequence([referenced_series_dataset])


def copy_details_from_input_dicom(dicom, input_dicom):
    data_elements = ['PatientID',
                     'PatientBirthDate',
                     'StudyInstanceUID',
                     'StudyDescription',
                     'PatientName',
                     'PatientSex',
                     'StudyID',
                     'StudyDate',
                     'StudyTime',
                     'ReferringPhysicianName',
                     'AccessionNumber']
    for de in data_elements:
        if input_dicom.__contains__(de):
            dicom.add(input_dicom.data_element(de))


def add_graphic_annotation(dicom, group_number, layer, type, origin, rows, columns, data):
    dicom[group_number, 0x1001] = DataElement(Tag(group_number, 0x1001), "CS", layer)
    dicom[group_number, 0x40] = DataElement(Tag(group_number, 0x40), "CS", type)
    dicom[group_number, 0x50] = DataElement(Tag(group_number, 0x50), "SS", origin)
    dicom[group_number, 0x10] = DataElement(Tag(group_number, 0x10), "US", rows)
    dicom[group_number, 0x11] = DataElement(Tag(group_number, 0x11), "US", columns)
    dicom[group_number, 0x100] = DataElement(Tag(group_number, 0x100), "US", 1)  # OverlayBitsAllocated
    dicom[group_number, 0x102] = DataElement(Tag(group_number, 0x102), "US", 0)  # OverlayBitPosition
    dicom[group_number, 0x3000] = DataElement(Tag(group_number, 0x3000), "OW", data)


def add_graphic_layer(dicom, layer_name, layer_description, layer_order):
    ds_graphic_layer = Dataset()
    ds_graphic_layer.GraphicLayer = layer_name
    ds_graphic_layer.GraphicLayerOrder = layer_order
    ds_graphic_layer.GraphicLayerRecommendedDisplayGrayscaleValue = 65535
    ds_graphic_layer.GraphicLayerDescription = layer_description
    if dicom.get("GraphicLayers"):
        dicom.GraphicLayers.append(ds_graphic_layer)
    else:
        dicom.GraphicLayers = Sequence([ds_graphic_layer])


def add_displayed_area_selection(dicom, columns, rows):
    ds_displayed_area_selection = Dataset()
    ds_displayed_area_selection.DisplayedAreaTopLeftHandCorner = [1, 1]
    ds_displayed_area_selection.DisplayedAreaBottomRightHandCorner = [columns, rows]
    ds_displayed_area_selection.PresentationSizeMode = "SCALE TO FIT"
    ds_displayed_area_selection.PresentationPixelAspectRatio = [1, 1]
    dicom.DisplayedAreaSelections = Sequence([ds_displayed_area_selection])


def add_presentation_lut(dicom):  # LUT - Look Up Table for colors
    ds_presentation_lut = Dataset()
    ds_presentation_lut.LUTDescriptor = [256, 0, 12]
    ds_presentation_lut.data_element("LUTDescriptor").VR = "US"
    ds_presentation_lut.LUTExplanation = "LUT with gamma 1.0, descriptor 256/0/12"
    ds_presentation_lut.LUTData = [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 273,
                                   289, 305, 321, 337, 353, 369, 385, 401, 417, 433, 449, 465, 481, 497, 513, 529, 546,
                                   562, 578, 594, 610, 626, 642, 658, 674, 690, 706, 722, 738, 754, 770, 786, 802, 819,
                                   835, 851, 867, 883, 899, 915, 931, 947, 963, 979, 995, 1011, 1027, 1043, 1059, 1075,
                                   1092, 1108, 1124, 1140, 1156, 1172, 1188, 1204, 1220, 1236, 1252, 1268, 1284, 1300,
                                   1316, 1332, 1348, 1365, 1381, 1397, 1413, 1429, 1445, 1461, 1477, 1493, 1509, 1525,
                                   1541, 1557, 1573, 1589, 1605, 1621, 1638, 1654, 1670, 1686, 1702, 1718, 1734, 1750,
                                   1766, 1782, 1798, 1814, 1830, 1846, 1862, 1878, 1894, 1911, 1927, 1943, 1959, 1975,
                                   1991, 2007, 2023, 2039, 2055, 2071, 2087, 2103, 2119, 2135, 2151, 2167, 2184, 2200,
                                   2216, 2232, 2248, 2264, 2280, 2296, 2312, 2328, 2344, 2360, 2376, 2392, 2408, 2424,
                                   2440, 2457, 2473, 2489, 2505, 2521, 2537, 2553, 2569, 2585, 2601, 2617, 2633, 2649,
                                   2665, 2681, 2697, 2713, 2730, 2746, 2762, 2778, 2794, 2810, 2826, 2842, 2858, 2874,
                                   2890, 2906, 2922, 2938, 2954, 2970, 2986, 3003, 3019, 3035, 3051, 3067, 3083, 3099,
                                   3115, 3131, 3147, 3163, 3179, 3195, 3211, 3227, 3243, 3259, 3276, 3292, 3308, 3324,
                                   3340, 3356, 3372, 3388, 3404, 3420, 3436, 3452, 3468, 3484, 3500, 3516, 3532, 3549,
                                   3565, 3581, 3597, 3613, 3629, 3645, 3661, 3677, 3693, 3709, 3725, 3741, 3757, 3773,
                                   3789, 3805, 3822, 3838, 3854, 3870, 3886, 3902, 3918, 3934, 3950, 3966, 3982, 3998,
                                   4014, 4030, 4046, 4062, 4078, 4095]
    ds_presentation_lut.data_element("LUTData").VR = "US"
    dicom.PresentationLUTSequence = Sequence([ds_presentation_lut])


def get_text_annotation(text, bounding_box, anchor_point=None):
    ds_text_object = Dataset()
    ds_text_object.BoundingBoxAnnotationUnits = bounding_box["BoundingBoxAnnotationUnits"]
    ds_text_object.UnformattedTextValue = text
    ds_text_object.BoundingBoxTopLeftHandCorner = bounding_box["BoundingBoxTopLeftHandCorner"]
    ds_text_object.BoundingBoxBottomRightHandCorner = bounding_box["BoundingBoxBottomRightHandCorner"]
    ds_text_object.BoundingBoxTextHorizontalJustification = "LEFT"

    if anchor_point is not None:
        ds_text_object.AnchorPointAnnotationUnits = anchor_point["AnchorPointAnnotationUnits"]
        ds_text_object.AnchorPoint = anchor_point["AnchorPoint"]
        ds_text_object.AnchorPointVisibility = anchor_point["AnchorPointVisibility"]
    return ds_text_object


def get_circle(cir_rad, cir_pos_x, cir_pos_y):
    ds_cir_object = Dataset()
    ds_cir_object.GraphicAnnotationUnits = "PIXEL"
    ds_cir_object.GraphicDimensions = 2
    ds_cir_object.NumberOfGraphicPoints = 2
    ds_cir_object.GraphicData = [
        cir_pos_x,  # x coordinate of middle of circle
        cir_pos_y,  # y coordinate of middle of circle
        cir_pos_x,  # x coordinate of point on circumference
        cir_pos_y + cir_rad]  # y coordinate of point on circumference
    ds_cir_object.GraphicType = "CIRCLE"
    ds_cir_object.GraphicFilled = "N"
    return ds_cir_object


def get_graphic_annotation(sop_class, sop_instance_uid, layer_name, graphic_objects, text_objects):
    ds_graphic_annotation = Dataset()
    referenced_sequence_dataset = Dataset()
    referenced_sequence_dataset.ReferencedSOPClassUID = sop_class
    referenced_sequence_dataset.ReferencedSOPInstanceUID = sop_instance_uid
    ds_graphic_annotation.ReferencedImageSequence = Sequence([referenced_sequence_dataset])
    ds_graphic_annotation.GraphicLayer = layer_name
    if graphic_objects is not None and len(graphic_objects)>0:
        ds_graphic_annotation.GraphicObjects = Sequence(graphic_objects)
    if text_objects is not None and len(text_objects) > 0:
        ds_graphic_annotation.TextObjects = Sequence(text_objects)
    return ds_graphic_annotation


def add_graphic_annotations(dicom, graphic_annotations):
    dicom.GraphicAnnotations = Sequence(graphic_annotations)
