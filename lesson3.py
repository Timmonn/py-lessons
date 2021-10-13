from hurry.filesize import size
dict_0 = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]
drive_number = int(input('Enter drive number 0-6 : '))
fmt = dict_0[drive_number][('total')]
fmu = dict_0[drive_number][('used')]
sz = size(fmt - fmu)
pcnt = '{0:.1f}'.format(fmu*100/fmt)
print(f'Free space in drive {drive_number} is: ', sz, 'or', pcnt, '%')