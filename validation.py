import json
from rules import *

def validate(parsed_j):
    print parsed_j

    line_num = parsed_j['label']
    logic_val = parsed_j['sentence']
    reason = parsed_j['justification']
    reference = parsed_j['reference']

    validation_map = {
        "REIT" : reit,
        "OR I" : orIntro,
        "OR E" : orElim,
        "AND I" : andIntro,
        "AND E" : andElim,
        "NOT I" : notIntro,
        "NOT E" : notElim,
        "CONTRA I" : contraIntro,
        "CONTRA E" : contraElim,
        "IMP I" : impIntro,
        "IMP E" : impElim,
        "BI I" : biIntro,
        "BI E" : biElim
    }

    if len(reference) == 0 and reason == "":
        return { "result": True }
    else:
        try:
            return {
                  "result": validation_map[reason](
                                logic_val, reference) }
        except ValueError:
            print 'UNSUPPORTED LOGIC RULE'
            return { "result": False }
