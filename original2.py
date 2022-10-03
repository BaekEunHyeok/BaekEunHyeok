# 처음 구상
import skimage.io as io #이미지 읽기 위한 라이브러리
import numpy as np

for i in range(1, 15):
    path = f'C:\\Users\\CVLab\\Desktop\\X-ray Image-20220628T003618Z-001\\X-ray Image\\220530 감자 130kV123uA5SS\\{i}.tif'
    img = io.imread(path)
    s = np.zeros_like(img).astype('float')
    # img = ex.adjust_log(img)
    height, width = img.shape

    for r in range(20, height - 20):
        for c in range(20, width - 20):
            # 한 픽셀에 대해 주변 40*40 범위의 평균과 표준편차를 구해 주변보다 밀도가 얼마나 차이나는지 구함
            try:
                if img[r, c] < 40000:
                    scale = 20
                    avg = np.mean(img[r - scale + 1:r + scale, c - scale:c + scale + 1])
                    avg2 = np.mean(img[r - 2:r+3, c-2:c+3])
                    std = np.std(img[r - scale:r + scale + 1, c - scale:c + scale + 1])
                    z = (avg2 - avg) / std
                    s[r, c] = z

            except:
                pass
    io.imshow(s, cmap='seismic')
    io.show()

# 흑백 이미지 읽으면 이미지 형태가 가로 세로 2차원이고 이미지 보여줄 때 cmap을 사용해도 되서 자동으로 색상이 처리가 됨

# 19, 21번째 줄 수정
