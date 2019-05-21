color = lambda c: ((c >> 16) & 255, (c >> 8) & 255, c & 255)

# ----------------- Standard of color-blindness test table ------------------

COLORS_ON = [
    [],
    [color(0xD98D53)],  # orange_number1
    [
        [color(0x9E635B), color(0xC5817E), color(0xEAA095)],  # pink
        [color(0x9A7C56), color(0xC99F6D), color(0xEAB77E)],  # brown
        [color(0x62937E), color(0x96d1bb), color(0xb3e0cc)]  # green
    ],  # number2
    [
        [color(0x9E635B), color(0xC5817E), color(0xEAA095)],  # pink
        [color(0x9A7C56), color(0xC99F6D), color(0xEAB77E)],  # brown
        [color(0x62937E), color(0x96d1bb), color(0xb3e0cc)]  # green
    ],  # number3
    [
        [color(0x29a58f), color(0x62d1bf), color(0x93d6c6)],  # cyan
        [color(0x7E8B5F), color(0x899668), color(0xA0AA6D)],  # green
        [color(0x9E635B), color(0xC5817E), color(0xEAA095)],  # pink
    ],  # number4
    [
        [color(0x29a58f), color(0x62d1bf), color(0x93d6c6)],  # cyan
        [color(0x7E8B5F), color(0x899668), color(0xA0AA6D)],  # green
        [color(0x9E635B), color(0xC5817E), color(0xEAA095)],  # pink
    ],  # number5
    [color(0xccb186), color(0xe0bb84), color(0xfcce81)],  # brown_number6
    [color(0xccb186), color(0xe0bb84), color(0xfcce81)],  # brown_number7
    [color(0x7E8B5F), color(0x899668), color(0xA0AA6D)],  # green_number8
    [
        [color(0x747570)],
        [color(0xAC766C)],
        [color(0x558669)]
    ],  # number9
    [
        [color(0x585B46), color(0x62684E), color(0x88906B)],  # green
        [color(0x554262), color(0x837090)]  # purple
    ],  # number10
    [
        [color(0x418377), color(0x5FA398), color(0x86B1A7)],  # cyan
        [color(0x7E8B5F), color(0x899668), color(0xA0AA6D)],  # green
        [color(0x9E635B), color(0xC5817E), color(0xEAA095)]  # pink
    ],  # number11
    [color(0x8A6C46), color(0xB29261), color(0xCCA36B)],  # brown_number12
    [
        [color(0xc37279), color(0xc66a6f), color(0xf09695)],  # pink
        [color(0x006e61), color(0x298270), color(0x46ab99)]  # cyan
    ],  # number13
    [
        [color(0xc37279), color(0xc66a6f), color(0xf09695)],  # pink
        [color(0x006e61), color(0x298270), color(0x46ab99)]  # cyan
    ],  # number14
    [
        [color(0x8d5554), color(0xa47472), color(0xc98987)],  # weak pink
        [color(0x668878), color(0x6b968c), color(0x87b2a9)]  # weak cyan
    ],  # number15
    [
        [color(0x8d5554), color(0xa47472), color(0xc98987)],  # weak pink
        [color(0x668878), color(0x6b968c), color(0x87b2a9)]  # weak cyan
    ],  # number16
    [
        [color(0x846560), color(0x9E7D78), color(0xB08F88)],  # very weak pink
        [color(0x49594E), color(0x5D6F63), color(0x6B8778)]  # very weak cyan
    ],  # number17
    [
        [color(0x846560), color(0x9E7D78), color(0xB08F88)],  # very weak pink
        [color(0x49594E), color(0x5D6F63), color(0x6B8778)] # very weak cyan
    ],  # number18
    [
        [color(0xc37279), color(0xc66a6f), color(0xf09695)],  # pink
        [color(0x006e61), color(0x298270), color(0x46ab99)]  # cyan
    ],  # number19
    [
        [color(0x8d5554), color(0xa47472), color(0xc98987)],  # weak pink
        [color(0x668878), color(0x6b968c), color(0x87b2a9)]  # weak cyan
    ],  # number20
    [
        [color(0x846560), color(0x9E7D78), color(0xB08F88)],  # very weak pink
        [color(0x49594E), color(0x5D6F63), color(0x6B8778)]  # very weak cyan
    ]  # number21
]

COLORS_OFF = [
    [],
    [
        [color(0x82837D)],
        [color(0x82837D)]
    ],  # gray_number1
    [color(0x768A57), color(0xADC277)],  # number2
    [color(0x8ea068), color(0x92a361), color(0xc1db7a)],  # green_number3
    [color(0xccb186), color(0xe0bb84), color(0xfcce81)],  # brown_number4
    [color(0xccb186), color(0xe0bb84), color(0xfcce81)],  # brown_number5
    [
        [color(0x8ea068), color(0x92a361), color(0xc1db7a)],  # green
        [color(0x418377), color(0x5FA398), color(0x86B1A7)]  # cyan
    ],  # number6
    [
        [color(0x8ea068), color(0x92a361), color(0xc1db7a)],  # green
        [color(0x418377), color(0x5FA398), color(0x86B1A7)]  # cyan
    ],  # number7
    [
        [color(0xccb186), color(0xe0bb84), color(0xfcce81)],  # brown
        [color(0x9E635B), color(0xC5817E), color(0xEAA095)]  # pink
    ],  # number8
    [
        [color(0xAF6042)],
        [color(0x6A6D42), color(0x614A3A), color(0x996D46)]
     ],  # number9
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number10
    [color(0x8A6C46), color(0xB29261), color(0xCCA36B)],  # brown_number11
    [
        [color(0x62937E), color(0x96d1bb), color(0xb3e0cc)],  # green
        [color(0x418377), color(0x5FA398), color(0x86B1A7)]  # cyan
    ],  # number12
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number13
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number14
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number15
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number16
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number17
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number18
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number19
    [color(0x464847), color(0x6A6A6A), color(0x969799)],  # gray_number20
    [color(0x464847), color(0x6A6A6A), color(0x969799)]  # gray_number21
]
