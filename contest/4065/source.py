target = input().split(" ")
a_time, b_time, duration = int(target[0]), int(target[1]), int(target[2])
local_dur = 0
round_counter = 0
pos = 1
while True:
    if round_counter == duration:
        break
    if pos == 1:
        local_dur += a_time
        pos = 2
        round_counter += 1
    elif pos == 2:
        local_dur += b_time
        pos = 1
        round_counter += 1
print(local_dur)
