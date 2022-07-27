import skimage.io as io
import numpy as np


def f(image, row_pixel, col_pixel):
    if image[row_pixel, col_pixel] > 30000:
        return [255, 255, 255]
    try:
        avg = 0 # 평균
        sum_of_squares = 0 # 제곱의 평균
        for row in range(row_pixel - 20, row_pixel + 21):
            for col in range(col_pixel - 20, col_pixel + 21):
                avg += image[row, col] // (41 * 41)
                sum_of_squares += image[row, col] ** 2 // (41 * 41)
        std = (sum_of_squares - avg ** 2) ** 0.5
        z_score = (image[row_pixel, col_pixel] - avg) / std
        #print(image[row_pixel, col_pixel], avg, std, z_score)
        if z > 0:
            return [255 - int(50 * z), 255 - int(50 * z), 255]  # RGB
        else:
            return [255, 255 + int(50 * z), 255 + int(50 * z)]
    except:
        return [255, 255, 255]


for i in range(13, 15):
    path = f'C:\\Users\\CVLab\\Desktop\\X-ray Image-20220628T003618Z-001\\X-ray Image\\220530 감자 130kV123uA5SS\\{i}.tif'
    img = io.imread(path)
    width, height = img.shape
    print(width, height)
    img1 = np.zeros((width, height, 3)) + 255
    # print(img1)
    for w in range(20, width - 20):
        for h in range(20, height - 20):

            z = f(w, h)
            print(z)
            if z < 0:
                img1[w, h, 0] = 255
                img1[w, h, 1] = 255 + int(50 * z)
                img1[w, h, 2] = 255 + int(50 * z)

            if z > 0:
                img1[w, h, 0] = 255 - int(50 * z)
                img1[w, h, 1] = 255 - int(50 * z)
                img1[w, h, 2] = 255
    io.imshow(img1)
    io.show()
    
# 2차원 흑백 이미지로 읽어서 3차원 RGB 영상으로 반환해야함.
