from dataclasses import dataclass, field
import uuid

@dataclass
class Question:
    id: str = field(init=False)
    text: str
    options: list[str]
    answer: str

    def __post_init__(self):
        self.id = str(uuid.uuid4())

QUIZ_QUESTIONS = [
    Question(
        text="What is Natural Language Processing (NLP)?",
        options=["A way for computers to speak like humans", 
                 "A method to help computers understand and work with human language", 
                 "A way for humans to process natural food", 
                 "A machine that can play chess"],
        answer="A method to help computers understand and work with human language"
    ),
    Question(
        text="Which of these is an example of Natural Language Processing?",
        options=["A robot cleaning the house", 
                 "A computer translating a sentence from English to Spanish", 
                 "A vacuum cleaner", 
                 "A video game"],
        answer="A computer translating a sentence from English to Spanish"
    ),
    Question(
        text="Which of the following can a computer do using NLP?",
        options=["Play soccer", 
                 "Recognize voices and answer questions", 
                 "Draw pictures", 
                 "Build a house"],
        answer="Recognize voices and answer questions"
    ),
    Question(
        text="What is 'speech recognition' in NLP?",
        options=["A computer recognizing colors", 
                 "A computer understanding and converting spoken words into text", 
                 "A computer drawing pictures of faces", 
                 "A computer singing songs"],
        answer="A computer understanding and converting spoken words into text"
    ),
    Question(
        text="Which of these is an example of 'text classification'?",
        options=["A robot reading a story aloud", 
                 "A computer sorting emails into 'spam' or 'not spam'", 
                 "A computer drawing pictures of animals", 
                 "A robot playing music"],
        answer="A computer sorting emails into 'spam' or 'not spam'"
    ),
    Question(
        text="Which of these is a task that NLP can help with?",
        options=["Organizing a birthday party", 
                 "Translating a book into different languages", 
                 "Cooking dinner", 
                 "Creating a new video game"],
        answer="Translating a book into different languages"
    ),
    Question(
        text="What is 'sentiment analysis' in NLP?",
        options=["A way to find out if a text is happy, sad, or angry", 
                 "A way to recognize faces in pictures", 
                 "A way to sort items in a store", 
                 "A way to build robots"],
        answer="A way to find out if a text is happy, sad, or angry"
    ),
    Question(
        text="What is a chatbot?",
        options=["A robot that can make sandwiches", 
                 "A computer program that can talk to people and answer questions", 
                 "A video game character", 
                 "A type of computer hardware"],
        answer="A computer program that can talk to people and answer questions"
    ),
    Question(
        text="What does NLP help computers understand?",
        options=["How to play music", 
                 "How to understand human language and words", 
                 "How to play soccer", 
                 "How to cook food"],
        answer="How to understand human language and words"
    ),
    Question(
        text="Which of these can be done using NLP?",
        options=["Make the computer sing a song", 
                 "Translate a sentence from one language to another", 
                 "Make the computer play chess", 
                 "Make the computer play a game of tag"],
        answer="Translate a sentence from one language to another"
    )
]