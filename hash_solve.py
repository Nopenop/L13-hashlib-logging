import logging
import hashlib
import os
#Creates dictionary of encryptions to be used
alg = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512
}

#removes results.log file when ran
os.remove('results.log')

#formats the way the program logs
format = '[%(asctime)s] %(levelname)s: %(message)s'
#when program logs, logs to results.log file
logging.basicConfig(level=logging.DEBUG, filename='results.log', format=format)

#Creates logging object to be used through
class Control_Log:

    """Log class to be used throughout program
    """
    def __init__(self, file):
        """Constructor for logging control class

        Args:
            file (string): name of file to work on
        """
        logging.info("Starting to procves {}".format(file))
    
    def log(self, success, test_num, algorithm):
        """log the attempt to find possible hash

        Args:
            success (bool): generated hash == given hash
            test_num (string): formatted string used to generate hash
            algorithm (string): algorithm used to generate hash
        """
        if success:
            logging.info(
                "Possible solution identified as {} using {}".format(test_num, algorithm)
                )
            print(
                "Using {} hash, the possible password is: {}".format(algorithm,test_num)
                )
        else:
            logging.debug("Trying value {} with {}".format(test_num, algorithm))


with open('password.txt', 'r+') as file:
    log = Control_Log(file.name)
    log.log(False, '10','balls')
    hash = file.readline()
    print("The password hash is {}".format(hash))

    for num in range(0,10000):
        for algo in alg:
            test_num = "{:04}".format(num)
            byte_code = bytes(test_num,encoding="ascii")
            success = alg[algo](byte_code).hexdigest() == hash
            log.log(success=success,test_num=test_num,algorithm=algo)