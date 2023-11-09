import pydicom
from skimage import segmentation
import matplotlib.pyplot as plt
import numpy as np

def read_dicom_file(filename):
    try:
        ds = pydicom.dcmread(filename)
        return ds.pixel_array
    except Exception as e:
        print(f"Failed to read DICOM file: {e}")
        return None

def segment_image(image, num_segments):
    labels = segmentation.felzenszwalb(image, num_segments)
    segment_colors = plt.get_cmap('jet')(labels / 10.0)
    return segment_colors

if __name__ == "__main__":
    # Replace this with the path to your DICOM file
    dicom_file_path = "./inputs/SPECT_1h.dcm"

    image = read_dicom_file(dicom_file_path)

    if image is not None:
        # Define the number of segments you want
        num_segments = 50

        # Apply the segmentation algorithm
        segment_colors = segment_image(image, num_segments)

        # Display the segmented image
        plt.figure(figsize=(10, 10))
        plt.imshow(segment_colors)
        plt.axis('off')
        plt.show()