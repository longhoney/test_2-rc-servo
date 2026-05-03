basic.showIcon(IconNames.Confused)
basic.showLeds(`
    . . . . .
    . . . . .
    # # # . .
    . . . . .
    . . . . .
    `)
basic.pause(200)
pins.servoWritePin(AnalogPin.P0, 0)
basic.pause(500)
pins.servoWritePin(AnalogPin.P0, 90)
basic.pause(500)
basic.showLeds(`
    . . # . .
    . . # . .
    . . # . .
    . . . . .
    . . . . .
    `)
pins.servoWritePin(AnalogPin.P12, 0)
basic.pause(500)
pins.servoWritePin(AnalogPin.P12, 90)
basic.pause(500)
basic.showIcon(IconNames.Yes)
