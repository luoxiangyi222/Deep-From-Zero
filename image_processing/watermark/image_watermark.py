
"""
Author: Akira Luo
Date: Feb 2021
"""

import cv2
import numpy as np
import os


def add_watermark(image_path, mask_path, alpha=0.5):
    """
    This method add watermark to every image, and save them into output_path

    Reference:
        https://blog.csdn.net/qq_36810544/article/details/89671249

    :param image_path: the path of input image
    :param mask_path: the path of the mask image
    :param alpha: Transparency of the mask image
    :return: an image with watermark at right-bottom
    """

    save_folder = '/watermark_output'

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # load img and mask
    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    img_h, img_w, _ = img.shape

    if img_w > img_h:
        rate = int(img_w * 0.1) / mask.shape[1]
    else:
        rate = int(img_h * 0.1) / mask.shape[0]

    mask = cv2.resize(mask, None, fx=rate, fy=rate)
    mask_h, mask_w, _ = mask.shape
    mask_channels = cv2.split(mask)

    b, g, r = cv2.split(mask)
    a = np.ones(b.shape, dtype=b.dtype) * 255  # creating a dummy alpha channel image.

    # compute location of mask
    # at right bottom corner

    ul_points = ((int(img_h) - int(mask_h) - 10), int(img_w) - int(mask_w) - 10)
    dr_points = (ul_points[0] + mask_h, ul_points[1] + mask_w)

    dst_channels = cv2.split(img)

    print('Generating: ------' + image_path.split('/')[-1] + '-----')
    for i in range(3):
        dst_channels[i][ul_points[0]: dr_points[0], ul_points[1]: dr_points[1]] = dst_channels[i][
                                                                                  ul_points[0]: dr_points[0],
                                                                                  ul_points[1]: dr_points[1]] \
                                                                                  * (255.0 - a * alpha) / 255
        dst_channels[i][ul_points[0]: dr_points[0], ul_points[1]: dr_points[1]] += np.array(
            mask_channels[i] * (a * alpha / 255), dtype=np.uint8)

    dst_img = cv2.merge(dst_channels)

    save_path = save_folder + image_path.split('/')[-1]
    cv2.imwrite(save_path, dst_img)

    print('Great! Image is saved successfully!')
