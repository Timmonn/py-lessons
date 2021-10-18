from hurry.filesize import size
dict_0 = [
    {'total': 999_641_890_816, 'used': 228_013_805_568}, #771_628_085_248
    {'total': 61_686_008_768, 'used': 52_522_710_872}, #9_163_297_896
    {'total': 149_023_482_194, 'used': 83_612_310_700}, #65_411_171_494
    {'total': 498_830_397_039, 'used': 459_995_976_927}, #38_834_420_112
    {'total': 93_386_008_768, 'used': 65_371_350_065}, #28_014_658_703
    {'total': 988_242_468_378, 'used': 892_424_683_789}, #95_817_784_589
    {'total': 49_705_846_287, 'used': 9_522_710_872}, #40_183_135_415
]
drv_num = int(input('Enter drive number 0-6 : '))
if drv_num < 0 or drv_num > 6:
    print("I' told you 0-6 !!!")
fmt = dict_0[drv_num][('total')]
fmu = dict_0[drv_num][('used')]
sz = (fmt - fmu)
print(sz)
pcnt = '{0:.1f}'.format(100-fmu*100/fmt)
print(pcnt)
if int(float(sz)) < 10_737_418_240 or int(float(pcnt) < 5):
    print(f'In drive {drv_num} critical low free space')
elif int(float(sz)) > 10_737_418_240 and int(float(sz)) < 32_212_254_725 or int(float(pcnt)) < 10:
    print(f'In drive {drv_num} low free space')
else:
    print(f'In drive {drv_num} enough free space')
sz = size(fmt-fmu)
print(f'Free space in drive {drv_num} is: ', sz, 'or', pcnt,'%')