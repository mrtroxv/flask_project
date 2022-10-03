from flask_restful import reqparse
from type.rating_args import rating_type
from type import id_args, String_args, date_args

req_dict = {}
parser = reqparse.RequestParser()


def add_arg():
    parser.add_argument("id", type=id_args.id_type, help="invalid id input")
    parser.add_argument("rating", type=rating_type, help="invalid rate input")
    parser.add_argument("type", type=String_args.string_type, help="invalid type input")
    parser.add_argument(
        "author",
        type=String_args.string_type,
        help="invalid  author input",
    )
    parser.add_argument(
        "name",
        type=String_args.string_type,
        help="invalid  name input",
    )
    parser.add_argument(
        "image_url",
        type=String_args.string_type,
        help="invalid  image_url input",
    )
    parser.add_argument(
        "file_url",
        type=String_args.string_type,
        help="invalid  file_url input",
    )
    parser.add_argument(
        "tag",
        type=String_args.string_type,
        help="invalid  tag input",
    )

    parser.add_argument(
        "time_created",
        type=date_args.date_type,
        help="invalid date value",
    )

    parser.add_argument(
        "time_updated",
        type=date_args.date_type,
        help="invalid date value",
    )


def make_req_full():
    add_arg()
    req_dict["id"] = parser.parse_args().get("id")
    req_dict["rating"] = parser.parse_args().get("rating")
    req_dict["author"] = parser.parse_args().get("author")
    req_dict["name"] = parser.parse_args().get("name")
    req_dict["image_url"] = parser.parse_args().get("image_url")
    req_dict["file_url"] = parser.parse_args().get("file_url")
    req_dict["tag"] = parser.parse_args().get("tag")
    req_dict["type"] = parser.parse_args().get("type")
    req_dict["time_created"] = parser.parse_args().get("time_created")
    req_dict["time_updated"] = parser.parse_args().get("time_updated")
    return req_dict


def make_req_semi():
    add_arg()
    if parser.parse_args().get("id") != None:
        req_dict["id"] = parser.parse_args().get("id")
    if parser.parse_args().get("rating") != None:
        req_dict["rating"] = parser.parse_args().get("rating")
    if parser.parse_args().get("author") != None:
        req_dict["author"] = parser.parse_args().get("author")
    if parser.parse_args().get("name") != None:
        req_dict["name"] = parser.parse_args().get("name")
    if parser.parse_args().get("image_url") != None:
        req_dict["image_url"] = parser.parse_args().get("image_url")
    if parser.parse_args().get("image_url") != None:
        req_dict["file_url"] = parser.parse_args().get("file_url")
    if parser.parse_args().get("tag") != None:
        req_dict["tag"] = parser.parse_args().get("tag")
    if parser.parse_args().get("type") != None:
        req_dict["type"] = parser.parse_args().get("type")
    return req_dict
