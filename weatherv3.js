let humid = 0
let tempF = 0
let preasure = 0
let temp = 0
let current_WindDirection_List = ""
let current_WindSpeed = 0
let rain = 0
let item = false
let itemT = 0
let rainData = " "
serial.redirectToUSB()
weatherbit.startWindMonitoring()
weatherbit.startWeatherMonitoring()
weatherbit.startRainMonitoring()
basic.forever(function () {
    current_WindSpeed = Math.trunc(weatherbit.windSpeed())
    current_WindDirection_List = weatherbit.windDirection()
    temp = Math.idiv(weatherbit.temperature(), 100)
    preasure = Math.idiv(weatherbit.pressure(), 25600)
    tempF = temp * 9 / 5 + 32
    humid = Math.idiv(weatherbit.humidity(), 1024)
    rain = weatherbit.rain()
    if (rain > 1) {
        rainData = rain.toString()
    } else {
        rainData = null
    }
    serial.writeLine("" + current_WindSpeed + "," + current_WindDirection_List + "," + temp + "," + tempF + "," + humid + "," + preasure + "," + rainData)
    basic.pause(1 * 3000)
})
