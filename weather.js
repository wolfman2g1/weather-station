let current_WindDirection_List = ""
let current_WindSpeed = 0
let itemT = 0
let temp = 0
let humid = 0
let preasure = 0
let item = false
let rain = 0
serial.redirectToUSB()
weatherbit.startWindMonitoring()
weatherbit.startWeatherMonitoring()
weatherbit.startRainMonitoring()
basic.forever(function () {
    current_WindSpeed = weatherbit.windSpeed()
    current_WindDirection_List = weatherbit.windDirection()
    if (item) {
        basic.showString("Speed")
        basic.showNumber(Math.trunc(current_WindSpeed))
    } else {
        basic.showString("Dir")
        basic.showString(current_WindDirection_List)
    }
    serial.writeLine("Speed" + " " + current_WindSpeed + "," + "Direction" + " " + current_WindDirection_List)
    if (itemT == 0) {
        basic.showString("Temp C: ")
        basic.showNumber(Math.idiv(weatherbit.temperature(), 100))
        temp = Math.idiv(weatherbit.temperature(), 100)
    } else if (itemT == 1) {
        basic.showString("Humidity %: ")
        basic.showNumber(Math.idiv(weatherbit.humidity(), 1024))
        humid = Math.idiv(weatherbit.humidity(), 1024)

    } else if (itemT == 2) {
        basic.showString("Pressure hPa: ")
        basic.showNumber(Math.idiv(weatherbit.pressure(), 25600))
        preasure = Math.idiv(weatherbit.pressure(), 25600)
    } else {
        itemT = 0
    }
    serial.writeLine("Temp" + " " + temp + "," + "Humidity" + " " + humid + "," + preasure)
    rain = weatherbit.rain()
    if (rain < 1) {
        serial.writeLine("Not Raining")
    } else {
        serial.writeLine("Rain" + " " + rain)
    }
})
