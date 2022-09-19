
class Redun:

  def __init__(self, gate1, int1, gate2, int2):
    self.gate1 = gate1
    self.int1 = int1
    self.gate2 = gate2
    self.int2 = int2

  def fail(self):
    print('Conection fail to gateway bla by interfaz bla')
  
  def succes(self):
    print('conection success to gateway '+ self.gate1 +' by interface '+ self.int1)

  def succes2(self):
    print('conection success to gateway '+ self.gate2 +' by interface '+ self.int2)
    












#hosts = ('8.8.8.8', 'kernel.org', 'yahoo.com')

#def ping(host):
#  ret = subprocess.call(['ping', '-c', '3', '-W', '5', host], stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
#  return ret == 0

#def net_is_up():
#  print(Checking if network is up % time.strftime("%Y-%m-%d %H:%M:%S")

#xtatus = 1

#  for h in hosts:
#    if ping(h):
#      print "[%s] Network is up!" % time.strftime("%Y-%m-%d %H:%M:%S")
#      xstatus = 0
#      break

#  if xstatus:
#    print "[%s] Network is down :(" % time.strftime("%Y-%m-%d %H:%M:%S")

#  return xstatus

#quit(net_is_up())
