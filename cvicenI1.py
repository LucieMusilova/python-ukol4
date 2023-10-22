import math

def zadej_tel(tel: str) -> bool:
  tel = tel.replace(" ", "")
  if len(tel) == 9:
    return True
  elif len(tel) == 13 and tel[:4] == "+420":
    return True
  else: 
    return False

def cena_zpravy(text: str) -> int: 
  CENA = 3
  cena = math.ceil(len(text) / 180) * CENA
  return cena

tel_cislo = (input("Na jaké číslo chcete odeslat zprávu?"))
  
if zadej_tel(tel_cislo):
  text_zpravy = input("Jaký je text zprávy, který chcete poslat?")
  if len(text_zpravy) > 0:
    print(f"Cena odeslané zprávy bude {cena_zpravy(text_zpravy)} Kč.")
  else:
    print("Nezadal/a jste žádný text.")
else: 
  print("Zadané číslo není v požadovaném formátu.")
  
