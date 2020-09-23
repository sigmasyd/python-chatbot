# de: Javier Sossa >> https://www.youtube.com/watch?v=K4kSXeLRvY4&ab_channel=Economiayfinanzas-JavierSossa
# mas: https://creditosrapidos.cash/formacion/
# chatbot avanzado: https://mega.nz/file/pyRy0ZRR#O5bixwWIHzdlRXED4kh6MpEcpvHO1MiSHGH5fCDDr5A


from nltk.chat.util import Chat, reflections
mis_reflexions = {
  "ir": "fui",
  "hola": "hey"
}
pares = [
  [
    r"mi nombre es (.*)",
    ["Hola %1, como estas ?",]
  ],
  [
    r"cual es tu nombre ?",
    ["Mi nombre es Chatbot",]
  ],
  [
    r"se me ha caido el hosting (.*)",
    ["Sentimos ese fallo, para reiniciarlo, entra en CPANEL y selecciona reiniciar",]
  ],
  [
    r"cuando hay que pagar la factura (.*)",
    ["Hay que pagarla el dia 15 de cada mes por tarjeta de credito",]
  ],
  [
    r"como estas ?",
    ["Bien y tu?",]
  ]
]
def chatear():
  print("Hola, soy el hosting server") # mensaje por defecto
  chat = Chat(pares, mis_reflexions)
  chat.converse()
if __name__=="__main__":
  chatear()

chatear()


