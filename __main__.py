from flask import Flask , jsonify
from DataBaseService import Libros 

app = Flask(__name__)


@app.route("/")
def GetLibros():
    return jsonify({"api/Libros/get":"Para Obtener los una lista de Libros ",
    "api/Libros/get{ id}":"Para Obtener los un libro por su id ",
    "api/Libros/post":"Para Reguistar Un libro en la  Lista de Libros  "})

@app.route("/api/Libros/get")
def LibrosGet():
    return jsonify(Libros)

@app.route("/api/Libros/get/<int:id>")
def LibrosGetByID(id):
    for i in Libros:
        if(i["id"] == id):
            return jsonify(i)
    



    

if (__name__=="__main__"):
    app.run(debug= True)