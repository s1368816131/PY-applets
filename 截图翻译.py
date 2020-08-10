import tkinter.messagebox
from tkinter import *

import pytesseract
from PIL import Image
from PIL import ImageGrab
from googletrans import Translator


def get_clip_image():
    """
    从剪切板获取图片，保存到本地
    :return:
    """
    image_result = None
    img = ImageGrab.grabclipboard()
    if img and isinstance(img, Image.Image):
        print(img.size)
        print(img.mode)
        image_result = './temp.png'
        img.save(image_result)
    return image_result


def image_ocr(image_path):
    """
    识别图像中的英文
    :return:
    """
    # 英文：lang='eng'
    # 中文：lang='chi_sim'
    return pytesseract.image_to_string(Image.open(image_path), lang='eng')


def trans_eng(content_eng):
    """
    英文-中文
    :param content:
    :return:
    """
    translator = Translator(service_urls=['translate.google.cn'])
    return translator.translate(content_eng, src='en', dest='zh-cn').text


image_path = get_clip_image()

if image_path:
    # 获取文本
    content_eng = image_ocr(image_path).replace("\r", " ").replace("\n", " ")

    # 翻译
    if content_eng:
        content_chinese = trans_eng(content_eng)
        print(content_chinese)

        # 实现主窗口隐藏
        root = Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('翻译结果', content_chinese)


# 1、从剪切板获取图片，保存到本地
img = ImageGrab.grabclipboard()
if img and isinstance(img, Image.Image):
    image_result = './temp.png'
    img.save(image_result)

    # 2、OCR识别
    content_eng = pytesseract.image_to_string(Image.open(image_result), lang='eng')

    # 3、翻译
    translator = Translator(service_urls=['translate.google.cn'])

    content_chinese = translator.translate(content_eng, src='en', dest='zh-cn').text

    # 4、显示
    root = Tk()
    root.withdraw()
    tkinter.messagebox.showinfo('翻译结果', content_chinese)