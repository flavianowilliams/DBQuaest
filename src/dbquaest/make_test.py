from dbquaest.mechanics import work_and_energy as mwe

class Test(mwe.Quest):

    def __init__(self, nquestion, ntest, qcode):
        self.nquestion = nquestion
        self.ntest = ntest
        self.qcode = qcode
        self.question_list = list()

    def setQuestion(self):

        for question in range(self.ntest):
            self.question_list.append(mwe.question(self.qcode))