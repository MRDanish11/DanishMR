
import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<Danish KING>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[•] Subscribe this my YouTube channel {white}')
    os.system('xdg-open https://www.youtube.com/@user-wd6ev1lz1k')
    time.sleep(0.05)
    import trt1
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
