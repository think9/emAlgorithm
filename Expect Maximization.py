class EM_Algorithm:
    tA, tB = 0, 0
    H_list = []
    T_list = []
    eA, eB = 0, 0
    A_dist, B_dist = 0, 0
    coinA_H = []
    coinA_T = []
    coinB_H = []
    coinB_T = []

    #초기값 설정
    def __init__(self, thetaA, thetaB):
        self.tA = thetaA
        self.tB = thetaB
        print("Set the Parameter")
        return

    #E-step
    def Estep(self, H, T):
        self.H_list.append(H)
        self.T_list.append(T)
        self.eA = self.tA**H * (1-self.tA)**T
        self.eB = self.tB**T * (1-self.tB)**H
        self.A_dist = self.eA/(self.eA+self.eB)
        self.B_dist = self.eB/(self.eA+self.eB)
        print("E-step")
        print("A_distibution : {}, B_distribution : {}".format(self.A_dist, self.B_dist))
        A_H = self.A_dist * H
        A_T = self.A_dist * T
        B_H = self.B_dist * H
        B_T = self.B_dist * T
        self.coinA_H.append(A_H)
        self.coinA_T.append(A_T)
        self.coinB_H.append(B_H)
        self.coinB_T.append(B_T)
        print("coinA_H : {}, coinA_T : {}".format(A_H, A_T))
        print("coinB_H : {}, coinB_T : {}".format(B_H, B_T))
        return

    #초기값 업데이트
    def Mstep(self):
        sumA_H = sum(self.coinA_H)
        sumA_T = sum(self.coinA_T)
        sumB_H = sum(self.coinB_H)
        sumB_T = sum(self.coinB_T)
        self.tA = sumA_H / (sumA_H+sumA_T)
        self.tB = sumB_H / (sumB_H+sumB_T)
        self.coinA_H = []
        self.coinA_T = []
        self.coinB_H = []
        self.coinB_T = []
        print("")
        print("Result")
        print("tA : {}, tB : {}".format(self.tA, self.tB))
        print("")
        return

    #위의 과정들을 n회만큼 반복하여 수행
    def loop(self, n):
        num = len(self.H_list)
        for i in range(n):
            for j in range(num):
                self.Estep(self.H_list[j], self.T_list[j])
            self.Mstep()
