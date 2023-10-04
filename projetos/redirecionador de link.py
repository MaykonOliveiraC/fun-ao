from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

links_sistema = {}

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        link_origem = request.form["link_origem"]
        caminho_destino = request.form["caminho_destino"]
        if caminho_destino not in links_sistema.keys():
            links_sistema[caminho_destino] = link_origem
            return f"Seu link: {request.url_root}{caminho_destino}"
        else:
            return "Caminho Destino não disponível, tente outro"
    else:
        return render_template("homepage.html")

@app.route("/<caminho_destino>")
def redirecionar(caminho_destino):
    link_origem = links_sistema.get(caminho_destino)
    if link_origem:
        return redirect(link_origem)
    else:
        return "Link não encontrado", 404

if __name__ == "__main__":
    app.run()