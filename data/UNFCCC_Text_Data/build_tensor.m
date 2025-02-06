%% Clear all things
clc; clear; close all; path(pathdef);

N = 10294;
D = 196;
Y = zeros(D, N, 10);
Y_tfidf = zeros(D, N, 10);

for year=16:25
    X = readtable(sprintf('./clean_data/COP%dDTM', year));
    counts = X{1:end, 2:end};
    Y(:, :, year-15) = counts;

    tf = counts;
    idf = D./(sum(counts>0)+1);
    tf_idf = floor(tf.*idf);
    Y_tfidf(:, :, year-15) = tf_idf;
end

figure();
imagesc(Y(:, :, 1));
title('original - the first year')
colorbar
exportgraphics(gcf, './png/original.png', 'resolution', 300);

figure();
imagesc(log(Y(:, :, 1)+1));
title('original - log(x+1) of the first year')
colorbar
exportgraphics(gcf, './png/original_log.png', 'resolution', 300);


figure();
imagesc(log(Y_tfidf(:, :, 1)+1));
title('tfidf - log(x+1) of the first year');
colorbar
exportgraphics(gcf, './png/tfidf_log.png', 'resolution', 300);

save('./mat_data/COP.mat', 'Y', 'Y_tfidf');


