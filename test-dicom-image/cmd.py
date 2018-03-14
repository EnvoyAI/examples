import pydicom
import functools

print(__doc__)

ds = pydicom.dcmread('/envoyai/input/in.dcm')

# Normal mode:
print()
print("Filename.....................:", '/envoyai/input/in.dcm')
print("Storage type.................:", ds.SOPClassUID)
print("SeriesInstanceUid............:", ds.SeriesInstanceUID)
print("SopInstanceUid...............:", ds.SOPInstanceUID)
print("MediaStorageSOPInstanceUID...:", ds.file_meta.MediaStorageSOPInstanceUID)
print()

pat_name = ds.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print("Patient's name.......:", display_name)
print("Modality.............:", ds.Modality)
print("TransferSyntax.......:", ds.file_meta.TransferSyntaxUID)

data = ds.pixel_array
vox = functools.reduce(lambda acc, v: ('{}' if acc is None else acc + ' x {}').format(v), data.shape, None)
oneFrame = 'NumberOfFrames' not in ds or ds.NumberOfFrames == 1
print('The image has {} voxels'.format(vox))
data_downsampling = data[::8, ::8] if oneFrame else data[::, ::8, ::8]

down_vox = functools.reduce(lambda acc, v: ('{}' if acc is None else acc + ' x {}').format(v), data_downsampling.shape,
                            None)
print('The downsampled image has {} voxels'.format(down_vox))

# copy the data back to the original data set
ds.PixelData = data_downsampling.tobytes()
# update the information regarding the shape of the data array
if oneFrame:
    ds.Rows, ds.Columns = data_downsampling.shape
else:
    ds.NumberOfFrames, ds.Rows, ds.Columns = data_downsampling.shape

print("Appending the instance and series uid")
ds.file_meta.MediaStorageSOPInstanceUID = ds.file_meta.MediaStorageSOPInstanceUID + ".1"
ds.SOPInstanceUID = ds.SOPInstanceUID + ".1"
ds.SeriesInstanceUID = ds.SeriesInstanceUID + ".1"
print("SeriesInstanceUid............:", ds.SeriesInstanceUID)
print("SopInstanceUid...............:", ds.SOPInstanceUID)
print("MediaStorageSOPInstanceUID...:", ds.file_meta.MediaStorageSOPInstanceUID)
ds.save_as('/envoyai/output/out.dcm')
exit(0)
