import datetime

class Journal:
    def __init__(self, filename='journal.txt'):
        self.filename = filename

    def add_entry(self, text):
        with open(self.filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}:\n{text}\n\n")

    def list_entries(self):
        try:
            with open(self.filename, 'r') as file:
                entries = file.read()
                return entries
        except FileNotFoundError:
            return "No journal entries found."
