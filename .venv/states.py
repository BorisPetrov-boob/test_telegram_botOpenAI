from aiogram.fsm.state import State, StatesGroup


class Person(StatesGroup):
    name = State()
    age = State()
    city = State()


class GPTDialog(StatesGroup):
    message = State()

class Talk(StatesGroup):
    persona = State()


class MessageTalks(StatesGroup):
    message = State()

class QuizStates(StatesGroup):
    choosing_topic = State()
    waiting_answer = State()
    
    
class TranslationStates(StatesGroup):
    waiting_for_language = State()
    waiting_for_text = State()
                
