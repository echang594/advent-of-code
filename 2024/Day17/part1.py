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
    global a
    a = a // 2**x


def bxl(x):
    global b
    b = b ^ x


@combo
def bst(x):
    global b
    b = x % 8


def jnz(x):
    global i
    if a:
        i = x
        return True


def bxc(x):
    global b
    b = b ^ c


@combo
def out(x):
    output.append(x % 8)


@combo
def bdv(x):
    global b
    b = a // 2**x


@combo
def cdv(x):
    global c
    c = a // 2**x


inst = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

with open("2024/Day17/input.txt", "r") as f:
    a, b, c, _, prog = f.read().splitlines()

a, b, c = (int(r.split()[-1]) for r in (a, b, c))
prog = [int(x) for x in prog.split()[-1].split(",")]
output = []

i = 0
while i < len(prog):
    opc, opr = prog[i], prog[i + 1]
    jmp = inst[opc](opr)
    if not jmp:
        i += 2

ans = ",".join(str(x) for x in output)
print(ans)
