import os
import pandas as pd

filepaths = [os.path.join(d,f)
             for (d, dirs, files) in os.walk('problems')
             for f in (dirs + files) if f.endswith(".info")]
miniframes = []
for path in filepaths:
    with open(path, 'rt') as infofile:
        g = path.split(".")
        entry = {
            'SeqVars' : int(g[0][-1:]),
            'N'       : g[3],
            'Run'     : g[5],
            'Solver'  : g[6],
            'Policy'  : g[7]
            }
        for line in infofile.readlines():
            k,v = tuple(line.split(':')[:2])
            entry[k.strip()] = float(v.strip())
        rowframe = pd.DataFrame({k:[v] for k,v in entry.items()})
        miniframes.append(rowframe)

bigframe = pd.concat(miniframes)
bigframe.to_csv("results.csv", index=False)

summary = bigframe.groupby(['Policy', 'Solver','N','SeqVars'])\
          ['TabulationTime', 'SavileRowTotalTime', 'SolverTotalTime', 'SolverNodes']\
          .median().reset_index()
summary['Arity'] = summary.SeqVars + 1
summary.to_csv("summary.csv", index=False)
print(summary.query("Policy=='tab' and Solver == 'minion'"))
