# Repo: https://github.com/alejandrofloresm/hp-hello-world

# Imprimir una cadena de texto
print("Hello world")

# Enteros
i_am_int = 5
print(i_am_int, "es un entero (int)")

# Flotantes
i_am_float = 5.5
print(i_am_float, "es un flotantes (float)")

# String
i_am_string = "Yo soy cadenín"
print("-",i_am_string,"- es una cadena (string)")

# Boolean
i_am_bool = True
print(i_am_bool, "es un booleano (bool)")

# Ejemplo de una función
def get_total_price(price_without_taxes):
  return price_without_taxes * 1.16

price_without_taxes = 15.5
total = get_total_price(price_without_taxes)
print(total, "es el precio considerando los impuestos")

# Manejo del input del usuario
print("¿Cuál es tu nombre?")
user_name = input()
print("¿Cuánto cuesta un kg de aguacate?")
avocado_price = float(input())
print("El nombre del usuario es:", user_name, "el kg de aguacate cuesta:", avocado_price)
