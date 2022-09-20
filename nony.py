from redun import Redun
import os

main = Redun('10.32.32.1', 'eth0', 'www.google.com', 'usb0')


def principal():
    
        main_ping = os.system('ping -c 4 ' + main.gate1 + ' -I ' + main.int1 )
        #print(main_ping)
        if main_ping == 0:
                main.succes()
                os.system('sudo ifmetric eth0 210')
                os.system('sudo ifmetric usb0 220')
                os.system('python3 /home/pi/SIATA/Software/Mqtt/Pruebas/prueba_envio_antena.py')
        else:
            print(main_ping)
            main.fail()
            os.system('sudo ifmetric eth0 220')
            os.system('sudo ifmetric usb0 210')
            if main_ping == 256:
                slave_ping = os.system('ping -c 4 ' + main.gate2 + ' -I ' + main.int2 )
                main.succes2()
                print(slave_ping)
                if slave_ping == 0:
                    print('change ip')
                    os.system('python3 /home/pi/SIATA/Software/Mqtt/Pruebas/prueba_envio.py')
