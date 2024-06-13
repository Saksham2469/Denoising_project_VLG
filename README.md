# Image Dehazing using Bilateral Filtering and Histogram Equalization

This repository contains the implementation of an image dehazing algorithm that enhances the quality of hazy images using bilateral filtering and histogram equalization. The algorithm is designed to reduce noise, sharpen edges, improve contrast, and increase color saturation, resulting in clearer and more visually appealing images.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Contributing](#contributing)

## Introduction

Hazy images often suffer from reduced contrast and clarity due to particles like dust and smoke in the air. This project addresses these issues by implementing a dehazing algorithm that combines several image processing techniques to enhance image quality.

## Features

- Bilateral Filtering for noise reduction while preserving edges
- Image Sharpening using a convolutional kernel
- Histogram Equalization to improve image contrast
- Saturation Adjustment for more vibrant colors
- Progress tracking using `tqdm` for processing multiple images

## Usage

1. Prepare your images:
    - Place the images you want to dehaze in the `./test/low/` directory.

2. Run the script:
    ```bash
    python main.py
    ```

3. The dehazed images will be saved in the `./test/predicted/` directory.

## Methodology

The dehazing process involves several steps:

1. **Reading the Image**:
    - Images are read from the input directory.

2. **Bilateral Filtering**:
    - Noise is reduced while preserving edges using `cv2.bilateralFilter`.

3. **Image Sharpening**:
    - Edges are enhanced using a sharpening kernel applied with `cv2.filter2D`.

4. **Histogram Equalization**:
    - Contrast is improved by applying histogram equalization to the luminance channel in the YUV color space.

5. **Saturation Adjustment**:
    - Color saturation is increased in the HSV color space to make the image more vibrant.

6. **Saving the Enhanced Image**:
    - Processed images are saved to the output directory.

## Results

The algorithm effectively enhances hazy images, making them clearer and more visually appealing. The combined use of bilateral filtering and histogram equalization significantly improves image quality.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.
