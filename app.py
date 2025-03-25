from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'pergunta': 'O que é, o que é? Quanto mais você tira, maior fica.', 'resposta': 'O buraco'},
    {'id': 2, 'pergunta': 'O que é, o que é? Tem cidades, mas não casas, tem montanhas, mas não árvores, tem água, mas não peixes.', 'resposta': 'O mapa'},
    {'id': 3, 'pergunta': 'O que é, o que é? Tem asas, mas não voa. Tem bico, mas não bica.', 'resposta': 'O bule'},
    {'id': 4, 'pergunta': 'O que é, o que é? Anda com os pés na cabeça?', 'resposta': 'O piolho'},
    {'id': 5, 'pergunta': 'O que é, o que é? Sempre está no meio da rua.', 'resposta': 'A letra "u"'},
    {'id': 6, 'pergunta': 'O que é, o que é? Fica cheia de boca para baixo e vazia de boca para cima.', 'resposta': 'O chapéu'},
    {'id': 7, 'pergunta': 'O que é, o que é? Quanto mais se tira, mais ele cresce.', 'resposta': 'O buraco'},
    {'id': 8, 'pergunta': 'O que é, o que é? Tem dentes, mas não morde.', 'resposta': 'O pente'},
    {'id': 9, 'pergunta': 'O que é, o que é? O que tem no meio da banana?', 'resposta': 'A letra "n"'},
    {'id': 10, 'pergunta': 'O que é, o que é? O que nasce grande e morre pequeno?', 'resposta': 'O lápis'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova_charada')
def nova_charada():
    return jsonify(random.choice(charadas))

if __name__ == '__main__':
    app.run(debug=True)
