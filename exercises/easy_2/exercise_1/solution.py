DEGREE_SYMBOL = "\u00B0"
MINUTE_SYMBOL = "'"
SECOND_SYMBOL = '"'
MINS_IN_DEGREE = 60
SECS_IN_MIN = 60
DEGREES_IN_CIRCLE = 360

def fmt_dms(degrees, minutes, seconds):
    return (f"{degrees}{DEGREE_SYMBOL}{minutes:02d}{MINUTE_SYMBOL}"
            f"{seconds:02d}{SECOND_SYMBOL}")

def get_mins(degrees):
    return degrees * MINS_IN_DEGREE

def get_secs(mins):
    return int(mins * SECS_IN_MIN)

def get_normalised_degrees(degrees):
    return degrees % DEGREES_IN_CIRCLE

def dms(degrees_num):
    norm_degrees = get_normalised_degrees(degrees_num)
    degrees = int(norm_degrees)
    degrees_fractional_part = norm_degrees - degrees

    mins_num = get_mins(degrees_fractional_part)
    mins = int(mins_num)
    mins_fractional_part = mins_num - mins
    secs = get_secs(mins_fractional_part)
    result = fmt_dms(degrees, mins, secs)
    return result

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-1) == "359°00'00\"")
print(dms(400) == "40°00'00\"")
print(dms(-40) == "320°00'00\"")
print(dms(-420) == "300°00'00\"")
print(dms(-1.5) == "358°30'00\"")
print(dms(-90) == "270°00'00\"")
print(dms(90) == "90°00'00\"")