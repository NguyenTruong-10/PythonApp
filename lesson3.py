# # init =  initialize => Khởi tạo
# # Các tham số truyền vào trong init nó cũng là các thuộc tính của class
# # # Ví dụ 
# # class Animal:
# #     def __init__(self, name, age, color):
# #         self.name = name #Tham số truyền vào được gán với THUỘC TÍNH của class
# #         self.age = age
# #         self.color = color

# # Btap 1
# class Phuongtien :
#     def __init__(self,loai_xe,hang_xe,mau_xe,so_cho,banh_xe,gia):
#         self.loai_xe = loai_xe
#         self.hang_xe = hang_xe 
#         self.mau_xe = mau_xe
#         self.so_cho = so_cho
#         self.banh_xe = banh_xe
#         self.gia = gia
#     def Inthongtin(self):
#         print("Loai xe cua ban la: ",self.loai_xe)
#         print("Hang xe cua ban la: ",self.hang_xe)
#         print("Mau xe cua ban la: ",self.mau_xe)
#         print("So cho xe cua ban la: ",self.so_cho)
#         print("So banh xe cua ban la: ",self.banh_xe)
#         print("Gia xe :",self.gia)

# xePorsche = Phuongtien("sieu xe","Porsche","black",2,4,10000)
# xePorsche.Inthongtin() #cu phap de su dung phuong thuc: tendoituong.phuongthuc()



class PhuongTien:
    def __init__(self,whatkind,brand,colour,seat,wheels,price):
        self.whatkind = whatkind
        self.brand = brand
        self.colour = colour
        self.seat = seat
        self.wheels = wheels
        self.price = price
    def Inthongtin(self):
        print("Loai xe cua ban la: ",self.whatkind)
        print("Hang xe cua ban la: ",self.brand)
        print("Mau xe cua ban la: ",self.colour)
        print("So cho xe cua ban la: ",self.seat)
        print("So banh xe cua ban la: ",self.wheels)
        print("Gia xe :",self.price)
# xeHonda_Vision = Vehicle("xe may","Honda","white",2,2,1400)
a = PhuongTien("sieu xe","Porsche","black",2,4,10000)
# a.Inthongtin()

class A():
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    def sum(self):
        return self.a+self.b
class Con(A):
    def devided(self):
        return self.a/self.b

c = Con(6,3)
print("Phep chia:",c.sum()) # sử dụng phương thức của lớp con
# print(c.sum(6,3)) # lớp con sử dụng phương của lớp cha

# Btap 2
# Xe => lớp cha
# XeHoi, XeDap => lớp con
class Xe:
    def __init__(self,brand, color,price):
        self.brand =  brand
        self.color = color
        self.price = price
    def Khoi_dong(self):
        print(f"Xe {self.brand} dang khoi dong")

class XeHoi(Xe):
    def chay_bang_bon_banh(self):
        print(f"Xe {self.brand} dang chay ve phia truoc bang dong co")
class XeDap(Xe):
    def dap_bang_hai_chan(self):
        print(f"Xe {self.brand} dang duoc dap ve phia truoc")

xe_hoi = XeHoi("Mercedes","Blak",10000)
xe_dap = XeDap("BMW","Red",20000)

xe_hoi.Khoi_dong()
xe_hoi.chay_bang_bon_banh()

xe_dap.Khoi_dong()
xe_dap.dap_bang_hai_chan()