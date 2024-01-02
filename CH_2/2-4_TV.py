# TV class

class TV:
    def __init__(self):
        self.is_on = False
        self.is_mute = False
        self.channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.n_channel = len(self.channel_list)
        self.channel_idx = 0
        self.max_volume = 10
        self.min_volume = 0
        self. volume = self.max_volume / 2

    def power(self):
        self.is_on = not self.is_on

    def volume_up(self):
        if not self.is_on: # if false return
            return
        if self.is_mute:
            self.is_mute = False
        if self.volume < self.max_volume:
            self.volume += 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_mute:
            self.is_mute = False
        if self.volume > self.min_volume:
            self.volume -= 1

    def channel_up(self):
        if not self.is_on:
            return
        self.channel_idx += 1
        if self.channel_idx == self.n_channel:
            self.channel_idx = 0

    def channel_down(self):
        if not self.is_on:
            return
        self.channel_idx -= 1
        if self.channel_idx < 0:
            self.channel_idx = 0

    def mute(self):
        if not self.is_on:
            return
        self.is_mute = not self.is_mute

    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_idx = self.channel_list.index(new_channel)

    def show(self):
        print()
        print('TV status')
        if self.is_on:
            print('TV is on')
            print(f'channel is {self.channel_idx}')
        else:
            print('TV is off')


oTV = TV()
oTV.power()
oTV.show()
