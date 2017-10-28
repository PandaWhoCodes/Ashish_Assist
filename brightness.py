import wmi


def setBrightness(value):
    value = int(10 / 13) * value
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(value, 0)
