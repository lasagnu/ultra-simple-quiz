from flask import Blueprint, render_template, request, redirect, url_for

from questions import QUIZ_QUESTIONS

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form.to_dict()

        if not (username:=user_answers.get('username')):
            username = 'Mr. Unknown'

        score = sum(
            1 for question in QUIZ_QUESTIONS 
            if user_answers.get(str(question.id)) == question.answer
        )

        return redirect(url_for('main.result', score=score, total=len(QUIZ_QUESTIONS), username=username))
    
    return render_template('quiz.html', questions=QUIZ_QUESTIONS)

@main.route('/result')
def result():
    score = int(request.args.get('score', 0))
    total = int(request.args.get('total', 0))
    username = request.args.get('username', 'Mr. Unknown')
    return render_template('result.html', score=score, total=total, name=username)