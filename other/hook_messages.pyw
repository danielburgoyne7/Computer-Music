import sys
from pythonosc.udp_client import SimpleUDPClient
from pynput import mouse, keyboard

#SUPPORT FOR pyHook
#https://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/
#http://pyhook.sourceforge.net/doc_1.5.0/
#https://www.youtube.com/watch?v=8BiOPBsXh0g

#SUPPORT FOR PYNPUT
#https://pynput.readthedocs.io/en/latest/mouse.html

#SUPPORT FOR pythonosc
#https://www.youtube.com/watch?v=T3jd-894Ar4

def OnKeyboardEvent(event):
  try:
    client.send_message("/kb",str(event)) #send pressed key
  except AttributeError:
    print("AttributeError")

def OnMouseEvent(x,y,button,pressed):
  route = "/mouse"
  button = str(button)
  if button == "Button.left":
    route += "/left"
  elif button == "Button.middle":
    route += "/middle"
  elif button == "Button.right":
    route += "/right"
  client.send_message(route,str(int(pressed))) #send 1 if down or 0 if up

if __name__ == "__main__":
  client = SimpleUDPClient("127.0.0.1",8000)
  kb_listener = keyboard.Listener(on_press=OnKeyboardEvent)
  kb_listener.start()
  mouse_listener = mouse.Listener(on_click=OnMouseEvent)
  mouse_listener.start()
