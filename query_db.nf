#!/usr/bin/env nextflow
 params.study = 'pilot'
 params.env_file= projectDir + '/.env'
 params.script_dir = projectDir + '/scripts'
 
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
    query_db_line(params.study, params.env_file, params.script_dir)
}