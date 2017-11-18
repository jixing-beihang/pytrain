from PIL import Image
import argparse


def get_char(r, g, b, alpha=256):
    '''
    将 RGB 映射到字符上
    :param r: red
    :param g: green
    :param b: blue
    :param alpha:
    :return: char
    '''
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    if alpha == 0:
        return ' '
    gray = (2126 * r + 7152 * g + 722 * b) / 10000
    length = len(ascii_char)
    index = int(gray / (256.0 + 1) * length)
    return ascii_char[index]


def save(out_file, text):
    '''

    :param out_file: save file to ...
    :param text: content
    :return: none
    '''
    with open(out_file, 'w') as f:
        f.write(text)


def parse_param():
    '''
    deal with input params
    :return:
    '''
    parse = argparse.ArgumentParser()
    parse.add_argument('in_file')
    parse.add_argument('-o', '--out_file')
    parse.add_argument('--width', type=int, default=30)
    parse.add_argument('--height', type=int, default=30)

    args = parse.parse_args()
    in_file, out_file, width, height = args.in_file, args.out_file, args.width, args.height
    return in_file, out_file, width, height


def main(picture='D:\\test.jpg', width=300, height=300, out_file='D:\\ascii_out'):
    im = Image.open(picture)
    im = im.resize((width, height), Image.NEAREST)

    text = ''
    for i in range(height):
        for j in range(width):
            text += get_char(*im.getpixel((j, i)))
        text += '\n'
    print(text)
    save(out_file, text)


if __name__ == '__main__':
    '''
    测试方法
    '''
    in_file, out_file, width, height = parse_param()
    main('D:\\test.jpg', width, height, out_file)
