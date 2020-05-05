# weather-station
project for making a weather station from a [sparkfun weatherbit](https://www.sparkfun.com/products/16274) and [raspberry pi zero W](https://www.amazon.com/gp/product/B0748MPQT4/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1)
**Disclaimer**
I'm not great a programming, most of this code was written using a combination of trial and error as well as lots of googling and help from friends, you may be a better programmer and have a better way of doing this. I'm open to pull requestes to
fix any idiotic mistakes that you may find. With that said, this is a good project for hobby tinkerers and for parents that want to expose their kids to programming and electronics as a hobby.

# Requirements for the current implementation:
1. [Sparkfun Weatherbit](https://www.sparkfun.com/products/16274)
2. [Raspberry Pi Zero W](https://www.amazon.com/gp/product/B0748MPQT4/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1)
3. [IP65 outdoor enclosure](https://www.amazon.com/gp/product/B0786ZLFSV/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1)

# I'm using solar to power my set up, here is a list of what I purchased
1. [100W solar panel](https://www.amazon.com/gp/product/B01HHDC6NQ/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1) - This doesn't need to be 100W as the combined power draw is liked tan 40W but I will have multiple projects running on my solar set up so I went big with plans to scale to 300W in the future.
2. [1 to 4 solar panel adaptor](https://www.amazon.com/gp/product/B07B4ZM8Y8/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1) - Same as above this is specific to my setup
3. [ Seal Lead Acid Batteries](https://www.amazon.com/gp/product/B00X01LSIO/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) - Specific to my set up, 1 batter should be enough. If you're only running this project a smaller battery or even a different battery type such as Li-Ion or LiPo should work
4. [USB Mini to USB Mini JTAG cable](https://www.amazon.com/gp/product/B01KG1696G/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) - The pi zero W doesn't have a full size USB port. If you buy a 3B+ or 4 then a standard USB (phone) charging cable will work
5. [USB charing cable](https://www.amazon.com/AmazonBasics-Cable-adaptador-macho-Micro/dp/B0711PVX6Z/ref=sxin_2_ac_d_rm?ac_md=1-1-bWljcm8gdXNiIGNhYmxl-ac_d_rm&crid=HRT7KFD43TPW&cv_ct_cx=usb+charger+cable&dchild=1&keywords=usb+charger+cable&pd_rd_i=B0711PVX6Z&pd_rd_r=5fdb8512-c33a-4448-a5c1-af0c271a62bf&pd_rd_w=uN7Ff&pd_rd_wg=Xa4m7&pf_rd_p=165462b8-b004-445b-8c70-cf9e9e805494&pf_rd_r=901ECWAD9N747FHGVRDQ&psc=1&qid=1588696349&sprefix=usb+char%2Caps%2C144&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081) - Standard phone charging cable to power the Pi
6. [Solar Charge Controller](https://www.ebay.com/itm/MPPT-Solar-Panel-Regulator-Charge-Controller-Auto-Focus-Tracking-30-100A-12V-24V/274215536376?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D225073%26meid%3D91e584c2f4bd49d288365a1b2d796e8a%26pid%3D100675%26rk%3D1%26rkt%3D15%26mehot%3Dpp%26sd%3D274215536376%26itm%3D274215536376%26pmt%3D1%26noa%3D1%26pg%3D2380057%26brand%3DUnbranded&_trksid=p2380057.c100675.m4236&_trkparms=pageci%3A2290b1be-8eee-11ea-86cb-74dbd1806a6d%7Cparentrq%3Ae5af48a31710aa66c6b0dbc1ffb87964%7Ciid%3A1) - Specific to my set up. If going solar you will need something like this to control charging and discharging of the battery. I have the 100A model for my requirements and a bit of head room for the possiblity of going with a 1KW panel in the future
7. [male USB to DIP adapter ](https://www.ebay.com/itm/5-PCS-male-USB-to-DIP-adapter-for-2-54mm-DIY-PCB-board-converter-4-pins/173963249674?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649) - To provide power to the Buck Converter
8. [4 USB 24V/12V to 5V 5A Step-down Buck Power Supply Module Converter Board+Case](https://www.ebay.com/itm/4-USB-24V-12V-to-5V-5A-Step-down-Buck-Power-Supply-Module-Converter-Board-Case/401773626602?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649) - To step down the 12V DC coming from the charge controller output to 5V required by the Pi. you can use something like [this](https://www.ebay.com/itm/DC-DC-Buck-step-down-Converter-6-24V-12V-24V-to-5V-3A-CAR-USB-Charger-Modul/262993129657?hash=item3d3b9cb0b9:m:ms3N-XdpxLH570LbkMVLTnw) if you only need a single usb output
9. [Solar Panel Extension Cable](https://www.ebay.com/itm/New-1-Pair-Black-Red-Solar-Panel-Extension-Cable-Wire-Connector-12-10-AWG/143333611997?ssPageName=STRK%3AMEBIDX%3AIT&var=442244232297&_trksid=p2057872.m2749.l2649) - may or may not need depending on how far away your panel(s) is from your charge controller
10.[10 GAUGE INLINE MAXI FUSE HOLDER WITH 30 AMP FUSE](https://www.ebay.com/itm/10-GAUGE-INLINE-MAXI-FUSE-HOLDER-WITH-30-AMP-FUSE-Water-Proof-Made-in-USA/383204145220?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649) - Extra protection for your battery(s) size as appropriate to your needs

**None of these links are affiliate links so feel free to shop around.**
#Python
* Python 3+
* PySerial
* Influxdb (optional)
* pika (optional)
