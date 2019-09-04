def main():
    f = open(0)
    print(f)
    f.readline()
    print(f)
    m = 1
    o = ""
    s = []
    for l in f:
        v = int(l)
        while v >= m:
            s.append(m)
            m += 1
            o += "+\n"
        if s.pop() != v:
            print("NO")
            return
        o += "-\n"
    print(o)
main()