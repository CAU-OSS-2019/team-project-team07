color = lambda c: ((c >> 16) & 255, (c >> 8) & 255, c & 255)

COLORS_ON = [   # 문자 색
    color(0xF9BB82), color(0xEBA170), color(0xFCCD84)
]
COLORS_OFF = [  # 배경 색
    color(0x9CA594), color(0xACB4A5), color(0xBBB964),
    color(0xD7DAAA), color(0xE5D57D), color(0xD1D6AF)
]
COLORS_TMP = [   # 문자 + 범위 임시색(11표)
    color(0x000000)
]

# --------------------한식 색각표 기준 -----------------

# number 1
COLORS_ON_1 = [
    color(0xD98D53)  # orange
]
COLORS_OFF_1 = [
    color(0x82837D)  # gray
]

# number 2
COLORS_ON_2 = [
    color(0x9E635B), color(0xC5817E), color(0xEAA095),  # pink
    color(0x9A7C56), color(0xC99F6D), color(0xEAB77E),  # brown
    color(0x62937E), color(0x78AF9C), color(0x97C4B0)  # green
]
COLORS_OFF_2 = [
    color(0x768A57), color(0xADC277)
]

# number 3
COLORS_ON_3 = [
    color(0x9E635B), color(0xC5817E), color(0xEAA095),  # pink
    color(0x9A7C56), color(0xC99F6D), color(0xEAB77E),  # brown
    color(0x62937E), color(0x78AF9C), color(0x97C4B0)  # green
]
COLORS_OFF_3 = [
    color(0x60703F), color(0x6F7F41), color(0x8DA253)  # green
]

# number 4
COLORS_ON_4 = [
    color(0x418377), color(0x5FA398), color(0x86B1A7),  # cyan
    color(0x7E8B5F), color(0x899668), color(0xA0AA6D),  # green
    color(0xA26962), color(0xC0908E), color(0xE0A3A0)  # pink
]
COLORS_OFF_4 = [
    color(0x987A53), color(0xB68C5A), color(0xD5A156)  # brown
]

# number 5
COLORS_ON_5 = [
    color(0x418377), color(0x5FA398), color(0x86B1A7),  # cyan
    color(0x7E8B5F), color(0x899668), color(0xA0AA6D)  # green
]
COLORS_OFF_5 = [
    color(0x8A6C46), color(0xB29261), color(0xCCA36B)  # brown
]

# number 6
COLORS_ON_6 = [
    color(0x8A6C46), color(0xB29261), color(0xCCA36B)  # brown
]
COLORS_OFF_6 = [
    color(0x60703F), color(0x6F7F41), color(0x8DA253),  # green
    color(0x418377), color(0x5FA398), color(0x86B1A7)  # cyan
]

# number 7
COLORS_ON_7 = [
    color(0x8A6C46), color(0xB29261), color(0xCCA36B)  # brown
]
COLORS_OFF_7 = [
    color(0x60703F), color(0x6F7F41), color(0x8DA253),  # green
    color(0x418377), color(0x5FA398), color(0x86B1A7)  # cyan
]

# number 8
COLORS_ON_8 = [
    color(0x7E8B5F), color(0x899668), color(0xA0AA6D)  # green
]
COLORS_OFF_8 = [
    color(0x8A6C46), color(0xB29261), color(0xCCA36B),  # brown
    color(0x9E635B), color(0xC5817E), color(0xEAA095)  # pink
]

# number 9
COLORS_ON_9 = [
    color(0x747570), color(0xAC766C), color(0x558669)
]
COLORS_OFF_9 = [
    color(0x6A6D42), color(0xAF6042), color(0x614A3A), color(0x996D46)
]

# number 10
COLORS_ON_10_1 = [
    color(0x585B46), color(0x62684E), color(0x88906B)  # green
]
COLORS_ON_10_2 = [
    color(0x554262), color(0x837090)  # purple
]
COLORS_OFF_10 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 11
COLORS_ON_11 = [
    color(0x418377), color(0x5FA398), color(0x86B1A7),  # cyan
    color(0x7E8B5F), color(0x899668), color(0xA0AA6D),  # green
    color(0x9E635B), color(0xC5817E), color(0xEAA095)  # pink
]
COLORS_OFF_11 = [
    color(0x8A6C46), color(0xB29261), color(0xCCA36B)  # brown
]

# number 12
COLORS_ON_12 = [
    color(0x8A6C46), color(0xB29261), color(0xCCA36B)  # brown
]
COLORS_OFF_12 = [
    color(0x62937E), color(0x78AF9C), color(0x97C4B0),  # green
    color(0x418377), color(0x5FA398), color(0x86B1A7)  # cyan
]

# number 13
COLORS_ON_13_1 = [
    color(0x9E635B), color(0xC5817E), color(0xEAA095)  # pink
]
COLORS_ON_13_2 = [
    color(0x0E6A5D), color(0x2E7F70), color(0x4A9380)  # cyan
]
COLORS_OFF_13 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 14
COLORS_ON_14_1 = [
    color(0x9E635B), color(0xC5817E), color(0xEAA095)  # pink
]
COLORS_ON_14_2 = [
    color(0x0E6A5D), color(0x2E7F70), color(0x4A9380)  # cyan
]
COLORS_OFF_14 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 15
COLORS_ON_15_1 = [
    color(0x7C5A58), color(0x956865), color(0xAE7E74)  # weak pink
]
COLORS_ON_15_2 = [
    color(0x466458), color(0x517363), color(0x6F8B7C)  # weak cyan
]
COLORS_OFF_15 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 16
COLORS_ON_16_1 = [
    color(0x7C5A58), color(0x956865), color(0xAE7E74)  # weak pink
]
COLORS_ON_16_2 = [
    color(0x466458), color(0x517363), color(0x6F8B7C)  # weak cyan
]
COLORS_OFF_16 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 17
COLORS_ON_17_1 = [
    color(0x846560), color(0x9E7D78), color(0xB08F88)  # very weak pink
]
COLORS_ON_17_2 = [
    color(0x49594E), color(0x5D6F63), color(0x6B8778)  # very weak cyan
]
COLORS_OFF_17 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 18
COLORS_ON_18_1 = [
    color(0x846560), color(0x9E7D78), color(0xB08F88)  # very weak pink
]
COLORS_ON_18_2 = [
    color(0x49594E), color(0x5D6F63), color(0x6B8778)  # very weak cyan
]
COLORS_OFF_18 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 19
COLORS_ON_19_1 = [
    color(0x9E635B), color(0xC5817E), color(0xEAA095)  # pink
]
COLORS_ON_19_2 = [
    color(0x0E6A5D), color(0x2E7F70), color(0x4A9380)  # cyan
]
COLORS_OFF_19 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 20
COLORS_ON_20_1 = [
    color(0x7C5A58), color(0x956865), color(0xAE7E74)  # weak pink
]
COLORS_ON_20_2 = [
    color(0x466458), color(0x517363), color(0x6F8B7C)  # weak cyan
]
COLORS_OFF_20 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]

# number 21
COLORS_ON_21_1 = [
    color(0x846560), color(0x9E7D78), color(0xB08F88)  # very weak pink
]
COLORS_ON_21_2 = [
    color(0x49594E), color(0x5D6F63), color(0x6B8778)  # very weak cyan
]
COLORS_OFF_21 = [
    color(0x464847), color(0x6A6A6A), color(0x969799)  # gray
]