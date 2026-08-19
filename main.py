def on_received_number(receivedNumber):
    global 音の回数
    if receivedNumber == 1:
        音の回数 += 1
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C1, 音の回数)
    elif receivedNumber == 2:
        音の回数 += 1
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C2, 音の回数)
    elif receivedNumber == 3:
        音の回数 += 1
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C3, 音の回数)
    elif receivedNumber == 4:
        音の回数 += 1
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C4, 音の回数)
    elif receivedNumber == 5:
        音の回数 += 1
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C5, 音の回数)
    elif receivedNumber == 6:
        音の回数 += 1
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C6, 音の回数)
    elif receivedNumber == 7:
        音の回数 += 1
        music.play(music.tone_playable(494, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C7, 音の回数)
    elif receivedNumber == 8:
        音の回数 += 1
        music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        makerbit.lcd_show_character1602(LcdChar.C7, 音の回数)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    servos.P0.run(5)
    radio.send_string("開始")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    servos.P0.stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

音の回数 = 0
radio.set_group(1)
makerbit.clear_lcd1602()
makerbit.connect_lcd(39)
音の回数 = 0
makerbit.lcd_make_character(LcdChar.C1,
    makerbit.lcd_character_pixels("""
        # . . # .
        # . . . #
        # . . . .
        # # . . .
        # . # . .
        # . . # .
        # . . . .
        # . . . .
        """))
makerbit.lcd_make_character(LcdChar.C2,
    makerbit.lcd_character_pixels("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # . . #
        . # . # .
        . # # . .
        . # . . .
        """))
makerbit.lcd_make_character(LcdChar.C3,
    makerbit.lcd_character_pixels("""
        # # # . .
        . . # # #
        . . . . .
        # # # . .
        . . # # #
        . . . . .
        # # # . .
        . . # # #
        """))
makerbit.lcd_make_character(LcdChar.C4,
    makerbit.lcd_character_pixels("""
        . . . . .
        # # # # .
        . . . # .
        . . # . .
        . # . . .
        # . # # #
        . . . # #
        . . . # .
        """))
makerbit.lcd_make_character(LcdChar.C5,
    makerbit.lcd_character_pixels("""
        . . . . .
        # . . . #
        . # . . #
        . . . . #
        . . . # .
        . . # . .
        # # . . .
        . . . . .
        """))
makerbit.lcd_make_character(LcdChar.C6,
    makerbit.lcd_character_pixels("""
        . . . . .
        . # # # .
        . . . . .
        # # # # #
        . . . . #
        . . . . #
        . . . # .
        # # # . .
        """))
makerbit.lcd_make_character(LcdChar.C7,
    makerbit.lcd_character_pixels("""
        . . . . .
        # # # . #
        . . . . #
        # # # . #
        . . . . #
        . . . . #
        . . . # .
        # # # . .
        """))
makerbit.lcd_make_character(LcdChar.C8,
    makerbit.lcd_character_pixels("""
        # . . # .
        # . . . #
        # . . . .
        # # . . .
        # . # . .
        # . . # .
        # . . . .
        # . . . .
        """))