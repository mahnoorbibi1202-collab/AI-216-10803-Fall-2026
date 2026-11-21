temperatures = [21.5 ,29.5, 32.5, 18.0, 35.2, 27.8, 14.0]
below_normal = 0
normal = 0
high = 0
for temperture in temeratures:
    if temperature < 15:
        print ("trmperature, "Below Normal")
            below_normal +=1
     elif 15 <= temperature <= 30:
          print(temperature, "Normal")
               normal +=1
     else:
         print(temerature , "High")
              high +=1
print("Final Summary :")
print ("Below Normal",below_normal)
print("Normal:", normal)
print("High: ", high)

      
