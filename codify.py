import base64

mensaje = "Hola, este es un mensaje para codificar en Base64."
mensaje_codificado = base64.b64encode(mensaje.encode("utf-8")).decode("utf-8")

print(mensaje_codificado)

