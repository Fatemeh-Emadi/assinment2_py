#BMI
weight=float(input("Weight in kg:"))
height=float(input("Height in m:"))

bmi=weight/(height**2)
print("BMI:",bmi)

if(bmi>16 and bmi<18.5):
  print("Underwight")
elif(bmi>18.5 and bmi<25):
  print("Normal")
elif(bmi>25 and bmi<30):
  print("Overweight")
elif(bmi>30):
  print("Obesity")
