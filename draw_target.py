import random

from colorset import *
from PIL import Image, ImageDraw

BACKGROUND = (255, 255, 255)

first_flag = True
resize_image1 = Image
resize_image2 = Image
resize_overlap_image1 = Image
resize_overlap_image2 = Image
images = []


def overlaps_motive(image, x_y_r):
    # 원의 겹침을 확인하는 함수, 반환값 : boolean
    x, y, r = x_y_r
    if image.getpixel((x, y))[:3] != BACKGROUND:
        return True
    return False


def circle_draw_type_1st(draw_image, image, image2, x_y_r, target_num):
    # 제 1, 7표 함수
    x, y, r = x_y_r
    global first_flag
    global resize_image1
    global resize_image2
    if first_flag:
        resize_image1 = Image.new('RGB', image.size, BACKGROUND)
        resize_image2 = Image.new('RGB', image2.size, BACKGROUND)
        image = image.resize((1400, 1400))
        image2 = image2.resize((1400, 1400))
        resize_image1.paste(image, box=(0, 300))
        resize_image2.paste(image2, box=(700, 300))
        images.append(resize_image1)
        images.append(resize_image2)
        first_flag = False
    if overlaps_motive(resize_image1, (x, y, r)) or overlaps_motive(resize_image2, (x, y, r)):
        fill_colors = COLORS_ON[target_num]
    else:
        fill_colors = COLORS_OFF[target_num][0] if random.random() < 0.7 else COLORS_OFF[target_num][1]

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def circle_draw_type_2nd(draw_image, image, image2, x_y_r, target_num):
    # 제 2표, 4표, 11표 함수
    x, y, r = x_y_r
    if overlaps_motive(image, (x, y, r)):
        if overlaps_motive(image2, (x, y, r)):
            fill_colors = COLORS_ON[target_num][0]
        else:
            fill_colors = COLORS_ON[target_num][1]
    elif overlaps_motive(image2, (x, y, r)):
        fill_colors = COLORS_ON[target_num][2]
    else:
        fill_colors = COLORS_OFF[target_num]

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def circle_draw_type_3rd(draw_image, image, image2, overlap_image, overlap_image2, x_y_r, target_num):
    # 제 3표, 5표
    x, y, r = x_y_r
    global first_flag
    global resize_image1
    global resize_image2
    global resize_overlap_image1
    global resize_overlap_image2
    global images
    if first_flag:
        resize_image1 = Image.new('RGB', image.size, BACKGROUND)
        resize_image2 = Image.new('RGB', image2.size, BACKGROUND)
        resize_overlap_image1 = Image.new('RGB', overlap_image.size, BACKGROUND)
        resize_overlap_image2 = Image.new('RGB', overlap_image2.size, BACKGROUND)
        image = image.resize((1400, 1400))
        image2 = image2.resize((1400, 1400))
        overlap_image = overlap_image.resize((1400, 1400))
        overlap_image2 = overlap_image2.resize((1400, 1400))
        resize_image1.paste(image, box=(0, 300))
        resize_image2.paste(image2, box=(700, 300))
        resize_overlap_image1.paste(overlap_image, box=(0, 300))
        resize_overlap_image2.paste(overlap_image2, box=(700, 300))
        images.append(resize_image1)
        images.append(resize_image2)
        images.append(resize_overlap_image1)
        images.append(resize_overlap_image2)
        first_flag = False
    if overlaps_motive(resize_image1, (x, y, r)):
        if overlaps_motive(resize_overlap_image1, (x, y, r)):
            fill_colors = COLORS_ON[target_num][0]
        else:
            fill_colors = COLORS_ON[target_num][1]
    elif overlaps_motive(resize_image2, (x, y, r)):
        if overlaps_motive(resize_overlap_image2, (x, y, r)):
            fill_colors = COLORS_ON[target_num][0]
        else:
            fill_colors = COLORS_ON[target_num][1]
    elif overlaps_motive(resize_overlap_image1, (x, y, r)) or overlaps_motive(resize_overlap_image2, (x, y, r)):
        fill_colors = COLORS_ON[target_num][2]
    else:
        fill_colors = COLORS_OFF[target_num]

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def circle_draw_type_4th(draw_image, image, x_y_r, target_num):
    # 제 6표, 8표, 12표 함수
    x, y, r = x_y_r
    if overlaps_motive(image, (x, y, r)):
        fill_colors = COLORS_ON[target_num]
    else:
        fill_colors = COLORS_OFF[target_num][0] if random.random() < 0.7 else COLORS_OFF[target_num][1]
    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def circle_draw_type_5th(draw_image, image, image2, x_y_r):
    # 제 9표 함수
    x, y, r = x_y_r
    if overlaps_motive(image, (x, y, r)):
        if overlaps_motive(image2, (x, y, r)):
            fill_colors = COLORS_ON[9][1]
        else:
            fill_colors = COLORS_ON[9][2] if random.random() < 0.8 else COLORS_ON[9][0]
    elif overlaps_motive(image2, (x, y, r)):
        fill_colors = COLORS_OFF[9][0]
    else:
        fill_colors = COLORS_OFF[9][1]

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def circle_draw_type_6th(draw_image, image, image2, x_y_r, target_num):
    # 제 10표, 13표, 14표, 15표, 16표, 17표, 18표 함수
    x, y, r = x_y_r
    global first_flag
    global resize_image1
    global resize_image2
    if first_flag:
        resize_image1 = Image.new('RGB', image.size, BACKGROUND)
        resize_image2 = Image.new('RGB', image2.size, BACKGROUND)
        image = image.resize((1400, 1400))
        image2 = image2.resize((1400, 1400))
        resize_image1.paste(image, box=(0, 300))
        resize_image2.paste(image2, box=(700, 300))
        images.append(resize_image1)
        images.append(resize_image2)
        first_flag = False
    if overlaps_motive(resize_image1, (x, y, r)):
        if overlaps_motive(resize_image2, (x, y, r)):
            fill_colors = COLORS_OFF[target_num]
        else:
            fill_colors = COLORS_ON[target_num][0]
    elif overlaps_motive(resize_image2, (x, y, r)):
        fill_colors = COLORS_ON[target_num][1]
    else:
        fill_colors = COLORS_OFF[target_num]
    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def circle_draw_type_7th(draw_image, image, image2, x_y_r, target_num):
    # 제 19표, 20표, 21표 함수
    x, y, r = x_y_r
    if overlaps_motive(image, (x, y, r)):
        if overlaps_motive(image2, (x, y, r)):
            fill_colors = COLORS_ON[target_num][0]
        else:
            fill_colors = COLORS_ON[target_num][0]
    elif overlaps_motive(image2, (x, y, r)):
        fill_colors = COLORS_ON[target_num][1]
    else:
        fill_colors = COLORS_OFF[target_num]

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)