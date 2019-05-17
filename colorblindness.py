import sys
import math

from draw_target import *

try:
    from scipy.spatial import cKDTree as KDTree
    import numpy as np
    IMPORTED_SCIPY = True
except ImportError:
    IMPORTED_SCIPY = False

TOTAL_CIRCLES = 410


def generate_circle(image_width, image_height, min_diameter, max_diameter):
    # 원의 위치를 결정 하는 함수, 반환값 : circle(x좌표, y좌표, 반지름)
    radius = random.triangular(min_diameter, max_diameter,
                               max_diameter * 0.8 + min_diameter * 0.2) / 2
    # 원의 직경은 삼각분포를 이루며 최대 직경값에 치우침

    angle = random.uniform(0, math.pi * 2)
    # 랜덤 각
    distance_from_center = random.uniform(0, image_width * 0.48 - radius)
    # 랜덤 거리
    x = image_width  * 0.5 + math.cos(angle) * distance_from_center
    y = image_height * 0.5 + math.sin(angle) * distance_from_center
    # 중앙으로 부터 랜덤한 위치에 랜덤한 직경의 원의 중심을 지정

    return x, y, radius


def circle_intersection(x1_y1_r1, x2_y2_r2):
    # 두원의 겹침 조사 함수 겹치지 않을 때 true 반환, 반환값 : boolean
    x1, y1, r1 = x1_y1_r1
    x2, y2, r2 = x2_y2_r2
    return (x2 - x1)**2 + (y2 - y1)**2 < 1.13*(r2 + r1)**2


first_flag = True
over_image = Image


def circle_draw(draw_image, image, x_y_r, target_num):
    global first_flag
    global over_image
    if target_num in [1]:
        circle_draw_type_1st(draw_image, image, x_y_r)
    elif target_num in [2, 4, 11]:
        if first_flag:
            print('input overlap image file name : ')
            overlap_image = input()
            over_image = Image.open('./sample_input/' + overlap_image + '.png')
            first_flag = False
        circle_draw_type_2nd(draw_image, image, over_image, x_y_r, target_num)
    elif target_num in [3, 5]:
        if first_flag:
            print('input second image file name : ')
            overlap_image = input()
            over_image = Image.open('./sample_input/' + overlap_image + '.png')
            first_flag = False
        circle_draw_type_3rd(draw_image, image, over_image, x_y_r, target_num)
    elif target_num in [6, 8, 12]:
        circle_draw_type_4th(draw_image, image, x_y_r, target_num)
    elif target_num in [7]:
        if first_flag:
            print('input second image file name : ')
            overlap_image = input()
            over_image = Image.open('./sample_input/' + overlap_image + '.png')
            first_flag = False
        circle_draw_type_5th(draw_image, image, over_image, x_y_r)
    elif target_num in [9]:
        circle_draw_type_6th(draw_image, image, over_image, x_y_r)
    elif target_num in [10, 13, 14, 15, 16, 17]:
        if first_flag:
            print('input second image file name : ')
            overlap_image = input()
            over_image = Image.open('./sample_input/' + overlap_image + '.png')
            first_flag = False
        circle_draw_type_7th(draw_image, image, over_image, x_y_r, target_num)
    elif target_num in [19, 20, 21]:
        if first_flag:
            print('input second image file name : ')
            overlap_image = input()
            over_image = Image.open('./sample_input/' + overlap_image + '.png')
            first_flag = False
        circle_draw_type_8th(draw_image, image, over_image, x_y_r, target_num)
    else:
        print('1~21 사이의 숫자를 입력해주세요')
        sys.exit()


def main():
    image = Image.open(sys.argv[1])
    image2 = Image.new('RGB', image.size, BACKGROUND)
    draw_image = ImageDraw.Draw(image2)

    width, height = image.size

    min_diameter = (width + height) / 110
    max_diameter = (width + height) / 40
    print('please input target number (1 ~ 21) : ')
    target_num = int(input())

    circle = generate_circle(width, height, min_diameter, max_diameter)
    circles = [circle]
    circle_draw(draw_image, image, circle, target_num)
    try:
        for i in range(TOTAL_CIRCLES):
            tries = 0
            if IMPORTED_SCIPY:
                kdtree = KDTree([(x, y) for (x, y, _) in circles])
                while True:
                    if i< TOTAL_CIRCLES/4:
                        circle = generate_circle(width, height, max_diameter, max_diameter)
                    else:
                        circle = generate_circle(width, height, min_diameter, max_diameter)
                    elements, indexes = kdtree.query([(circle[0], circle[1])], k=12)
                    # 거리 상한이 12인 인접한 원들을 찾아 내어 비교
                    for element, index in zip(elements[0], indexes[0]):
                        # 무한댓값 없고 원이 겹치지 않으면 루프 탈출
                        if not np.isinf(element) and circle_intersection(circle, circles[index]):
                            break
                    else:
                        break
                    tries += 1
            else:
                while any(circle_intersection(circle, circle2) for circle2 in circles):
                    tries += 1
                    circle = generate_circle(width, height, min_diameter, max_diameter)

            print('{}/{} {}'.format(i, TOTAL_CIRCLES, tries))

            circles.append(circle)
            circle_draw(draw_image, image, circle, target_num)
    except (KeyboardInterrupt, SystemExit):
        pass

    image2.show()
    # 생성된 색약 이미지를 띄워줌
    image2.save('./sample_output/new_colorblindness_sample.jpg')
    # 생성된 색약 이미지 저장


if __name__ == '__main__':
    main()