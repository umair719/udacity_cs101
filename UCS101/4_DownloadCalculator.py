__author__ = 'Umair'
# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print(2 ** 10)      # one kilobit, kb
#print(2 ** 10 * 8)  # one kilobyte, kB
#
#print(2 ** 20)      # one megabit, Mb
#print(2 ** 20 * 8)  # one megabyte, MB
#
#print(2 ** 30)      # one gigabit, Gb
#print(2 ** 30 * 8)  # one gigabyte, GB
#
#print(2 ** 40)      # one terabit, Tb
#print(2 ** 40 * 8)  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def download_time(fs, fs_unit, bw, bw_unit):
    #print("--------------")
    fs_in_bits = convert_to_bits(fs, fs_unit)
    bw_in_bits = convert_to_bits(bw, bw_unit)
    #print(fs_in_bits)
    #print(bw_in_bits)
    time_in_sec = fs_in_bits / bw_in_bits
    return convert_seconds(time_in_sec)


def convert_to_bits(size, unit):
    multiple = 1
    if unit[0] == 'k' or unit[0] == 'K':
        multiple = 10
    elif unit[0] == 'M':
        multiple = 20
    elif unit[0] == 'G':
        multiple = 30
    elif unit[0] == 'T':
        multiple = 40
    if unit[1] == 'B':
        return size * 2.0 ** multiple * 8
    else:
        return size * 2.0 ** multiple


def convert_seconds(in_seconds):
    print(in_seconds)
    hours = int(in_seconds / 60 / 60)
    hours_in_sec = hours * 60 * 60
    mins = int((in_seconds - hours_in_sec) / 60)
    mins_in_sec = mins * 60
    sec = in_seconds - (hours_in_sec + mins_in_sec)
    sec = int(sec) if sec % 1 == 0 else sec
    label_hours = "hours" if hours > 1 or hours == 0 else "hour"
    label_min = "minutes" if mins > 1 or mins == 0 else "minute"
    label_sec = "seconds" if sec > 1 or sec == 0 else "second"
    return str(int(hours)) + " " + label_hours + ", " + str(int(mins)) + " " + label_min + ", " + str(
        sec) + " " + label_sec


print(download_time(11, 'GB', 5, 'MB'))
# 0 hours, 37 minutes, 32.8 seconds

print(download_time(1024, 'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


