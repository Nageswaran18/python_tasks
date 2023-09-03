import logging


def main()-> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d',
        filename='test.log')

    logging.debug("this is the debug message")
    logging.info("this is the info mesg")

if __name__=='__main__':
    main()
 



