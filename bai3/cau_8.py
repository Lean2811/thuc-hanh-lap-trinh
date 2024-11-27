print("le van an")
print("235752021610044")
import math
pos = [0, 0]

while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        pass
    ###################
print(int(round(math.sqrt(pos[0]**2 + pos[1]**2))))
