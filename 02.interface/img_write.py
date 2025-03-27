import cv2

img_file = '/Users/simseunghwan/Desktop/github/insightbook.opencv_project_python/dog/dog2.jpg'
save_file = '/Users/simseunghwan/Desktop/github/insightbook.opencv_project_python/dog/dog2_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장에 따름
cv2.waitKey()
cv2.destroyAllWindows()
