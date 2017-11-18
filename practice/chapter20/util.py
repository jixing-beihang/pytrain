def lines(file):
    f = open(file,'r',1)
    for line in f.readlines():
        yield line  # generator 生成器
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
