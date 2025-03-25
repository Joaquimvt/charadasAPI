from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

charadas = [
    {'pergunta': 'O que é, o que é? Quanto mais você tira, maior fica.', 'resposta': 'O buraco'},
    {'pergunta': 'O que é, o que é? Tem cidades, mas não casas, tem montanhas, mas não árvores, tem água, mas não peixes.', 'resposta': 'O mapa'},
    {'pergunta': 'O que é, o que é? Tem asas, mas não voa. Tem bico, mas não bica.', 'resposta': 'O bule'},
    {'pergunta': 'O que é, o que é? Anda com os pés na cabeça?', 'resposta': 'O piolho'},
    {'pergunta': 'O que é, o que é? Sempre está no meio da rua.', 'resposta': 'A letra "u"'},
    {'pergunta': 'O que é, o que é? Fica cheia de boca para baixo e vazia de boca para cima.', 'resposta': 'O chapéu'},
    {'pergunta': 'O que é, o que é? Quanto mais se tira, mais ele cresce.', 'resposta': 'O buraco'},
    {'pergunta': 'O que é, o que é? Tem dentes, mas não morde.', 'resposta': 'O pente'},
    {'pergunta': 'O que é, o que é? O que tem no meio da banana?', 'resposta': 'A letra "n"'},
    {'pergunta': 'O que é, o que é? O que nasce grande e morre pequeno?', 'resposta': 'O lápis'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova_charada')
def nova_charada():
    return jsonify(random.choice(charadas))

if __name__ == '__main__':
    app.run(debug=True)
