import logging
logging.basicConfig(filename='kam1',format='%(asctime)s %(message)s',filemode='w',level=logging.DEBUG)

def fact(n):
    logging.debug(n)
    total=1
    for i in range(n+1):
        logging.debug(i)
        total*=i
        logging.debug(total)
    return total

fact(5)