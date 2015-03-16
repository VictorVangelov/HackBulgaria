from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from random import randint
from datetime import datetime
from sqlalchemy import func
import os

Base = declarative_base()




def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])


class HighScore(Base):
    __tablename__ = "highscore"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return "{} - {}".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()





class DoMath():
    MAX_OPERAND_VAUE = 20
    MAX_RAISED_GRADE = 5
    MUL = 0
    DIV = 1
    SUM = 2
    SUB = 3
    RISING = 4
    operands = ["*", "/", "+", "-", "^"]
    functions = {0: lambda z, y: z * y,
                 1: lambda z, y: z / y,
                 2: lambda z, y: z + y,
                 3: lambda z, y: z - y,
                 4: lambda z, y: z ** y}
    score = 0
    playing = True
    menu = '''start\nhighscore\nquit\n'''
    greatings = '''Hallo , now we will check, how good are u in math.   '''

    def generate_operator_and_operands():
        operand1 = randint(1, DoMath.MAX_OPERAND_VAUE)
        rand_operator = randint(0, len(DoMath.functions) - 1)
        if rand_operator == DoMath.RISING:
            operand2 = randint(1, DoMath.MAX_RAISED_GRADE)
            operand1 = operand1 // 2
        else:
            operand2 = randint(1, DoMath.MAX_OPERAND_VAUE)
        return (operand1, rand_operator, operand2)

    def prevent_imposible_dividing(operand1, operand2):
        result = operand1 / operand2
        while len(str(result)) > 6:
            operand2 -= 1
            result = operand1 / operand2
        return (operand1, operand2)

    def game(session):
        user = input("Enter your name >>> ")
        question = "Question #{}:\nWhat is the answer to {} {} {}?"
        while DoMath.playing:
            op1, operator, op2 = DoMath.generate_operator_and_operands()
            operand1, operand2 = DoMath.prevent_imposible_dividing(op1, op2)
            print (question.format(DoMath.score + 1, operand1, DoMath.operands[operator], operand2))
            answer = DoMath.functions[operator](operand1, operand2)
            UI = input("?> ")
            try:
                if float(UI) == answer:
                    print("Correct!")
                    DoMath.score += 1
                else:
                    DoMath.game_over(user, session)
            except ValueError:
                print("Type only numbers!!!")

    def is_correct_answer():
        pass

    def game_over(user, session):
        print(
            "Incorrect! Ending game. You score is:{}".format(DoMath.score ** 2))
        DoMath.save_score(session, user, DoMath.score ** 2)
        DoMath.score = 0
        DoMath.playing = False
        cls()
        DoMath.main_menu(session)

    def save_score(session, username, score):
        session.add(HighScore(name=username, score=score))
        session.commit()

    def print_highscore(session):
        top_10 = session.query(HighScore).filter(
            HighScore.score)
        for score in top_10:
            print(score)

    def main_menu(session):
        commands = {"start": DoMath.game,
            "highscore": DoMath.print_highscore, "quit": DoMath.quit}
        print(DoMath.menu)
        ui = input(">>>")
        try:
            commands[ui](session)
        except KeyError:
            print("Incorrect command")
            DoMath.main_menu(session)

    def quit(session):
        print("Bye Bye")

if __name__ == '__main__':
    engine = create_engine("sqlite:///DoMathHighScore.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    print(DoMath.greatings)
    DoMath.main_menu(session)
