import cv2 as cv


class Picture:
    def __init__(self, filepath):
        self.img = cv.imread(filepath, cv.IMREAD_COLOR)

    def get_img_info(self):
        """
        返回由图片的高度、宽度和维度三者组成的元组
        :return: Tuple of (height, width, dimension)
        """
        # print(f"Image shape: {self.img.shape}")
        return self.img.shape

    def show_image(self):
        """
        显示图片
        :return: None
        """
        cv.imshow("image", self.img)
        cv.waitKey()