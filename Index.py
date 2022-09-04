from flask import request, jsonify, make_response
from flask_api import status
from database_interaction import database_delete, database_insert, database_select, database_update
from database_interaction.database import app
from validation import insert_and_update_validation, is_valid_id
from sqlalchemy.exc import IntegrityError


#****************select api***********************************#
@app.route('/song/<int:id>', methods=['GET'])
def select(id: int):
    if not is_valid_id.is_valid(id):
        return make_response("ur id is not valid",
                             status.HTTP_400_BAD_REQUEST)
    else:
        content = jsonify(database_select.select(id))
        return make_response(content, status.HTTP_200_OK)

#*************************insert api************************************#


@app.route('/song', methods=['POST'])
def insert():
    req = request.json
    if not insert_and_update_validation.is_valid_insert(req):
        return make_response("not correct input",
                             status.HTTP_400_BAD_REQUEST)
    else:
        try:
            database_insert.insert_mydata(req)
            return make_response("the data inserted thank u",
                                 status.HTTP_201_CREATED)
        except IntegrityError:
            return make_response("Ur input id is already exist", status.HTTP_400_BAD_REQUEST)

#***********************delete api*************************************#


@app.route('/song/<int:id>', methods=['DELETE'])
def delete(id: int):
    if not is_valid_id.is_valid(id):
        return make_response("ur id is not valid",
                             status.HTTP_400_BAD_REQUEST)

    else:
        database_delete.delete(id)
        return make_response("the data deleted", status.HTTP_204_NO_CONTENT)


#***********************update api************************************#


@app.route('/song/<int:id>', methods=['PUT'])
def update(id: int):
    req = request.json
    if not insert_and_update_validation.is_valid_insert(req):
        return make_response("not correct input",
                             status.HTTP_400_BAD_REQUEST)
    else:
        database_update.update(req, id)
        return make_response("the data updated", status.HTTP_200_OK)


app.run(debug=True)