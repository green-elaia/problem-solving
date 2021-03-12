def solution(skill, skill_trees):
    import re

    answer = 0
    for skill_tree in skill_trees:
        sk_tree_str = ""
        for c in skill_tree:
            if c in skill:
                sk_tree_str += c
        if not sk_tree_str:
            answer += 1
            continue
        elif sk_tree_str[0] != skill[0]:
            continue

        pattern = re.compile(sk_tree_str)
        matched = pattern.search(skill)
        if matched:
            answer += 1

    return answer
