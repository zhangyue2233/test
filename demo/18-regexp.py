import re
def test_string(your_patten):
    patten = re.compile(your_patten)
    strlist = [
        'abc','def','123','ABC','___'
    ]
    for i in strlist:
        if not re.match(patten,i):
            print('error')
            pass
        elif not i:
            print('can not null')
            pass
        else:
            print('pass')
            pass

ptn = r"[a-zA-Z0-9].*?"
test_string(ptn)