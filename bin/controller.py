from gpiozero import Robot
import sys

try:
    dir = sys.argv[1]  # Get the direction from arguments
    print('Received direction ' + dir + ' from dart')
    robby = Robot(left=(9, 10), right=(7, 8))

    while True:
        if dir == 'forward':
            robby.forward()
        elif dir == 'backward':
            robby.backward()
        elif dir == 'right':
            robby.right()
        elif dir == 'left':
            robby.left()
        else:
            robby.stop()

except Exception as e:
    print(e)

# try:
#     robby = Robot(left=(9, 10), right=(7, 8))
#     while True:
#         print('Forward...')
#         robby.forward(speed)
#         time.sleep(5)
#         robby.stop()
#         print('Stopped')
#         time.sleep(1)

#         print('Reverse...')
#         robby.backward(speed)
#         time.sleep(5)
#         robby.stop()
#         print('Stopped')
#         time.sleep(1)

#         print('Right...')
#         robby.right(speed)
#         time.sleep(5)
#         robby.stop()
#         print('Stopped')
#         time.sleep(1)

#         print('Left...')
#         robby.left(speed)
#         time.sleep(5)
#         robby.stop()
#         print('Stopped')
#         time.sleep(1)
# except Exception as e:
#     print(e)
