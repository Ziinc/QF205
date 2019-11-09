import datetime


class Invoice():
    def __init__(self, *args, **kwargs):

        self.validate_invoice_inputs(*args, **kwargs)
        self.assign_attrs(*args, **kwargs)

    def assign_attrs(self, amt, date, credit_term, factor_pct, factor_start_date=None, company_name='Unknown Company'):
        now = datetime.datetime.now()

        self.id = datetime.datetime.timestamp(now)
        self.company_name = company_name
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

    @staticmethod
    def validate_invoice_inputs(amt, date, credit_term, factor_pct, **kwargs):
        if type(amt) == str or amt == None:
            raise AttributeError(
                f'Invoice Amount should be numerical. Received {amt}')

        if type(date) != str:
            raise AttributeError(
                f'Invoice Date should be a string with ISO YYYY-MM-DD format. Received {date}')
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise AttributeError(
                f'Invoice Date should be a string with ISO YYYY-MM-DD format. Received {date}')

        if type(credit_term) != int:
            raise AttributeError(
                f'Invoice Credit Term should be an integer. Received {credit_term}')

        if type(factor_pct) != float or not (0 < factor_pct < 1):
            raise AttributeError(
                f'Invoice Factor Percentage should be numerical, between 0 and 1. Received {factor_pct}')

        if len(kwargs) > 0:
            for (k, v) in kwargs.items():

                if k == 'factor_start_date':
                    if type(v) != str:
                        raise AttributeError(
                            f'Factor start date should be a string with ISO YYYY-MM-DD format. Received {v}')
                    try:
                        datetime.datetime.strptime(date, '%Y-%m-%d')
                    except ValueError:
                        raise AttributeError(
                            f'Factor start date should be a string with ISO YYYY-MM-DD format. Received {v}')

                if k == 'company_name':
                    if type(v) != str:
                        raise AttributeError(
                            f'Company name a string with ISO YYYY-MM-DD format. Received {v}')

        return True
