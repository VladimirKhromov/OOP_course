class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        method = request.get('method').upper()
        if request["method"] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = self.__getattribute__(method.lower())
        if method_request:
            return method_request(request) 





class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
print(html)   # GET: https://stepik.org/course/116336/
