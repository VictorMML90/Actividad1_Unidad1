from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

contenido = {
    "/": """<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Ana Lee</title>
  </head>
  <body>
    <h1>Ana Lee</h1>
    <h2>Desarrolladora Web</h2>
    <h3><a href="/proyecto/1">Proyecto 1</a></h3>
    <h3><a href="/proyecto/2">Proyecto 2</a></h3>
    <h3><a href="/proyecto/3">Proyecto 3</a></h3>
  </body>
</html>
""",

    "/proyecto/1": """
<html>
  <h1>Proyecto 1</h1>
  <p>App de recomendación de libros</p>
  <a href="/">Volver</a>
</html>
""",

    "/proyecto/2": """
<html>
  <h1>Proyecto 2</h1>
  <p>MeFalta - películas y series</p>
  <a href="/">Volver</a>
</html>
""",

    "/proyecto/3": """
<html>
  <h1>Proyecto 3</h1>
  <p>Foto22 - gestión de fotos</p>
  <a href="/">Volver</a>
</html>
"""
}


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    #def query_data(self):
      #  return dict(parse_qsl(self.url().query))

    def do_GET(self):


        ruta = self.url().path

        if ruta in contenido:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(contenido[ruta].encode("utf-8"))
        else:
            self.send_error(404, "Ruta no encontrada")


        #if self.url().path == "/":
         #   try:
          #      with open("home.html", "r", encoding = "utf-8") as f:
           #      contenido = f.read()

            #    self.send_response(200)
             #   self.send_header("Content-Type", "text/html")
              #  self.end_headers()
               # self.wfile.write(contenido.encode("utf-8"))
            
            #except FileNotFoundError:
             #   self.send_error(404,"Archivo home.html no se ha encontrado")
        #else:
         #   self.send_error(404,"Ruta no encontrada")
        
        
        #if self.valida_request():
         #   self.send_response(200)
          #  self.send_header("Content-Type", "text/html")
           # self.end_headers()
            #self.wfile.write(self.get_html(self.url().path, self.query_data()).encode("utf-8")) 
        #else: 
         #   self.send_error(404, 'El autor no existe')
        


    #def valida_request(self):
     #   if 'autor'in self.query_data():
      #      return True
       # else:
        #    return False    
        
    #def get_html(self, path, qs):
     #   return f"""
      #  <h1>Proyecto: {path} Autor: {qs['autor']} </h1>

    #def get_response(self):
     #   return f"""
    #<h1> Hola Web </h1>
    #<p> URL Parse Result : {self.url()}         </p>
    #<p> Path Original: {self.path}         </p>
    #<p> Headers: {self.headers}      </p>
    #<p> Query: {self.query_data()}   </p>



if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
