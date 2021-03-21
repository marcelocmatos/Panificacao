from flask import Flask, request, render_template
from tipo_fermento import Tipo_Fermento


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicio():
	nome = ''
	tipo = ''
	peso = ''
	fermento = ''
	if request.method == 'POST' and 'nome' in request.form:
		nome = request.form.get('nome')
		tipo = request.form.get('tipo_fermento')
		peso = request.form.get('peso_fermento')
		fermento = Tipo_Fermento.tipo_fermento(tipo, peso)

	return render_template('index.html', nome=nome, fermento=fermento)

app.run()

