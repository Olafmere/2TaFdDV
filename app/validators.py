import re


def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email)


def validar_rfc(rfc):
    patron = r'^[A-ZÑ&]{4}[0-9]{6}[A-Z0-9]{3}$'
    return re.match(patron, rfc)