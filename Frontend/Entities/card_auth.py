from re import A
import re
import user
import logging
import time

logger = logging.getLogger("Logging system for Credit/Debit card authentication")
logger.propagate = False
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler(filename='card_history.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

class payment_card():

    def __init__(self) -> None:
        self.__cardnumber = 0
        self.__cvv = 0
        self.__balance = 0
        self.__valid_thru = ""
        
    def v_auth(self, inp_c_vt):
        ym = time.strftime("%m/%Y")
        if ym <= inp_c_vt:
            logger.info("Card is valid")
            self.__valid_thru = inp_c_vt
            return 1
        else:
            logger.warning("Card is invalid!")
            return -1

    def cno_auth(self, inp_c_no):
        if inp_c_no.length == 16:
            logger.info("Card length valid")
            if inp_c_no == self.__cardnumber:
                logger.info("Card number is authenticated")
                return 1
            else:
                logger.warning("Card is not authenticated")
                return -1
        else:
            logger.warning("Card length invalid") 
            return -1
            
    def cvv_auth(self, inp_cvv):
        if 0 < inp_cvv < 999:
            logger.info("Valid CVV")
            if inp_cvv == self.__cvv:
                logger.info("CVV authenticated")
                return 1
            else:
                return -1
        else:
            return -1

    def check_bal(self):
        return self.__balance

    def card_auth(self, inp_c_no, inp_cvv, inp_c_vt):
        cno = self.cno_auth(inp_c_no)
        cv_no = self.cvv_auth(inp_cvv)
        vt_no = self.v_auth(inp_c_vt)

        if cno == 1 and cv_no == 1 and vt_no == 1:
            logger.info("Valid card!")

        else:
            logger.warning("Invalid card")
