from flask_restful import reqparse
import werkzeug

req_dict = {}
parser = reqparse.RequestParser()


def add_arg():
    parser.add_argument(
        "data_file",
        type=werkzeug.datastructures.FileStorage,
        location="files",
        required=True,
        help="invalid file input",
    )
    parser.add_argument(
        "tag", default=None, help="incorrect tag input", location="form"
    )
    parser.add_argument(
        "force_replace",
        default=False,
        help="incorrect force replace input ",
        location="form",
    )


def make_req_by_arg_insert_file():
    add_arg()
    req_dict["data_file"] = parser.parse_args().get("data_file")
    req_dict["tag"] = parser.parse_args().get("tag")
    req_dict["force_replace"] = parser.parse_args().get("force_replace")
    return req_dict
