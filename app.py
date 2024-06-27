from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

number_to_guess = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess')
def guess():
    global number_to_guess
    try:
        user_guess = int(request.args.get('number'))
    except ValueError:
        return jsonify({"message": "Por favor, insira um número válido."})
    
    if user_guess < number_to_guess:
        return jsonify({"message": "Muito baixo!"})
    elif user_guess > number_to_guess:
        return jsonify({"message": "Muito alto!"})
    else:
        number_to_guess = random.randint(1, 100)
        return jsonify({"message": "Parabéns! Você adivinhou o número! O jogo foi reiniciado."})

if __name__ == '__main__':
    app.run(debug=True)
