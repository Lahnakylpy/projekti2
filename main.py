MoottoriPäällä = 0
Suoritetaan = 0
MoottorinVoima = 0

def on_button_pressed_a():
    global Suoritetaan, MoottorinVoima
    if MoottoriPäällä == 1:
        if Suoritetaan == 0:
            Suoritetaan = 1
            for index in range(2):
                basic.pause(1000)
                MoottorinVoima = 12
                basic.pause(1000)
                MoottorinVoima = 54
                basic.pause(1000)
                MoottorinVoima = 126
                basic.pause(1000)
                MoottorinVoima = 255
                basic.pause(1000)
                MoottorinVoima = 600
                basic.pause(2000)
                MoottorinVoima = 0
            Suoritetaan = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global MoottoriPäällä
    if MoottoriPäällä == 1:
        MoottoriPäällä = 0
    else:
        MoottoriPäällä = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if MoottoriPäällä == 1:
        pins.analog_write_pin(AnalogPin.P0, MoottorinVoima)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
basic.forever(on_forever)
