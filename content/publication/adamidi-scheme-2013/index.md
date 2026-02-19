---
title: "A scheme for X-ray medical image denoising using sparse representations"
date: 2013-01-01
doi: "10.1109/bibe.2013.6701544"
publishDate: 2013-01-01
authors: ['Adamidi, E.', 'Vlachos, E.', 'Dermitzakis, A.', 'Berberidis, K.', 'Pallikarakis, N.']
publication_types: ["1"]
abstract: "This paper addresses the problem of noise removal in X-ray medical images. A novel scheme for image denoising is proposed, by leveraging recent advances in sparse and redundant representations. The noisy X-ray image is decomposed, with respect to an overcomplete dictionary which is either fixed or trained on the noisy image, and it is reconstructed using greedy techniques. The new scheme has been tested with both artificial and real X-ray images and it turns out that it may offer superior denoising results as compared to other existing methods."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE 13th International Conference on Bioinformatics and Bioengineering (BIBE)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposes a novel denoising scheme for X-ray images leveraging sparse and redundant representations over learned dictionaries.
- Investigates the impact of different dictionary types (fixed, trained on natural images, trained on X-ray images, trained on noisy images) on denoising performance.
- Evaluates the effect of dictionary size and sparsity level on denoising results.

## Results & Insights

{{< figure src="fig1.png" caption="Comparison of denoising performance across different dictionary types (DCT, general K-SVD, specialized K-SVD, noisy K-SVD) versus noise standard deviation." >}}
This plot demonstrates that specialized and noisy dictionaries generally outperform fixed DCT dictionaries, especially at higher noise levels.

{{< figure src="fig2.png" caption="Comparison of denoising performance across different dictionary types (DCT, general K-SVD, specialized K-SVD, noisy K-SVD) versus the number of nonzero coefficients in the representation." >}}
This plot shows that increasing the sparsity level generally improves denoising performance, with the noisy dictionary consistently performing best.

{{< figure src="fig3.png" caption="Comparison of different dictionaries in terms of PSNR of the denoised image versus the size of image patch." >}}
This plot indicates that larger patch sizes (e.g., 8x8) generally lead to better denoising performance across all dictionary types.

{{< figure src="fig4.png" caption="Comparison of different dictionaries in terms of PSNR of the denoised image versus the number of nonzero elements of the representation vector." >}}
This plot reveals that increasing the number of nonzero elements (sparsity) improves denoising performance, with the noisy dictionary showing the highest PSNR.

{{< figure src="fig5.png" caption="Example denoising results showing the improvement in Contrast to Noise Ratio (CNR) and visual quality." >}}
This figure visually demonstrates the effectiveness of the proposed method in enhancing image contrast and revealing finer details like calcifications.

{{< figure src="fig6.png" caption="Example denoising results showing the improvement in Contrast to Noise Ratio (CNR) and visual quality." >}}
This figure provides a qualitative assessment of the denoising performance, clearly showing the enhanced clarity and reduced noise in the reconstructed image.
