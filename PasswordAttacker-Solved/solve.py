class Solve:
    def __init__(self, f_i, f_o):
        self.file_name_out = f_o
        self.file_name = f_i
        self.debug = False
        self.mat = None

    def load(self):
        with open(self.file_name_out, 'w') as file_out:
            with open(self.file_name, 'r') as file:
                self.test_cases = int(file.readline())

                for test_case_no in range(self.test_cases):
                    self.mat = None
                    print("Test",test_case_no+1)
                    M, N = file.readline().rstrip("\n\r").split(" ")
                    self.mat = [[-1 for i in range(int(N)+1)] for j in range(int(M)+1)]
                    result = (self.nb(int(N), int(M)) % (1000000007))
                    print("Case #%d: %d" % (test_case_no + 1, result))
                    file_out.write("Case #%d: %d \n" % (test_case_no + 1, result))

    def nb(self, n, m):
        if not self.mat[m][n] == -1:
            return self.mat[m][n]

        if m == 1:
            res = 1
        elif n == 1:
            res = 0
        else:
            res = m * (self.nb(n - 1, m - 1) + self.nb(n - 1, m))
            self.mat[m][n] = res
        return res % 1000000007

# s = Solve('A-small-practice.in', 'A-small-practice.out')
# s.load()
s = Solve('A-large-practice.in', 'A-large-practice.out')
s.load()

