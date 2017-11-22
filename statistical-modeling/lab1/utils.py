TEST_TEMPLATE = '{value:.3f} {sign} {delta:.3f} | test {result}'


def get_test_result(value, delta):
    return ['<', 'passed 👌'] if value < delta else ['>=', 'failed 😭']


def format_test_result(value, delta, k=None):
    template = TEST_TEMPLATE
    if k:
        template = 'k = {k} | ' + TEST_TEMPLATE
    sign, result = get_test_result(value, delta)
    return template.format(k=k, value=value, sign=sign, delta=delta, result=result)
