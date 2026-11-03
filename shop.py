from pay import charge

def call_api():
    # Real implementation that calls an external service
    return 100

def get_price():
    return call_api()


def charge_customer():
    return charge()