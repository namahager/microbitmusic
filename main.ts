radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        音の回数 += 1
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c1, 音の回数)
    } else if (receivedNumber == 2) {
        音の回数 += 1
        music.play(music.tonePlayable(294, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c2, 音の回数)
    } else if (receivedNumber == 3) {
        音の回数 += 1
        music.play(music.tonePlayable(330, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c3, 音の回数)
    } else if (receivedNumber == 4) {
        音の回数 += 1
        music.play(music.tonePlayable(349, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c4, 音の回数)
    } else if (receivedNumber == 5) {
        音の回数 += 1
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c5, 音の回数)
    } else if (receivedNumber == 6) {
        音の回数 += 1
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c6, 音の回数)
    } else if (receivedNumber == 7) {
        音の回数 += 1
        music.play(music.tonePlayable(494, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c7, 音の回数)
    } else if (receivedNumber == 8) {
        音の回数 += 1
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        makerbit.lcdShowCharacter1602(LcdChar.c8, 音の回数)
    }
    basic.pause(100)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "開始") {
        servos.P1.run(5)
        servos.P0.run(5)
    } else if (receivedString == "停止") {
        servos.P0.stop()
        servos.P1.stop()
    }
})
let 音の回数 = 0
radio.setGroup(1)
makerbit.clearLcd1602()
makerbit.connectLcd(39)
音の回数 = 0
makerbit.lcdMakeCharacter(LcdChar.c1, makerbit.lcdCharacterPixels(`
    # . . # .
    # . . . #
    # . . . .
    # # . . .
    # . # . .
    # . . # .
    # . . . .
    # . . . .
    `))
makerbit.lcdMakeCharacter(LcdChar.c2, makerbit.lcdCharacterPixels(`
    . # . . .
    . # . . .
    . # . . .
    . # . . .
    . # . . #
    . # . # .
    . # # . .
    . # . . .
    `))
makerbit.lcdMakeCharacter(LcdChar.c3, makerbit.lcdCharacterPixels(`
    # # # . .
    . . # # #
    . . . . .
    # # # . .
    . . # # #
    . . . . .
    # # # . .
    . . # # #
    `))
makerbit.lcdMakeCharacter(LcdChar.c4, makerbit.lcdCharacterPixels(`
    . . . . .
    # # # # .
    . . . # .
    . . # . .
    . # . . .
    # . # # #
    . . . # #
    . . . # .
    `))
makerbit.lcdMakeCharacter(LcdChar.c5, makerbit.lcdCharacterPixels(`
    . . . . .
    # . . . #
    . # . . #
    . . . . #
    . . . # .
    . . # . .
    # # . . .
    . . . . .
    `))
makerbit.lcdMakeCharacter(LcdChar.c6, makerbit.lcdCharacterPixels(`
    . . . . .
    . # # # .
    . . . . .
    # # # # #
    . . . . #
    . . . . #
    . . . # .
    # # # . .
    `))
makerbit.lcdMakeCharacter(LcdChar.c7, makerbit.lcdCharacterPixels(`
    . . . . .
    # # # . #
    . . . . #
    # # # . #
    . . . . #
    . . . . #
    . . . # .
    # # # . .
    `))
makerbit.lcdMakeCharacter(LcdChar.c8, makerbit.lcdCharacterPixels(`
    # . . # .
    # . . . #
    # . . . .
    # # . . .
    # . # . .
    # . . # .
    # . . . .
    # . . . .
    `))
