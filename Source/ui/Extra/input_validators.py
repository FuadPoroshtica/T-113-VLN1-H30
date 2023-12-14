class Name_Length_Exception(Exception):
    pass

def validate_name(name):
    if len(name) >= 50:
        raise Name_Length_Exception()