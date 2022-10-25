from flask import Flask,request,Response
from flask_restful import Resource,Api, reqparse
from Database.Database_handler import Database_handler
from Object_template.Add import add_book
from Object_template.Borrow import borrow_book
from Object_template.Return import return_book
from flask_cors import CORS


app=Flask(__name__)
api=Api(app)
CORS(app)

class SearchByKeyword(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument("keyword", type=str, required=True, help ="No keyword provided",location="args")
        args = parser.parse_args()
        message=Database_handler().search_by_keyword(args["keyword"])

        if message:
            return Response(
                    response=message,
                    status=200,
                    mimetype="application/json"
                )
        else:
            return Response(
                    response="""{"message":"no book found"}""",
                    status=200,
                    mimetype="application/json"
                )



class SearchByISBN13(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument("ISBN13", type=str, required=True, help ="No ISBN13 provided",location="args")
        args = parser.parse_args()
        print(args["ISBN13"])
        message=Database_handler().search_by_ISBN(args["ISBN13"])

        if message:
            return Response(
                    response=message,
                    status=200,
                    mimetype="application/json"
                )
        else:
            return Response(
                    response="""{"message":"no book found"}""",
                    status=200,
                    mimetype="application/json"
                )

class Borrow(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            borrow_object=borrow_book((request_data["ISBN13"],request_data["username"],request_data["password"]))
            message=Database_handler().Borrow(borrow_object)
        except:
            message="""{"message":"input error"}"""
    
        return Response(
                response=message,
                status=200,
                mimetype="application/json"
            )

class Return(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            borrow_object=return_book((request_data["ISBN13"],request_data["username"],request_data["password"]))
            message=Database_handler().Return(borrow_object)

        except:
            message="""{"message":"input error"}"""


    
        return Response(
                response=message,
                status=200,
                mimetype="application/json"
            )

class Add(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            if request_data["quantity"]==0:
                message="""{"message":"quantity can not be 0"}"""
            else:
                borrow_object=add_book((request_data["ISBN13"],request_data["title"],request_data["quantity"],request_data["username"],request_data["password"]))
                message=Database_handler().Add(borrow_object)
        except:
            message="""{"message":"input error"}"""

    
        return Response(
                response=message,
                status=200,
                mimetype="application/json"
            )

api.add_resource(SearchByKeyword,"/search/keyword")
api.add_resource(SearchByISBN13,"/search/ISBN13")
api.add_resource(Borrow,"/Borrow")
api.add_resource(Return,"/Return")
api.add_resource(Add,"/Add")


app.run(port=5000,debug=True)