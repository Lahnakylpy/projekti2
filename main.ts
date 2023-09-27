input.onButtonPressed(Button.A, function () {
    if (MoottoriPäällä == 1) {
        for (let index = 0; index < 350; index++) {
            basic.pause(25)
            MoottorinVoima += 1
        }
        for (let index = 0; index < 350; index++) {
            basic.pause(75)
            MoottorinVoima += -1
        }
        MoottorinVoima = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (MoottoriPäällä == 1) {
        MoottoriPäällä = 0
    } else {
        MoottoriPäällä = 1
    }
})
let MoottorinVoima = 0
let MoottoriPäällä = 0
MoottoriPäällä = 1
basic.forever(function () {
    basic.showNumber(MoottorinVoima)
    if (MoottoriPäällä == 1) {
        pins.analogWritePin(AnalogPin.P0, MoottorinVoima)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
})
