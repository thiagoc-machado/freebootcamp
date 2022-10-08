import operator
from typing import Sequence, NamedTuple, Literal

ops = {"+": operator.add, "-": operator.sub}


class Problem(NamedTuple):
    x: int
    y: int
    op: Literal['+', '-']

    @classmethod
    def parse(cls, s: str) -> 'Problem':
        x, op, y = s.split()

        # tests errors
        for n in (x, y):
            if not n.isdigit():
                raise ValueError('Error: Numbers must only contain digits.')

        return cls(x=int(x), y=int(y), op=op)

    def validate(self) -> None:
        for n in (self.x, self.y):
            if abs(n) >= 1e4:
                raise ValueError('Error: Number cannot be more than four digits.')

        if self.op not in ops:
            raise ValueError(
                'Error: Operator must be '
                + ' or '.join(f"'{o}'" for o in ops.keys())
            )

    # draw operations
    def format_lines(self, solve: bool = False) -> tuple[str, ...]:
        longest = max(self.x, self.y)
        width = len(str(longest))
        lines = (
            f'{self.x:>{width + 2}}',
            f'{self.op} {self.y:>{width}}',
            f'{"":->{width + 2}}',
        )
        if solve:
            lines += (f'{self.answer:>{width + 2}}',)
        return lines

    @property
    def answer(self) -> int:
        return ops[self.op](self.x, self.y)

# validating
def arithmetic_arranger(problem_strings: Sequence[str], solve: bool = False) -> None:
    if len(problem_strings) > 5:
        print('Error: Too many problems.')
        return

    try:
        problems = [Problem.parse(s) for s in problem_strings]
        for problem in problems:
            problem.validate()
    except ValueError as e:
        print(e)
        return
    # print oprations
    lines = zip(*(p.format_lines(solve) for p in problems))
    print('\n'.join('    '.join(groups) for groups in lines))

if __name__ == "__main__":
    arithmetic_arranger(("32 + 698", "3801 - 2", "45 + 43", "123 + 49"), solve=True)
