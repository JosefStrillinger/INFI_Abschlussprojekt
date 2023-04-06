from xml.etree.ElementTree import PI

WRIST = 0 # https://google.github.io/mediapipe/solutions/hands.html
THUMB_CMC = 1 
THUMB_MCP = 2
THUMB_IP = 3
THUMB_TIP = 4
INDEX_FINGER_MCP = 5
INDEX_FINGER_PIP = 6
INDEX_FINGER_DIP = 7
INDEX_FINGER_TIP = 8
MIDDLE_FINGER_MCP = 9
MIDDLE_FINGER_PIP = 10
MIDDLE_FINGER_DIP = 11
MIDDLE_FINGER_TIP = 12
RING_FINGER_MCP = 13
RING_FINGER_PIP = 14
RING_FINGER_DIP = 15
RING_FINGER_TIP = 16
PINKY_MCP = 17
PINKY_PIP = 18
PINKY_DIP = 19
PINKY_TIP = 20

def is_stein(points):
    return points[MIDDLE_FINGER_MCP].y > points[MIDDLE_FINGER_PIP].y and points[PINKY_MCP].y > points[PINKY_PIP].y and \
        points[RING_FINGER_MCP].y > points[RING_FINGER_PIP].y and points[INDEX_FINGER_MCP].y > points[INDEX_FINGER_PIP].y

def is_schere(points):
    return points[INDEX_FINGER_TIP].y > points[INDEX_FINGER_DIP].y and points[MIDDLE_FINGER_TIP].y > points[MIDDLE_FINGER_DIP].y and \
        points[RING_FINGER_DIP].y > points[RING_FINGER_TIP].y and points[PINKY_DIP].y > points[PINKY_TIP].y and \
            points[INDEX_FINGER_DIP].y > points[INDEX_FINGER_MCP].y and points[MIDDLE_FINGER_DIP].y > points[MIDDLE_FINGER_MCP].y and \
                points[RING_FINGER_PIP].y > points[RING_FINGER_DIP].y and points[PINKY_PIP].y > points[PINKY_DIP].y

def is_papier(points):
    return points[INDEX_FINGER_DIP].y < points[INDEX_FINGER_TIP].y and points[MIDDLE_FINGER_DIP].y < points[MIDDLE_FINGER_TIP].y and \
        points[RING_FINGER_DIP].y < points[RING_FINGER_TIP].y and points[PINKY_DIP].y < points[PINKY_TIP].y and \
            points[INDEX_FINGER_DIP].y > points[INDEX_FINGER_MCP].y and points[MIDDLE_FINGER_DIP].y > points[MIDDLE_FINGER_MCP].y and \
                points[RING_FINGER_DIP].y > points[RING_FINGER_MCP].y and points[PINKY_DIP].y > points[PINKY_MCP].y

def is_spock(points):
    return points[INDEX_FINGER_DIP].y < points[INDEX_FINGER_TIP].y and points[MIDDLE_FINGER_PIP].y > points[MIDDLE_FINGER_TIP].y and \
        points[RING_FINGER_PIP].y > points[RING_FINGER_TIP].y and points[PINKY_DIP].y < points[PINKY_TIP].y and \
            points[INDEX_FINGER_DIP].y > points[INDEX_FINGER_MCP].y and points[PINKY_DIP].y > points[PINKY_MCP].y

def is_echse(points):
    return points[INDEX_FINGER_PIP].y > points[INDEX_FINGER_TIP].y and points[MIDDLE_FINGER_PIP].y > points[MIDDLE_FINGER_TIP].y and \
        points[RING_FINGER_PIP].y > points[RING_FINGER_TIP].y and points[PINKY_PIP].y > points[PINKY_TIP].y