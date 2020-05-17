from endpoints.sampleauth import sampleauth

def test_auth_test():

    getauth = sampleauth()
    result = getauth.authtests()

    assert result.status_code == 200