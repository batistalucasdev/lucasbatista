def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Definir a string ou solicitar ao usuário
string_original = input("Digite uma string para inverter: ")

# Exibir a string invertida
print(f"String invertida: {inverter_string(string_original)}")
