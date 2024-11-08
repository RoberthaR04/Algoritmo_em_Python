def calcular_digito_verificador(cpf, multiplicador):
    soma = sum(int(cpf[i]) * multiplicador[i] for i in range(len(multiplicador)))
    digito = (soma * 10) % 11
    return digito if digito < 10 else 0

def validar_cpf(cpf):
   cpf = cpf.replace('.', '').replace('-', '')

   if len(cpf) != 11 or not cpf.isdigit():
      return False

   primeiro_digito = calcular_digito_verificador(cpf[:9], list(range(10, 1, -1)))
   if primeiro_digito != int(cpf[9]):
      return False

   segundo_digito = calcular_digito_verificador(cpf[:10], list(range(11, 1, -1)))
   return segundo_digito == int(cpf[10])

cpf_usuario = input("Informe o CPF para validar:")  

if validar_cpf(cpf_usuario):
    print("CPF válido.")
else:
    print("CPF inválido.")