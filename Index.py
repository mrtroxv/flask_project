from script import read_from_file
from args import arg_insert_by_file, args_operation
from flask_restful import reqparse, Resource, Api
from flask import request, make_response, jsonify
from data_object.request_data import FileInsertionRequestData
from flask_api import status
from database_interaction import (
    database_delete,
    database_insert,
    database_select,
    database_update,
)
from database_interaction.database import app
from validation import is_valid_id, content_validation
from sqlalchemy.exc import IntegrityError

req_dict = {}

parser = reqparse.RequestParser()
api = Api(app)


class Song(Resource):
    def get(self, id):
        if not is_valid_id.is_valid(id):
            return make_response("ur id is not valid", status.HTTP_400_BAD_REQUEST)
        else:
            content = jsonify(database_select.select(id))
            return make_response(content, status.HTTP_200_OK)

    def post(self):
        req_dict = args_operation.make_req_full()
        try:
            database_insert.insert_mydata(req_dict)
        except IntegrityError:
            return make_response(
                "you have similar id value", status.HTTP_400_BAD_REQUEST
            )

        return make_response("the data inserted thank u", status.HTTP_201_CREATED)

    def delete(self, id):
        if not is_valid_id.is_valid(id):
            return make_response("ur id is not valid", status.HTTP_400_BAD_REQUEST)

        else:
            database_delete.delete(id)
            return make_response("the data deleted", status.HTTP_204_NO_CONTENT)

    def put(self, id):
        if not is_valid_id.is_valid(id):
            return make_response("ur id is not valid", status.HTTP_400_BAD_REQUEST)
        else:
            req_dict = args_operation.make_req_semi()
            database_update.update(req_dict, id)
            return make_response("the data updated", status.HTTP_200_OK)


class SongSelectAndInsert(Resource):
    def post(self):
        req_dict = arg_insert_by_file.make_req_by_arg_insert_file()
        the_req_obj = FileInsertionRequestData(
            req_dict.get("data_file"),
            req_dict.get("tag"),
            req_dict.get("force_replace"),
        )
        the_req_obj = content_validation.content_make_valid(the_req_obj)
        if not read_from_file.read_from_file_api(the_req_obj):
            return make_response(
                "the content has not correct format", status.HTTP_400_BAD_REQUEST
            )
        return make_response("your data is uptodate", status.HTTP_200_OK)

    def get(self):
        req_dict = args_operation.make_req_semi()
        parser.add_argument(
            "page",
            type=int,
            default=1,
            help="the page value incorrect",
        )
        page = parser.parse_args().get("page")
        if page <= 0:
            return make_response("invalid page number ", status.HTTP_400_BAD_REQUEST)
        content = jsonify(database_select.select_by_filters(req_dict, page))
        return make_response(content, status.HTTP_200_OK)


api.add_resource(Song, "/song/<int:id>", "/song")
api.add_resource(SongSelectAndInsert, "/song_as_file", "/song_select")


if __name__ == "__main__":
    app.run(debug=True)
