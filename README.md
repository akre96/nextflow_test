# Example NextFlow Workflow to Read Database
This is intended as an example script for how to use nextflow to run analyses using the HPC

## Steps
1. Log in to the HPC environment
2. Start a tmux session
    - `tmux new -s nextflow_test`
3. Enter an interactive node
    - `srun --exclusive --partition F2 --pty bash`
4. Download nextflow if not already installed
    - `curl -s https://get.nextflow.io | bash`
    - creates `nextflow` in home directory, may need to chmod to allow execution
5. Clone this repository
    - `git clone https://github.com/akre96/nextflow_test.git`
6. Enter the repository: `cd nextflow_test`
7. Run the nextflow query
    - `../nextflow run query_db.nf --study [study_name]`
    - Example: `../nextflow run query_db.nf --study pilot`