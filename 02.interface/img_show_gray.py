import cv2

img_file = "/Users/simseunghwan/Desktop/github/insightbook.opencv_project_python/dog/dog2.jpg" 
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 읽기

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')
    