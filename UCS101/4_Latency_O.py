__author__ = 'Umair'

# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.0  # km per second


def speed_fraction(time_in_ms, distance_in_km):
    time_in_sec = time_in_ms / 1000
    total_distance_in_km = 2 * distance_in_km
    speed_data_travels = total_distance_in_km / time_in_sec
    return speed_data_travels / speed_of_light


print(speed_fraction(50.0, 5000.0))
#>>> 0.666666666667

print(speed_fraction(50.0, 10000.0))
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?
