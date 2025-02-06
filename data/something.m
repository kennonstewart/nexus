%% Clear all things
clc; clear; close all; path(pathdef);

num_years = 18;
% state_data = zeros(3137, 3137, 18);
% Y = zeros(3137, 3137, 18);
% for year=1:num_years
%     year
%     file_name = sprintf('./county_migration_counts/county_time_%d.csv', year);
%     data = readmatrix(file_name);
%     data = data(2:end, 2:end);
%     Y(:, :, year) = data;
% end
load('all.mat', 'Y')

data = load('./county_migration_counts/LA_extra/data.mat');
indices = data.Data.index;
for year=1:18
    row = Y(1143, :, year);
    destinationFilter = row>0;
    destinationsInd = find(destinationFilter);

    insideCount = sum(ismember(destinationsInd, indices));
    fprintf('Year: %d \n', year);
    fprintf('Orleans to LA: %d\n', insideCount);
    fprintf('Orleans to other states: %d\n\n', sum(destinationFilter) - insideCount)
end

fprintf('--------------------------------------\n')
fprintf('--------------------------------------\n')
fprintf('--------------------------------------\n')

for year=1:18
    row = Y(1143, :, year);
    destinationFilter = row>0;
    destinationsInd = find(destinationFilter);

    inside = destinationsInd(ismember(destinationsInd, indices));
    inside = row(inside);
    outside = destinationsInd(~ismember(destinationsInd, indices));
    outside = row(outside);
    fprintf('Year: %d \n', year);
    fprintf('Sum Orleans to LA: %d\n', sum(inside));
    fprintf('Sum Orleans to other states: %d\n\n', sum(outside));
end


