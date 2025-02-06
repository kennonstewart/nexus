%% Clear all things
clc; clear; close all; path(pathdef);
addpath('./../visualization/')


year = 1;
file_name = './county_migration_counts/CA/county_time_10.csv';
data = readmatrix(file_name);
data = data(2:end, 2:end);

x = load('cali.mat');
sum(data - x.data.Y(:, :, 10), 'all')

data = load('./county_migration_counts/CA/data.mat');

sum(data.Data.index(:) - x.data.index(:))
%
% options = struct;
% options.us_county_file = './../visualization/map/tl_2017_us_county.shp';
% options.county_name_msa_name_file = './county_migration_counts/CountyName_MSAName.csv';
% options.path_to_one_year = './county_migration_counts/county_time_1.csv';
% m = mapping_name(options);
