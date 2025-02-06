%% Clear all things
clc; clear; close all; path(pathdef);

X = readtable('dis.csv', 'Format', '%s%s%f');
G = graph(X.county1, X.county2, X.mi_to_county);
G = simplify(G);
A = adjacency(G, 'weighted');
sigma2 = 900^2;

W = exp(-A.^2/sigma2);
D = sum(W);
L = diag(D) - W;

figure()
imagesc(log(L+1))
title('log(L+1)')
colorbar
exportgraphics(gcf, 'log_laplacian.png', 'resolution', 300);

save('laplacian_matrix.mat', 'L');


