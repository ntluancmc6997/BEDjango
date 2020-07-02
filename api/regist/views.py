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

        response = contants.get_response_regist(code_output)

    except Exception as e:
        print('regist.views -> regist_requesters -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def requesters_add(request, format=None):
    response = contants.get_response_regist(None)
    try:
        data_input = request.data
        obj_data_input = {
            "requesters_id": data_input['requesters_id'],
            "technicals_id": data_input['technicals_id'],
            "name": data_input['name'],
            "device": data_input['device'],
            "detail": data_input['detail'],
            "status": data_input['status']
        }

        data_output = models.requesters_add(obj_data_input)

        code_ouput = data_output['code']
        response = contants.get_response_regist(code_ouput)
    except Exception as e:
        print('regist.views -> requesters_add -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def requesters_edit(request, format=None):
    response = contants.get_response_regist(None)
    try:
        data_input = request.data
        obj_data_input = {
            "id": data_input['id'],
            "name": data_input['name'],
            "device": data_input['device'],
            "detail": data_input['detail'],
            "status": data_input['status']
        }

        data_output = models.requesters_edit(obj_data_input)

        code_ouput = data_output['code']
        response = contants.get_response_regist(code_ouput)
    except Exception as e:
        print('regist.views -> requesters_edit -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def requesters_del(request, format=None):
    response = contants.get_response_regist(None)
    try:
        data_input = request.data
        obj_data_input = {
            "id": data_input['id']
        }

        data_output = models.requesters_del(obj_data_input)

        code_ouput = data_output['code']
        response = contants.get_response_regist(code_ouput)
    except Exception as e:
        print('regist.views -> requesters_del -> ex: ', e)

    return Response(response)
