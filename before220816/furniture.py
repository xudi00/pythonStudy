class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    
    def __str__(self) -> str:
        return "%s item is %.2f area" % (self.name,self.area)


class House:
    def __init__(self,style,total_area):
        self.style = style
        self.total_area = total_area
        self.free_area = total_area
        self.item_list = []
    
    def add(self,item):
        # 1.判断屋子能否放下
        if self.free_area <= 0:
            print("房子放不下了！")
            return
        # 2.计算剩余面积
        self.free_area -= item.area
        # 3.将家具放进房子里面
        self.item_list.append(item.name)

    def __str__(self) -> str:
        return ("[%s] house has %.2f areas left now\n [total %.2f area]\n The furniture is %s..."
        % (self.style,self.free_area,self.total_area,self.item_list))


bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)

print(bed)
print(chest)
print(table)

alice_family = House("两室一厅",60)
alice_family.add(bed)
alice_family.add(chest)
alice_family.add(table)
print(alice_family)