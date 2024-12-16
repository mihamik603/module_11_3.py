def objekt_info(subj):

    subj_type = type(subj).__name__

    attributes = dir(subj)

    methods = [attr for attr in attributes if callable(getattr(subj, attr))]

    module = subj.__mod__

    info = {'type': subj_type,'attributes': attributes,'methods': methods,'module': module}

    return info


number_info = objekt_info(15)
print(number_info)
