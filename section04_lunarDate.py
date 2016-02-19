from lunardate import LunarDate

# print LunarDate.fromSolarDate(2016, 1, 30)
# print LunarDate(2016, 1, 1, 0).toSolarDate()

solar_date = LunarDate(2016,1,1).toSolarDate()
print solar_date