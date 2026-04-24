basic.show_icon(IconNames.CONFUSED)
basic.show_leds("""
    . . # . .
    . # # # .
    # . # . #
    . . # . .
    . . # . .
    """)
basic.pause(200)
pins.servo_write_pin(AnalogPin.P0, 0)
basic.pause(500)
pins.servo_write_pin(AnalogPin.P0, 90)
basic.pause(500)
basic.show_leds("""
    . . # . .
    . . # . .
    # . # . #
    . # # # .
    . . # . .
    """)
pins.servo_write_pin(AnalogPin.P12, 0)
basic.pause(500)
pins.servo_write_pin(AnalogPin.P12, 90)
basic.pause(500)

def on_forever():
    basic.show_icon(IconNames.YES)
basic.forever(on_forever)
