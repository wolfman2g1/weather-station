let rain = 0
let humid = 0
let temp = 0
let current_WindDirection_List = ""
let current_WindSpeed = 0
let item = false
let tempF = 0
let itemT = 0
serial.redirectToUSB()
weatherbit.startWindMonitoring()
weatherbit.startWeatherMonitoring()
weatherbit.startRainMonitoring()
basic.forever(function () {
    current_WindSpeed = Math.trunc(weatherbit.windSpeed())
    current_WindDirection_List = weatherbit.windDirection()
    temp = Math.idiv(weatherbit.temperature(), 100)
    tempF = temp * 9 / 5 + 32
    humid = Math.idiv(weatherbit.humidity(), 1024)
    serial.writeLine("Wind" + " " + current_WindSpeed + "," +
        "Direction" + " " + current_WindDirection_List + "," +
        "Temp" + " " + temp + "," +
        "TempF" + " " + tempF + "," +
        "Humidity" + " " + humid)
    rain = weatherbit.rain()
    if (rain < 1) {
        serial.writeLine("Not Raining")
    } else {
        serial.writeLine("Rain" + " " + rain)
    }
    basic.pause(1 * 30000)
})
