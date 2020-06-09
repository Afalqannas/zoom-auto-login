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



## Additional
- if you want to create a custom firefox profile go to this link for more information: https://support.mozilla.org/en-US/kb/profile-manager-create-remove-switch-firefox-profiles#w_creating-a-profile

### to convert python code to exe:
1- pip install pyinstaller 
2- open command prompt or anaconda prompt
3- pyinstaller -i zoom.ico -n ZoomAuto -w -F zoom_auto_login.py