import pytest
from television import *

class Test:
    def setup(self): #sets up
        self.tv1 = Television()

    def teardown(self): #deletes
        del self.tv1

    def test_init(self): #tests __init__
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

    def test_power(self): #tests power

        self.tv1.power()
        assert self.tv1.__str__() == 'power = True channel = 0 volume = 0'

        self.tv1.power()
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

    def test_mute(self): #tests mute
        self.tv1.mute()
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

        self.tv1.power()
        self.tv1.mute()
        assert self.tv1.__str__() == 'power = True channel = 0 volume = 0'

        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'power = True channel = 0 volume = 0'
        self.tv1.power() #realism

    def test_volume(self): #tests volume up and volume down
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

        self.tv1.power()
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'power = True channel = 0 volume = 1'

        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'power = True channel = 0 volume = 2'

        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'power = True channel = 0 volume = 0'


        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.mute()
        self.tv1.volume_down()

        assert self.tv1.__str__() == 'power = True channel = 0 volume = 1'

        self.tv1.power()  # realism

    def test_channel(self): #tests channal up and channal down
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

        self.tv1.channel_down()
        assert self.tv1.__str__() == 'power = False channel = 0 volume = 0'

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'power = True channel = 1 volume = 0'

        self.tv1.channel_down()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()

        assert self.tv1.__str__() == 'power = True channel = 0 volume = 0'

        self.tv1.channel_down()
        assert self.tv1.__str__() == 'power = True channel = 3 volume = 0'

        self.tv1.power() #realism
