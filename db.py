class Note:
    id: str
    date: str
    title: str
    text: str


class db:
    id_ = 0
    storage = {}

    def Create(self, note: Note):
        self.id_ += 1
        self.storage[self.id_] = note

    def List(self):
        for x, y in self.storage.items():
            print(x, y.id, y.date, y.title, y.text)

    def Read(self, ident: str) -> Note:
        for x, y in self.storage.items():
            if (y.id == ident):
                return(y)
        print("NotFoun")
    def Update(self, ident: str, note: Note):
        for x, y in self.storage.items():
            if (y.id == ident):
                self.storage[x].id = note.id
                self.storage[x].date = note.date
                self.storage[x].title = note.title
                self.storage[x].text = note.text
                print("200")
        print("NotFound")

def dec(text: str) -> Note:
    temp = text.split('|')
    if (len(temp) == 4):
        done = Note()
        done.id = temp[0]
        done.date = temp[1]
        done.title = temp[2]
        done.text = temp[3]
        return (done)
    if (len(temp) == 2):
        done = Note()
        done.id = temp[0]
        done.date = temp[1]
        return (done)


def code(note: Note) -> str:
    try:
        done = note.id + "|" + note.date + "|" + note.title + "|" + note.text
        return (done)
    except AttributeError:
        return("NotFound")


st = db()
aboba = "12|negr|ad|asd"
st.Create(dec(aboba))
st.Update("12",dec("12|asd|asd|asd"))
print(code(st.Read("11")))


