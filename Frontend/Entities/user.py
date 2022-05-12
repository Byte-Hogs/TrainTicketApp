#Basic user system for SE project
import datetime as dt
from xmlrpc.client import Boolean
import logging

logger = logging.getLogger("Logging system for User Module")
logger.propagate = False
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler(filename='user_history.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


idlist = []

class user(object):

    def __init__(self) -> None:
        self.__userid = 0
        self.__first_name = ""
        self.__middle_name = ""
        self.__last_name = ""
        self.__dob = ""
        self.__gender = ""
        self.__marital_status = 0
        self.__nationality = ""
        self.__mobile = ""
        self.__address = ""
        self.__pincode = 0
        self.__pref_lang = ""
        self.__id_proof = ""
        self.__username = ""
        self.__password = ""
        self.__sec_question = ""
        self.__sec_answer = ""
        self.__access = 1

    def user_det(self) -> None:
        self.__username = ""
        self.__password = ""
        self.__sec_question = ""
        self.__sec_answer = ""
        self.__access = 1

    def userid(self) -> str:
        return self.__userid

    def name(self) -> str :
        return (self.__first_name + self.__middle_name + self.__last_name)

    def dob(self) -> str:
        return self.__dob

    def gender(self) -> str:
        return self.__gender
    
    def marital_status(self) -> str:
        return self.__marital_status

    def addr(self) -> str:
        return self.__address + str(self.__pincode)

    def mobile(self) -> str:
        return str(self.__mobile)

    def pref_lang(self) -> str:
        return self.__pref_lang

    def nationality(self) -> str:
        return self.__nationality

    def user_name(self) -> str:
        return self.__username

    def password(self) -> str:
        return self.__password

    def sec_question(self) -> str:
        return self.__sec_question

    def sec_answer(self) -> str:
        return self.__sec_answer

    def id_proof(self) -> str:
        return self.__id_proof

    def __del__(self) -> None:
        user.idlist.remove(self.__userid)

    def access_level(self) -> bool:
        return self.__access

    def modify_name(self, inp_name):
        f_name, m_name, l_name = inp_name.strip()
        self.__first_name = f_name
        self.__middle_name = m_name
        self.__last_name = l_name
        logger.info("Name of user modified to:", str(self.__first_name + self.__middle_name + self.__last_name))
    
    def modify_name(self, u_name):
        self.__username = u_name
        logger.info("username of user modified to:", self.__username)

    def modify_dob(self, inp_dob):
        self.__dob = inp_dob
        logger.info("Date of Birth modified to:", self.__dob)

    def modify_address(self, inp_address, inp_pincode):
        self.__address = inp_address
        self.__pincode = inp_pincode
        logger.info('Address of user modified to:', self.__address)
        logger.info('Pincode of user modified to:', self.__pincode)

    def auth_user(self, inp_u_name, inp_u_pass):
        if inp_u_name == "":
            logger.warning("Empty username field!")
        else:
            if inp_u_pass == "":
                logger.warning("Empty password field!")
            else:
                for ele in idlist:
                    if ((ele.__username == inp_u_name) and (ele.__password == inp_u_pass)):
                        logger.info("User authenticated!")
                        ele.__access = 1
                        break
                    else:
                        logger.warning("User credentials invalid")
                        continue
    
