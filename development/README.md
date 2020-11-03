# Requirements for development:

- python 3

## libraries
- selenium
- tkinter
- datetime
- Timer
- os

Also you need to download firefox webdriver from here: https://github.com/mozilla/geckodriver/releases
(or use the copy in firefox_driver folder)

### Note:
- when you run 'ZoomAuto.exe' the two folders 'firefox_driver' and 'o253xtdm.zoom_auto' should be in the same path with 'ZoomAuto.exe' 

## Additional
- if you want to create a custom firefox profile go to this link for more information: https://support.mozilla.org/en-US/kb/profile-manager-create-remove-switch-firefox-profiles#w_creating-a-profile

### to convert python code to exe:
- open command prompt or anaconda prompt
- pip install pyinstaller 
- pyinstaller -i zoom.ico -n ZoomAuto -w -F zoom_auto_login.py
