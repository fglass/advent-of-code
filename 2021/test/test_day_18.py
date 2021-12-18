from solution.day_18 import part1, part2, INPUT, _flatten, _explode, _reduce

EXPLODE_EXAMPLES = {
    "[[[[[9,8],1],2],3],4]": "[[[[0,9],2],3],4]",
    "[7,[6,[5,[4,[3,2]]]]]": "[7,[6,[5,[7,0]]]]",
    "[[6,[5,[4,[3,2]]]],1]": "[[6,[5,[7,0]]],3]",
    "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]": "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
    "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]": "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
}

EXAMPLE_INPUT = [
    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
    "[[[5,[2,8]],4],[5,[[9,9],0]]]",
    "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
    "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
    "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
    "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
    "[[[[5,4],[7,7]],8],[[8,3],8]]",
    "[[9,3],[[9,9],[6,[4,9]]]]",
    "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
    "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
]


def test_explode():
    for i, o in EXPLODE_EXAMPLES.items():
        assert _explode(_flatten(i))[0] == _flatten(o)


def test_reduce():
    i = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    o = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    assert _reduce(_flatten(i)) == _flatten(o)


def test_part_1():
    assert part1(EXAMPLE_INPUT) == 4140
    assert part1(INPUT) == 3793


def test_part_2():
    assert part2(EXAMPLE_INPUT) == 3993
    assert part2(INPUT) == 4695
