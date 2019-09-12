%%
%Impletmenting basic smoothing filters - Box, Gaussian, Median filters
%%

%Read image
I1 = imread('pepper.jpeg');
I = rgb2gray(I1);

%Box filter with a 5x5 window
Box = imboxfilt(I,5);

%Gaussian filter with sigma=3
Gaus = imgaussfilt(I,3);

%Median filter
for c = 1 : 3
    Med = medfilt2(I, [5, 5]);
end

subplot(2,2,1)
imshow(I)
title('Original Image')

subplot(2,2,2)
imshow(Box)
title('Box Filter ([5x5])')

subplot(2,2,3)
imshow(Gaus)
title('Gaussian Filter (sigma=3)')

subplot(2,2,4)
imshow(Med)
title('Median Filter ([5x5])')