log_list = [
    'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
    'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
    'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
    'May 20 11:01:12 PC-00102 PackageKit: daemon start',
    'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
    'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
    'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
    'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
    'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
    'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'
]
list_log_dict = []
s2 = (a.split() for a in log_list)
for lst in s2:
    log_dict = {
        'time': " ".join(lst[:3]),
        'pc_name': "".join(lst[3]),
        'service_name': "".join(lst[4][:-1]),
        'message': " ".join(lst[5:])
    }
    list_log_dict.append(log_dict)
print(list(i['time'] for i in list_log_dict)) # РЕШЕНИЕ
dates = {}
times = {}
l = []
for elem in list_log_dict:
    dates['date']=elem['time'][:6]
    times['time']=elem['time'][7:16]
    elem.update(dates)
    elem.update(times)
    l.append(elem)
print(list(item.get("time") for item in l))
print(list(msg.get("message") for msg in l if msg['pc_name']=='PC0078'))
list_log_dict_new = [100,101,102,103,104,105,106,107,108,109,110] #Тут конечно нужен генератор, пока по простому
list_dict_new = dict(zip(list_log_dict_new, log_list))
print(list_dict_new[104])
