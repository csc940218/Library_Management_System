from Object_template.book import book
from json import JSONEncoder
class DeptDetailsEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, book):
            return {"ISBN13": o.ISBN13, "title": o.title, "availiability":o.availiability,"total":o.total}
        return super().default(o)