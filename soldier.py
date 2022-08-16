class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_num = 0
    
    def add_bullet(self,num):
        self.bullet_num += num
        print("枪里面有 %d 发子弹" % self.bullet_num)
    
    def shoot(self):
        self.bullet_num -= 1
        print("开枪射击，突突突...")
    

class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None
    
    def fire(self,num):
        # 1.判断手里面有没有枪
        if self.gun is None:
            print("没有枪...")
            return
        # 2.装填子弹
        self.gun.add_bullet(num)
        # 3.发射子弹，枪射击子弹
        self.gun.shoot()

    def __str__(self) -> str:
        return "%s 冲啊" % self.name

ak67 = Gun("AK67")
# ak67.add_bullet(50)
# ak67.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak67
xusanduo.fire(60)
print(xusanduo)