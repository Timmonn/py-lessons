s0 = ('May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated', 'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.', 'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...', 'May 20 11:01:12 PC-00102 PackageKit: daemon start', 'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...', 'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00', 'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"', 'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device', 'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio', 'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.', 'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.')
sn = int(input('Укажите строку от 0 до 10: '))
s2 = s0[sn].split()
dict0 = {'time':" ".join(s2[:3]), 'pc_name':"".join(s2[3]), 'service_name':"".join(s2[4]), 'message':" ".join(s2[5:])}
new_dict = {dict0['pc_name']:dict0['message']}
print(new_dict)
s3 = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
s4 = ['time', 'pc_name', 'service_name', 'message']
dict1 =dict(zip(s4, s3))
list_dict = [dict0, dict1]
print(list_dict)
set1 = set(list_dict[0])
set2 = set(list_dict[1])
print('list of identical values:', set1 & set2)
