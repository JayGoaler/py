import requests
import cv2
import os

imagePath = "D:/Downloads/images/"
haarcascade_frontalface_default_path = "lib/haarcascade_frontalface_default.xml"
lbpcascade_animeface_path = "lib/lbpcascade_animeface.xml"


# 下载图像
def get_image_by_page(num):
    page = int(num) + 1
    header = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/87.0.4280.88 Safari/537.36 '
    }
    n = 0
    pn = 1
    # pn是从第几张图片获取 百度图片下滑时默认一次性显示30张
    for m in range(1, page):
        url = 'https://image.baidu.com/search/acjson?'

        param = {
            'tn': 'resultjson_com',
            'logid': '8846269338939606587',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': '亚洲女性头像',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': '亚洲女性头像',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': 'girl',
            'pn': pn,  # 从第几张图片开始
            'rn': '30',
            'gsm': '1e',
        }
        page_text = requests.get(url=url, headers=header, params=param)
        page_text.encoding = 'utf-8'
        page_text = page_text.json()
        info_list = page_text['data']
        del info_list[-1]
        img_path_list = []
        for i in info_list:
            img_path_list.append(i['thumbURL'])

        for img_path in img_path_list:
            img_data = requests.get(url=img_path, headers=header).content
            img_path = imagePath + str(n) + '.jpg'
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
            if not check_image(img_path):
                os.remove(img_path)
            else:
                n = n + 1

        pn += 29
        print('下载完成')


# 检查图像是否包含人脸
def check_image(filepath):
    img = cv2.imread(filepath)  # 读取图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色

    # OpenCV人脸识别分类器
    classifier = cv2.CascadeClassifier(haarcascade_frontalface_default_path)
    # 调用识别人脸
    faceRects = classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(faceRects):
        img_gray = cv2.equalizeHist(gray)  # 直方图均衡化
        face_cascade = cv2.CascadeClassifier(lbpcascade_animeface_path)  # 加载级联分类器
        faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测
        if len(faces):
            return True
    return False


# 检测人脸 适用动漫脸
def face_detect(file_name):
    img = cv2.imread(file_name)  # 读取图片
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    face_cascade = cv2.CascadeClassifier(lbpcascade_animeface_path)  # 加载级联分类器
    faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测
    for (x, y, w, h) in faces:  # 遍历所有检测到的动漫脸
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 5)  # 绘制矩形框
    cv2.imshow('Face detection', img)  # 检测效果预览
    cv2.waitKey(0)  # 保持窗口显示
    return faces


if __name__ == '__main__':
    # get_image_by_page(5)
    print(face_detect(imagePath+'16.jpg'))
