from flask import Flask, request
from flask_restful import Api, Resource
from models import db, BookModel

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Books_RESTAPI.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)


class BooksView(Resource):
    def get(self):
        books = BookModel.query.all()
        return {"Books": list(x.json() for x in books)}

    def post(self):
        data = request.get_json()
        print("Hello:-",data)
        new_book = BookModel(data['name'], data['price'], data['author'])
        db.session.add(new_book)
        db.session.commit()
        return new_book.json(), 201


class BookView(Resource):
    def get(self,name):
        book = BookModel.query.filter_by(name=name).first()
        if book:
            return book.json()
        return {'message':'book not found'}, 404
 
    def put(self,name):
        print(request)
        data = request.get_json()

        book = BookModel.query.filter_by(name = name).first()
        if book:
            book.price = data["price"]
            book.author = data["author"]
        else:
            book = BookModel(name=name, **data)
        
        db.session.add(book)
        db.session.commit()

        return book.json()
 
    def delete(self,name):
        book = BookModel.query.filter_by(name=name).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'book not found'}, 404

api.add_resource(BooksView, '/books')
api.add_resource(BookView,'/book/<string:name>')


@app.before_first_request
def create_table():
    db.create_all()

app.debug = True
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)