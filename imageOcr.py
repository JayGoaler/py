import cv2
import pytesseract
import numpy as np
from PIL import Image, ImageGrab


def get_clipboard_image():
    # 保存剪切板内图片
    im = ImageGrab.grabclipboard()

    if isinstance(im, Image.Image):
        print("Image: size : %s, mode: %s" % (im.size, im.mode))
        return im
    else:
        print("clipboard is empty")
        return None


def img_show():
    while True:
        img = cv2.imread("img/xly.jpeg")
        cv2.imshow("image", img)
        # 监控是否按下 S 键
        if cv2.waitKey(1) & 0xff == ord("s"):
            im = get_clipboard_image()
        if cv2.waitKey(1) & 0xff == ord("o"):
            im = get_clipboard_image()
            if im is not None:
                do_ocr(im)
        # 如果按下Q键，则退出视频
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    # video.release()
    cv2.destroyAllWindows()

# 123456


def do_ocr(pic):
    num = pytesseract.image_to_string(pic, lang="chi_sim").replace(' ','')
    print(num)
    if num == "12345":
        print("找到指定字符："+num)


if __name__ == '__main__':
    img_show()
