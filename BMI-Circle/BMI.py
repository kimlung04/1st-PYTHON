def Convert_Height(h):
    if h > 10: # ถ้าuserใส่ค่าส่วนสูง เป็น cm ให้แปลงเป็น M
        h=h/100
        print("your height :",h,"m")
    elif h<10 : # ถ้าuserใส่ค่าส่วนสูง เป็น ft ให้แปลงเป็น M
        if h>3: 
            h=h/3.2808  
            print("your height :",h,"m")
        #ถ้าค่าต่ำกว่า 3 แปลว่า user ใส่ค่าส่วนสูงเป็นเมตรอยู่แล้ว
    return h

def Compile_BMI(bmi):
    print("Your BMI :",bmi) #แสดงค่าbmiของUser
    if bmi > 30: #ถ้ามากกว่า 30 แสดงว่าอ้วนมากๆ
        print("Obese")
    elif bmi >25: #ถ้าอยู่ในช่วง 25-29.9 แสดงว่าอ้วน
        print("Fat")
    elif bmi >23: #ถ้าอยู่ในช่วง 23-24.9 แสดงว่าน้ำหนักเกิน
        print("Over weight")
    elif bmi >18.5: #ถ้าอยู่ในช่วง 18.5-22.9 แสดงว่าสมส่วน
        print("Normal weight")
    else : #ถ้าต่ำกว่า18.5 แสดงว่า ผอมเกินไป
        print("Skinny")

w = float(input("Your weight(KG): ")) #รับค่าน้ำหนักจากUser
h = float(input("Your height: ")) #รับค่าส่วนสูงจากUser
h=Convert_Height(h)
bmi = w/(h*h) #สมการหาค่าBMI น้ำหนักหน่วยเป็น KG ส่วนสูงหน่วยเป็น M
Compile_BMI(bmi)

