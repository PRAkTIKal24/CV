%% Program to apply smoothing filters to a given image
clear
clc
%Read the image
I = imread('batman.jpeg');
%Convert to grayscale for easier operation
I = rgb2gray(I);

%Box filter with W=5
w = 5; 
kernelB = ones(w) / w^2;
Box = conv2(I, kernelB, 'full')/255;

%Gaussian filter with sigma=3
sigma = 3;
h = fspecial('gaussian',[5 5],sigma);
Gaus = conv2(I, h, 'full')/255;

%Median filter with a 5x5 window
Med = zeros(size(I),class(I));
for m = 3 : size(I,1)-2
    for n = 3 : size(I,2)-2
        list = I(m-2:m+2,n-2:n+2);
        Med(m,n) = median(list(:));
    end
end

subplot(2,2,1)
imshow(I)
title('Original Image')

subplot(2,2,2)
imshow(Box)
title('Box filter')

subplot(2,2,3)
imshow(Gaus)
title('Gaussian filter')

subplot(2,2,4)
imshow(Med)
title('Median filter')
