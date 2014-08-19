__author__ = 'Umair'

# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(in_seconds):
    hours = int(in_seconds / 60 / 60)
    hours_in_sec = hours * 60 * 60
    mins = int((in_seconds - hours_in_sec) / 60)
    mins_in_sec = mins * 60
    sec = round(in_seconds - (hours_in_sec + mins_in_sec), 1)
    sec = int(sec) if sec % 1 == 0 else sec
    label_hours = "hours" if hours > 1 or hours == 0 else "hour"
    label_min = "minutes" if mins > 1 or mins == 0 else "minute"
    label_sec = "seconds" if sec > 1 or sec == 0 else "second"
    return str(int(hours)) + " " + label_hours + ", " + str(int(mins)) + " " + label_min + ", " + str(
        sec) + " " + label_sec


print(convert_seconds(1000))

print(convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print(convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds