import cv2
import numpy as np

# 이미지 불러오기
path = 'C:\\Users\\CVLab\\Desktop\\blur\\original.tif'
original_image = cv2.imread(path)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
image_ = np.divide(gray_image, 255.0, dtype=np.single)
# kernels for Lapace filter
kernel1 = np.array([[1, -2, 1]])
kernel2 = np.array([[1],
                    [-2],
                    [1]])

# 이미지를 Laplace filter 통과 (2차미분)
pass1 = cv2.filter2D(image_, cv2.CV_32F, kernel1, borderType=cv2.BORDER_CONSTANT)
pass2 = cv2.filter2D(image_, cv2.CV_32F, kernel2, borderType=cv2.BORDER_CONSTANT)

# 절대값으로 변환
pass1 = np.absolute(pass1)
pass2 = np.absolute(pass2)

# pass1 + pass2
lap = cv2.add(pass1, pass2, dtype = cv2.CV_32F)

# Region Of Interesting (관심 영역)
ROI = np.zeros_like(gray_image)
rows, columns = np.shape(gray_image)
sum = 0
count = 0
for r in range(rows):
    for c in range(columns):
        if gray_image[r,c] < 240:
            count +=1
            sum += lap[r,c]
#print(rows, columns, rows*columns)
#print(sum), print(count), print(np.max(gray_image))
mean = sum / count
print(f'Sharpness : {mean}')

# original 0.024805
# blur3 0.00639
# blur5 0.00443
