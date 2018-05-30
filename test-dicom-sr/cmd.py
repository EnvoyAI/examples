from datetime import datetime
import pydicom
from pydicom.dataset import Dataset, FileDataset
from pydicom.sequence import Sequence
from pydicom.uid import generate_uid

print(__doc__)

dcm_in = pydicom.read_file('/envoyai/input/in.dcm')

# Normal mode:
print()
print("Filename.....................:", '/envoyai/input/in.dcm')
print("Storage type.................:", dcm_in.SOPClassUID)
print("SeriesInstanceUid............:", dcm_in.SeriesInstanceUID)
print("SopInstanceUid...............:", dcm_in.SOPInstanceUID)
print("MediaStorageSOPInstanceUID...:", dcm_in.file_meta.MediaStorageSOPInstanceUID)
print()

pat_name = dcm_in.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print("Patient's name.......:", display_name)
print("Modality.............:", dcm_in.Modality)
print("TransferSyntax.......:", dcm_in.file_meta.TransferSyntaxUID)

instanceId = generate_uid()
seriesId = generate_uid()
sopClass = "1.2.840.10008.5.1.4.1.1.88.11"  # Basic Text SR IOD
file_meta = Dataset()
file_meta.MediaStorageSOPClassUID = sopClass
file_meta.MediaStorageSOPInstanceUID = instanceId
file_meta.ImplementationClassUID = "1.2.276.0.7230010.3.0.3.4.2"  # ask josh
file_meta.ImplementationVersionName = "Bone age SR"
file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
sr_out = FileDataset("sr.dcm", {}, file_meta=file_meta, preamble=b"\0" * 128)
sr_out.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
sr_out.is_little_endian = True
sr_out.is_implicit_VR = False
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
    sr_out.add(dcm_in.data_element(de))
sr_out.Modality = 'SR'
sr_out.SOPClassUID = sopClass
sr_out.SOPInstanceUID = instanceId
sr_out.SeriesInstanceUID = seriesId
sr_out.SeriesNumber = 1
sr_out.InstanceNumber = 1
sr_out.PreliminaryFlag = 'PRELIMINARY'
sr_out.CompletionFlag = 'PARTIAL'
sr_out.VerificationFlag = 'UNVERIFIED'
sr_out.ContentDate = datetime.now().date().strftime("%Y%m%d")
sr_out.ContentTime = datetime.now().time().strftime("%H%M%S")
referencedSequenceDataset = Dataset()
referencedSequenceDataset.ReferencedSOPClassUID = dcm_in.SOPClassUID
referencedSequenceDataset.ReferencedSOPInstanceUID = dcm_in.SOPInstanceUID
purposeOfReferenceDataset = Dataset()
purposeOfReferenceDataset.CodeValue = "121335"
purposeOfReferenceDataset.CodingSchemeDesignator = "DCM"
purposeOfReferenceDataset.CodingSchemeVersion = "20061023"
purposeOfReferenceDataset.CodeMeaning = "Source Document"
referencedSequenceDataset.PurposeOfReferenceCodeSequence = Sequence([purposeOfReferenceDataset])
sr_out.ReferencedInstanceSequence = Sequence([referencedSequenceDataset])
sr_out.ValueType = "CONTAINER"
conceptNameDataset = Dataset()
conceptNameDataset.CodeValue = "126000"
conceptNameDataset.CodingSchemeDesignator = "DCM"
conceptNameDataset.CodeMeaning = "Imaging Measurement Report"
sr_out.ConceptCodeSequence = Sequence([conceptNameDataset])
referencedSopSequence = Dataset()
referencedSopSequence.ReferencedSOPClassUID = dcm_in.SOPClassUID
referencedSopSequence.ReferencedSOPInstanceUID = dcm_in.SOPInstanceUID
sr_out.ReferencedSOPSequence = Sequence([referencedSopSequence])
nameDataset = Dataset()
nameDataset.RelationshipType = "CONTAINS"
nameDataset.ValueType = "TEXT"
nameConceptNameDataset = Dataset()
nameConceptNameDataset.CodeValue = "371484003"
nameConceptNameDataset.CodingSchemeDesignator = "SNM3"
nameConceptNameDataset.CodeMeaning = "Patient name (observable entity)"
nameDataset.ConceptNameCodeSequence = Sequence([nameConceptNameDataset])
nameDataset.TextValue = display_name
sr_out.ContentSequence = Sequence([nameDataset])
pydicom.write_file('/envoyai/output/sr.dcm', sr_out)

print("SeriesInstanceUid............:", sr_out.SeriesInstanceUID)
print("SopInstanceUid...............:", sr_out.SOPInstanceUID)
print("MediaStorageSOPInstanceUID...:", sr_out.file_meta.MediaStorageSOPInstanceUID)
pydicom.write_file('/envoyai/output/out.dcm',sr_out)
exit(0)
