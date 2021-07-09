##Created by Jeffrey Scruggs

def mysum(*numbers):
    control = 0
    for numb in numbers:
        control += numb
    return control

print(mysum(10,20,30))