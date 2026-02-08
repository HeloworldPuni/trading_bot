//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Vortex_Indicator
// ID_model: AAPL_5Min_2MV0_c5dc629f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAPL_5Min_2MV0_c5dc629f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAPL_5Min_c5dc629f(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Negative_Money_Flow <= 848033 )
		if( Negative_Money_Flow_Sum <= 2.59066e+09 )
			if( VIP_VIM <= 0.61285 )
				if( Positive_Money_Flow_Sum <= 2.46238e+09 )
					if( Raw_Money_Flow <= 1.7856e+08 )
						if( Negative_Money_Flow_Sum <= 1.35213e+09 )
							if( VIP <= 0.91635 )
								if( Positive_Money_Flow_Sum <= 3.93955e+08 )
									ret := -0.033501
								if( Positive_Money_Flow_Sum > 3.93955e+08 )
									ret := 0.085686
							if( VIP > 0.91635 )
								if( Negative_Money_Flow_Sum <= 753894 )
									ret := -0.254237
								if( Negative_Money_Flow_Sum > 753894 )
									ret := 0.048840
						if( Negative_Money_Flow_Sum > 1.35213e+09 )
							if( MFI_Low <= -4.04288 )
								if( VIP_VIM <= -0.639366 )
									ret := 0.500000
								if( VIP_VIM > -0.639366 )
									ret := 0.033537
							if( MFI_Low > -4.04288 )
								if( VIP <= 0.780305 )
									ret := -0.426966
								if( VIP > 0.780305 )
									ret := -0.112128
					if( Raw_Money_Flow > 1.7856e+08 )
						if( Raw_Money_Flow <= 2.7183e+08 )
							if( Negative_Money_Flow_Sum <= 1.45757e+09 )
								if( Positive_Money_Flow_Sum <= 2.1093e+09 )
									ret := 0.164591
								if( Positive_Money_Flow_Sum > 2.1093e+09 )
									ret := 0.623529
							if( Negative_Money_Flow_Sum > 1.45757e+09 )
								if( VIM <= 1.38514 )
									ret := 0.523466
								if( VIM > 1.38514 )
									ret := -1.000000 // sell
						if( Raw_Money_Flow > 2.7183e+08 )
							if( Positive_Money_Flow_Sum <= 2.34732e+09 )
								if( Negative_Money_Flow_Sum <= 2.28396e+07 )
									ret := -0.318841
								if( Negative_Money_Flow_Sum > 2.28396e+07 )
									ret := -0.023991
							if( Positive_Money_Flow_Sum > 2.34732e+09 )
								if( Positive_Money_Flow <= 1.27356e+09 )
									ret := 0.703704 // buy
								if( Positive_Money_Flow > 1.27356e+09 )
									ret := -0.125000
				if( Positive_Money_Flow_Sum > 2.46238e+09 )
					if( Positive_Money_Flow_Sum <= 2.88168e+09 )
						if( Money_Flow_Ratio <= 3.47428 )
							if( Raw_Money_Flow <= 3.44196e+08 )
								if( VIM <= 0.908123 )
									ret := -0.800000 // sell
								if( VIM > 0.908123 )
									ret := -0.322034
							if( Raw_Money_Flow > 3.44196e+08 )
								if( Positive_Money_Flow_Sum <= 2.59859e+09 )
									ret := 0.700000 // buy
								if( Positive_Money_Flow_Sum > 2.59859e+09 )
									ret := -0.285714
						if( Money_Flow_Ratio > 3.47428 )
							if( Money_Flow_Ratio <= 3.95224 )
								if( Typical_Price <= 198.407 )
									ret := -0.222222
								if( Typical_Price > 198.407 )
									ret := 0.722222 // buy
							if( Money_Flow_Ratio > 3.95224 )
								if( Negative_Money_Flow_Sum <= 3.91039e+08 )
									ret := -0.056075
								if( Negative_Money_Flow_Sum > 3.91039e+08 )
									ret := -0.414634
					if( Positive_Money_Flow_Sum > 2.88168e+09 )
						if( Money_Flow_Ratio <= 2.33379 )
							if( Positive_Money_Flow <= 1.95301e+07 )
								ret := 0.000000
							if( Positive_Money_Flow > 1.95301e+07 )
								if( VIM <= 1.00748 )
									ret := -0.846154 // sell
								if( VIM > 1.00748 )
									ret := -0.400000
						if( Money_Flow_Ratio > 2.33379 )
							if( MFI <= 73.8425 )
								if( Raw_Money_Flow <= 2.32184e+07 )
									ret := 0.000000
								if( Raw_Money_Flow > 2.32184e+07 )
									ret := 0.777778 // buy
							if( MFI > 73.8425 )
								if( Money_Flow_Ratio <= 4.50448 )
									ret := -0.282828
								if( Money_Flow_Ratio > 4.50448 )
									ret := 0.090535
			if( VIP_VIM > 0.61285 )
				if( Negative_Money_Flow_Sum <= 8.80021e+07 )
					if( Positive_Money_Flow <= 1.96731e+08 )
						if( VIM <= 0.622229 )
							if( Negative_Money_Flow_Sum <= 525851 )
								if( Positive_Money_Flow_Sum <= 8.50509e+06 )
									ret := -0.272727
								if( Positive_Money_Flow_Sum > 8.50509e+06 )
									ret := 0.866667 // buy
							if( Negative_Money_Flow_Sum > 525851 )
								if( Money_Flow_Ratio <= 4.52019 )
									ret := -0.133858
								if( Money_Flow_Ratio > 4.52019 )
									ret := -0.411538
						if( VIM > 0.622229 )
							if( Positive_Money_Flow_Sum <= 1.25615e+07 )
								if( Positive_Money_Flow <= 458740 )
									ret := -0.016897
								if( Positive_Money_Flow > 458740 )
									ret := -0.181524
							if( Positive_Money_Flow_Sum > 1.25615e+07 )
								if( Typical_Price <= 172.975 )
									ret := -0.450000
								if( Typical_Price > 172.975 )
									ret := 0.227273
					if( Positive_Money_Flow > 1.96731e+08 )
						if( Positive_Money_Flow <= 4.00336e+08 )
							if( VIP <= 1.40336 )
								if( Typical_Price <= 179.709 )
									ret := -0.393939
								if( Typical_Price > 179.709 )
									ret := -0.827160 // sell
							if( VIP > 1.40336 )
								ret := 0.500000
						if( Positive_Money_Flow > 4.00336e+08 )
							if( Negative_Money_Flow_Sum <= 3.33046e+07 )
								if( Positive_Money_Flow <= 5.35649e+08 )
									ret := 0.823529 // buy
								if( Positive_Money_Flow > 5.35649e+08 )
									ret := 0.150000
							if( Negative_Money_Flow_Sum > 3.33046e+07 )
								if( VIM <= 0.57527 )
									ret := -1.000000 // sell
								if( VIM > 0.57527 )
									ret := -0.200000
				if( Negative_Money_Flow_Sum > 8.80021e+07 )
					if( VIP_VIM <= 0.972849 )
						if( Typical_Price <= 180.049 )
							if( VIM <= 0.519202 )
								if( Negative_Money_Flow_Sum <= 2.12629e+08 )
									ret := 0.250000
								if( Negative_Money_Flow_Sum > 2.12629e+08 )
									ret := 1.000000 // buy
							if( VIM > 0.519202 )
								if( Positive_Money_Flow_Sum <= 1.3133e+09 )
									ret := -0.060606
								if( Positive_Money_Flow_Sum > 1.3133e+09 )
									ret := -0.380282
						if( Typical_Price > 180.049 )
							if( Positive_Money_Flow_Sum <= 7.90593e+08 )
								if( Positive_Money_Flow_Sum <= 6.49084e+08 )
									ret := -0.060606
								if( Positive_Money_Flow_Sum > 6.49084e+08 )
									ret := 0.587156
							if( Positive_Money_Flow_Sum > 7.90593e+08 )
								if( Positive_Money_Flow_Sum <= 3.86298e+09 )
									ret := -0.004854
								if( Positive_Money_Flow_Sum > 3.86298e+09 )
									ret := 0.500000
					if( VIP_VIM > 0.972849 )
						if( Positive_Money_Flow_Sum <= 1.53774e+09 )
							if( MFI <= 67.14 )
								ret := 1.000000 // buy
							if( MFI > 67.14 )
								ret := -0.333333
						if( Positive_Money_Flow_Sum > 1.53774e+09 )
							ret := 1.000000 // buy
		if( Negative_Money_Flow_Sum > 2.59066e+09 )
			if( Raw_Money_Flow <= 2.61949e+08 )
				if( MFI_High <= -76.8205 )
					if( Positive_Money_Flow_Sum <= 9.63145e+07 )
						if( Positive_Money_Flow_Sum <= 3.31779e+07 )
							ret := 0.333333
						if( Positive_Money_Flow_Sum > 3.31779e+07 )
							if( Money_Flow_Ratio <= 0.010438 )
								ret := -0.250000
							if( Money_Flow_Ratio > 0.010438 )
								ret := 0.000000
					if( Positive_Money_Flow_Sum > 9.63145e+07 )
						if( MFI_Low <= -17.6053 )
							ret := 1.000000 // buy
						if( MFI_Low > -17.6053 )
							ret := 0.500000
				if( MFI_High > -76.8205 )
					if( Positive_Money_Flow <= 1.39585e+07 )
						if( VIP <= 0.691376 )
							ret := 0.500000
						if( VIP > 0.691376 )
							if( VIM <= 1.35532 )
								if( Negative_Money_Flow_Sum <= 2.63786e+09 )
									ret := -0.375000
								if( Negative_Money_Flow_Sum > 2.63786e+09 )
									ret := -0.065000
							if( VIM > 1.35532 )
								ret := -1.000000 // sell
					if( Positive_Money_Flow > 1.39585e+07 )
						if( Negative_Money_Flow_Sum <= 2.65921e+09 )
							if( VIM <= 1.14799 )
								if( Negative_Money_Flow_Sum <= 2.63118e+09 )
									ret := -0.250000
								if( Negative_Money_Flow_Sum > 2.63118e+09 )
									ret := 0.750000 // buy
							if( VIM > 1.14799 )
								ret := 1.000000 // buy
						if( Negative_Money_Flow_Sum > 2.65921e+09 )
							if( MFI <= 21.1969 )
								if( Raw_Money_Flow <= 1.69803e+08 )
									ret := -0.376471
								if( Raw_Money_Flow > 1.69803e+08 )
									ret := 0.241379
							if( MFI > 21.1969 )
								if( VIM <= 0.951932 )
									ret := 0.000000
								if( VIM > 0.951932 )
									ret := -0.755556 // sell
			if( Raw_Money_Flow > 2.61949e+08 )
				if( Negative_Money_Flow_Sum <= 3.76384e+09 )
					if( Typical_Price <= 210.747 )
						if( VIM <= 1.16561 )
							if( VIP <= 0.87995 )
								ret := -0.250000
							if( VIP > 0.87995 )
								ret := -1.000000 // sell
						if( VIM > 1.16561 )
							ret := -1.000000 // sell
					if( Typical_Price > 210.747 )
						ret := -0.500000
				if( Negative_Money_Flow_Sum > 3.76384e+09 )
					if( Raw_Money_Flow <= 3.78195e+08 )
						if( MFI_High <= -56.5388 )
							ret := -0.400000
						if( MFI_High > -56.5388 )
							if( Typical_Price <= 181.637 )
								ret := -0.500000
							if( Typical_Price > 181.637 )
								ret := 0.750000 // buy
					if( Raw_Money_Flow > 3.78195e+08 )
						if( MFI <= 22.8565 )
							ret := -0.250000
						if( MFI > 22.8565 )
							ret := -0.833333 // sell
	if( Negative_Money_Flow > 848033 )
		if( Negative_Money_Flow_Sum <= 3.27004e+08 )
			if( VIP_VIM <= 0.142483 )
				if( VIP <= 0.815591 )
					if( VIM <= 1.5738 )
						if( Negative_Money_Flow <= 4.63805e+07 )
							if( Raw_Money_Flow <= 2.149e+07 )
								if( Negative_Money_Flow_Sum <= 6.05588e+07 )
									ret := 0.237910
								if( Negative_Money_Flow_Sum > 6.05588e+07 )
									ret := 0.505319
							if( Raw_Money_Flow > 2.149e+07 )
								if( VIM <= 1.14925 )
									ret := 0.863158 // buy
								if( VIM > 1.14925 )
									ret := -0.125000
						if( Negative_Money_Flow > 4.63805e+07 )
							if( VIP <= 0.676382 )
								if( VIM <= 1.0636 )
									ret := 0.000000
								if( VIM > 1.0636 )
									ret := -0.894737 // sell
							if( VIP > 0.676382 )
								if( Typical_Price <= 184.365 )
									ret := 0.642857
								if( Typical_Price > 184.365 )
									ret := -0.241379
					if( VIM > 1.5738 )
						if( MFI_Low <= -14.4695 )
							if( VIP_VIM <= -1.14238 )
								ret := 1.000000 // buy
							if( VIP_VIM > -1.14238 )
								ret := 0.400000
						if( MFI_Low > -14.4695 )
							if( Money_Flow_Ratio <= 0.219629 )
								if( VIP <= 0.549425 )
									ret := -0.840000 // sell
								if( VIP > 0.549425 )
									ret := -0.435897
							if( Money_Flow_Ratio > 0.219629 )
								if( Negative_Money_Flow_Sum <= 2.23244e+07 )
									ret := 0.093750
								if( Negative_Money_Flow_Sum > 2.23244e+07 )
									ret := -0.750000 // sell
				if( VIP > 0.815591 )
					if( Negative_Money_Flow_Sum <= 2.31274e+08 )
						if( Typical_Price <= 223.083 )
							if( Negative_Money_Flow <= 9.65595e+06 )
								if( MFI_Low <= -17.472 )
									ret := 0.782609 // buy
								if( MFI_Low > -17.472 )
									ret := 0.132530
							if( Negative_Money_Flow > 9.65595e+06 )
								if( VIP_VIM <= -0.137824 )
									ret := -0.287356
								if( VIP_VIM > -0.137824 )
									ret := 0.072254
						if( Typical_Price > 223.083 )
							if( Money_Flow_Ratio <= 0.370621 )
								if( Negative_Money_Flow_Sum <= 6.98905e+07 )
									ret := 0.450704
								if( Negative_Money_Flow_Sum > 6.98905e+07 )
									ret := -0.304348
							if( Money_Flow_Ratio > 0.370621 )
								if( MFI_High <= -37.8598 )
									ret := -0.377778
								if( MFI_High > -37.8598 )
									ret := -0.031818
					if( Negative_Money_Flow_Sum > 2.31274e+08 )
						if( Negative_Money_Flow_Sum <= 2.84101e+08 )
							if( MFI_Low <= 22.4498 )
								if( Raw_Money_Flow <= 2.44183e+06 )
									ret := 0.200000
								if( Raw_Money_Flow > 2.44183e+06 )
									ret := 0.861111 // buy
							if( MFI_Low > 22.4498 )
								if( Positive_Money_Flow_Sum <= 3.95693e+08 )
									ret := 0.152778
								if( Positive_Money_Flow_Sum > 3.95693e+08 )
									ret := 0.572650
						if( Negative_Money_Flow_Sum > 2.84101e+08 )
							if( VIM <= 0.999512 )
								if( Negative_Money_Flow_Sum <= 3.04258e+08 )
									ret := -0.028986
								if( Negative_Money_Flow_Sum > 3.04258e+08 )
									ret := 0.496970
							if( VIM > 0.999512 )
								if( Negative_Money_Flow_Sum <= 3.25869e+08 )
									ret := -0.010582
								if( Negative_Money_Flow_Sum > 3.25869e+08 )
									ret := 1.000000 // buy
			if( VIP_VIM > 0.142483 )
				if( MFI_Low <= 37.9074 )
					if( Positive_Money_Flow_Sum <= 2.12988e+07 )
						if( Positive_Money_Flow_Sum <= 1.51115e+07 )
							if( MFI_High <= -47.8545 )
								if( VIP <= 1.19006 )
									ret := -0.512195
								if( VIP > 1.19006 )
									ret := -0.038462
							if( MFI_High > -47.8545 )
								if( Negative_Money_Flow_Sum <= 1.19833e+07 )
									ret := -0.076389
								if( Negative_Money_Flow_Sum > 1.19833e+07 )
									ret := 0.294872
						if( Positive_Money_Flow_Sum > 1.51115e+07 )
							if( Negative_Money_Flow_Sum <= 1.79043e+07 )
								if( VIM <= 1.00659 )
									ret := 0.461538
								if( VIM > 1.00659 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 1.79043e+07 )
								if( VIP_VIM <= 0.178644 )
									ret := -0.444444
								if( VIP_VIM > 0.178644 )
									ret := 0.400000
					if( Positive_Money_Flow_Sum > 2.12988e+07 )
						if( Negative_Money_Flow <= 1.23322e+07 )
							if( Typical_Price <= 177.984 )
								if( MFI_Low <= 15.355 )
									ret := 0.100000
								if( MFI_Low > 15.355 )
									ret := -0.782051 // sell
							if( Typical_Price > 177.984 )
								if( Negative_Money_Flow_Sum <= 2.47372e+07 )
									ret := -0.714286 // sell
								if( Negative_Money_Flow_Sum > 2.47372e+07 )
									ret := -0.163043
						if( Negative_Money_Flow > 1.23322e+07 )
							if( Negative_Money_Flow <= 2.79598e+07 )
								if( Typical_Price <= 226.65 )
									ret := 0.500000
								if( Typical_Price > 226.65 )
									ret := -0.428571
							if( Negative_Money_Flow > 2.79598e+07 )
								if( Positive_Money_Flow_Sum <= 3.88286e+08 )
									ret := -0.062500
								if( Positive_Money_Flow_Sum > 3.88286e+08 )
									ret := -0.833333 // sell
				if( MFI_Low > 37.9074 )
					if( Positive_Money_Flow_Sum <= 1.09077e+09 )
						if( Positive_Money_Flow_Sum <= 7.83229e+08 )
							if( Money_Flow_Ratio <= 14.6726 )
								if( Money_Flow_Ratio <= 11.7697 )
									ret := 0.086296
								if( Money_Flow_Ratio > 11.7697 )
									ret := -0.722222 // sell
							if( Money_Flow_Ratio > 14.6726 )
								if( MFI_High <= 17.9548 )
									ret := 0.681818
								if( MFI_High > 17.9548 )
									ret := -0.125000
						if( Positive_Money_Flow_Sum > 7.83229e+08 )
							if( VIM <= 0.836316 )
								if( Negative_Money_Flow <= 1.02738e+08 )
									ret := 0.610619
								if( Negative_Money_Flow > 1.02738e+08 )
									ret := 0.093750
							if( VIM > 0.836316 )
								if( MFI_High <= -6.10674 )
									ret := 0.500000
								if( MFI_High > -6.10674 )
									ret := -0.269841
					if( Positive_Money_Flow_Sum > 1.09077e+09 )
						if( Positive_Money_Flow_Sum <= 1.23653e+09 )
							if( Money_Flow_Ratio <= 6.57348 )
								if( VIM <= 0.754449 )
									ret := -0.357143
								if( VIM > 0.754449 )
									ret := -0.843750 // sell
							if( Money_Flow_Ratio > 6.57348 )
								if( MFI <= 90.2337 )
									ret := 0.250000
								if( MFI > 90.2337 )
									ret := 0.000000
						if( Positive_Money_Flow_Sum > 1.23653e+09 )
							if( MFI <= 89.3083 )
								if( Money_Flow_Ratio <= 7.25307 )
									ret := -0.022727
								if( Money_Flow_Ratio > 7.25307 )
									ret := 0.655172
							if( MFI > 89.3083 )
								if( MFI <= 92.5934 )
									ret := -0.431034
								if( MFI > 92.5934 )
									ret := -0.007407
		if( Negative_Money_Flow_Sum > 3.27004e+08 )
			if( VIP <= 0.917436 )
				if( Raw_Money_Flow <= 2.21339e+08 )
					if( Positive_Money_Flow_Sum <= 6.54132e+08 )
						if( VIM <= 1.13044 )
							if( Typical_Price <= 228.581 )
								if( Negative_Money_Flow_Sum <= 8.32596e+08 )
									ret := 0.029630
								if( Negative_Money_Flow_Sum > 8.32596e+08 )
									ret := -0.150000
							if( Typical_Price > 228.581 )
								if( Positive_Money_Flow_Sum <= 4.56554e+08 )
									ret := -0.772727 // sell
								if( Positive_Money_Flow_Sum > 4.56554e+08 )
									ret := 0.166667
						if( VIM > 1.13044 )
							if( MFI <= 29.1407 )
								if( Typical_Price <= 197.153 )
									ret := -0.036466
								if( Typical_Price > 197.153 )
									ret := 0.290014
							if( MFI > 29.1407 )
								if( Money_Flow_Ratio <= 0.853477 )
									ret := 0.210191
								if( Money_Flow_Ratio > 0.853477 )
									ret := -0.317073
					if( Positive_Money_Flow_Sum > 6.54132e+08 )
						if( Negative_Money_Flow_Sum <= 8.91294e+08 )
							if( MFI_Low <= 27.1863 )
								if( MFI_High <= -35.9179 )
									ret := 0.000000
								if( MFI_High > -35.9179 )
									ret := 0.829268 // buy
							if( MFI_Low > 27.1863 )
								if( Money_Flow_Ratio <= 1.82373 )
									ret := 0.151515
								if( Money_Flow_Ratio > 1.82373 )
									ret := -0.222222
						if( Negative_Money_Flow_Sum > 8.91294e+08 )
							if( Positive_Money_Flow <= 1.91752e+07 )
								if( Positive_Money_Flow_Sum <= 7.80408e+08 )
									ret := -0.323760
								if( Positive_Money_Flow_Sum > 7.80408e+08 )
									ret := -0.052529
							if( Positive_Money_Flow > 1.91752e+07 )
								if( Raw_Money_Flow <= 1.2515e+08 )
									ret := -0.538462
								if( Raw_Money_Flow > 1.2515e+08 )
									ret := -1.000000 // sell
				if( Raw_Money_Flow > 2.21339e+08 )
					if( Positive_Money_Flow_Sum <= 1.07415e+09 )
						if( MFI <= 25.2001 )
							if( Positive_Money_Flow_Sum <= 2.28401e+07 )
								if( Typical_Price <= 169.834 )
									ret := 1.000000 // buy
								if( Typical_Price > 169.834 )
									ret := -0.555556
							if( Positive_Money_Flow_Sum > 2.28401e+07 )
								if( Negative_Money_Flow_Sum <= 4.24549e+08 )
									ret := -0.777778 // sell
								if( Negative_Money_Flow_Sum > 4.24549e+08 )
									ret := 0.048598
						if( MFI > 25.2001 )
							if( Negative_Money_Flow <= 5.20239e+08 )
								if( Negative_Money_Flow_Sum <= 1.06619e+09 )
									ret := -0.292857
								if( Negative_Money_Flow_Sum > 1.06619e+09 )
									ret := -0.722543 // sell
							if( Negative_Money_Flow > 5.20239e+08 )
								if( VIM <= 0.99034 )
									ret := -0.900000 // sell
								if( VIM > 0.99034 )
									ret := 0.206897
					if( Positive_Money_Flow_Sum > 1.07415e+09 )
						if( VIP_VIM <= -0.147635 )
							if( VIP_VIM <= -0.560376 )
								if( VIP_VIM <= -0.605543 )
									ret := 0.000000
								if( VIP_VIM > -0.605543 )
									ret := -0.833333 // sell
							if( VIP_VIM > -0.560376 )
								if( MFI_Low <= 15.0666 )
									ret := 0.690476
								if( MFI_Low > 15.0666 )
									ret := 0.268657
						if( VIP_VIM > -0.147635 )
							if( Negative_Money_Flow <= 3.84627e+08 )
								ret := 0.000000
							if( Negative_Money_Flow > 3.84627e+08 )
								ret := -1.000000 // sell
			if( VIP > 0.917436 )
				if( VIP_VIM <= 0.063511 )
					if( MFI_High <= -44.3839 )
						if( Positive_Money_Flow_Sum <= 1.14423e+09 )
							if( MFI_Low <= -13.3461 )
								if( Typical_Price <= 176.633 )
									ret := 0.727273 // buy
								if( Typical_Price > 176.633 )
									ret := 0.057692
							if( MFI_Low > -13.3461 )
								if( Negative_Money_Flow <= 8.96605e+07 )
									ret := -0.204239
								if( Negative_Money_Flow > 8.96605e+07 )
									ret := 0.125828
						if( Positive_Money_Flow_Sum > 1.14423e+09 )
							if( MFI_High <= -47.8872 )
								if( Raw_Money_Flow <= 1.27856e+07 )
									ret := 0.500000
								if( Raw_Money_Flow > 1.27856e+07 )
									ret := 1.000000 // buy
							if( MFI_High > -47.8872 )
								if( Negative_Money_Flow <= 1.72223e+08 )
									ret := 0.750000 // buy
								if( Negative_Money_Flow > 1.72223e+08 )
									ret := 0.000000
					if( MFI_High > -44.3839 )
						if( MFI_High <= -42.4709 )
							if( Positive_Money_Flow_Sum <= 3.23295e+08 )
								if( VIP_VIM <= -0.152927 )
									ret := 0.312500
								if( VIP_VIM > -0.152927 )
									ret := 0.777778 // buy
							if( Positive_Money_Flow_Sum > 3.23295e+08 )
								if( Negative_Money_Flow_Sum <= 6.69605e+08 )
									ret := -0.367347
								if( Negative_Money_Flow_Sum > 6.69605e+08 )
									ret := 0.435754
						if( MFI_High > -42.4709 )
							if( Positive_Money_Flow_Sum <= 2.3879e+08 )
								if( Raw_Money_Flow <= 3.58472e+07 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 3.58472e+07 )
									ret := 0.333333
							if( Positive_Money_Flow_Sum > 2.3879e+08 )
								if( Negative_Money_Flow <= 4.52073e+07 )
									ret := -0.007407
								if( Negative_Money_Flow > 4.52073e+07 )
									ret := 0.153139
				if( VIP_VIM > 0.063511 )
					if( Positive_Money_Flow_Sum <= 4.64062e+09 )
						if( Raw_Money_Flow <= 1.39589e+08 )
							if( Positive_Money_Flow_Sum <= 1.01723e+09 )
								if( Negative_Money_Flow_Sum <= 3.7475e+08 )
									ret := -0.080134
								if( Negative_Money_Flow_Sum > 3.7475e+08 )
									ret := 0.115385
							if( Positive_Money_Flow_Sum > 1.01723e+09 )
								if( Positive_Money_Flow_Sum <= 1.10106e+09 )
									ret := -0.389961
								if( Positive_Money_Flow_Sum > 1.10106e+09 )
									ret := -0.104355
						if( Raw_Money_Flow > 1.39589e+08 )
							if( VIP <= 1.37567 )
								if( Negative_Money_Flow <= 1.53224e+08 )
									ret := 0.368966
								if( Negative_Money_Flow > 1.53224e+08 )
									ret := 0.104427
							if( VIP > 1.37567 )
								if( Negative_Money_Flow_Sum <= 4.81715e+08 )
									ret := 0.000000
								if( Negative_Money_Flow_Sum > 4.81715e+08 )
									ret := -0.941176 // sell
					if( Positive_Money_Flow_Sum > 4.64062e+09 )
						if( Raw_Money_Flow <= 2.52353e+08 )
							if( VIM <= 0.761884 )
								if( VIP_VIM <= 0.605519 )
									ret := -0.750000 // sell
								if( VIP_VIM > 0.605519 )
									ret := 0.500000
							if( VIM > 0.761884 )
								if( Raw_Money_Flow <= 7.95687e+07 )
									ret := 0.000000
								if( Raw_Money_Flow > 7.95687e+07 )
									ret := 0.666667
						if( Raw_Money_Flow > 2.52353e+08 )
							if( VIP_VIM <= 0.509832 )
								if( Negative_Money_Flow_Sum <= 1.98899e+09 )
									ret := -0.111111
								if( Negative_Money_Flow_Sum > 1.98899e+09 )
									ret := 1.000000 // buy
							if( VIP_VIM > 0.509832 )
								ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Money_Flow_Index 
//@version=5
//indicator title="Money Flow Index (MFI)", shorttitle="MFI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)

// Input parameters
length_MFI = input.int(14, minval=1, title="MFI Length")

// Calculate the Typical Price
Typical_Price = (high + low + close) / 3

// Calculate Raw Money Flow
Raw_Money_Flow = Typical_Price * volume

// Calculate Positive and Negative Money Flow
Positive_Money_Flow = Raw_Money_Flow * (Typical_Price > Typical_Price[1] ? 1 : 0)
Negative_Money_Flow = Raw_Money_Flow * (Typical_Price < Typical_Price[1] ? 1 : 0)

// Sum of Positive and Negative Money Flow over the given length
Positive_Money_Flow_Sum = ta.sma(Positive_Money_Flow, length_MFI) * length_MFI
Negative_Money_Flow_Sum = ta.sma(Negative_Money_Flow, length_MFI) * length_MFI

// Calculate Money Flow Ratio
Money_Flow_Ratio = Positive_Money_Flow_Sum / Negative_Money_Flow_Sum

// Calculate MFI
MFI = 100 - (100 / (1 + Money_Flow_Ratio))

// Calculate MFI high and low bands
MFI_High = MFI - 80
MFI_Low = MFI - 20

// Plot the MFI
plot(MFI, color=color.blue, title="MFI")

// Plot the MFI high and low bands
hline(80, "MFI High", color=color.red, linestyle=hline.style_dashed)
hline(20, "MFI Low", color=color.green, linestyle=hline.style_dashed)
plot(MFI_High, color=color.red, title="MFI High Band")
plot(MFI_Low, color=color.green, title="MFI Low Band")


//CODE associated with the technical indicator L_Vortex_Indicator 
//@version=5
//indicator title = "Vortex Indicator", shorttitle="VI", format=format.price, precision=4, timeframe="", timeframe_gaps=true)
period_ = input.int(14, title="Length", minval=2)
VMP = math.sum( math.abs( high - low[1]), period_ )
VMM = math.sum( math.abs( low - high[1]), period_ )
STR = math.sum( ta.atr(1), period_ )
VIP = VMP / STR
VIM = VMM / STR

VIP_VIM = VIP - VIM

plot(VIP, title="VI +", color=#2962FF)
plot(VIM, title="VI -", color=#E91E63)
// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_AAPL_5Min_c5dc629f(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, VIP, VIM, VIP_VIM)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


