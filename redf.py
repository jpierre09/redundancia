from redun import Redun
import os

main = Redun('10.32.32.1', 'wlp0s20f3', 'www.google.com', 'wlp0s20f3')


def principal():
    
        main_ping = os.system('ping -c 2 ' + main.gate1 + ' -I ' + main.int1 )
        #print(main_ping)
        if main_ping == 0:
                main.succes()
        else:
            print(main_ping)
            main.fail()
            if main_ping == 512:
                slave_ping = os.system('ping -c 2 ' + main.gate2 + ' -I ' + main.int2 )
                main.succes2()
                print(slave_ping)
                if slave_ping == 0:
                    print('change ip')

                
            

principal()

#print(main.gate1)
#print(main.int1)
#print(main.gate2)
#print(main.int2)


#main.succes()