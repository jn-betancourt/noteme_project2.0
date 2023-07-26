from rest_framework.views import APIView, Response, status
import requests
import json

# Create your views here.


class RegisterGithub(APIView):
    def post(self, request, format=None):
        print(request.data)
        params = request.data["data"]
        params = f"client_id={params['client_id']}&client_secret={params['client_secrets']}&code={params['code']}"
        res = requests.post(
            f"https://github.com/login/oauth/access_token?{params}",
            headers={"accept": "application/json"},
        )

        if res.status_code == 200:
            data = res.content.decode()
            json_data = json.loads(data)
            print(json_data)
            user_data = requests.get(
                "https://api.github.com/user",
                headers={"Authorization": f"Bearer {json_data['access_token']}"},
            )
            user_data = json.loads(user_data.content.decode())
            print(user_data)

        return Response(status=status.HTTP_200_OK)
