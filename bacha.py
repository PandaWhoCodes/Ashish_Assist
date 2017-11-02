import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

def getage():
    subscription_key = '2c2c93c599a86540841e5ac01a2e0635fe3be'
    uri_base = 'https://westcentralus.api.cognitive.microsoft.com'
    # Request headers.
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    # Request parameters.
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    filename = 'bacha.jpg'
    f = open(filename, "rb")
    body = f.read()
    f.close()

        # Body. The URL of a JPEG image to analyze.
    body = body
    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', data=body, headers=headers,
                                    params=params)
        parsed = json.loads(response.text)
        print(parsed)
        age = parsed[0]['faceAttributes']["age"]
        return(age)

    except Exception as e:
        print('Error:')
        print(e)
