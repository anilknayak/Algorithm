import re

class StringDecompose:
    def __init__(self, input='3[2[a]2[b]]', method='rex'):
        if method == 'recursion':
            print('Solving using Recursion')
            self.recursion_method(input)
        elif method == 'rex':
            print('Solving using Regular Expression')
            self.regular_expression_method(input)

    def regular_expression_method(self, input):
        while '[' in input:
            pos = [(m.start(0), m.end(0)) for m in re.finditer(r"\[([A-Za-z0-9]+)\]", input)]
            start = pos[0][0]
            end = pos[0][1]
            digit = input[start - 1]
            string = input[start + 1:end - 1]
            old = input[start - 1: end]
            new = str(string) * int(digit)
            input = input.replace(str(old), str(new))
        print("Solution : ", input)

    def recursion_method(self, input):
        sub_problem_counter = 0
        start = None
        end = None
        digit = None

        if '[' not in input:
            print(input)
            return input

        for i in range(0, len(input)):
            pos_c = input[i]
            if pos_c == "[":
                sub_problem_counter += 1
                digit = input[i - 1]
                print(digit)
                digit = None
                end_pos = i
                j = 1
                flag = True
                while flag:
                    if input[end_pos-j:end_pos].isdigit():
                        j+=1
                        continue
                    else:
                        if end_pos-j < 0:
                            digit = input[0: end_pos]
                        else:
                            digit = input[end_pos - j: end_pos]
                        flag = False
                start = i+1
            elif pos_c == "]":
                end = i
                break

        old = input[int(start): int(end)]
        new = str(old) * int(digit)
        input = input.replace(str(digit+"["+old+"]"), str(new))

        self.recursion_method(input)


decompose = StringDecompose(method='recursion', input="3[2[a]2[b]]")
