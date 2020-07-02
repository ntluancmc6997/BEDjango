from utils import mysql_connection
from utils import response_json


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



def requesters_add(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_add = """INSERT INTO requests (
            requesters_id,
            technicals_id,
            name,
            device,
            detail,
            status,
            request_date,
            start_time,
            end_time
            ) VALUES (%s,%s,%s,%s,%s,%s,NOW(),CURTIME(),CURTIME())"""

        cursor.execute(sql_add,
                       (obj_data_input['requesters_id'],
                        obj_data_input['technicals_id'],
                        obj_data_input['name'],
                        obj_data_input['device'],
                        obj_data_input['detail'],
                        obj_data_input['status']
                        ))

        connection.commit()
        response['code'] = 0

    except Exception as e:
        print('regist.models -> requesters_add -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


def requesters_edit(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_edit = """UPDATE requests SET 
                name = %s,
                device = %s,
                detail = %s,
                status = %s,
                request_date = NOW(),
                start_time = CURTIME(),
                end_time = CURTIME()
            WHERE id = %s"""

        cursor.execute(sql_edit,
                       (
                        obj_data_input['name'],
                        obj_data_input['device'],
                        obj_data_input['detail'],
                        obj_data_input['status'],
                        obj_data_input['id']
                        ))

        connection.commit()
        response['code'] = 0

    except Exception as e:
        print('regist.models -> requesters_edit -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


def requesters_del(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_del = "UPDATE requests SET del_flg = 1 WHERE id = %s"

        cursor.execute(sql_del, (obj_data_input['id']))

        connection.commit()
        response['code'] = 0

    except Exception as e:
        print('regist.models -> requesters_del -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response

