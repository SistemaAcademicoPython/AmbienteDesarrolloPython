from datetime import time
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import *

def validateDateEs(date):
    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return result



def validate_codigo(value):
    if value == "":
        raise ValidationError(
            _('{0} No se puede crear un modulo sin codigo. porfavor ingrese uno'.format(value)))
    return value



def longitud(value):
    if len(value) < 6:
        raise ValidationError('El nombre de usuario debe contener al menos 6 caracteres')
        return value
    elif len(value) > 12:
        raise ValidationError('El nombre de usuario debe contener maximo 12 caracteres')
        return value

    else:
        return value
def alfanumerico(value):
    if value.isalnum() == True:
        raise ValidationError('El nombre de usuario puede contener solo letras y numeros')
        return value
    else:
        return value

def validate_nombre(value):
    if len(value) == " ":
        raise ValidationError(
            _('%(values)s Ya esta creada esta Unidad'),
            code="invalid",
            params={'value': value},)
    elif " " == True:
        return value
    else:
        return value

def validar_espacios(value):
    if value.count == '':
        raise ValidationError(
            _(' agregar cosas correctas'),
            code="invalid",
            params={'value': value}, )
    else:
        return value == True


def longitudPassword(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres')
        return value
    elif len(value) > 15:
        raise ValidationError('La contraseña debe tener maximo 15 caracteres')
        return value

    else:
        return value


def minuscula(value):
        letras_minuscula=False
        for carac in value:
            if carac.islower()==True:
                letras_minuscula=True
        if not letras_minuscula:
            raise ValidationError('La contraseña debe tener al menos una minuscula')
            return value
        else:
            return value

def mayuscula(value):
        letras_mayuscula=False
        for carac in value:
            if carac.isupper()==True:
                letras_mayuscula=True
        if not letras_mayuscula:
            raise ValidationError('La contraseña debe tener al menos una mayuscula')
            return value
        else:
            return value

def numero(value):
        num=False
        for carac in value:
            if carac.isdigit()== True:
                num=True

        if not num:
            raise ValidationError('La contraseña debe tener al menos un numero')
            return value
        else:
            return value

def espacios(value):
        if value.count(" ")> 0:
            raise ValidationError('La contraseña no puede contener espacios en blanco')
            return value
        else:
            return value

def alfanumericoPassword(value):
    if value.isalnum() == False:
        raise ValidationError('La contraseña puede contener solo letras y numeros')
        return value
    else:
        return value

def validate_descripcion(value):
    if " " in value or value == "":
        raise ValidationError(
            _('No se puede crear un menu sin un nombre. porfavor ingrese uno'))
    return value


def validate_cedula(value):
    if(len(value)!=10 or not value.isdigit()):
        raise Exception(
            _('%(value)s no es una cédula válida'),
            code="invalid",
            params={'value': 'value'},
        )
    else:
        impares = int(value[1]) + int(value[3]) + int(value[5]) + int(value[7])
        pares = 0
        for i in range(0,9):
            if(i%2==0):
                res = int(value[i])*2
                if(res>=10):
                    res = res-9
                pares = pares+res
        total = impares+pares
        dig_validador = (((total+10)//10)*10)-total
        if(dig_validador==10):
            dig_validador = 0
        if (not(int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[-1])==dig_validador)):
            raise ValidationError(
                _('%(value)s no es una cédula válida'),
                code="invalid",
                params={'value': value},
            )

def ruc_natural(value):
    impares = int(value[1]) + int(value[3]) + int(value[5]) + int(value[7])
    pares = 0
    for i in range(0,9):
        if(i%2==0):
            res = int(value[i])*2
            if(res>=10):
                res = res-9
            pares = pares+res
    total = impares+pares
    dig_validador = (((total+10)//10)*10)-total
    if(dig_validador==10):
        dig_validador = 0
    return int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[9])==dig_validador and int(value[10:13])>=1

#Tercer dígito 9
def ruc_juridica(value):
    d1 = int(value[0])*4
    d2 = int(value[1])*3
    d3 = int(value[2])*2
    d4 = int(value[3])*7
    d5 = int(value[4])*6
    d6 = int(value[5])*5
    d7 = int(value[6])*4
    d8 = int(value[7])*3
    d9 = int(value[8])*2
    total = d1+d2+d3+d4+d5+d6+d7+d8+d9
    dig_validador = 0
    residuo = total%11
    if(residuo!=0):
        dig_validador = 11-residuo
    return int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[2])==9 and int(value[9])==dig_validador and int(value[10:13])>=1

#Tercer dígito 6
def ruc_publica(value):
    d1 = int(value[0])*3
    d2 = int(value[1])*2
    d3 = int(value[2])*7
    d4 = int(value[3])*6
    d5 = int(value[4])*5
    d6 = int(value[5])*4
    d7 = int(value[6])*3
    d8 = int(value[7])*2
    total = d1+d2+d3+d4+d5+d6+d7+d8
    dig_validador = 0
    residuo = total%11
    if(residuo!=0):
        dig_validador = 11-residuo
    return int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[2])==6 and int(value[8])==dig_validador and int(value[9:13])>=1

def validate_ruc(value):
    if value == 13:
        return value

    elif (not value.isdigit() or not len(value)==13 or not(ruc_natural(value) or ruc_juridica(value) or ruc_publica(value))):
        raise ValidationError(
            _('%(value)s no es un RUC válido'),
            code="invalid",
            params={'value': value},
        )

def validate_letras(value):
    if (not value.isalpha()):
        raise ValidationError(
            _('%(value)s no contiene únicamente letras'),
            code="invalid",
            params={'value': value},
        )

def validate_fono_convencional(value):
    if (not value.isdigit() or not(len(value)==7 or len(value)==9)):
        raise ValidationError(
            _('%(value)s no es un teléfono convencional correcto'),
            code="invalid",
            params={'value': value},
        )

def validate_celular(value):
    if (not value.isdigit() or not len(value)>=10):
        raise ValidationError(
            _('%(value)s no es un celular correcto'),
            code="invalid",
            params={'value': value},
        )



def validate_positive(value):
    if(value<0):
        raise ValidationError(
            _('%(values)s no es un numero positivo'),
            code="invalid",
            params={'value': value},
        )


class usuario_validar():
    errors = []

    def longitud(self, username):
        if len(username) < 6:
            self.errors.append('El nombre de usuario debe contener al menos 6 caracteres')
            return False

        elif len(username) > 12:
            self.errors.append('El nombre de usuario debe contener maximo 12 caracteres')
            return False

        else:
            return True

    def alfanumerico(self, username):
        if username.isalnum() == False:
            self.errors.append('El nombre de usuario puede contener solo letras y numeros')
            return False
        else:
            return True

    def validar_usuario(self, username):
        valido = self.longitud(username) and self.alfanumerico(username)
        return valido


def pasaporte(value):
    if value.isalnum() == True:
        return True
    else:
        raise ValidationError(
            _('%(values)s no es un pasaporte correcto'),
            code="invalid",
            params={'value': value},)


def identificar(value):
    if len(value) == 10:
        validate_cedula(value)

    elif len(value) == 13:
        validate_ruc(value)

    elif value.count == " ":
        pasaporte(value)

    return True


def validar_anio(value):
    if value >= "2020":
        raise ValidationError(_('%(values) No se puede crear otro año lectivo repetido'),
                              code="invalid",
                              params={'value': value},
                              )

    elif 2020 == 2020:
        raise Exception(_('%(values) No se puede crear otro año lectivo comenzado '))


def validar_ciclo(value):
    if "" == "":
        raise ValidationError(_('%(values) No se puede crear otro ciclo repetido'),
                              code="invalid",
                              params={'value': value},
                              )

    elif "" == False:
        raise Exception(_('%(values)sNo se puede crear otro ciclo... :) '))
    return value


def validate_vacios(value):
    if "" in value or value == "":
        return True

    elif value == "":
        raise Exception(_('No puede dejar campos vacios'))

    return value


def validar_select(value):
    if "opcion" == "CEDULA":
        value(validate_cedula(value))

    elif "opcion" == "RUC":
        value(validate_ruc(value))

    elif "opcion" == "PASAPORTE":
        value(pasaporte(value))
        raise Exception(_('%(values) identificacion incorrecta'))
    return value

