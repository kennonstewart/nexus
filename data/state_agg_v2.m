%% Clear all things
clc; clear; close all; path(pathdef);
addpath('./../visualization/utils')

all_state_index_data = readtable('./migration_v2/all_state_index.txt');
output_dir = './migration_v2/state_level_90_18/';
YEARS = 1990:2018;
num_years = numel(YEARS);
input_dir = './migration_v2/';

num_states = size(all_state_index_data, 1);
state_data = zeros(num_states, num_states, num_years);
for y=1:num_years
    y
    file_name = sprintf('%s/IRS_Migration_Matrix_%d.csv', input_dir, YEARS(y));
    data = readmatrix(file_name);
    data = data(2:end, 2:end);
    for i=1:num_states
        for j=1:num_states
            transmitter_county_index = all_state_index_data.Var3(i);
            transmitter_county_index = cell2mat(textscan(transmitter_county_index{1}, '%d', 'Delimiter', ','));

            reciever_county_index = all_state_index_data.Var3(j);
            reciever_county_index = cell2mat(textscan(reciever_county_index{1}, ...
                '%d', 'Delimiter', ','));

            state_data(i, j, y) = sum(data(transmitter_county_index, ...
                reciever_county_index), 'all');
        end
    end
end

Data = struct;
Data.Y = state_data;
Data.state_names = all_state_index_data.Var2;
Data.idx2Names = all_state_index_data.Var1;
Data.idx2Fips = all_state_index_data.Var2;


for i=1:num_years
    for j=1:size(state_data, 1)
        state_data(j, j, i) = 0;
    end
end
Data.diag_state_data = state_data;
save(sprintf('%s/data.mat', output_dir), 'Data');

figure();
imagesc(state_data(:, :, 1))
colorbar
title(sprintf('Immigration of %d states of the first slab', num_states))
exportgraphics(gcf, sprintf('%s/state_data.png', output_dir), 'resolution', 300);


% Just checking
options = struct;
options.state_data = sprintf('%s/data.mat', output_dir);
m = mapping_name(options);
