

def Calcurate_Area(r):
    A = 3.14159265359*(r**2) #สมการหาค่า พื้นที่วงกลม
    print("Circle Area:%0.2f"%A) #แสดงค่า พื้นที่วงกลม

def Calcurate_Circumference(r):
    C = 2*3.14159265359*r #สมการหาค่า เส้นรอบวง
    print("Circumference:%0.2f"%C) #แสดงค่า เส้นรอบวง

r = float(input("Radius(cm): ")) #รับค่ารัศมีจากUser
Calcurate_Area(r)
Calcurate_Circumference(r)