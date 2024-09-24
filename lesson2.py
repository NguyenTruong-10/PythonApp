# Ví du 
# class Dogs:
#     age = ""
#     type = ""
#     name = ""
#     color = ""
# Husky = Dogs() # Khởi tạo 1 đối tượng
# Husky.name = "Hú Kỳ" # Thay đổi thuộc tính của một đối tượng
# print(Husky.name)

# VDu2
class VatNuoi:
    Giong = ""
    MauSac = ""
    Tuoi = 0
    CanNang = 0
Pet = VatNuoi()
Pet.Giong = "Chó"
Pet.MauSac = "black"
Pet.Tuoi = 10
Pet.CanNang = 20
print("Giong loai: ",Pet.Giong) # In ra
print("Mau sac: ",Pet.MauSac)
print("Tuoi: ",Pet.Tuoi)
print("Can nang:",Pet.CanNang)



# Phương thức khởi tạo
class Things():
    def __init__(self,material, color, usage):
        self.material = material
        self.color = color
        self.usage = usage
    def Create(sefl,material, color):
        table = material + color
        print(table)
