def solution(key, lock):
    m = len(key)
    n = len(lock)
    k1 = key
    k2 = []  # clockwise 90
    for j in range(m):
        tmp = []
        for i in range(m):
            tmp.append(key[m-i-1][j])
        k2.append(tmp)
    k3 = []   # counter clockwise 90
    for j in range(m):
        tmp = []
        for i in range(m):
            tmp.append(key[i][m-j-1])
        k3.append(tmp)
    k4 = []   # clockwise 180
    for i in range(m):
        k4.append(key[m-i-1].reverse())

    # lock zero padding
    tmp = [0] * (m-1)
    for i in range(n):
        lock[i] = tmp + lock[i] + tmp
    tmp = [0] * (2*m - 2 + n)
    tmp2 = []
    for _ in range(m-1):
        tmp2.append(tmp)
    lock = tmp2 + lock + tmp2

    keys = [k1, k2, k3, k4]
    for key in keys:
        for i in range(n + m -1):
            for j in range(n + m -1):
                lock_tmp = lock
                for m_i in range(m):
                    for m_j in range(m):
                       lock_tmp[i+m_i][j+m_j] += key[m_i][m_j]
                if check(lock_tmp, n, m):
                    return True
    else:
        return False

def check(lock_tmp, n, m):
    for i in range(n):
        for j in range(n):
            if lock_tmp[m+i][m+j] == 0:
                return False
    else:
        return True
