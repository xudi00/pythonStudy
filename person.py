class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def run(self):
        print("%s runs and loses 0.5" % self.name)
        self.weight -= 0.5
    
    def eat(self):
        print("%s eats and weights 1.0" % self.name)
        self.weight += 1.0
    
    def __str__(self) -> str:
        return ("%s finally weight %.2f" % (self.name,self.weight))

xiaoming = Person("XiaoMing",85)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("XiaoMei",60)
xiaomei.run()
xiaomei.eat()
print(xiaomei)