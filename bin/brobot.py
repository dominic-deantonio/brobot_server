from flask import Flask, request
from gpiozero import Robot

print(
    "                  ____            _           _   \n" +
    "                  |  _\\          | |         | |  \n" +
    "                  | |_) |_ __ ___ | |__   ___ | |_ \n" +
    "                  |  _ <| '__/ _ \\| '_ \\ / _ \\| __|\n" +
    "                  | |_) | | | (_) | |_) | (_) | |_ \n" +
    "                  |____/|_|  \\___/|_.__/ \\___/ \\__|\n" +
    "")

api = Flask(__name__)

robby = Robot(left=(9, 10), right=(7, 8))
robby.stop()


@api.route('/move', methods=['GET'])
def move():
    dir = request.args.get('dir')
    print('Received command: ' + dir)
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
    return 'OK'


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8000)
