# 普通二维码
'''
import qrcode

# Link for website
input_data = "https://github.com/s1368816131"

#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('GitHub.png')'''

# 动态背景
from MyQR import myqr

myqr.run(words='https://github.com/s1368816131',
         version = 1,

         picture='pic.gif',
         save_name='GitHub动态.gif',
         colorized=True)