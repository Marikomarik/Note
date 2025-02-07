class Note:
    id: str
    date: str
    title: str
    text: str


class db:
    id_ = 0
    storage = {}

    def create(self, note: Note):
        self.id_ += 1
        self.storage[self.id_] = note

    def List(self):
        for x, y in self.storage.items():
            print(x, y.id, y.date, y.title, y.text)

    def Read(self, ident: str) -> Note:
        for x, y in self.storage.items():
            if (y.id == ident):
                return (y)


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
    done = note.id + "|" + note.date + "|" + note.title + "|" + note.text
    return (done)


st = db()
aboba = "12|negr|ad|asd"
st.create(dec(aboba))

st.List()


