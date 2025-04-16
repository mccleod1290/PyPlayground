# Image Processing Programs

This repository contains implementations of various image processing techniques in Python. Each program demonstrates a different image manipulation or enhancement technique.

## Dependencies

To run these programs, you'll need to install the following packages:
```bash
pip install opencv-python numpy
```

## Implemented Programs

### 1. Image Translation
Image translation shifts an image by a specified number of pixels in the x and y directions.

Implementation:
- Uses OpenCV's warpAffine function
- Creates transformation matrix for translation
- Preserves image dimensions
- Handles both positive and negative translations

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/translation.py)

### 2. Image Reflection
Image reflection creates a mirror image of the original image, either horizontally or vertically.

Implementation:
- Uses OpenCV's flip function
- Supports horizontal and vertical reflection
- Preserves image quality
- Maintains original image dimensions

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/reflection.py)

### 3. Image Rotation
Image rotation rotates an image by a specified angle around its center point.

Implementation:
- Uses OpenCV's getRotationMatrix2D and warpAffine
- Handles arbitrary rotation angles
- Preserves image quality
- Maintains image dimensions

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/rotation.py)

### 4. Image Scaling
Image scaling resizes an image by specified factors in the x and y directions.

Implementation:
- Uses OpenCV's resize function
- Supports different scaling factors for x and y
- Uses linear interpolation
- Maintains aspect ratio if desired

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/scaling.py)

### 5. Image Cropping
Image cropping extracts a rectangular region from an image based on specified coordinates.

Implementation:
- Uses array slicing for cropping
- Supports arbitrary rectangular regions
- Preserves image quality
- Maintains color information

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/cropping.py)

### 6. Image Shearing (X-axis)
Image shearing along the x-axis distorts the image by shifting pixels horizontally.

Implementation:
- Uses affine transformation
- Creates shear matrix
- Preserves image dimensions
- Handles various shear factors

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/shearing_x.py)

### 7. Image Shearing (Y-axis)
Image shearing along the y-axis distorts the image by shifting pixels vertically.

Implementation:
- Uses affine transformation
- Creates shear matrix
- Preserves image dimensions
- Handles various shear factors

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/shearing_y.py)

### 8. Brightness Enhancement
Brightness enhancement adjusts the overall brightness of an image.

Implementation:
- Uses OpenCV's add function
- Adjusts pixel values uniformly
- Preserves image structure
- Handles both positive and negative adjustments

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/brightness.py)

### 9. Color Enhancement
Color enhancement adjusts the saturation of colors in an image.

Implementation:
- Converts to HSV color space
- Modifies saturation channel
- Preserves image structure
- Handles various enhancement factors

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/color_enhancement.py)

### 10. Contrast Enhancement
Contrast enhancement adjusts the difference between light and dark areas of an image.

Implementation:
- Uses OpenCV's convertScaleAbs
- Adjusts pixel intensity range
- Preserves image structure
- Handles various contrast factors

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/contrast.py)

### 11. Sharpness Enhancement
Sharpness enhancement increases the clarity of edges and details in an image.

Implementation:
- Uses convolution with sharpening kernel
- Applies Laplacian filter
- Preserves image structure
- Handles various kernel sizes

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/sharpness.py)

### 12. RGB to Grayscale Conversion
Converts a color image to grayscale by combining color channels.

Implementation:
- Uses OpenCV's cvtColor function
- Applies standard conversion formula
- Preserves image structure
- Reduces image to single channel

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/rgb_to_grayscale.py)

### 13. RGB to HSV Conversion
Converts an image from RGB color space to HSV color space.

Implementation:
- Uses OpenCV's cvtColor function
- Preserves image structure
- Separates color information
- Maintains image dimensions

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/rgb_to_hsv.py)

### 14. Supervised Segmentation
Performs image segmentation based on color thresholds.

Implementation:
- Uses HSV color space
- Applies color thresholding
- Creates binary mask
- Extracts segmented regions

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/supervised_segmentation.py)

### 15. Morphological Operations
Applies basic morphological operations (erosion and dilation) to an image.

Implementation:
- Uses OpenCV's morphological functions
- Creates structuring element
- Supports erosion and dilation
- Handles various kernel sizes

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/image-processing/morphological.py)

## Usage

Each program can be run independently and will prompt for the necessary input. The programs demonstrate various image processing techniques and their effects.

## Note

These implementations are for educational purposes and demonstrate basic image processing concepts. For production use, additional error handling and optimization may be required. 