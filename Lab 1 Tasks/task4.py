def caught_speeding(speed, anniversary):
    if anniversary:
        speed -= 10

    if speed <= 70:
        return "No fine"
    elif speed <= 80:
        return "Less Fine"
    else:
        return "Car seize"


print(caught_speeding(70, False))
print(caught_speeding(75, False))
print(caught_speeding(85, False))
print(caught_speeding(80, True))