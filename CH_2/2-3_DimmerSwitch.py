# DimmerSwitch class

class DimmerSwitch:
    def __init__(self):
        self.switch_status = False
        self.brightness = 0

    def turn_off(self):
        self.switch_status = False

    def turn_on(self):
        self.switch_status = True

    def level_up(self):
        if self.brightness < 10:
            self.brightness += 1

    def level_down(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print(f'Switch is on? {self.switch_status}')
        print(f'Brightness is: {self.brightness}')


odimmer = DimmerSwitch()
# turn on and raise brightness 5 times
odimmer.turn_on()
odimmer.level_up()
odimmer.level_up()
odimmer.level_up()
odimmer.level_up()
odimmer.level_up()
odimmer.show()

# lower brightness 2 times
odimmer.level_down()
odimmer.level_down()
odimmer.turn_off()
odimmer.show()

odimmer.level_up()
odimmer.level_up()
odimmer.level_up()
odimmer.show()

