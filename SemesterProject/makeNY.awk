BEGIN{
    /*The following reads the raw daya, for all zipcodes. It then extracts all of the zip codes for NY, filtering by field 6 - state. The results are then contained in a file, NYZips, which is processed later*/
    FS = "|"

     /*raw data for all zip codes and informations */
    raw_zips = "/data/raw/ZIPcodes/ZIPcodes.gz"
   
    input_com = "zcat " raw_zips

    /*field 6 contains the state. Make a file of only information for NY zip codes which can then be examined*/
    while((input_com |getline)>0)
	if ($6 == "NY"){
	    print $0 > "NYZips"
	}
}
