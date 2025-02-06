%% Clear all things
clc; clear; close all; path(pathdef);
addpath('./../visualization/utils')

YEARS = 1990:2018;
input_dir = './migration_v2/CA_90_18/';
path_to_one_year = './migration_v2/CA_90_18/IRS_Migration_Matrix_1990.csv';
deleteDiagonal = true;
isMsa = false;

X = [];
for i=1:numel(YEARS)
    fileName = sprintf('%s/IRS_Migration_Matrix_%d.csv', input_dir, YEARS(i));
    X{i} = readtable(fileName);
    i
end

noCounties= size(X{1}, 1)-1;
Y = zeros(noCounties, noCounties, length(X));
county_indices = [];
for i=1:numel(YEARS)
    Y(:, :, i) = table2array(X{i}(2:end, 2:end));
    if i==1
        county_indices = X{i}.Var1(2:end)+1;
    else
        assert(all(county_indices == X{i}.Var1(2:end)+1));
    end
end

Data = struct;
Data.Y = Y;
% Data.index = [county_indices];
% save(sprintf('%s/data.mat', input_dir), 'Data', '-v7.3');

figure();
tensorSize = size(Y);
if deleteDiagonal
    for i=1:tensorSize(3)
        for j=1:tensorSize(1)
            Y(j, j, i) = 0;
        end
    end
end
imagesc((Y(:, :, 1)));
% title('First slab in log space')
colorbar
exportgraphics(gcf, sprintf( '%s/data.png', input_dir), 'resolution', 300);


% Just checking
options = struct;
options.us_county_file = './../visualization/map/tl_2017_us_county.shp';
options.county_name_msa_name_file = './migration_v2/origin/CountyName_MSAName.csv';'./migration_v2/origin/msa_name.csv'; 
options.path_to_one_year = path_to_one_year;
options.area_code = '-1';
options.isMsa = isMsa;
m = mapping_name(options);
m

