#!/usr/bin/env nextflow
 params.study = 'pilot'
 project_dir = projectDir
 
/*
 * A trivial Perl script that produces a list of number pairs
 */
process query_db_line{
    input:
        val study
    output:
        stdout
 
    shell:
    '''
    python !{project_dir}/query_db_line.py !{study}
    '''
}
 
workflow {
    query_db_line(params.study)
}