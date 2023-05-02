from problog.extern import problog_export
times = []

@problog_export('+list','-int')
def collect_all(a):
    times.append(a)
    return 1

@problog_export('-list')
def sort():
    return [Tuple((Number(i), val)) for i, val in enumerate(sorted(times))]
