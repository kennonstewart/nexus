%% Clear all things
clc; clear; close all; path(pathdef);

root_dir = './migration_v2/LA_90_18/';
main(root_dir);

function [A] = main(root_dir, varargin) 
% ----------------------------------------------------------------------
% 
% Summary of this function goes here
% Detailed explanation goes here

% Author: Tri Nguyen (nguyetr9@oregonstate.edu)

% ----------------------------------------------------------------------
    
    % Check the options structure.
    p = inputParser;
    p.addOptional('verbose', 0);
    p.addOptional('debug', 0);
    p.KeepUnmatched = true;
    p.parse(varargin{:});
    options = p.Results;

    X = readtable(sprintf('%s/IRS_Migration_Matrix_1990.csv', root_dir));
    list_counties = X{1, 2:end};
    list_counties = arrayfun(@(x) ['0000' num2str(x)], list_counties, 'UniformOutput', false);
    list_counties = cellfun(@(x) x(end-4:end), list_counties, 'UniformOutput', false);

    X = readtable('dis.csv', 'Format', '%s%s%f');
    G = graph(X.county1, X.county2, X.mi_to_county);
    G = simplify(G);
    G = subgraph(G, list_counties);
    G = reordernodes(G, list_counties);
    A = adjacency(G, 'weighted');

    path2file = sprintf('%s/dis.mat', root_dir);
    save(path2file, 'A');
    fprintf('Saved to %s \n', path2file);
end
