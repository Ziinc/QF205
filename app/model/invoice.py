import datetime


class Invoice():
    def __init__(self, amt, date,):
        self.amt = amt
        self.date_iso_string = date
        self.date = datetime.date.fromisoformat(date)
