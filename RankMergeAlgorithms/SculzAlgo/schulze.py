from py3votecore.schulze_pr import SchulzePR

input = [
            {"count": 6, "ballot": [["a"], ["d"], ["b"], ["c"], ["e"]]},
            {"count": 12, "ballot": [["a"], ["d"], ["e"], ["c"], ["b"]]},
            {"count": 72, "ballot": [["a"], ["d"], ["e"], ["b"], ["c"]]},
            {"count": 6, "ballot": [["a"], ["e"], ["b"], ["d"], ["c"]]},
            {"count": 30, "ballot": [["b"], ["d"], ["c"], ["e"], ["a"]]},
            {"count": 48, "ballot": [["b"], ["e"], ["a"], ["d"], ["c"]]},
            {"count": 24, "ballot": [["b"], ["e"], ["d"], ["c"], ["a"]]},
            {"count": 168, "ballot": [["c"], ["a"], ["e"], ["b"], ["d"]]},
            {"count": 108, "ballot": [["d"], ["b"], ["e"], ["c"], ["a"]]},
            {"count": 30, "ballot": [["e"], ["a"], ["b"], ["d"], ["c"]]}
        ]
output = SchulzePR(input, ballot_notation=SchulzePR.BALLOT_NOTATION_GROUPING).as_dict()

print(output["order"])