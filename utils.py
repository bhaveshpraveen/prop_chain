from time import strftime, localtime

"""Contains some of the common utilities"""

def validate_argument_type(arg_type=None):
    def inner(function):
        def wrapper(self, *args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if not isinstance(arg, arg_type):
                    raise TypeError(
                        "Expected object of type {}." \
                        "Received {}".format(
                            type(arg_type).__name__, 
                            type(arg).__name__)
                    )
            return function(self, *args, **kwargs)
        return wrapper
    return inner


def get_all_transactions_as_str(self):
    """Return a str which contains the information enclosed in all transactions"""
    instance = self
    transactions = instance.transactions
    # str(transaction) uses the __str__ method of Transaction
    transactions_as_list = [str(transaction) for transaction in transactions]
    return "".join(transactions_as_list)
    

def get_local_time(time):
    """Returns the local time as string
    args:
        time: obtained as a result of time.time() 
    """
    
    return strftime("%a, %d %b %Y %H:%M:%S +0000", localtime(time))