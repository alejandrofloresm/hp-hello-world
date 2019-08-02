# Ejercicio 2
# 1) Revisa si son palíndomos
def reverse_str(str):
  return str[::-1]

def is_palindrome(str):
  return str == reverse_str(str)

print("Ejercicio 1: Palíndomos")
print("========================")
print("¿Qué palabra quieres revisar por palíndromos?")
inp = input()
res = is_palindrome(inp)
print("La palabra -", inp, "- es un palíndomo:", res)

print("\n\n\nEjercicio 2: Non o par")
print("========================")
# 2) Revisa si es non
print("Escribe el número entero a revisar por non o par:")
inp = int(input())
# Ref: http://book.pythontips.com/en/latest/ternary_operators.html
# (if_test_is_false, if_test_is_true)[test]
res = ["non", "par"][((inp % 2) == 0)]
print("El número", inp, "es", res)
