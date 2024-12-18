def get_first_output(a, b, c, prog):
    def combo(f):
        def wrapper(x):
            match x:
                case 4:
                    x = a
                case 5:
                    x = b
                case 6:
                    x = c
            return f(x)

        return wrapper

    @combo
    def adv(x):
        nonlocal a
        a = a // 2**x

    def bxl(x):
        nonlocal b
        b = b ^ x

    @combo
    def bst(x):
        nonlocal b
        b = x % 8

    def jnz(x):
        nonlocal i
        if a:
            i = x
            return True

    def bxc(x):
        nonlocal b
        b = b ^ c

    @combo
    def out(x):
        nonlocal output
        output = x % 8

    @combo
    def bdv(x):
        nonlocal b
        b = a // 2**x

    @combo
    def cdv(x):
        nonlocal c
        c = a // 2**x

    inst = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

    i = 0
    output = None
    while i < len(prog):
        opc, opr = prog[i], prog[i + 1]
        jmp = inst[opc](opr)
        if output is not None:
            break
        if not jmp:
            i += 2

    return output


with open("2024/Day17/input.txt", "r") as f:
    prog = [int(x) for x in f.read().split()[-1].split(",")]

ADV_CONSTANT = 8
ans = 0


def test(a, i):
    global ans
    if i == -1:
        ans = a
        return
    for pa in range(a * ADV_CONSTANT, (a + 1) * ADV_CONSTANT):
        if get_first_output(pa, 0, 0, prog) == prog[i]:
            test(pa, i - 1)
        if ans:
            return


test(0, len(prog) - 1)

print(ans)
