P = 0.96# 晴天的概率
INF = 1e5
m_use_e_2 = [[0.0]*180 for i in range(180)]
m_use_e_1 = [[0.0]*180 for i in range(180)]
m_use_e_0 = [[0.0]*180 for i in range(180)]


def initialize():
    for w in range(180):
        for f in range(180):
            if w < 18 or f < 18:
                m_use_e_2[w][f] = INF
            if w < 36 or f < 36:
                m_use_e_1[w][f] = INF
            if w < 54 or f < 54:
                m_use_e_0[w][f] = INF


def fill():
    for w in range(18, 180):
        for f in range(18, 180):
            m_use_e_2[w][f] = 110 * P + (1-P) * min(270, 135 + m_use_e_2[w-9][f-9])  # fill 2
    for w in range(36, 180):
        for f in range(36, 180):
            m_use_e_1[w][f] = P * (110 + m_use_e_2[w-6][f-8]) + (1-P) * min(270+m_use_e_2[w-9][f-9], 135 + m_use_e_1[w-9][f-9])  # fill 1
    for w in range(54, 180):
        for f in range(54, 180):
            m_use_e_0[w][f] = P * (110 + m_use_e_1[w-6][f-8]) + (1-P) * min(270 + m_use_e_1[w-9][f-9], 135 + m_use_e_0[w-9][f-9])



def main():
    initialize()
    fill()
    for i in m_use_e_2:
        for j in i:
            print(f'{j:.3f}',end=', ')
        print()
   # print(m_use_e_2[18][18], m_use_e_1[36][36], m_use_e_0[54][54], sep='\n')

if __name__ == '__main__':
    main()
