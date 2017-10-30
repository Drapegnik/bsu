TEST_TEMPLATE = '{value:.3f} {sign} {delta:.3f} | test {result}'


def extrapolate(seq, k):
    return [int(el * k) for el in seq]


def get_test_result(value, delta):
    return ['<', 'passed 👌'] if value < delta else ['>=', 'failed 😭']


def get_pearson_result(value, delta, k):
    template = 'k = {k} | ' + TEST_TEMPLATE
    sign, result = get_test_result(value, delta)
    return template.format(k=k, value=value, sign=sign, delta=delta, result=result)
