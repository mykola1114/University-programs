import pandas as pd

class Notation:
    def __init__(self):
        self.top = -1
        # Ініціалізуємо стек
        self.stack = []
        # Ініціалізуємо вихідний рядок
        self.output = []
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.stack.append(op)

    def isOperand(self, ch):
        return ch.isdigit()

    def notGreater(self, i):
        try:
            a = self.operators[i]
            b = self.operators[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # Основна функція
    def infixToPostfix(self, exp):
        df = pd.DataFrame(columns=['Що читаємо','Вихідний рядок','Стек'])

        for i in exp:

            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while ((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

            df.loc[len(df.index)] = [i, ",".join(self.output), ",".join(self.stack)]


        while not self.isEmpty():
            self.output.append(self.pop())

        df.loc[len(df.index)] = ['', ",".join(self.output), '']

        return ",".join(self.output), df


if __name__ == "__main__":
    exp = "2+4*(5-3)+(3^(2-1))/3"
    obj = Notation()
    result, dataFrame = obj.infixToPostfix(exp)
    print('Зворотний польський запис:', result)
    print(dataFrame)
