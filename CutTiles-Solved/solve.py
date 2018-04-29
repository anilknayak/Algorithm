class Solve:
    def __init__(self, f_i, f_o):
        self.file_name_out = f_o
        self.file_name = f_i
        self.debug = False

    def load(self):
        with open(self.file_name_out, 'w') as file_out:
            with open(self.file_name, 'r') as file:
                self.test_cases = int(file.readline())

                for test_case_no in range(self.test_cases):
                    test_case = file.readline().rstrip("\n\r").split(" ")
                    N = test_case[0]
                    M = test_case[1]
                    S = [int(i) for i in test_case[2:]]

                    n = self.solve(int(N), int(M), S)
                    print("Case #%d: %d" % (test_case_no + 1, n))
                    file_out.write("Case #%d: %d \n" % (test_case_no + 1, n))

    def solve(self, N, M, S):
        tiles = [[M, M]]
        required = 1
        s_S = sorted(S, reverse=True)

        for s in s_S:
            size = pow(2, s)
            flag = True
            while flag:
                for tile in tiles:
                    w = tile[0]
                    h = tile[1]

                    if w >= size and h >= size:
                        flag = False
                        nw = w - size
                        nh = h - size
                        tiles.remove(tile)

                        if nw == 0 and nh == 0:
                            # print("0=0")
                            break
                        elif not nw == 0 and not nh == 0:
                            tiles.append([nw, size])
                            tiles.append([w, nh])
                        elif nw == 0 and not nh == 0:
                            tiles.append([w, nh])
                        elif nh == 0 and not nw == 0:
                            tiles.append([nw, h])

                        break

                if flag:
                    tiles.append([M, M])
                    required += 1

        return required


# s = Solve('test.in','test.out')
# s = Solve('D-small-practice.in', 'D-small-practice.out')
s = Solve('D-large-practice.in', 'D-large-practice.out')
s.load()
