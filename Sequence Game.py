def solve(n,a):
    result = []
    for i in range(n):
        x = a[i]
        if i and result[-1] > x:
            result.append(1)
        result.append(x)
    return result

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())  
        a = list(map(int, input().split()))  
        ans = solve(n,a)
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()
