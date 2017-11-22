'''
优点：
1、减少了系统之间的相互依赖，提高了系统的灵活；
2、提高了整体系统的安全性：封装起的系统对外的接口才可以用，隐藏了很多内部接口细节，若方法不允许使用，则在门面中可以进行灵活控制。
使用场景：
1、为一个复杂的子系统提供一个外界访问的接口。这类例子是生活还是蛮常见的，例如电视遥控器的抽象模型，电信运营商的用户交互设备等；
2、需要简化操作界面时。例如常见的扁平化系统操作界面等，在生活中和工业中都很常见。
门面模式的缺点
1、门面模式的缺点在于，不符合开闭原则，一旦系统成形后需要修改，几乎只能重写门面代码，这比继承或者覆写等方式，或者其它一些符合开闭原则的模式风险都会大一些。

'''


class AlarmSensor():
    def run(self):
        print("Alarm Ring...")


class WaterSprinker():
    def run(self):
        print("Spray Water...")


class EmergencyDialer():
    def run(self):
        print("Dial 119...")


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()

    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()


if __name__ == "__main__":
    emergency_facade = EmergencyFacade()
    emergency_facade.runAll()
