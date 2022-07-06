import time

class TrafficLight:
    __color = ['Зеленый', 'Желтый', 'Красный']


    def running(self, color, switch):
        print('Светофор работает')
        time.sleep(1)
        self.__color = color
        self.switch = switch

        for t in switch:
            if t == 7:
                print(f'Светофор {self.__color[2]}')
                time.sleep(7)
            elif t == 2:
                print(f'Светофор {self.__color[1]}')
                time.sleep(2)
            else:
                print(f'Светофор {self.__color[0]}')
                time.sleep(4)


traffic = TrafficLight()

print(traffic.running(color=[0], switch=(4, 4, 4)))















