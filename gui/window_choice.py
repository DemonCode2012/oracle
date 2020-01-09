import DataFile
import User
import Object
import Exp
import ExplainPlan


def choice(curs, cho):
    if cho == '1':
        DataFile.ora_datafile(curs)
    elif cho == '2':
        User.ora_user(curs)
    elif cho == '3':
        Object.ora_object(curs)
    elif cho == '8':
        ExplainPlan.getplan(curs)
    elif cho == '10':
        Exp.ora_exp(curs)
    else:
        return True
