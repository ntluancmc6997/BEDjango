from utils import mysql_connection
from utils import response_json
from . import contants


def regist_requesters(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_search_exist = f"SELECT * FROM requesters WHERE user_name=\"{obj_data_input['user_name']}\" "

        cursor.execute(sql_search_exist)

        if cursor.rowcount > 0:
            response['code'] = 1

        elif cursor.rowcount == 0:
            sql_insert = f"INSERT INTO requesters(user_name, password, created_date, update_date) values(\"{obj_data_input['user_name']}\", \"{obj_data_input['password']}\", now(), now())"

            cursor.execute(sql_insert)
            connection.commit()

            response['code'] = 0

    except Exception as e:
        print('regist.models -> regist_requesters -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response



def add_request(obj_data_input):
    # user_id, name, device, detail, request_date, end_time, start_time
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)

    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_search_exist = f"SELECT * FROM requests WHERE name=\"{obj_data_input['name']}\" and device=\"{obj_data_input['device']}\" "
        cursor.execute(sql_search_exist)
        if cursor.rowcount > 0:
            response['code'] = 3

        elif cursor.rowcount == 0:
            sql_insert = f"INSERT INTO requests(requesters_id, technicals_id, name," \
                         f" device, detail, status, request_date, end_time, start_time, created_date, updated_date)" \
                         f" values(%s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now())"

            cursor.execute(sql_insert, (obj_data_input['requesters_id'], obj_data_input['technicals_id'],
                                        obj_data_input['name'], obj_data_input['device'], obj_data_input['detail'],
                                        obj_data_input['status'], obj_data_input['request_date'],
                                        obj_data_input['end_time'], obj_data_input['start_time']))
            connection.commit()

            response['code'] = 0
    except Exception as e:
        print('editRequest.models -> add_request -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


def edit_request(obj_data_input):
    # user_id, name, device, detail, request_date, end_time, start_time
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_search_exist = f"SELECT * FROM requests WHERE id={obj_data_input['id']} "
        print(sql_search_exist)
        cursor.execute(sql_search_exist)

        if cursor.rowcount == 0:
            response['code'] = 1
        elif cursor.rowcount > 0:
            for obj in obj_data_input:
                if obj != "id":
                    sql_update = f"UPDATE requests SET {obj} = \"{obj_data_input[obj]}\" WHERE id = \"{obj_data_input['id']}\""
                    cursor.execute(sql_update)
                    connection.commit()
                    print(f"Modify {obj} to {obj_data_input[obj]}")

            response['code'] = 0
    except Exception as e:
        print('editRequest.models -> edit_request -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response

# TODO: Change SQL action for delete request
def delete_request(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_search_exist = f"SELECT * FROM requests WHERE id={obj_data_input['id']} "
        print(sql_search_exist)
        cursor.execute(sql_search_exist)

        if cursor.rowcount == 0:
            response['code'] = 1
        elif cursor.rowcount > 0:
            sql_update = f"""UPDATE requests SET del_flg = 1 WHERE id = \"{obj_data_input['id']}\""""
            cursor.execute(sql_update)
            connection.commit()

            response['code'] = 0
    except Exception as e:
        print('editRequest.models -> delete_request -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response

