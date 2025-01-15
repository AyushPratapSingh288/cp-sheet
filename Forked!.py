def main():
    a, b = map(int, (input().split()))
    xk, yk = map(int, (input().split()))
    xq, yq = map(int, (input().split()))
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    st1 = set()
    st2 = set()   
    for j in range(4):
        st1.add((xk + dx[j] * a, yk + dy[j] * b))
        st2.add((xq + dx[j] * a, yq + dy[j] * b))
        st1.add((xk + dx[j] * b, yk + dy[j] * a))
        st2.add((xq + dx[j] * b, yq + dy[j] * a))
         
    ans = len(st1.intersection(st2))   
    print(ans)


if __name__ == "__main__":
    t = int(input())
    while t>0:
        main()
        t-=1

