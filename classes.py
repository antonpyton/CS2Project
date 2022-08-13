class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        self.__ch = 0
        self.__vol = 0
        self.__status = False

    def power(self):
        '''


        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def channel_up(self):
        if self.__status == True:
            if self.__ch == 3:
                self.__ch = 0
            else:
                self.__ch += 1

    def channel_down(self):
        if self.__status == True:
            if self.__ch == 0:
                self.__ch = 3
            else:
                self.__ch -= 1

    def volume_up(self):
        if self.__status == True:
            if self.__vol == 2:
                self.__vol += 0
            else:
                self.__vol += 1

    def volume_down(self):
        if self.__status == True:
            if self.__vol == 0:
                self.__vol -= 0
            else:
                self.__vol -= 1

    def __str__(self):
        return f'Is on = {self.__status}, Channel = {self.__ch}, Volume = {self.__vol}'