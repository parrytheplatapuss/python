class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):

        if self.__status == True:
            self.__status = False
        elif self.__status == False:
            self.__status = True
    def mute(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            elif self.__muted == False:
                self.__muted = True
    def channel_up(self):
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1
    def channel_down(self):
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1
    def volume_up(self):
        if self.__status == True:
            self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume = self.__volume + 1
    def volume_down(self):
        if self.__status == True:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = self.__volume - 1
    def __str__(self):
        if self.__muted == True:
            return f'power = {self.__status} channel = {self.__channel} volume = {self.MIN_VOLUME}'
        else:
            return f'power = {self.__status} channel = {self.__channel} volume = {self.__volume}'