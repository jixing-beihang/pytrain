from PIL import Image, ImageFilter

# # 打开文件
# img = Image.open('D:\\test.jpg')
# w, h = img.size
# print('Oraginal size:%sx%s' % (w, h))
# # 图片处理
# thumbImg = img.thumbnail((w // 2, h // 2))
# print('Resize Img size:%sx%s' % (w // 2, h // 2))
# # 图片保存
# img.save('D:\\thumbnail.jpg', 'jpeg')

img = Image.open('D:\\test.jpg')
img_blur = img.filter(ImageFilter.BLUR)
img_blur.save('D:\\blur.jpg','jpeg')



