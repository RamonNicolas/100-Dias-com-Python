from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome =db.Column(db.String(80), nullable=False)
    comentario=db.Column(db.String(), nullable=False)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://edtnewowkyudxk:6afc02d1af908ff9aa113ec75dd8feaee39f57501bbac79d4e8b246c6ba850aa@ec2-52-203-164-61.compute-1.amazonaws.com:5432/d7sdu01cl5qa4l'
    app.db = db.init_app(app)
    Migrate(app,db)
    
    @app.route("/")
    def index():
        return render_template('index.html')
        

    @app.route("/post", methods=['POST'])
    def post():
        form = request.form
        comment = Comentario(
            nome=form['nome'],
            comentario=form['comentario']
            )

        db.session.add(comment)
        db.session.commit()
        return redirect("/")


    return app 

