def check_registration_rules(**kwargs):
    def pass_check(password):
        password = list(password)
        for digit in password:
            if not digit.isdigit():
                return True

    passed_list = []
    for key in kwargs:
        if 4 <= len(key):
            if not key == "quera":
                if not key == "codecup":
                    if 6 <= len(kwargs[key]):
                        if pass_check(kwargs[key]):
                            passed_list.append(key)
    return passed_list


print(check_registration_rules(ald="123234234a", saeed="scdsas", sina="vkmkv"))
