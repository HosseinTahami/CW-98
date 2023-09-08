class AuthenticationDecorator:
    def __init__(self, my_api):
        self.api = my_api

    def __call__(self, request):
        if self.is_authenticated(request):
            return self.api(request)
        raise ValueError("Login Error")

    @staticmethod
    def is_authenticated(request):
        return request.get("header").get("token") == "helloworld"


@AuthenticationDecorator
class API:
    def __init__(self, request):
        self.request = request

    def end_point(self):
        return "EndPoint"


@AuthenticationDecorator
def API(request):
    return "EndPoint"


request = {"header": {"token": "helloworld"}}
result = API(request)
print(result)
