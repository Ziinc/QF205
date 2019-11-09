import datetime


class Invoice():
    def __init__(self, amt, date, credit_term, factor_pct, factor_start_date=None):
        now = datetime.datetime.now()
        self.id = datetime.datetime.timestamp(now)
        self.amt = amt
        self.date_iso_string = date
        self.date = datetime.date.fromisoformat(date)
        self.credit_term = credit_term

        if factor_start_date:
            self.factor_start_date = datetime.date.fromisoformat(
                factor_start_date)
        else:
            self.factor_start_date = datetime.date.today()

        self.factor_pct = factor_pct

    def validate_and_update(self, attrs):
        # TODO: perform validations
        for k, v in attrs.items():
            setattr(self, k, v)
        return self
