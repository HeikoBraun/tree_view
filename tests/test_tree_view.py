"""tests for tree_view"""
from tree_view.tree_view import tree


def test_1():
    """1. test"""
    res = tree(
        {
            "top": {
                "sub1": {"subsub1": {}, "subsub2": {}},
                "sub2": {},
                "sub3": {"subsub3": {"subsubsub3": {}}},
            }
        }
    )
    exp = """top
├─ sub1
│  ├─ subsub1
│  └─ subsub2
├─ sub2
└─ sub3
   └─ subsub3
      └─ subsubsub3"""
    assert res == exp
