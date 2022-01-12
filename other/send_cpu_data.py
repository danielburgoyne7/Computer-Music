import psutil, time
from pythonosc.udp_client import SimpleUDPClient

#SUPPORT FOR PSUTIL
#https://psutil.readthedocs.io/en/latest/

client = SimpleUDPClient("127.0.0.1",8000)

def Transmit(idle_delta):
  #send cpu usage percentage (overall)
  client.send_message("/cpu/usage/all",str(psutil.cpu_percent()))
  #send cpu usage percentages (per CPU)
  for index,item in enumerate(psutil.cpu_percent(interval=None,percpu=True)):
    client.send_message("/cpu/usage/"+str(index),str(item))
  #send battery percentage
  client.send_message("/cpu/battery/percent",str(psutil.sensors_battery().percent))
  client.send_message("/cpu/battery/secsleft",str(psutil.sensors_battery().secsleft))
  client.send_message("/cpu/battery/charging",psutil.sensors_battery().power_plugged)
  #send cpu idle time delta
  client.send_message("/cpu/idle_delta",str(idle_delta))
  #send cpu frequency (does not seem to change very often)
  client.send_message("/cpu/freq",str(psutil.cpu_freq().current))
  client.send_message("/memory",str(psutil.virtual_memory().percent))

def GetCPUIdleDelta(prev_idle):
  current_idle = psutil.cpu_times().idle
  idle_delta = current_idle - prev_idle
  return current_idle,idle_delta

idle = psutil.cpu_times().idle #init idle time
while True:
  time.sleep(0.05)
  idle,idle_delta = GetCPUIdleDelta(idle)
  Transmit(idle_delta) #send all data thru OSC

    prev_time = time.time()
