# import State 
from aiogram.dispatcher.filters.state import State, StatesGroup

class SearchState(StatesGroup):
    search = State()

class CourseState(StatesGroup):
    course = State()
    lesson = State()