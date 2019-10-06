# coding:utf-8
"""
mysql manipulate return data status code
"""
status_success = 0
status_fail = -1
success_data_format = {
    'status': status_success,
    'data': None,
    'msg': '',
}

fail_data_format = {
    'status': status_fail,
    'data': None,
    'msg': '',
}
