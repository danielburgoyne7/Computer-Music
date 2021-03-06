# Computer-Music
'Computer Music' is an algorithmic, data-driven music program, written in Max and Python 3.7.

The program maps to music live data relating to the computer user,
their computer and the ways in which the two interact, utilising appropriated sonification
methods applied to algorithmic music.

The program is under further development.

![cm2](https://user-images.githubusercontent.com/90904328/149199805-93b75ccb-e6a3-46b6-a797-ba649b6824f4.png)

## HOW TO RUN THE COMPUTER MUSIC PROGRAM:
*Operating systems tested on:
Windows 10, Mac OSX El Capitan*

Required software:
- Max 8
- Required Max packages (can be installed within Max):
  - VIDDLL by Rob Ramirez (tested on v1.2.4)
  - CNMAT Externals (tested on v1.0.4)
  - RTC-lib by Karlheinz Essl (at least v7.1)
    - For Mac users, simply install from inside Max
    - For Windows users, download RTC-lib v7.1 from here: https://www.essl.at/works/rtc.html
- Python 3.7 (at least), with the IDLE (should be installed automatically)
- Required Python libraries (all can be remotely installed using ‘pip’ in the command prompt or
terminal; please use the latest version of pip; https://pip.pypa.io/en/stable/installing/#):
  - psutil (https://pypi.org/project/psutil/)
  - pynput (https://pypi.org/project/pynput/)
  - python-osc (https://pypi.org/project/python-osc/)

Instructions:
1. Make sure your router port 8000 is free (it likely is), as Python will need to send OSC
messages through it.
2. Launch two separate instances of the Python IDLE (search ‘IDLE’ in your Windows or
Spotlight search bar)
2a. (WINDOWS) - Launch one instance normally. In the taskbar, right-click the IDLE icon and
left-click the IDLE application (not the window you just opened). This should open a second
instance of the IDLE.
2b. (MAC) - Launch one instance normally. Open Terminal, type ‘idle3’ and hit return. This
should open a second instance of the IDLE.
3. In one instance of the IDLE, open and run the file ‘Computer
Music/other/hook_messages.pyw’. In the other instance, open and run the file ‘Computer
Music/other/send_cpu_data.py’.
4. Open ‘Computer Music/Computer Music.maxproj’. ‘Computer Music.maxpat’ should
automatically open.
KNOWN BUG:
pynput does not send keyboard ASCII values to Max on Mac OSX El Capitan 10.11.6


*Project created by Daniel Burgoyne*
