




def test_cast_get(client):
    response = client.get("/api/cast")
    assert response
    