class RenderList:
    def __init__(self, type_list):
        self.type_list = self.check_type_list(type_list)

    def check_type_list(self, type_list):
        if type_list == "ol":
            return "ol"
        else:
            return "ul"

    def __call__(self, arr:list):
        return f"<{self.type_list}>\n" + '\n'.join(["<li>" + i + "</li>" for i in arr]) + f"\n</{self.type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)