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


def circle_draw_type_1st(draw_image, image, x_y_r):
    # 제 1표 함수
    x, y, r = x_y_r
    fill_colors = COLORS_ON[1] if overlaps_motive(image, (x, y, r)) else COLORS_OFF[1]
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


def circle_draw_type_4th(draw_image, image, x_y_r, target_num):
    # 제 6표, 8표, 12표 함수
    x, y, r = x_y_r
    fill_colors = COLORS_ON[target_num] if overlaps_motive(image, (x, y, r)) else random.choice(COLORS_OFF[target_num])
    # 비율 조정 필요
    fill_color = random.choice(fill_colors)
    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)