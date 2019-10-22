import datetime


class Invoice():
    def __init__(self, amt, date):
        now = datetime.datetime.now()
        self.id = datetime.datetime.timestamp(now)
        self.amt = amt
        self.date_iso_string = date
        self.date = datetime.date.fromisoformat(date)

    def validate_and_update(self, attrs):
        # TODO: perform validations, update the invoice object
        return self
