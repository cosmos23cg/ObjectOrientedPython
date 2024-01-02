# OO_LightSwitch

class LightSwitch:
    def __init__(self):
        self.switch_status = False

    def switch_on(self):
        self.switch_status = True

    def switch_off(self):
        self.switch_status = False

    def show(self):
        print(self.switch_status)


light_switch = LightSwitch()

light_switch.show()
light_switch.switch_on()
light_switch.show()
light_switch.switch_off()
light_switch.show()
light_switch.switch_on()
light_switch.show()

