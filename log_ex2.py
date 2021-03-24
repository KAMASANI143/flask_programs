import logging

a=2
b=7

logging.basicConfig(filename="kam.log",
                    format='%(asctime)s - %(message)s',
                    filemode='w',
                    level=logging.DEBUG)

if a>b:
    logging.info('a')

else:
    logging.info('b')

