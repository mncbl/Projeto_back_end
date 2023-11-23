import pydicom
import matplotlib.pyplot as plt
import SimpleITK as sitk
import os

# Replace this with the path to your DICOM file
dicom_file_path = "./uploads/anonimizado_SPECT_24h.dcm"

# Carregar a imagem DICOM 3D
image = sitk.ReadImage(dicom_file_path)

def read_dicom_file(filename):
    try:
        ds = pydicom.dcmread(filename)
        return ds.pixel_array, ds
    except Exception as e:
        print(f"Failed to read DICOM file: {e}")
        return None, None

def preprocess_image(image):
    # Normalize pixel values to be between 0 and 1
    image = (image - sitk.GetArrayViewFromImage(image).min()) / (sitk.GetArrayViewFromImage(image).max() - sitk.GetArrayViewFromImage(image).min())
    return image

if __name__ == "__main__":

    if image is not None:
        # Preprocess the image
        image = preprocess_image(image)

        # Define thresholds
        lower_threshold = 0.2  # Change this according to your data
        upper_threshold = 0.8  # Change this according to your data

        # Apply intensity thresholding
        segmentation = sitk.BinaryThreshold(image, lower_threshold, upper_threshold, 1, 0)

        # Save the segmented image as NRRD
        save_directory = r'./segmentacao'
        save_path_nrrd = os.path.join(save_directory, 'segmented_image.nrrd')
        sitk.WriteImage(segmentation, save_path_nrrd)

        print(f"Segmented image saved as NRRD at: {save_path_nrrd}")
