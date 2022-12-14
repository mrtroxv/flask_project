from script import read_from_file
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
from validation import insert_and_update_validation, is_valid_id, content_validation
from sqlalchemy.exc import IntegrityError


# ****************select api***********************************#
@app.route("/song/<int:id>", methods=["GET"])
def select(id: int):
    if not is_valid_id.is_valid(id):
        return make_response("ur id is not valid", status.HTTP_400_BAD_REQUEST)
    else:
        content = jsonify(database_select.select(id))
        return make_response(content, status.HTTP_200_OK)


# *************************insert api************************************#


@app.route("/song", methods=["POST"])
def insert():
    req = request.json
    if not insert_and_update_validation.is_valid_insert(req):
        return make_response("not correct input", status.HTTP_400_BAD_REQUEST)
    else:
        try:
            database_insert.insert_mydata(req)
            return make_response("the data inserted thank u", status.HTTP_201_CREATED)
        except IntegrityError:
            return make_response(
                "Ur input id is already exist", status.HTTP_400_BAD_REQUEST
            )


# ***********************delete api*************************************#


@app.route("/song/<int:id>", methods=["DELETE"])
def delete(id: int):
    if not is_valid_id.is_valid(id):
        return make_response("ur id is not valid", status.HTTP_400_BAD_REQUEST)

    else:
        database_delete.delete(id)
        return make_response("the data deleted", status.HTTP_204_NO_CONTENT)


# ***********************update api************************************#


@app.route("/song/<int:id>", methods=["PUT"])
def update(id: int):
    req = request.json
    if not insert_and_update_validation.is_valid_insert(req):
        return make_response("not correct input", status.HTTP_400_BAD_REQUEST)
    else:
        database_update.update(req, id)
        return make_response("the data updated", status.HTTP_200_OK)


# *************************insert file Api***********************************#
@app.route("/song_as_file", methods=["POST"])
def insert_file():
    the_req_obj = FileInsertionRequestData(
        request.files.get("data_file"),
        request.form.get("tag"),
        request.form.get("force_replace"),
    )
    if not content_validation.is_valid(the_req_obj):
        return make_response("Content is not valid", status.HTTP_400_BAD_REQUEST)
    else:
        the_req_obj = content_validation.content_make_valid(the_req_obj)
        if not read_from_file.read_from_file_api(the_req_obj):
            return make_response(
                "the content has not correct format", status.HTTP_400_BAD_REQUEST
            )
        return make_response("your data is uptodate", status.HTTP_200_OK)


# ***********************************select by filter Api*******************************#
@app.route("/song_select", methods=["GET"])
def select_by_filters():
    request_data = request.args
    try:
        page = int(request_data.get("page"))
        if page <= 0:
            return make_response(
                "the page number must grater than  zero", status.HTTP_400_BAD_REQUEST
            )
    except TypeError:
        page = 1
    except ValueError:
        return make_response("invalid page value", status.HTTP_400_BAD_REQUEST)

    try:
        content = jsonify(database_select.select_by_filters(request_data, page))
    except:
        return make_response("invalid date value", status.HTTP_400_BAD_REQUEST)
    return make_response(content, status.HTTP_200_OK)


app.run(debug=True)
