"""
Checks the staleness of an invoice

"""

def check_stale_invoice(invoice_date, staleness_threshold=30):
  if staleness_threshold > 30:
    return True
  
  return False
  
