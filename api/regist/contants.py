from rest_framework import status


def get_response_regist(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Display data successful'

    return response


def get_response_edit(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later!',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Edit successfully'
        elif code == 3:
            response['message'] = 'The request is already exists'
        elif code == "1":
            response['message'] = 'The request is not exists'
        elif code == "2":
            response['message'] = 'Wrong password'

    return response
