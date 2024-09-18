# Função para inverter os caracteres de uma string sem usar funções prontas
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string_para_inverter = input("Digite Algo: ")
string_invertida = inverter_string(string_para_inverter)
print(string_invertida)
