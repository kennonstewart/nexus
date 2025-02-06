# DESCRIPTION
All necessary files are uploaded to our shared drive: https://drive.google.com/drive/u/1/folders/1OdXuBauDUuq2j1a3ZEAjuqu22mq8LIpx

## DATA FOR CA's COUNTIES

- File 'cali.mat'. Contain a variable named 'data'. It is a structure including these fields:
    + Y: 58x58x18 --> raw data of 58 counties of California
    + Y_log: 58x58x18 --> log-scaled data 58 counties of California
    + index: Indices of 58 counties respected to the data of the whole country (3137 counties), which is the original data.

- File 'mapping_name.m': Function mapping_name
+ Input: No parameter. But you'll need to change path to 2 files: CountyName_MSAName.csv and country_time_1.csv. 
    . I belived CountyName_MSAName.csv: is uploaded by Prof. Zack in shared drive. I uploaded to my directory just for convenient.
    . country_time_1.csv: one of 18 files data.
+ Output: idx2County
A cell array mapping from index to county's name where the index is respected to the original data (3137 counties)

These 2 files should provide enough information about 58 counties in California. 



## MAP VISUALIZATION
- You will need to install Mapping toolbox for Matlab, which can be found here: https://www.mathworks.com/products/mapping.html
- 'tl_2017_us_county.shp': Geometric counties data for map visualization of the US (data published in 2017)
- 'mapping_demo.m': Basically, you only need to change path to file `tl_2017_us_county.shp`, then you are good to run this demo. It will show how to highlight specified counties in CA.

