target = int(input())
start_point = [0, 0]
router = {'right': 'up',
          'up': 'left',
          'left': 'down',
          'down': 'right',
          }
gps = 'right'
for index in range(1, target):
    if gps is 'right':
        start_point[0] = abs(start_point[0])
        start_point[0] = (start_point[0] + 1)
    elif gps is 'up':
        start_point[1] = abs(start_point[1])
        start_point[1] = (start_point[1] + 1)
    elif gps is 'left':
        start_point[0] = -abs(start_point[0])
    elif gps is 'down':
        start_point[1] = - abs(start_point[1])
    gps = router[gps]
print(start_point[0], end=" ")
print(start_point[1])
