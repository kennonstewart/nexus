X = {};
years= [1990:5:2010];
for i=1:numel(years)
    fileName = sprintf('csv/world_migration_time_%d.csv', years(i));
    X{i} = readtable(fileName, 'ReadRowNames', true);
    i
end

num_cols = size(X{1}, 1);
Y = zeros(num_cols, num_cols, length(X));
for i=1:numel(years)
    Y(:, :, i) = table2array(X{i});
end

Data =struct;
Data.Y = Y;
Data.countries = X{1}.Properties.VariableNames;
save('./mat/data.mat', 'Data');

