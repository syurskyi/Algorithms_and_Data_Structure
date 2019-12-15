from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, st, dt):
        self._notice = st
        self._expiry = dt

    @property
    def expired(self):
        return self._expiry < NOW
