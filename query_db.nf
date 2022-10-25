#!/usr/bin/env nextflow
 params.study = 'pilot'

 // Environment file has database credentials
 params.env_file= projectDir + '/.env'

 // Path to folder with script being run
 params.script_dir = projectDir + '/scripts'
 
// Reads first line of demographics table from a study
process query_db_line{
    input:
        val study
        path env_file
        path script_dir
    output:
        stdout
 
    shell:
    '''
    python !{script_dir}/query_db_line.py !{study} !{env_file}
    '''
}
 
workflow {
    // run process -> view printed statements in standard output
    query_db_line(params.study, params.env_file, params.script_dir) | view
}