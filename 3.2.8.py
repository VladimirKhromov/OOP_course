class HandlerGET:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, request, *args, **kwargs):
        m = request.get("method", "GET")
        if m == "GET":
            return self.get(self.func, request)
        return 


    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"











## TEST ## 

@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"