def test_get_user_sucessfully(user_api):
    res = user_api.get_user(1)
    assert res.status_code == 200
    data = res.json()
    name = data["name"]
    
    assert name == "Leanne Graham"

