#!/usr/bin/gawk -f
BEGIN{
    /*The following extracts from the raw data of 311 service requests made, all of the request about graffiti. i.e, all of the graffiti complaints made to NYC*/
    FS = "\t"
    /*the file is raw 311 data calls, from NYC*/
    file = "/data/raw/NYC311/311_Service_Requests_from_2010_to_Present.tsv.gz" 
    output_file = "311_graffiti"
    
    command = "zcat " file
    output_command =  output_file 

    /*extract from the 311 data all graffiti complaints*/
    while((command | getline)>0)
    {
	/*field 6 contains the complaint descriptor*/
	if(toupper($6)=="GRAFFITI"){
	    print $0  > output_command
	}
    }
    close(command)
    /*output now contains only graffiti calls*/
}

