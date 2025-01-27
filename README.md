# TabID Experiments

Software, models and instances for the journal version of TabID.

Includes a special release of Savile Row based on 1.10.0 with additional flags
`-tabulate2` and `-tabulate-diagnostics`, where `-tabulate2` is the version of
tabulation corresponding to the paper.

The other files are organised as follows:

- `main-experiment/` relates to the main *TabID* vs *no tabulation* experiments.
  - `featured-problems/` - the models and instances for the baseline problems
    and new case studies
  - `sr-2017-problems/` - models and instances for section 7 titled
    "Experimental Evaluation of TabID on Other Problem Classes"
  - `experiment-config.json` - a configuration file showing various settings
    including the command-line options for the solvers
  - `infos-raw.csv.gz` - the raw information from Savile Row `.info` files
    resulting from each individual run
  - `timings-clean.csv.gz` - the collated timings per instance/solver/setting
- `scaling-experiment/` relates to section 8 titled "Scalability of TabID"
  - `problems/` - the custom models and instances used to investigate
    scalability
  - `experiment-config.json` - command-line settings
  - `infos-raw.csv` - the contents of the Savile Row `.info` files

