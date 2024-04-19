class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize a Television object."""
        self.__power: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power state of television."""
        self.__power = not self.__power

    def mute(self) -> None:
        """Toggle the mute state of  television."""
        if self.__power:
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """Increase the channel by one."""
        if self.__power:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel by one."""
        if self.__power:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by one."""
        if self.__power:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one."""
        if self.__power:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = 1

    def __str__(self) -> str:
        """Return representation of the television."""
        return f'Power = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}'
