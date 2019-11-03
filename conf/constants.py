# coding:utf-8
"""
mysql manipulate return data status code
"""
status_success = 0
status_fail = -1
success_format = {
    'status': status_success,
    'data': None,
    'msg': '',
}

fail_format = {
    'status': status_fail,
    'data': None,
    'msg': '',
}
