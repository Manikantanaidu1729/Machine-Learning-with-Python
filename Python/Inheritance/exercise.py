class MobilePhone:
    def __init__(self,screentype,networktype,dualsim,frontcamera,rearcamera,ram,storage):
        self.screentype=screentype
        self.networktype=networktype
        self.dualsim=dualsim
        self.frontcamera=frontcamera
        self.rearcamera=rearcamera
        self.ram=ram
        self.storage=storage

    def make_call(self):
        return "making a call"

    def receive_call(self):
        return "receiving a call"

    def take_a_picture(self):
        return "taking a photo"


class Apple(MobilePhone):
    def __init__(self,screentype,networktype,dualsim,frontcamera,rearcamera,ram,storage,company):
        super().__init__(screentype,networktype,dualsim,frontcamera,rearcamera,ram,storage)
        self.company=company



class Samsung(MobilePhone):
    def __init__(self,screentype,networktype,dualsim,frontcamera,rearcamera,ram,storage,company):
        super().__init__(screentype,networktype,dualsim,frontcamera,rearcamera,ram,storage)
        self.company=company


apple = Apple("touchscreen","5G",True,"12MP","48MP","4GB","8GB","Apple")

samsung = Samsung("touchscreen","4G",False,"8MP","32MP","4GB","8GB","Samsung")

print(apple.make_call())
print(apple.company)