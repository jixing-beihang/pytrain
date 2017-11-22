'''
适配器可以认为是对现在业务的补偿式应用，所以，尽量不要在设计阶段使用适配器模式，在两个系统需要兼容时可以考虑使用适配器模式
优点：
1、适配器模式可以让两个接口不同，甚至关系不大的两个类一起运行；
2、提高了类的复用度，经过“伪装”的类，可以充当新的角色；
3、适配器可以灵活“拆卸”。
应用场景：
1、不修改现有接口，同时也要使该接口适用或兼容新场景业务中，适合使用适配器模式。例如，在一个嵌入式系统中，原本要将数据从Flash读入，
现在需要将数据从磁盘读入，这种情况可以使用适配器模式，将从磁盘读入数据的接口进行“伪装”，以从Flash中读数据的接口形式，从磁盘读入数据。
适配器模式缺点
1、适配器模式与原配接口相比，毕竟增加了一层调用关系，所以，在设计系统时，不要使用适配器模式
'''


class AStaff():
    _name = ''
    _id = ''
    _phone = ''

    def __init__(self, id):
        self._id = id

    def getName(self):
        print('A protocol getName method...id: %s ' % self._id)
        return self._name

    def setName(self, name):
        print("A protocol setName method...id:%s" % self._id)
        self._name = name

    def getPhone(self):
        print("A protocol getPhone method...id:%s" % self._id)
        return self._phone

    def setPhone(self, phone):
        print("A protocol setPhone method...id:%s" % self._id)
        self._phone = phone


class BStaff():
    _name = ''
    _id = ''
    _telephone = ''

    def __init__(self, id):
        self._id = id

    def get_name(self):
        print("B protocol get_name method...id:%s" % self._id)
        return self._name

    def set_name(self, name):
        print("B protocol set_name method...id:%s" % self._id)
        self._name = name

    def get_telephone(self):
        print("B protocol get_telephone method...id:%s" % self._id)
        return self._telephone

    def set_telephone(self, phone):
        print("B protocol get_name method...id:%s" % self._id)
        self._telephone = phone


class StaffAdapter():
    _bStaff = ''

    def __init__(self, id):
        self._bStaff = BStaff(id)

    def getName(self):
        return self._bStaff.get_name()

    def setName(self, name):
        self._bStaff.set_name(name)

    def getPhone(self):
        return self._bStaff.get_telephone()

    def setPhone(self, phone):
        self._bStaff.set_telephone(phone)


if __name__ == "__main__":
    acpn_staff = AStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print("A Staff Name:%s" % acpn_staff.getName())
    print("A Staff Phone:%s" % acpn_staff.getPhone())

    bcpn_staff = StaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print("B Staff Name:%s" % bcpn_staff.getName())
    print("B Staff Phone:%s" % bcpn_staff.getPhone())
