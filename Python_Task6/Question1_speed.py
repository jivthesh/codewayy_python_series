#Q1

speed=int(input("Enter your Speed:"))
def check_speed(speed):
    if(speed <= 70):
        return "OK"

    else:
        speed1=(speed-70)//5

        if(speed1<=12):
            return print(f"Point:{speed1}")

        else:
            return print("License Suspended")

check_speed(speed)
