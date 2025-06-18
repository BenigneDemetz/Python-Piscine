#! /usr/bin/env python3

from PIL import Image
from numpy import array
from benigne.load_image import ft_load

def main() -> int:
    """Main function to zoom an image."""
    path = "animal.jpeg"
    array_img = ft_load(path)
    x_target = 400
    y_target = 400
    x_start = array_img.shape[0] // 2 - x_target // 2
    y_start = array_img.shape[1] // 2 - y_target // 2
    x_slicer = slice(x_start, x_start + x_target)
    y_slicer = slice(y_start, y_start + y_target)
    array_zoomed = array_img[x_slicer, y_slicer]
    array_gray = array_zoomed.mean(axis=2, keepdims=True).astype('uint8')
    print(array_gray)
    print(f"New shape after slicing: {array_gray.shape} or {array_gray.squeeze().shape}")
    return 0    

if __name__ == "__main__":
    main()
