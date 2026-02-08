//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Money_Flow_Index
// ID_model: SNAP_1Min_2CM0_37bb30a6 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Min_2CM0_37bb30a6", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Min_37bb30a6(mf, ad, ad_mf, Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ad <= 21.9272 )
		if( Negative_Money_Flow <= 0.170428 )
			if( ad_mf <= -0.992971 )
				if( MFI_Low <= 49.2459 )
					if( Positive_Money_Flow_Sum <= 88055 )
						if( Raw_Money_Flow <= 18232.3 )
							if( Positive_Money_Flow_Sum <= 52163.2 )
								if( mf <= 0.282264 )
									ret := 0.462857
								if( mf > 0.282264 )
									ret := -0.230769
							if( Positive_Money_Flow_Sum > 52163.2 )
								if( ad_mf <= -859.507 )
									ret := 0.346154
								if( ad_mf > -859.507 )
									ret := 0.815217 // buy
						if( Raw_Money_Flow > 18232.3 )
							if( Negative_Money_Flow_Sum <= 46362.4 )
								if( Money_Flow_Ratio <= 1.79087 )
									ret := -1.000000 // sell
								if( Money_Flow_Ratio > 1.79087 )
									ret := -0.200000
							if( Negative_Money_Flow_Sum > 46362.4 )
								if( Negative_Money_Flow_Sum <= 180062 )
									ret := 0.488889
								if( Negative_Money_Flow_Sum > 180062 )
									ret := -0.277778
					if( Positive_Money_Flow_Sum > 88055 )
						if( Typical_Price <= 9.6816 )
							if( Raw_Money_Flow <= 16187.2 )
								if( Negative_Money_Flow_Sum <= 330139 )
									ret := -0.675000
								if( Negative_Money_Flow_Sum > 330139 )
									ret := 0.153846
							if( Raw_Money_Flow > 16187.2 )
								if( Raw_Money_Flow <= 933100 )
									ret := 0.062852
								if( Raw_Money_Flow > 933100 )
									ret := -0.192308
						if( Typical_Price > 9.6816 )
							if( Positive_Money_Flow <= 1.11981e+06 )
								if( MFI_High <= -18.6179 )
									ret := 0.139101
								if( MFI_High > -18.6179 )
									ret := 0.310902
							if( Positive_Money_Flow > 1.11981e+06 )
								if( Typical_Price <= 15.9917 )
									ret := 0.089744
								if( Typical_Price > 15.9917 )
									ret := -0.318182
				if( MFI_Low > 49.2459 )
					if( Raw_Money_Flow <= 140974 )
						if( Raw_Money_Flow <= 102252 )
							if( Positive_Money_Flow <= 4570.78 )
								if( Typical_Price <= 13.3585 )
									ret := 0.694444
								if( Typical_Price > 13.3585 )
									ret := 0.000000
							if( Positive_Money_Flow > 4570.78 )
								if( mf <= 0.528367 )
									ret := 0.035519
								if( mf > 0.528367 )
									ret := -0.433333
						if( Raw_Money_Flow > 102252 )
							if( Negative_Money_Flow_Sum <= 536990 )
								if( MFI <= 86.115 )
									ret := 0.800000 // buy
								if( MFI > 86.115 )
									ret := 0.090909
							if( Negative_Money_Flow_Sum > 536990 )
								if( mf <= -0.069933 )
									ret := 0.538462
								if( mf > -0.069933 )
									ret := -0.041667
					if( Raw_Money_Flow > 140974 )
						if( Positive_Money_Flow_Sum <= 2.06408e+07 )
							if( Positive_Money_Flow_Sum <= 3.55309e+06 )
								if( Positive_Money_Flow <= 2.10725e+06 )
									ret := -0.185294
								if( Positive_Money_Flow > 2.10725e+06 )
									ret := -0.935484 // sell
							if( Positive_Money_Flow_Sum > 3.55309e+06 )
								if( Negative_Money_Flow_Sum <= 6.74969e+06 )
									ret := -0.012808
								if( Negative_Money_Flow_Sum > 6.74969e+06 )
									ret := 0.857143 // buy
						if( Positive_Money_Flow_Sum > 2.06408e+07 )
							if( Positive_Money_Flow_Sum <= 2.74692e+07 )
								if( Positive_Money_Flow <= 1.18935e+06 )
									ret := -0.500000
								if( Positive_Money_Flow > 1.18935e+06 )
									ret := -0.823529 // sell
							if( Positive_Money_Flow_Sum > 2.74692e+07 )
								if( Typical_Price <= 14.5898 )
									ret := 0.428571
								if( Typical_Price > 14.5898 )
									ret := -0.609756
			if( ad_mf > -0.992971 )
				if( Raw_Money_Flow <= 5348.99 )
					if( Positive_Money_Flow <= 46.5133 )
						if( MFI <= 41.7909 )
							if( MFI_Low <= -9.18128 )
								if( Negative_Money_Flow_Sum <= 43013.7 )
									ret := -0.625000
								if( Negative_Money_Flow_Sum > 43013.7 )
									ret := 0.075269
							if( MFI_Low > -9.18128 )
								if( Typical_Price <= 9.725 )
									ret := 0.059459
								if( Typical_Price > 9.725 )
									ret := 0.281746
						if( MFI > 41.7909 )
							if( Positive_Money_Flow_Sum <= 19462.6 )
								if( ad_mf <= -0.007738 )
									ret := 0.722222 // buy
								if( ad_mf > -0.007738 )
									ret := 0.090909
							if( Positive_Money_Flow_Sum > 19462.6 )
								if( MFI_High <= -33.8883 )
									ret := -0.480769
								if( MFI_High > -33.8883 )
									ret := -0.074554
					if( Positive_Money_Flow > 46.5133 )
						if( Positive_Money_Flow_Sum <= 58478.9 )
							if( Negative_Money_Flow_Sum <= 80961.1 )
								if( Negative_Money_Flow_Sum <= 55233.2 )
									ret := -0.116203
								if( Negative_Money_Flow_Sum > 55233.2 )
									ret := -0.409326
							if( Negative_Money_Flow_Sum > 80961.1 )
								if( MFI <= 20.3436 )
									ret := -0.201613
								if( MFI > 20.3436 )
									ret := 0.193939
						if( Positive_Money_Flow_Sum > 58478.9 )
							if( Positive_Money_Flow_Sum <= 74147.7 )
								if( ad_mf <= -0.239167 )
									ret := 0.000000
								if( ad_mf > -0.239167 )
									ret := -0.567708
							if( Positive_Money_Flow_Sum > 74147.7 )
								if( Positive_Money_Flow <= 519.61 )
									ret := -0.809524 // sell
								if( Positive_Money_Flow > 519.61 )
									ret := -0.218720
				if( Raw_Money_Flow > 5348.99 )
					if( MFI <= 68.1653 )
						if( Positive_Money_Flow <= 6823.39 )
							if( MFI_Low <= 18.3312 )
								if( MFI <= 0.363592 )
									ret := -0.529412
								if( MFI > 0.363592 )
									ret := 0.007979
							if( MFI_Low > 18.3312 )
								if( Positive_Money_Flow <= 489.816 )
									ret := 0.108346
								if( Positive_Money_Flow > 489.816 )
									ret := 0.333333
						if( Positive_Money_Flow > 6823.39 )
							if( Positive_Money_Flow_Sum <= 1.28312e+07 )
								if( Positive_Money_Flow_Sum <= 1.36259e+06 )
									ret := -0.067460
								if( Positive_Money_Flow_Sum > 1.36259e+06 )
									ret := 0.042669
							if( Positive_Money_Flow_Sum > 1.28312e+07 )
								if( MFI <= 35.766 )
									ret := 0.375000
								if( MFI > 35.766 )
									ret := -0.341772
					if( MFI > 68.1653 )
						if( Positive_Money_Flow_Sum <= 28622 )
							if( MFI_High <= -6.67727 )
								ret := 0.000000
							if( MFI_High > -6.67727 )
								if( Money_Flow_Ratio <= 5.94993 )
									ret := -1.000000 // sell
								if( Money_Flow_Ratio > 5.94993 )
									ret := -0.500000
						if( Positive_Money_Flow_Sum > 28622 )
							if( Positive_Money_Flow_Sum <= 1.68618e+07 )
								if( ad_mf <= 0.073048 )
									ret := -0.105753
								if( ad_mf > 0.073048 )
									ret := 0.016502
							if( Positive_Money_Flow_Sum > 1.68618e+07 )
								if( Typical_Price <= 9.16879 )
									ret := -0.722222 // sell
								if( Typical_Price > 9.16879 )
									ret := -0.197080
		if( Negative_Money_Flow > 0.170428 )
			if( Raw_Money_Flow <= 76472.9 )
				if( Negative_Money_Flow_Sum <= 1.03333e+06 )
					if( ad <= -0.111261 )
						if( Raw_Money_Flow <= 5875.02 )
							if( MFI <= 11.2666 )
								if( Positive_Money_Flow_Sum <= 7809.96 )
									ret := 1.000000 // buy
								if( Positive_Money_Flow_Sum > 7809.96 )
									ret := -0.571429
							if( MFI > 11.2666 )
								if( MFI_Low <= 68.594 )
									ret := 0.759375 // buy
								if( MFI_Low > 68.594 )
									ret := 0.166667
						if( Raw_Money_Flow > 5875.02 )
							if( Positive_Money_Flow_Sum <= 1.04068e+06 )
								if( Negative_Money_Flow_Sum <= 485732 )
									ret := 0.403438
								if( Negative_Money_Flow_Sum > 485732 )
									ret := 0.629630
							if( Positive_Money_Flow_Sum > 1.04068e+06 )
								if( Positive_Money_Flow_Sum <= 1.39312e+06 )
									ret := -0.126437
								if( Positive_Money_Flow_Sum > 1.39312e+06 )
									ret := 0.381910
					if( ad > -0.111261 )
						if( MFI_High <= -21.7031 )
							if( Typical_Price <= 15.1072 )
								if( Negative_Money_Flow <= 9918.2 )
									ret := 0.417614
								if( Negative_Money_Flow > 9918.2 )
									ret := 0.225296
							if( Typical_Price > 15.1072 )
								if( MFI_Low <= -17.4396 )
									ret := -0.800000 // sell
								if( MFI_Low > -17.4396 )
									ret := 0.226075
						if( MFI_High > -21.7031 )
							if( Money_Flow_Ratio <= 1.71785 )
								if( Negative_Money_Flow_Sum <= 55456.5 )
									ret := -0.255474
								if( Negative_Money_Flow_Sum > 55456.5 )
									ret := 0.153846
							if( Money_Flow_Ratio > 1.71785 )
								if( Negative_Money_Flow <= 7634.67 )
									ret := 0.297038
								if( Negative_Money_Flow > 7634.67 )
									ret := 0.059621
				if( Negative_Money_Flow_Sum > 1.03333e+06 )
					if( Money_Flow_Ratio <= 0.146542 )
						if( mf <= 0.942027 )
							if( Positive_Money_Flow <= 6863.53 )
								if( Positive_Money_Flow <= 940.921 )
									ret := 0.275862
								if( Positive_Money_Flow > 940.921 )
									ret := -0.500000
							if( Positive_Money_Flow > 6863.53 )
								if( ad <= -1029.94 )
									ret := 0.500000
								if( ad > -1029.94 )
									ret := 1.000000 // buy
						if( mf > 0.942027 )
							if( Money_Flow_Ratio <= 0.002387 )
								ret := 0.666667
							if( Money_Flow_Ratio > 0.002387 )
								if( Typical_Price <= 9.87826 )
									ret := 0.750000 // buy
								if( Typical_Price > 9.87826 )
									ret := 1.000000 // buy
					if( Money_Flow_Ratio > 0.146542 )
						if( Negative_Money_Flow_Sum <= 5.42964e+06 )
							if( ad_mf <= -1263.88 )
								if( Negative_Money_Flow <= 29685 )
									ret := 0.353846
								if( Negative_Money_Flow > 29685 )
									ret := 0.036424
							if( ad_mf > -1263.88 )
								if( Positive_Money_Flow <= 34424.6 )
									ret := -0.083019
								if( Positive_Money_Flow > 34424.6 )
									ret := -1.000000 // sell
						if( Negative_Money_Flow_Sum > 5.42964e+06 )
							if( Positive_Money_Flow <= 20759.4 )
								if( Positive_Money_Flow <= 157.114 )
									ret := 0.181818
								if( Positive_Money_Flow > 157.114 )
									ret := -0.500000
							if( Positive_Money_Flow > 20759.4 )
								ret := 1.000000 // buy
			if( Raw_Money_Flow > 76472.9 )
				if( ad <= -731394 )
					if( mf <= -0.071828 )
						if( Typical_Price <= 14.6682 )
							if( Negative_Money_Flow_Sum <= 2.18717e+07 )
								ret := 0.500000
							if( Negative_Money_Flow_Sum > 2.18717e+07 )
								if( Negative_Money_Flow_Sum <= 4.43959e+07 )
									ret := 0.904762 // buy
								if( Negative_Money_Flow_Sum > 4.43959e+07 )
									ret := 1.000000 // buy
						if( Typical_Price > 14.6682 )
							ret := 0.500000
					if( mf > -0.071828 )
						ret := -0.250000
				if( ad > -731394 )
					if( Typical_Price <= 15.8648 )
						if( ad <= -22430.3 )
							if( mf <= -0.76773 )
								if( MFI <= 2.826 )
									ret := 0.400000
								if( MFI > 2.826 )
									ret := -0.809524 // sell
							if( mf > -0.76773 )
								if( MFI <= 87.224 )
									ret := 0.140721
								if( MFI > 87.224 )
									ret := -0.414634
						if( ad > -22430.3 )
							if( Negative_Money_Flow_Sum <= 538861 )
								if( MFI_High <= -69.8076 )
									ret := -0.291667
								if( MFI_High > -69.8076 )
									ret := 0.349112
							if( Negative_Money_Flow_Sum > 538861 )
								if( Negative_Money_Flow_Sum <= 1.13402e+07 )
									ret := 0.050769
								if( Negative_Money_Flow_Sum > 1.13402e+07 )
									ret := 0.251765
					if( Typical_Price > 15.8648 )
						if( MFI_High <= -34.8425 )
							if( mf <= -0.461061 )
								if( Negative_Money_Flow <= 479119 )
									ret := 0.130435
								if( Negative_Money_Flow > 479119 )
									ret := -0.659091
							if( mf > -0.461061 )
								if( MFI_Low <= -14.6846 )
									ret := 0.705882 // buy
								if( MFI_Low > -14.6846 )
									ret := 0.080645
						if( MFI_High > -34.8425 )
							if( Negative_Money_Flow <= 1.72343e+06 )
								if( Positive_Money_Flow <= 84301.9 )
									ret := -0.087411
								if( Positive_Money_Flow > 84301.9 )
									ret := 0.666667
							if( Negative_Money_Flow > 1.72343e+06 )
								if( Typical_Price <= 17.1678 )
									ret := 0.245614
								if( Typical_Price > 17.1678 )
									ret := -0.800000 // sell
	if( ad > 21.9272 )
		if( Positive_Money_Flow_Sum <= 1.07009e+06 )
			if( MFI_High <= -43.8735 )
				if( Positive_Money_Flow <= 2073.84 )
					if( Negative_Money_Flow <= 3.19679e+06 )
						if( Negative_Money_Flow_Sum <= 98025.4 )
							if( ad <= 405.69 )
								if( Negative_Money_Flow_Sum <= 61313 )
									ret := 0.000000
								if( Negative_Money_Flow_Sum > 61313 )
									ret := -0.909091 // sell
							if( ad > 405.69 )
								if( Typical_Price <= 15.5865 )
									ret := -0.016667
								if( Typical_Price > 15.5865 )
									ret := -1.000000 // sell
						if( Negative_Money_Flow_Sum > 98025.4 )
							if( Positive_Money_Flow_Sum <= 571048 )
								if( Negative_Money_Flow_Sum <= 124814 )
									ret := 0.682927
								if( Negative_Money_Flow_Sum > 124814 )
									ret := 0.154532
							if( Positive_Money_Flow_Sum > 571048 )
								if( Raw_Money_Flow <= 1.61226e+06 )
									ret := -0.059126
								if( Raw_Money_Flow > 1.61226e+06 )
									ret := 0.875000 // buy
					if( Negative_Money_Flow > 3.19679e+06 )
						if( Positive_Money_Flow_Sum <= 441580 )
							ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 441580 )
							ret := 0.285714
				if( Positive_Money_Flow > 2073.84 )
					if( Raw_Money_Flow <= 7592.56 )
						if( Negative_Money_Flow_Sum <= 247595 )
							if( mf <= -0.23909 )
								if( Negative_Money_Flow_Sum <= 102013 )
									ret := -0.800000 // sell
								if( Negative_Money_Flow_Sum > 102013 )
									ret := 0.153846
							if( mf > -0.23909 )
								if( Typical_Price <= 11.419 )
									ret := -0.906250 // sell
								if( Typical_Price > 11.419 )
									ret := -0.636364
						if( Negative_Money_Flow_Sum > 247595 )
							if( Negative_Money_Flow_Sum <= 254627 )
								ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 254627 )
								if( Positive_Money_Flow_Sum <= 214638 )
									ret := -0.444444
								if( Positive_Money_Flow_Sum > 214638 )
									ret := 0.666667
					if( Raw_Money_Flow > 7592.56 )
						if( Positive_Money_Flow_Sum <= 34637.8 )
							if( mf <= -0.092691 )
								if( Positive_Money_Flow <= 11318.7 )
									ret := 0.428571
								if( Positive_Money_Flow > 11318.7 )
									ret := -0.714286 // sell
							if( mf > -0.092691 )
								if( Typical_Price <= 9.7663 )
									ret := 0.470588
								if( Typical_Price > 9.7663 )
									ret := 0.952381 // buy
						if( Positive_Money_Flow_Sum > 34637.8 )
							if( Typical_Price <= 15.0767 )
								if( ad_mf <= 535.204 )
									ret := 0.321429
								if( ad_mf > 535.204 )
									ret := -0.203297
							if( Typical_Price > 15.0767 )
								if( Negative_Money_Flow_Sum <= 6.07479e+06 )
									ret := -0.006803
								if( Negative_Money_Flow_Sum > 6.07479e+06 )
									ret := 0.600000
			if( MFI_High > -43.8735 )
				if( Negative_Money_Flow <= 8.53824 )
					if( MFI_Low <= 48.3205 )
						if( Negative_Money_Flow_Sum <= 67892.4 )
							if( Positive_Money_Flow_Sum <= 20716.2 )
								if( Positive_Money_Flow <= 11310.1 )
									ret := -0.250000
								if( Positive_Money_Flow > 11310.1 )
									ret := 1.000000 // buy
							if( Positive_Money_Flow_Sum > 20716.2 )
								if( mf <= -0.390377 )
									ret := 0.750000 // buy
								if( mf > -0.390377 )
									ret := -0.513333
						if( Negative_Money_Flow_Sum > 67892.4 )
							if( Negative_Money_Flow_Sum <= 94642.5 )
								if( ad_mf <= 3639.42 )
									ret := 0.184713
								if( ad_mf > 3639.42 )
									ret := -0.666667
							if( Negative_Money_Flow_Sum > 94642.5 )
								if( Raw_Money_Flow <= 104788 )
									ret := -0.348066
								if( Raw_Money_Flow > 104788 )
									ret := -0.040323
					if( MFI_Low > 48.3205 )
						if( Typical_Price <= 15.1372 )
							if( ad <= 701.598 )
								if( mf <= 0.347248 )
									ret := -0.714286 // sell
								if( mf > 0.347248 )
									ret := -0.333333
							if( ad > 701.598 )
								if( Money_Flow_Ratio <= 7.43039 )
									ret := -0.286863
								if( Money_Flow_Ratio > 7.43039 )
									ret := -0.565574
						if( Typical_Price > 15.1372 )
							if( Negative_Money_Flow_Sum <= 15656.6 )
								if( Negative_Money_Flow_Sum <= 13916.8 )
									ret := -0.200000
								if( Negative_Money_Flow_Sum > 13916.8 )
									ret := 0.750000 // buy
							if( Negative_Money_Flow_Sum > 15656.6 )
								if( mf <= 0.275051 )
									ret := -0.567308
								if( mf > 0.275051 )
									ret := -0.813333 // sell
				if( Negative_Money_Flow > 8.53824 )
					if( Negative_Money_Flow_Sum <= 66672.3 )
						if( mf <= 0.143072 )
							if( Negative_Money_Flow_Sum <= 22205 )
								if( ad <= 485.922 )
									ret := 0.894737 // buy
								if( ad > 485.922 )
									ret := 0.125000
							if( Negative_Money_Flow_Sum > 22205 )
								if( Positive_Money_Flow_Sum <= 106217 )
									ret := -0.032787
								if( Positive_Money_Flow_Sum > 106217 )
									ret := -0.689655
						if( mf > 0.143072 )
							if( Typical_Price <= 9.47832 )
								if( mf <= 0.22808 )
									ret := -0.888889 // sell
								if( mf > 0.22808 )
									ret := 0.150000
							if( Typical_Price > 9.47832 )
								if( mf <= 0.646742 )
									ret := -0.742857 // sell
								if( mf > 0.646742 )
									ret := 0.000000
					if( Negative_Money_Flow_Sum > 66672.3 )
						if( Negative_Money_Flow_Sum <= 96371.2 )
							if( Raw_Money_Flow <= 29094.3 )
								if( mf <= 0.403052 )
									ret := 0.500000
								if( mf > 0.403052 )
									ret := -0.272727
							if( Raw_Money_Flow > 29094.3 )
								if( mf <= -0.025052 )
									ret := 0.700000 // buy
								if( mf > -0.025052 )
									ret := -0.466667
						if( Negative_Money_Flow_Sum > 96371.2 )
							if( Positive_Money_Flow_Sum <= 246414 )
								if( Positive_Money_Flow_Sum <= 98322.9 )
									ret := -0.058824
								if( Positive_Money_Flow_Sum > 98322.9 )
									ret := -0.535714
							if( Positive_Money_Flow_Sum > 246414 )
								if( mf <= 0.07715 )
									ret := -0.263158
								if( mf > 0.07715 )
									ret := 0.137097
		if( Positive_Money_Flow_Sum > 1.07009e+06 )
			if( MFI <= 64.2536 )
				if( Typical_Price <= 11.6975 )
					if( Money_Flow_Ratio <= 1.14086 )
						if( Positive_Money_Flow <= 5.54534e+06 )
							if( MFI_High <= -26.7455 )
								if( Negative_Money_Flow_Sum <= 3.75206e+07 )
									ret := -0.053497
								if( Negative_Money_Flow_Sum > 3.75206e+07 )
									ret := 0.388889
							if( MFI_High > -26.7455 )
								if( Positive_Money_Flow <= 142479 )
									ret := -0.750000 // sell
								if( Positive_Money_Flow > 142479 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow > 5.54534e+06 )
							if( ad_mf <= 602692 )
								if( Positive_Money_Flow <= 6.2684e+06 )
									ret := -0.750000 // sell
								if( Positive_Money_Flow > 6.2684e+06 )
									ret := -1.000000 // sell
							if( ad_mf > 602692 )
								ret := -0.142857
					if( Money_Flow_Ratio > 1.14086 )
						if( ad <= 19121.2 )
							if( Raw_Money_Flow <= 160461 )
								if( Money_Flow_Ratio <= 1.36091 )
									ret := 0.156425
								if( Money_Flow_Ratio > 1.36091 )
									ret := -0.130435
							if( Raw_Money_Flow > 160461 )
								if( Negative_Money_Flow_Sum <= 5.59655e+06 )
									ret := 0.184534
								if( Negative_Money_Flow_Sum > 5.59655e+06 )
									ret := 0.627119
						if( ad > 19121.2 )
							if( mf <= -0.163008 )
								if( Positive_Money_Flow <= 408535 )
									ret := -0.040000
								if( Positive_Money_Flow > 408535 )
									ret := -0.660000
							if( mf > -0.163008 )
								if( MFI_Low <= 34.6801 )
									ret := 0.172619
								if( MFI_Low > 34.6801 )
									ret := -0.030108
				if( Typical_Price > 11.6975 )
					if( Positive_Money_Flow_Sum <= 4.00906e+07 )
						if( Positive_Money_Flow_Sum <= 2.43671e+07 )
							if( Negative_Money_Flow_Sum <= 1.04951e+07 )
								if( Negative_Money_Flow_Sum <= 6.94111e+06 )
									ret := 0.050857
								if( Negative_Money_Flow_Sum > 6.94111e+06 )
									ret := 0.201652
							if( Negative_Money_Flow_Sum > 1.04951e+07 )
								if( Negative_Money_Flow <= 1.18459e+06 )
									ret := -0.118852
								if( Negative_Money_Flow > 1.18459e+06 )
									ret := 0.183391
						if( Positive_Money_Flow_Sum > 2.43671e+07 )
							if( MFI_Low <= 35.6516 )
								if( Typical_Price <= 15.1797 )
									ret := 0.710280 // buy
								if( Typical_Price > 15.1797 )
									ret := 0.000000
							if( MFI_Low > 35.6516 )
								if( mf <= 0.170586 )
									ret := 0.134615
								if( mf > 0.170586 )
									ret := -0.736842 // sell
					if( Positive_Money_Flow_Sum > 4.00906e+07 )
						if( Positive_Money_Flow_Sum <= 1.07954e+08 )
							if( Negative_Money_Flow_Sum <= 3.11789e+07 )
								ret := 0.200000
							if( Negative_Money_Flow_Sum > 3.11789e+07 )
								if( ad_mf <= 565484 )
									ret := -0.962963 // sell
								if( ad_mf > 565484 )
									ret := -0.500000
						if( Positive_Money_Flow_Sum > 1.07954e+08 )
							ret := 1.000000 // buy
			if( MFI > 64.2536 )
				if( Raw_Money_Flow <= 3.21695e+06 )
					if( Positive_Money_Flow_Sum <= 2.81907e+07 )
						if( Raw_Money_Flow <= 394234 )
							if( Negative_Money_Flow_Sum <= 3.78894e+06 )
								if( Negative_Money_Flow_Sum <= 860076 )
									ret := -0.024201
								if( Negative_Money_Flow_Sum > 860076 )
									ret := -0.144116
							if( Negative_Money_Flow_Sum > 3.78894e+06 )
								if( MFI_High <= -9.84205 )
									ret := -0.121212
								if( MFI_High > -9.84205 )
									ret := -0.835821 // sell
						if( Raw_Money_Flow > 394234 )
							if( Negative_Money_Flow_Sum <= 1.43683e+06 )
								if( Negative_Money_Flow_Sum <= 393084 )
									ret := -0.230415
								if( Negative_Money_Flow_Sum > 393084 )
									ret := 0.172253
							if( Negative_Money_Flow_Sum > 1.43683e+06 )
								if( Raw_Money_Flow <= 1.02821e+06 )
									ret := -0.131077
								if( Raw_Money_Flow > 1.02821e+06 )
									ret := 0.044762
					if( Positive_Money_Flow_Sum > 2.81907e+07 )
						if( Raw_Money_Flow <= 527835 )
							if( Positive_Money_Flow_Sum <= 2.93318e+07 )
								if( Typical_Price <= 11.0861 )
									ret := 1.000000 // buy
								if( Typical_Price > 11.0861 )
									ret := 0.400000
							if( Positive_Money_Flow_Sum > 2.93318e+07 )
								if( MFI_Low <= 69.4736 )
									ret := -0.555556
								if( MFI_Low > 69.4736 )
									ret := -0.047619
						if( Raw_Money_Flow > 527835 )
							if( Typical_Price <= 15.7517 )
								if( mf <= 0.049983 )
									ret := 0.083333
								if( mf > 0.049983 )
									ret := 0.842105 // buy
							if( Typical_Price > 15.7517 )
								if( ad <= 46113.2 )
									ret := 0.000000
								if( ad > 46113.2 )
									ret := -0.800000 // sell
				if( Raw_Money_Flow > 3.21695e+06 )
					if( Negative_Money_Flow_Sum <= 3.50824e+06 )
						if( MFI_High <= 17.6974 )
							if( Raw_Money_Flow <= 4.2667e+06 )
								if( ad <= 275399 )
									ret := -0.235294
								if( ad > 275399 )
									ret := -1.000000 // sell
							if( Raw_Money_Flow > 4.2667e+06 )
								if( Positive_Money_Flow <= 7.87187e+06 )
									ret := 0.354839
								if( Positive_Money_Flow > 7.87187e+06 )
									ret := 0.869565 // buy
						if( MFI_High > 17.6974 )
							if( ad <= 362459 )
								ret := -0.428571
							if( ad > 362459 )
								ret := -1.000000 // sell
					if( Negative_Money_Flow_Sum > 3.50824e+06 )
						if( mf <= -0.000475 )
							if( Raw_Money_Flow <= 1.29091e+07 )
								if( Typical_Price <= 14.2793 )
									ret := 0.666667
								if( Typical_Price > 14.2793 )
									ret := -0.600000
							if( Raw_Money_Flow > 1.29091e+07 )
								ret := 1.000000 // buy
						if( mf > -0.000475 )
							if( ad <= 77855.5 )
								if( Negative_Money_Flow_Sum <= 1.11328e+07 )
									ret := -0.424242
								if( Negative_Money_Flow_Sum > 1.11328e+07 )
									ret := 0.600000
							if( ad > 77855.5 )
								if( Typical_Price <= 14.512 )
									ret := -0.417722
								if( Typical_Price > 14.512 )
									ret := -0.753968 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Chaikin_Money_Flow 
 //@version=5
//indicator title="Chaikin Money Flow", shorttitle="CMF", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
var cumVol = 0.
cumVol += nz(volume)
if barstate.islast and cumVol == 0
    runtime.error("No volume is provided by the data vendor.")
length_CMF = input.int(20, minval=1)
ad = close==high and close==low or high==low ? 0 : ((2*close-low-high)/(high-low))*volume
mf = math.sum(ad, length_CMF) / math.sum(volume, length_CMF)
plot(mf, color=#43A047, title="MF")
hline(0, color=#787B86, title="Zero", linestyle=hline.style_dashed)


ad_mf = ad - mf

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
float op_operation = decision_tree_0_SNAP_1Min_37bb30a6(mf, ad, ad_mf, Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow)

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


