%% Clear all things
clc; clear; close all; path(pathdef);
addpath('./../visualization/')

noYears = 18;
input_dir = './county_migration_counts/LA_extra/'


X = [];
for i=1:noYears
    fileName = sprintf('%s/county_time_%d.csv', input_dir, i);
    X{i} = readtable(fileName);
    i
end

noCounties= size(X{1}, 1)-1;
Y = zeros(noCounties, noCounties, length(X));
county_indices = [];
for i=1:noYears
    Y(:, :, i) = table2array(X{i}(2:end, 2:end));
    if i==1
        county_indices = X{i}.Var1(2:end)+1;
    % else
    %     assert(all(county_indices(:) == tmp(1, 2:end)'+1));
    end
end

Data = struct;
Data.Y = Y;
Data.index = [county_indices];
save(sprintf('%s/data.mat', input_dir), 'Data');

figure();
tensorSize = size(Y);
for i=1:tensorSize(3)
    for j=1:tensorSize(1)
        Y(j, j, i) = 0;
    end
end
imagesc(Y(:, :, 1))

colorbar
exportgraphics(gcf, sprintf( '%s/data.png', input_dir), 'resolution', 300);


options = struct;
options.us_county_file = './../visualization/map/tl_2017_us_county.shp';
options.county_name_msa_name_file = './county_migration_counts/CountyName_MSAName.csv';
options.path_to_one_year = './county_migration_counts/county_time_1.csv';
m = mapping_name(options);
county_names = arrayfun(@(x) m(x), Data.index(1:end-1))
