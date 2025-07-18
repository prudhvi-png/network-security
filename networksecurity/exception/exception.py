import sys
from networksecurity.logging import logger


def custom_exception(error_message,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    custom_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
            file_name, lineno, str(error_message))
    return custom_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = custom_exception(error_message=error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message



