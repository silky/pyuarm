from tools.list_uarms import uarm_ports
import pyuarm

# Firmata

REPORT_FIRMATA_VERSION = 0x79

# parameters
SERVO_BOTTOM = 0
SERVO_LEFT = 1
SERVO_RIGHT = 2
SERVO_HAND = 3

SERVO_BOTTOM_ANALOG_PIN = 2
SERVO_LEFT_ANALOG_PIN = 0
SERVO_RIGHT_ANALOG_PIN = 1
SERVO_HAND_ANALOG_PIN = 3

# communication protocol
START_SYSEX = 0xF0
UARM_CODE = 0xAA
END_SYSEX = 0xF7

READ_ANGLE = 0X10
WRITE_ANGLE = 0X11
READ_COORDS = 0X12
WRITE_COORDS = 0X13
READ_DIGITAL = 0X14
WRITE_DIGITAL = 0X15
READ_ANALOG = 0X16
WRITE_ANALOG = 0X17
READ_EEPROM = 0X1A
WRITE_EEPROM = 0X1B
DETACH_SERVO = 0X1C
PUMP_STATUS = 0X1D
WRITE_STRETCH = 0X1E
WRITE_LEFT_RIGHT_ANGLE = 0X1F
GRIPPER_STATUS = 0X20
READ_SERIAL_NUMBER = 0x21
WRITE_SERIAL_NUMBER = 0x22
REPORT_LIBRARY_VERSION = 0x23
BUZZER_ALERT = 0x24

CONFIRM_FLAG = 0x80
CALIBRATION_FLAG = 10
CALIBRATION_LINEAR_FLAG = 11
CALIBRATION_SERVO_FLAG = 12
CALIBRATION_STRETCH_FLAG = 13

LINEAR_INTERCEPT_START_ADDRESS = 70
LINEAR_SLOPE_START_ADDRESS = 50
OFFSET_START_ADDRESS = 30
OFFSET_STRETCH_START_ADDRESS = 20

SERIAL_NUMBER_ADDRESS = 100

EEPROM_DATA_TYPE_BYTE = 1
EEPROM_DATA_TYPE_INTEGER = 2
EEPROM_DATA_TYPE_FLOAT = 4

BUTTON_D7 = 7
BUTTON_D4 = 4
BUTTON_D2 = 2
PUMP_PIN = 6
VALVE_PIN = 5

PULL_UP = 1
INPUT = 0

HIGH = 1
LOW  = 0

def get_uarm():
    """
    ===============================
    Get First uArm Port instance
    ===============================
    It will return the first uArm Port detected by **pyuarm.tools.list_uarms**,
    If no available uArm ports, will print *There is no uArm port available*

    .. raw:python
    >>> import pyuarm
    >>> uarm = pyuarm.get_uarm()
    There is no uArm port available


    :returns: uArm() Instance

    """
    ports = uarm_ports()
    if len(ports) > 0:
        return pyuarm.uArm(port=ports[0])
    else:
        print("There is no uArm port available")

def getValueAsOne7bitBytes(val):
    """

    :param val:

    """
    return bytearray([val])


def getValueAsTwo7bitBytes(val):
    """

    :param val:

    """
    int_val = int(val)
    return bytearray([abs(int_val) % 128, abs(int_val) >> 7])


def getFloatAsThree7bitBytes(val):
    """

    :param val:

    """
    int_val = int(val)
    decimal_val = int(round((val - int_val) * 100))
    return bytearray([abs(int_val) % 128, abs(int_val) >> 7, abs(decimal_val)])


def getIntegerAsThree7bitBytes(val):
    """

    :param val:

    """
    return bytearray([0 if val > 0 else 1, abs(val) % 128, abs(val) >> 7])


def getFloatAsFour7bitBytes(val):
    """

    :param val:

    """
    int_val = int(val)
    decimal_val = int(round((val - int_val) * 100))
    return bytearray([0 if val > 0 else 1, abs(int_val) % 128, abs(int_val) >> 7, abs(decimal_val)])

class NoUArmPortException(IOError):
    """
    .. _NoUArmPortException:
    """
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return repr(self.error)


class UnkwonFirmwareException(Exception):
    """
    .. _UnkwonFirmwareException:
    """
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return repr(self.error)