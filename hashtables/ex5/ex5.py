def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    files_dict = {}
    queries_dict = {}

    for f in files:
        split = f.split('/')
        file_name = split[-1]

        if file_name not in files_dict:
            files_dict[file_name] = []

        files_dict[file_name].append(f)

    for q in queries:
        if q not in queries_dict:
            queries_dict[q] = q

    for q in queries_dict:
        if q in files_dict:
            result.extend(files_dict[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
