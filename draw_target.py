import random

from colorset import *

BACKGROUND = (255, 255, 255)


def overlaps_motive(image, x_y_r):
    # 원의 겹침을 확인하는 함수, 반환값 : boolean
    x, y, r = x_y_r
    points_x = [x, x, x, x-r, x+r, x-r*0.93, x-r*0.93, x+r*0.93, x+r*0.93]
    points_y = [y, y-r, y+r, y, y, y+r*0.93, y-r*0.93, y+r*0.93, y-r*0.93]

    for xy in zip(points_x, points_y):
        if image.getpixel(xy)[:3] != BACKGROUND:
            return True
        # 배열[행:열] 앞의 예는 3열을 고정시킨것, getpixel() 해당 점의 RGB 값 반환

    return False


def circle_draw_target_1st(draw_image, image, x_y_r):
    # 이미지에 원을 그려주는 함수
    x, y, r = x_y_r
    fill_colors = COLORS_ON_1 if overlaps_motive(image, (x, y, r)) else COLORS_OFF_1
    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)
    # 원 생성 메소드


def circle_draw_target_2nd(draw_image, image, image2, x_y_r):
    # 제 2표 그려주는 함수
    x, y, r = x_y_r
    if overlaps_motive(image, (x, y, r)):
        if overlaps_motive(image2, (x, y, r)):
            fill_colors = COLORS_ON_2_1
        else:
            fill_colors = COLORS_ON_2_2
    elif overlaps_motive(image2, (x, y, r)):
        fill_colors = COLORS_ON_2_3
    else:
        fill_colors = COLORS_OFF_2

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)
    # 원 생성 메소드


def circle_draw_target_11th(draw_image, image, image2, x_y_r):
    # 제 11표 그려주는 함수
    x, y, r = x_y_r
    if overlaps_motive(image, (x, y, r)):
        if overlaps_motive(image2, (x, y, r)):
            fill_colors = COLORS_ON_11_1
        else:
            fill_colors = COLORS_ON_11_2
    elif overlaps_motive(image2, (x, y, r)):
        fill_colors = COLORS_ON_11_3
    else:
        fill_colors = COLORS_OFF_11

    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)
    # 원 생성 메소드
