from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.decorators import parser_classes
from rest_framework.renderers import JSONRenderer
from . import models, contants


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def regist_requesters(request, format=None):
    response = contants.get_response_regist(None)
    try:
        request_data = request.data

        obj_data_input = {
            "user_name": request_data['email'],
            "password": request_data['password']
        }

        data_output = models.regist_requesters(obj_data_input)
        code_output = data_output['code']

        response = contants.get_response_get_data_search(code_output)

    except Exception as e:
        print('regist.views -> regist_requesters -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def add_request(request, format=None):
    response = contants.get_response_regist(None)
    try:

        data_request = request.data

        obj_input_data = {
            "requesters_id": data_request["requesters_id"],
            "technicals_id": data_request["technicals_id"],
            "name": data_request["name"],
            "device": data_request["device"],
            "detail": data_request["detail"],
            "status": data_request["status"],
            "request_date": data_request["request_date"],
            "end_time": data_request["end_time"],
            "start_time": data_request["start_time"]
        }
        data_output = models.add_request(obj_input_data)

        code_ouput = data_output['code']

        response = contants.get_response_edit(code_ouput)

    except Exception as e:
        print('editRequest.views -> add_request -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def update_request(request, format=None):
    response = contants.get_response_edit(None)
    try:
        data_request = request.data
        print(data_request)
        data_output = models.edit_request(data_request)
        code_output = data_output['code']
        response = contants.get_response_edit(code_output)

    except Exception as e:
        print('editRequest.views -> update_request -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def delete_request(request, format=None):
    response = contants.get_response_edit(None)
    try:
        data_request = request.data
        data_output = models.delete_request(data_request)
        code_output = data_output['code']
        response = contants.get_response_edit(code_output)

    except Exception as e:
        print('editRequest.views -> delete_request -> ex: ', e)

    return Response(response)


