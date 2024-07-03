from EDA.Exception import SpecialException
from EDA.Logger import logging

import sys

def test_exception():
    try :
        logging.info("ERROR HAI")
        a = 1/0
    except Exception as e :
        raise SpecialException(e,sys)
    

if __name__ == "__main__":

    try :
        test_exception()
    except Exception as e:
        print(e)