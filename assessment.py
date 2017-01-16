"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   abstraction: it hides the details we dont need, using something that works
   in expected and consistent ways is more important than knowing how it 
   does it
   polymorphism: interchangability of concepts, classes that share some but not 
   all of their characteristics can inherit from a common anscestor, but have their
   own attributes as well, this can make defining objects both easier and DRYer
   encaptualization: wrapping together data and behavior, this can be very useful
   because not only does the object Lucy know her name etc, but knows that she can 
   jump, sit, or any other things that object should be able to do


2. What is a class?

    a class the definition of an object, so Dog, would be the class of Lucy
    who would be an instance of that class

3. What is an instance attribute?

    an instance attribute is a piece of information that some instance
    of your class, so some object, knows about itself
    for example a dog, say Lucy, could be an example of a class of Dog
    she would know her name lucy.name = lucy, her age lucy.age = 6, etc
    
4. What is a method?
    
    a method is a function on a class or an object (class method or instance method)

5. What is an instance in object orientation?

    an 'instance' of a class, ie an object
    for example Dog could be a class, but my dog Lucy is one instance of
    this class Dog

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    A class attribute is something all objects of that class share, eg a dog has a tail
    (tail = True)
    an instance attribute is something each object of that type has independetly,
    eg this dog's name is Lucy (lucy.name = 'Lucy')

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object): 
    '''A student (who will take the exam(s)'''

    def __init__(self, first_name, last_name, address):
        '''sets up the initizalization of a student'''

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.address = address


class Question(object):
    '''This defines a question and is able to check is correctness'''

    def __init__(self, question, answer):
        '''sets up the initalization of a question'''

        self.question = question
        self.answer = answer.lower()

    def ask_and_evaluate(self):
        '''Returns true if a question is answered correctly'''

        user_answer = raw_input(self.question + "> ").lower()
        if user_answer == self.answer:
            return True
        return False 


class Exam(object):
    '''An object that represents an exam with questions and answers''' 

    def __init__(self, name):
        '''set up the initialization of an exam'''

        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        '''Adds a question to an instance of an exam'''

        question = Question(question, answer)
        self.questions.append(question)

    def administer(self):
        '''Scores a quiz

        A quiz is like an exam, but instead of a percentage, you pass if you
        get 50% or more right and otherwise fail'''

        score = 0.0
        self.wrong_answers = []

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
            else:
                self.wrong_answers.append(question)

        return score/len(self.questions)


class Quiz(Exam):
    '''This sets up an exam'''

    def administer(self):
        student_score = super(Quiz, self).administer()

        if student_score >= .5:
            return True

        return False


def take_test(student, exam):
    '''This runs all the code to set up, have the student take the tests, and score them

    Any questions that a student got wrong are printed at the end with their correct
    answers
    '''

    test_type = type(exam)
    print "Hello, {} {}, you are about to take a {}".format(student.first_name, student.last_name, test_type.__name__)
    student.score = exam.administer()

    if test_type == Exam:
        print "{}: Your score is {:.0f}%".format(student.first_name, student.score * 100)

    elif test_type == Quiz:
        passed = 'did not pass'

        if student.score == True:
            passed = 'passed'
        print '{}: You {} the quiz'.format(student.first_name, passed)

    if len(exam.wrong_answers) > 0:
        print
        print "Here are the answers you got wrong:"
        for wrong_answer in exam.wrong_answers:
            print "The answer to {} Should have been {}".format(wrong_answer.question, wrong_answer.answer)



def example_exam():
    '''This is an example exam'''

    exam = Exam('example exam')

    exam.add_question('What color is the sky?', 'blue')
    exam.add_question('What\'s 2+2?', '4')
    exam.add_question('What do you generally swim in?', 'water')

    student = Student('kelly', 'ann', '123 Road St')

    take_test(student, exam)

def example_quiz():
    '''This is an example quiz'''

    quiz = Quiz('example quiz')

    quiz.add_question('What is the answer to life, the universe, and everything?', '42')
    quiz.add_question('Are you my mother?', 'No')
    quiz.add_question('Why does Snoop Dogg carry an umbrella', 'Fo\'Drizzle')
    quiz.add_question('What\'s red and bad for your teeth?', 'a brick')


    student = Student('Angela', 'Merkle', 'Germany')

    take_test(student, quiz)




if __name__ == "__main__":
    '''The examples only run if you run your program from the command line'''
    example_exam()
    print
    example_quiz()







