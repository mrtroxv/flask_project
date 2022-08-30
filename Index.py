from flask import request, jsonify, make_response
from flask_api import status
from database_interaction import DatabaseSelect, DataBaseInsert, DatabaseDelete, DatabaseUpdate
from database_interaction import Database
from database_interaction.Database import app
from validation import IsValidId, InsertAndUpdateValidation


#****************select api***********************************#
@app.route('/select_song', methods=['GET'])
def select():
    req = request.json
    req_id = req['id']
    if IsValidId.is_valid(req_id):
        Nres = make_response("ur id is not valid",
                             status.HTTP_406_NOT_ACCEPTABLE)
        return Nres
    else:
        dict = {}
        dict = DatabaseSelect.select(req_id)
        content = jsonify({
            "name": dict['name'],
            "author": dict['author'],
            'type': dict['type'],
            'image_url': dict['image_url'],
            'file_url': dict['file_url'],
            'rating': dict['rating'],
            'tag': dict['tag']
        })
        res = make_response(content, status.HTTP_302_FOUND)
        return res

#*************************insert api************************************#


@app.route('/insert_song', methods=['POST'])
def insert():
    req = request.json
    if InsertAndUpdateValidation.is_valid_insert(req):
        res = make_response("not correct input",
                            status.HTTP_406_NOT_ACCEPTABLE)
        return res
    else:
        DataBaseInsert.insert_mydata(req)
        res = make_response("the data inserted thank u",
                            status.HTTP_202_ACCEPTED)
        return res

#***********************delete api*************************************#


@app.route('/delete', methods=['DELETE'])
def delete():
    req = request.json
    if IsValidId.is_valid(req['id']):
        Nres = make_response("ur id is not valid",
                             status.HTTP_406_NOT_ACCEPTABLE)
        return Nres
    else:
        DatabaseDelete.delete(req['id'])
        res = make_response("the data deleted", status.HTTP_200_OK)
        return res

#***********************update api************************************#


@app.route('/update', methods=['PUT'])
def update():
    req = request.json
    if InsertAndUpdateValidation.is_valid_insert(req):
        res = make_response("not correct input",
                            status.HTTP_406_NOT_ACCEPTABLE)
        return res
    else:
        DatabaseUpdate.update(req)
        res = make_response("the data updated", status.HTTP_202_ACCEPTED)
        return res


app.run(debug=True)
