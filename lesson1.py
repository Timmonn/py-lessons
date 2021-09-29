log_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print (log_str[:15]) #1.1
print (log_str[24:34]) #1.2
print (log_str.replace('ideapad', 'PC-12092')) #1.3
print (log_str.find('failed')) #1.4
print ('Letter "S" is: ',log_str.lower().count('s')) #1.5
c = (log_str[7:15]).replace(':', '+') #1.6
c = eval(c)
print ('Sum three digits = ',c)
