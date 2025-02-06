%% Clear all things
clc; clear; close all; path(pathdef);
addpath('./../visualization/utils')

input_dir = './migration_v2';
deleteDiagonal = true;


load(sprintf('%s/data.mat', input_dir));
Y = Data.Y;

figure();
tensorSize = size(Y);
if deleteDiagonal
    for i=1:tensorSize(3)
        for j=1:tensorSize(1)
            Y(j, j, i) = 0;
        end
    end
end
YEARS = 1990:2018;
i=1;
imagesc((log(Y(:, :, i))));
title(sprintf('Year %d', YEARS(i)))
colorbar
exportgraphics(gcf, sprintf('%s/data_%d.png', input_dir, YEARS(i)), 'resolution', 300);

