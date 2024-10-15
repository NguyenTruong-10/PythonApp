class HocSinh():
    def __init__(self, idStudent, nameStudent, AddressStudent,hight,weight,ability):
        self.idStudent = idStudent
        self.nameStudent = nameStudent
        self.AddressStudent = AddressStudent
        self.hight = hight
        self.weight = weight
        self.ability = ability
    def Information(self):
        print("Id student",self.idStudent)
        print("Name: ",self.nameStudent)
        print("Address: ",self.AddressStudent)
        print("hight: ",self.hight)
        print("weight: ",self.weight)
        print("academic_performance: ",self.ability)
    def UpdateAddress(self,AddressStudent):
        self.AddressStudent = AddressStudent
        print("Dia chi duoc Update:",self.AddressStudent)
    def Update_Hight_weight(self,hight,weight):
        self.hight =hight
        self.weight = weight
        print("Chieu cao duoc cap nhan:",self.hight)
        print("Can nang duoc cap nhan:",self.weight)

studentA = HocSinh(1,"Binh","Ha Noi",160,56,"tốt")
studentA.Information()

studentA.UpdateAddress("HCM")

studentA.Update_Hight_weight(170,70)
studentA.Information()
