import pathlib
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"


class MainApp:
    __toplevel = None
    __start_date_entry = None
    __end_date_entry = None
    __date_range_text = ""
    __search_button = None
    __date_range_variable = None

    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__toplevel = builder.get_object('toplevel', master)
        self.__start_date_entry = builder.get_object('start_date_entry', master)
        self.__end_date_entry = builder.get_object('end_date_entry', master)
        self.__date_range_text = builder.get_object('date_range_text', master)
        self.__search_button = builder.get_object('search_button', master)
        self.__date_range_variable = builder.get_variable('date_range_variable')
        builder.connect_callbacks(self)
        self.__start_date_entry.set_date('10/01/2022')  # A date before any message log entries
        self.do_search()  # default values

    def do_search(self):
        self.__date_range_variable.set(self.__start_date_entry.get() + ' - ' + self.__end_date_entry.get())
        print(self.__start_date_entry.get())

    def run(self):
        self.__toplevel.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.run()
