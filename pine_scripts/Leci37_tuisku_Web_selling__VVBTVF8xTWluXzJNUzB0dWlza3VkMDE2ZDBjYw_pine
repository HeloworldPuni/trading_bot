//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Stochastic_RSI
// ID_model: UPST_1Min_2MS0_d016d0cc Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_UPST_1Min_2MS0_d016d0cc", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_UPST_1Min_d016d0cc(Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow, rsi1, d, k, smoothD_d, d_k, smoothK_k)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Negative_Money_Flow <= 1.29315 )
		if( Negative_Money_Flow_Sum <= 550996 )
			if( rsi1 <= 47.0726 )
				if( Raw_Money_Flow <= 1.46942e+06 )
					if( d <= 44.4009 )
						if( rsi1 <= 38.6024 )
							if( Typical_Price <= 28.6269 )
								if( Negative_Money_Flow_Sum <= 111192 )
									ret := 0.365591
								if( Negative_Money_Flow_Sum > 111192 )
									ret := -0.045614
							if( Typical_Price > 28.6269 )
								if( d <= 24.107 )
									ret := 0.187215
								if( d > 24.107 )
									ret := 0.476636
						if( rsi1 > 38.6024 )
							if( Negative_Money_Flow_Sum <= 157773 )
								if( MFI_Low <= 23.6318 )
									ret := 0.362069
								if( MFI_Low > 23.6318 )
									ret := 0.025105
							if( Negative_Money_Flow_Sum > 157773 )
								if( Positive_Money_Flow_Sum <= 156024 )
									ret := -0.246964
								if( Positive_Money_Flow_Sum > 156024 )
									ret := -0.009494
					if( d > 44.4009 )
						if( Negative_Money_Flow_Sum <= 133621 )
							if( Typical_Price <= 28.1177 )
								if( Negative_Money_Flow_Sum <= 90975.1 )
									ret := 0.507042
								if( Negative_Money_Flow_Sum > 90975.1 )
									ret := -0.102041
							if( Typical_Price > 28.1177 )
								if( d <= 47.7337 )
									ret := 0.222222
								if( d > 47.7337 )
									ret := -0.363636
						if( Negative_Money_Flow_Sum > 133621 )
							if( Negative_Money_Flow_Sum <= 160990 )
								if( rsi1 <= 45.6504 )
									ret := 0.789474 // buy
								if( rsi1 > 45.6504 )
									ret := 0.222222
							if( Negative_Money_Flow_Sum > 160990 )
								if( Typical_Price <= 22.7883 )
									ret := -0.094340
								if( Typical_Price > 22.7883 )
									ret := 0.275410
				if( Raw_Money_Flow > 1.46942e+06 )
					if( d_k <= 12.995 )
						ret := -0.750000 // sell
					if( d_k > 12.995 )
						ret := -1.000000 // sell
			if( rsi1 > 47.0726 )
				if( Negative_Money_Flow_Sum <= 19087.1 )
					if( Money_Flow_Ratio <= 9.95745 )
						if( Positive_Money_Flow_Sum <= 55543.5 )
							if( Positive_Money_Flow <= 3073.75 )
								if( MFI_High <= -9.59024 )
									ret := 0.000000
								if( MFI_High > -9.59024 )
									ret := 0.250000
							if( Positive_Money_Flow > 3073.75 )
								ret := -0.250000
						if( Positive_Money_Flow_Sum > 55543.5 )
							if( rsi1 <= 66.4663 )
								ret := 1.000000 // buy
							if( rsi1 > 66.4663 )
								if( Typical_Price <= 24.535 )
									ret := 0.454545
								if( Typical_Price > 24.535 )
									ret := -0.111111
					if( Money_Flow_Ratio > 9.95745 )
						if( rsi1 <= 68.5077 )
							if( Typical_Price <= 27.0367 )
								if( d <= 74.5093 )
									ret := 0.500000
								if( d > 74.5093 )
									ret := 0.000000
							if( Typical_Price > 27.0367 )
								ret := 1.000000 // buy
						if( rsi1 > 68.5077 )
							if( d_k <= -5.3661 )
								if( smoothD_d <= 78.1749 )
									ret := -1.000000 // sell
								if( smoothD_d > 78.1749 )
									ret := -0.250000
							if( d_k > -5.3661 )
								if( MFI_High <= 14.7001 )
									ret := 0.500000
								if( MFI_High > 14.7001 )
									ret := -0.153846
				if( Negative_Money_Flow_Sum > 19087.1 )
					if( Positive_Money_Flow_Sum <= 453456 )
						if( rsi1 <= 63.8401 )
							if( MFI_High <= -17.7045 )
								if( Money_Flow_Ratio <= 1.20707 )
									ret := -0.120722
								if( Money_Flow_Ratio > 1.20707 )
									ret := -0.288566
							if( MFI_High > -17.7045 )
								if( Raw_Money_Flow <= 36044.8 )
									ret := 0.062432
								if( Raw_Money_Flow > 36044.8 )
									ret := -0.212885
						if( rsi1 > 63.8401 )
							if( Positive_Money_Flow <= 38038.7 )
								if( Raw_Money_Flow <= 13255.7 )
									ret := -0.316222
								if( Raw_Money_Flow > 13255.7 )
									ret := -0.139130
							if( Positive_Money_Flow > 38038.7 )
								if( Negative_Money_Flow_Sum <= 490524 )
									ret := -0.474164
								if( Negative_Money_Flow_Sum > 490524 )
									ret := 0.769231 // buy
					if( Positive_Money_Flow_Sum > 453456 )
						if( rsi1 <= 80.0627 )
							if( Raw_Money_Flow <= 1.5656e+06 )
								if( d_k <= -0.264336 )
									ret := -0.089965
								if( d_k > -0.264336 )
									ret := 0.042517
							if( Raw_Money_Flow > 1.5656e+06 )
								if( Positive_Money_Flow <= 3.24636e+06 )
									ret := 0.410256
								if( Positive_Money_Flow > 3.24636e+06 )
									ret := -0.296296
						if( rsi1 > 80.0627 )
							if( Money_Flow_Ratio <= 65.2163 )
								if( Positive_Money_Flow_Sum <= 5.6168e+06 )
									ret := -0.155211
								if( Positive_Money_Flow_Sum > 5.6168e+06 )
									ret := -0.620000
							if( Money_Flow_Ratio > 65.2163 )
								if( Raw_Money_Flow <= 1.81799e+06 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 1.81799e+06 )
									ret := 0.500000
		if( Negative_Money_Flow_Sum > 550996 )
			if( Positive_Money_Flow <= 486691 )
				if( Positive_Money_Flow_Sum <= 6.70602e+06 )
					if( rsi1 <= 81.2269 )
						if( MFI <= 71.1813 )
							if( Money_Flow_Ratio <= 2.18716 )
								if( smoothK_k <= 25.2469 )
									ret := -0.017612
								if( smoothK_k > 25.2469 )
									ret := 0.040594
							if( Money_Flow_Ratio > 2.18716 )
								if( Positive_Money_Flow_Sum <= 4.35777e+06 )
									ret := -0.091566
								if( Positive_Money_Flow_Sum > 4.35777e+06 )
									ret := -0.382979
						if( MFI > 71.1813 )
							if( Positive_Money_Flow <= 308437 )
								if( Positive_Money_Flow_Sum <= 2.85753e+06 )
									ret := 0.237389
								if( Positive_Money_Flow_Sum > 2.85753e+06 )
									ret := -0.057728
							if( Positive_Money_Flow > 308437 )
								if( d_k <= -20.3744 )
									ret := -0.555556
								if( d_k > -20.3744 )
									ret := 0.259557
					if( rsi1 > 81.2269 )
						if( MFI_High <= 3.50639 )
							if( Negative_Money_Flow_Sum <= 609393 )
								if( d <= 91.1496 )
									ret := -0.500000
								if( d > 91.1496 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 609393 )
								if( Positive_Money_Flow_Sum <= 3.4757e+06 )
									ret := 0.041096
								if( Positive_Money_Flow_Sum > 3.4757e+06 )
									ret := -0.380000
						if( MFI_High > 3.50639 )
							if( d <= 96.0306 )
								if( rsi1 <= 84.5562 )
									ret := -1.000000 // sell
								if( rsi1 > 84.5562 )
									ret := -0.736842 // sell
							if( d > 96.0306 )
								if( Money_Flow_Ratio <= 6.38866 )
									ret := -0.545455
								if( Money_Flow_Ratio > 6.38866 )
									ret := 0.166667
				if( Positive_Money_Flow_Sum > 6.70602e+06 )
					if( Positive_Money_Flow_Sum <= 7.00473e+06 )
						if( rsi1 <= 60.6529 )
							if( Raw_Money_Flow <= 431459 )
								if( Positive_Money_Flow_Sum <= 6.78478e+06 )
									ret := 0.166667
								if( Positive_Money_Flow_Sum > 6.78478e+06 )
									ret := -0.500000
							if( Raw_Money_Flow > 431459 )
								if( d_k <= 3.57553 )
									ret := 0.000000
								if( d_k > 3.57553 )
									ret := 0.818182 // buy
						if( rsi1 > 60.6529 )
							if( Typical_Price <= 37.2185 )
								if( smoothD_d <= 85.2224 )
									ret := -0.969697 // sell
								if( smoothD_d > 85.2224 )
									ret := -0.523810
							if( Typical_Price > 37.2185 )
								ret := 0.000000
					if( Positive_Money_Flow_Sum > 7.00473e+06 )
						if( Negative_Money_Flow_Sum <= 6.66702e+06 )
							if( MFI_Low <= 62.6676 )
								if( Positive_Money_Flow_Sum <= 1.16944e+07 )
									ret := 0.157576
								if( Positive_Money_Flow_Sum > 1.16944e+07 )
									ret := -0.174603
							if( MFI_Low > 62.6676 )
								if( d_k <= 11.9365 )
									ret := -0.411765
								if( d_k > 11.9365 )
									ret := 0.375000
						if( Negative_Money_Flow_Sum > 6.66702e+06 )
							if( Positive_Money_Flow <= 82730.1 )
								if( d <= 4.62645 )
									ret := -0.625000
								if( d > 4.62645 )
									ret := -0.105691
							if( Positive_Money_Flow > 82730.1 )
								if( smoothD_d <= 40.6455 )
									ret := -0.666667
								if( smoothD_d > 40.6455 )
									ret := -0.213115
			if( Positive_Money_Flow > 486691 )
				if( MFI <= 37.3785 )
					if( Raw_Money_Flow <= 727534 )
						if( Raw_Money_Flow <= 529887 )
							if( k <= 49.8566 )
								if( d <= 12.8464 )
									ret := 0.315068
								if( d > 12.8464 )
									ret := -0.302632
							if( k > 49.8566 )
								if( Typical_Price <= 26.1163 )
									ret := -0.142857
								if( Typical_Price > 26.1163 )
									ret := 0.547619
						if( Raw_Money_Flow > 529887 )
							if( d <= 59.9519 )
								if( Typical_Price <= 39.5535 )
									ret := -0.243316
								if( Typical_Price > 39.5535 )
									ret := 0.061224
							if( d > 59.9519 )
								if( rsi1 <= 44.2463 )
									ret := -0.661538
								if( rsi1 > 44.2463 )
									ret := 0.076923
					if( Raw_Money_Flow > 727534 )
						if( Positive_Money_Flow_Sum <= 5.31939e+06 )
							if( k <= 12.9509 )
								if( Negative_Money_Flow_Sum <= 1.47e+07 )
									ret := -0.022346
								if( Negative_Money_Flow_Sum > 1.47e+07 )
									ret := -0.630435
							if( k > 12.9509 )
								if( Typical_Price <= 34.4292 )
									ret := 0.419355
								if( Typical_Price > 34.4292 )
									ret := 0.125490
						if( Positive_Money_Flow_Sum > 5.31939e+06 )
							if( Negative_Money_Flow_Sum <= 1.92727e+07 )
								if( rsi1 <= 38.8698 )
									ret := -0.576389
								if( rsi1 > 38.8698 )
									ret := 0.011364
							if( Negative_Money_Flow_Sum > 1.92727e+07 )
								if( Negative_Money_Flow_Sum <= 2.24877e+07 )
									ret := 0.655738
								if( Negative_Money_Flow_Sum > 2.24877e+07 )
									ret := -0.044944
				if( MFI > 37.3785 )
					if( Money_Flow_Ratio <= 4.37986 )
						if( Typical_Price <= 37.673 )
							if( MFI_High <= -3.04157 )
								if( Positive_Money_Flow_Sum <= 1.84982e+06 )
									ret := -0.284404
								if( Positive_Money_Flow_Sum > 1.84982e+06 )
									ret := 0.144255
							if( MFI_High > -3.04157 )
								if( Raw_Money_Flow <= 1.15047e+06 )
									ret := 0.534545
								if( Raw_Money_Flow > 1.15047e+06 )
									ret := 0.248705
						if( Typical_Price > 37.673 )
							if( Positive_Money_Flow_Sum <= 1.05655e+07 )
								if( MFI_High <= -38.6868 )
									ret := 0.384146
								if( MFI_High > -38.6868 )
									ret := 0.082564
							if( Positive_Money_Flow_Sum > 1.05655e+07 )
								if( smoothK_k <= 16.8976 )
									ret := 0.250000
								if( smoothK_k > 16.8976 )
									ret := -0.235075
					if( Money_Flow_Ratio > 4.37986 )
						if( Typical_Price <= 34.1318 )
							if( Positive_Money_Flow_Sum <= 4.4218e+06 )
								if( Raw_Money_Flow <= 982987 )
									ret := 0.136364
								if( Raw_Money_Flow > 982987 )
									ret := 0.750000 // buy
							if( Positive_Money_Flow_Sum > 4.4218e+06 )
								if( d <= 87.114 )
									ret := -0.472826
								if( d > 87.114 )
									ret := -0.130435
						if( Typical_Price > 34.1318 )
							if( Negative_Money_Flow_Sum <= 1.2299e+06 )
								if( Raw_Money_Flow <= 1.66993e+06 )
									ret := 0.248485
								if( Raw_Money_Flow > 1.66993e+06 )
									ret := 0.666667
							if( Negative_Money_Flow_Sum > 1.2299e+06 )
								if( Positive_Money_Flow_Sum <= 5.21529e+07 )
									ret := -0.130621
								if( Positive_Money_Flow_Sum > 5.21529e+07 )
									ret := 0.491803
	if( Negative_Money_Flow > 1.29315 )
		if( Negative_Money_Flow <= 45125 )
			if( rsi1 <= 54.6829 )
				if( Raw_Money_Flow <= 9947.4 )
					if( MFI <= 25.5708 )
						if( Negative_Money_Flow_Sum <= 260376 )
							if( Positive_Money_Flow_Sum <= 56700.2 )
								if( d_k <= -15.2246 )
									ret := -0.916667 // sell
								if( d_k > -15.2246 )
									ret := 0.220588
							if( Positive_Money_Flow_Sum > 56700.2 )
								if( Raw_Money_Flow <= 6454.18 )
									ret := -1.000000 // sell
								if( Raw_Money_Flow > 6454.18 )
									ret := -0.235294
						if( Negative_Money_Flow_Sum > 260376 )
							if( Negative_Money_Flow_Sum <= 397328 )
								if( MFI_Low <= 4.21694 )
									ret := 0.666667
								if( MFI_Low > 4.21694 )
									ret := -0.428571
							if( Negative_Money_Flow_Sum > 397328 )
								if( Negative_Money_Flow_Sum <= 417841 )
									ret := -0.666667
								if( Negative_Money_Flow_Sum > 417841 )
									ret := 0.296296
					if( MFI > 25.5708 )
						if( rsi1 <= 47.7888 )
							if( Positive_Money_Flow_Sum <= 138080 )
								if( Negative_Money_Flow_Sum <= 47231.1 )
									ret := 0.741573 // buy
								if( Negative_Money_Flow_Sum > 47231.1 )
									ret := 0.273504
							if( Positive_Money_Flow_Sum > 138080 )
								if( MFI_Low <= 20.3712 )
									ret := 0.732824 // buy
								if( MFI_Low > 20.3712 )
									ret := 0.457143
						if( rsi1 > 47.7888 )
							if( smoothD_d <= 43.0002 )
								if( Negative_Money_Flow <= 1179.53 )
									ret := 0.615385
								if( Negative_Money_Flow > 1179.53 )
									ret := 0.017621
							if( smoothD_d > 43.0002 )
								if( Typical_Price <= 22.8427 )
									ret := -0.173913
								if( Typical_Price > 22.8427 )
									ret := 0.457801
				if( Raw_Money_Flow > 9947.4 )
					if( Negative_Money_Flow <= 5706.95 )
						if( rsi1 <= 44.6796 )
							if( Positive_Money_Flow_Sum <= 82096.9 )
								if( Typical_Price <= 36.0754 )
									ret := 0.411765
								if( Typical_Price > 36.0754 )
									ret := -1.000000 // sell
							if( Positive_Money_Flow_Sum > 82096.9 )
								if( smoothK_k <= -0.783715 )
									ret := -0.200000
								if( smoothK_k > -0.783715 )
									ret := 0.714286 // buy
						if( rsi1 > 44.6796 )
							if( d <= 30.2292 )
								if( k <= 22.7291 )
									ret := -0.043478
								if( k > 22.7291 )
									ret := -1.000000 // sell
							if( d > 30.2292 )
								if( Raw_Money_Flow <= 11503.5 )
									ret := -0.230769
								if( Raw_Money_Flow > 11503.5 )
									ret := 0.565217
					if( Negative_Money_Flow > 5706.95 )
						if( Typical_Price <= 25.7621 )
							if( MFI_Low <= -8.65643 )
								if( Typical_Price <= 21.3133 )
									ret := -0.333333
								if( Typical_Price > 21.3133 )
									ret := 0.663043
							if( MFI_Low > -8.65643 )
								if( smoothK_k <= 36.2195 )
									ret := 0.020346
								if( smoothK_k > 36.2195 )
									ret := 0.212087
						if( Typical_Price > 25.7621 )
							if( MFI <= 9.07666 )
								if( rsi1 <= 20.7949 )
									ret := -0.894737 // sell
								if( rsi1 > 20.7949 )
									ret := 0.037037
							if( MFI > 9.07666 )
								if( Negative_Money_Flow_Sum <= 269122 )
									ret := 0.195380
								if( Negative_Money_Flow_Sum > 269122 )
									ret := 0.337012
			if( rsi1 > 54.6829 )
				if( Positive_Money_Flow <= 530971 )
					if( Negative_Money_Flow_Sum <= 21330.5 )
						if( d_k <= 5.66422 )
							if( Positive_Money_Flow <= 9.39846 )
								if( Raw_Money_Flow <= 4004.64 )
									ret := -0.200000
								if( Raw_Money_Flow > 4004.64 )
									ret := -0.727273 // sell
							if( Positive_Money_Flow > 9.39846 )
								ret := -1.000000 // sell
						if( d_k > 5.66422 )
							ret := 0.400000
					if( Negative_Money_Flow_Sum > 21330.5 )
						if( Positive_Money_Flow <= 376.778 )
							if( d <= 36.4914 )
								if( Raw_Money_Flow <= 34195.8 )
									ret := -0.047059
								if( Raw_Money_Flow > 34195.8 )
									ret := -0.441176
							if( d > 36.4914 )
								if( smoothK_k <= 59.9984 )
									ret := 0.234000
								if( smoothK_k > 59.9984 )
									ret := 0.088530
						if( Positive_Money_Flow > 376.778 )
							if( Positive_Money_Flow <= 2358.9 )
								if( Typical_Price <= 28.4186 )
									ret := -0.661972
								if( Typical_Price > 28.4186 )
									ret := 0.000000
							if( Positive_Money_Flow > 2358.9 )
								if( k <= 93.6556 )
									ret := 0.045208
								if( k > 93.6556 )
									ret := -0.442623
				if( Positive_Money_Flow > 530971 )
					if( d_k <= -5.82972 )
						ret := 0.500000
					if( d_k > -5.82972 )
						ret := 1.000000 // buy
		if( Negative_Money_Flow > 45125 )
			if( Positive_Money_Flow_Sum <= 3.40308e+07 )
				if( Negative_Money_Flow_Sum <= 2.58438e+07 )
					if( d_k <= 0.371422 )
						if( Raw_Money_Flow <= 574959 )
							if( rsi1 <= 20.6203 )
								if( rsi1 <= 17.5228 )
									ret := 0.046296
								if( rsi1 > 17.5228 )
									ret := -0.287736
							if( rsi1 > 20.6203 )
								if( Positive_Money_Flow_Sum <= 129584 )
									ret := 0.285714
								if( Positive_Money_Flow_Sum > 129584 )
									ret := 0.047631
						if( Raw_Money_Flow > 574959 )
							if( Money_Flow_Ratio <= 0.930205 )
								if( Positive_Money_Flow_Sum <= 4.55003e+06 )
									ret := -0.057437
								if( Positive_Money_Flow_Sum > 4.55003e+06 )
									ret := -0.292072
							if( Money_Flow_Ratio > 0.930205 )
								if( Raw_Money_Flow <= 3.99378e+06 )
									ret := 0.101190
								if( Raw_Money_Flow > 3.99378e+06 )
									ret := -0.863636 // sell
					if( d_k > 0.371422 )
						if( Negative_Money_Flow <= 3.33505e+06 )
							if( Negative_Money_Flow_Sum <= 6.57684e+06 )
								if( Negative_Money_Flow_Sum <= 338120 )
									ret := 0.218092
								if( Negative_Money_Flow_Sum > 338120 )
									ret := 0.042805
							if( Negative_Money_Flow_Sum > 6.57684e+06 )
								if( Positive_Money_Flow_Sum <= 1.66273e+07 )
									ret := 0.191915
								if( Positive_Money_Flow_Sum > 1.66273e+07 )
									ret := -0.206107
						if( Negative_Money_Flow > 3.33505e+06 )
							if( MFI <= 44.1779 )
								if( Negative_Money_Flow_Sum <= 2.31099e+07 )
									ret := 0.715847 // buy
								if( Negative_Money_Flow_Sum > 2.31099e+07 )
									ret := -0.555556
							if( MFI > 44.1779 )
								if( d_k <= 18.9765 )
									ret := -0.583333
								if( d_k > 18.9765 )
									ret := 0.200000
				if( Negative_Money_Flow_Sum > 2.58438e+07 )
					if( Typical_Price <= 54.8732 )
						if( d_k <= 8.78728 )
							if( Positive_Money_Flow_Sum <= 1.67012e+07 )
								if( Positive_Money_Flow_Sum <= 9.72219e+06 )
									ret := 0.144928
								if( Positive_Money_Flow_Sum > 9.72219e+06 )
									ret := 0.901639 // buy
							if( Positive_Money_Flow_Sum > 1.67012e+07 )
								if( rsi1 <= 45.247 )
									ret := -0.145455
								if( rsi1 > 45.247 )
									ret := 0.782609 // buy
						if( d_k > 8.78728 )
							if( MFI_Low <= 24.4384 )
								if( Typical_Price <= 29.5705 )
									ret := 0.750000 // buy
								if( Typical_Price > 29.5705 )
									ret := 1.000000 // buy
							if( MFI_Low > 24.4384 )
								ret := 0.250000
					if( Typical_Price > 54.8732 )
						ret := -1.000000 // sell
			if( Positive_Money_Flow_Sum > 3.40308e+07 )
				if( Typical_Price <= 35.3316 )
					if( Positive_Money_Flow <= 4.74641e+06 )
						if( d_k <= -5.19253 )
							if( Positive_Money_Flow_Sum <= 3.92149e+07 )
								ret := -0.800000 // sell
							if( Positive_Money_Flow_Sum > 3.92149e+07 )
								ret := 1.000000 // buy
						if( d_k > -5.19253 )
							if( Positive_Money_Flow <= 2.65554e+06 )
								if( Positive_Money_Flow_Sum <= 6.67828e+07 )
									ret := 0.898876 // buy
								if( Positive_Money_Flow_Sum > 6.67828e+07 )
									ret := 0.500000
							if( Positive_Money_Flow > 2.65554e+06 )
								if( MFI <= 66.5038 )
									ret := 1.000000 // buy
								if( MFI > 66.5038 )
									ret := 0.000000
					if( Positive_Money_Flow > 4.74641e+06 )
						ret := 0.000000
				if( Typical_Price > 35.3316 )
					if( Negative_Money_Flow <= 2.82635e+06 )
						if( Positive_Money_Flow_Sum <= 3.59979e+07 )
							ret := 0.750000 // buy
						if( Positive_Money_Flow_Sum > 3.59979e+07 )
							if( MFI_Low <= 56.3734 )
								if( Negative_Money_Flow_Sum <= 3.23841e+07 )
									ret := 0.294118
								if( Negative_Money_Flow_Sum > 3.23841e+07 )
									ret := -1.000000 // sell
							if( MFI_Low > 56.3734 )
								if( k <= 80.5172 )
									ret := -1.000000 // sell
								if( k > 80.5172 )
									ret := 0.250000
					if( Negative_Money_Flow > 2.82635e+06 )
						if( d_k <= -0.289361 )
							if( MFI_High <= -3.22331 )
								if( Raw_Money_Flow <= 3.8073e+06 )
									ret := -1.000000 // sell
								if( Raw_Money_Flow > 3.8073e+06 )
									ret := 0.333333
							if( MFI_High > -3.22331 )
								ret := -1.000000 // sell
						if( d_k > -0.289361 )
							if( Typical_Price <= 39.194 )
								if( Typical_Price <= 37.3864 )
									ret := 0.833333 // buy
								if( Typical_Price > 37.3864 )
									ret := -0.250000
							if( Typical_Price > 39.194 )
								if( Raw_Money_Flow <= 3.20128e+06 )
									ret := 0.333333
								if( Raw_Money_Flow > 3.20128e+06 )
									ret := 0.952381 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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


//CODE associated with the technical indicator L_Stochastic_RSI 
//@version=5
//indicator title="Stochastic RSI", shorttitle="Stoch RSI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
smoothK = input.int(3, "K", minval=1)
smoothD = input.int(3, "D", minval=1)
lengthRSI = input.int(14, "RSI Length", minval=1)
lengthStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)
plot(k, "K", color=#2962FF)
plot(d, "D", color=#FF6D00)

d_k = d - k
smoothD_d = d - smoothD
smoothK_k = k - smoothK

h0 = hline(80, "Upper Band", color=#787B86)
hline(50, "Middle Band", color=color.new(#787B86, 50))
h1 = hline(20, "Lower Band", color=#787B86)
fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")
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
float op_operation = decision_tree_0_UPST_1Min_d016d0cc(Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow, rsi1, d, k, smoothD_d, d_k, smoothK_k)

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


