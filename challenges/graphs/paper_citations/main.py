def paper_paths(papers, a, b, path=[]):
    if a == b:
        yield path
    else:
        _, citations = papers[a]
        for a in citations:
            for p in paper_paths(papers, a, b, path + [a]):
                yield p


def author_paths(papers, a1, a2):
    p1, p2 = [], []
    for title, content in papers.items():
        authors, citations = content
        if a1 in authors:
            p1.append(title)
        if a2 in authors:
            p2.append(title)
    for a in p1:
        for b in p2:
            for path in paper_paths(papers, a, b, [a]):
                yield path


def paths(papers, a, b):
    return [path for path in author_paths(papers, a, b)]


papers = {
    '1': (
        set(['a', 'b']),
        set()
    ),
    '2': (
        set(['c']),
        set(['1'])
    ),
    '3': (
        set(['b', 'c']),
        set(['1', '2'])
    ),
    '4': (
        set(['a', 'd', 'e']),
        set(['2', '3'])
    ),
    '5': (
        set(['b', 'd']),
        set(['1', '4'])
    )
}

print paths(papers, 'b', 'a')
