//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Money_Flow_Index
// ID_model: EPAM_15Min_2CM0_9b330aca Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_EPAM_15Min_2CM0_9b330aca", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_EPAM_15Min_9b330aca(mf, ad_mf, ad, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( Typical_Price <= 321.863 )
		if( Raw_Money_Flow <= 9.22990e+06 )
			if( Positive_Money_Flow <= 6.74453e+06 )
				if( Negative_Money_Flow_Sum <= 7.21409e+07 )
					if( MFI_High <= -35.9681 )
						if( Typical_Price <= 227.413 )
							if( MFI_High <= -73.7081 )
								if( mf <= 0.032758 )
									ret := 0.247706
								if( mf > 0.032758 )
									ret := 1.000000 // buy
							if( MFI_High > -73.7081 )
								if( ad_mf <= -5825.13 )
									ret := 0.016454
								if( ad_mf > -5825.13 )
									ret := -0.074167
						if( Typical_Price > 227.413 )
							if( MFI_High <= -37.5079 )
								if( Money_Flow_Ratio <= 0.1331 )
									ret := -0.160494
								if( Money_Flow_Ratio > 0.1331 )
									ret := 0.075147
							if( MFI_High > -37.5079 )
								if( Raw_Money_Flow <= 3.66127e+06 )
									ret := -0.167722
								if( Raw_Money_Flow > 3.66127e+06 )
									ret := -0.421488
					if( MFI_High > -35.9681 )
						if( Negative_Money_Flow <= 5.36146e+06 )
							if( Raw_Money_Flow <= 4.34703e+06 )
								if( Positive_Money_Flow <= 3.80583e+06 )
									ret := 0.031284
								if( Positive_Money_Flow > 3.80583e+06 )
									ret := 0.179758
							if( Raw_Money_Flow > 4.34703e+06 )
								if( mf <= 0.274828 )
									ret := -0.053748
								if( mf > 0.274828 )
									ret := -0.369565
						if( Negative_Money_Flow > 5.36146e+06 )
							if( MFI <= 59.805 )
								if( ad <= 24795.1 )
									ret := 0.401198
								if( ad > 24795.1 )
									ret := -0.588235
							if( MFI > 59.805 )
								if( mf <= 0.222223 )
									ret := -0.087464
								if( mf > 0.222223 )
									ret := 0.289855
				if( Negative_Money_Flow_Sum > 7.21409e+07 )
					if( ad_mf <= 13287.9 )
						if( MFI <= 14.6184 )
							if( MFI_High <= -70.4189 )
								if( ad_mf <= -3728.6 )
									ret := 0.706897 // buy
								if( ad_mf > -3728.6 )
									ret := 0.130802
							if( MFI_High > -70.4189 )
								if( Negative_Money_Flow_Sum <= 7.54717e+07 )
									ret := -0.324324
								if( Negative_Money_Flow_Sum > 7.54717e+07 )
									ret := 0.656028
						if( MFI > 14.6184 )
							if( ad_mf <= -17767.7 )
								if( Typical_Price <= 222.163 )
									ret := 0.217391
								if( Typical_Price > 222.163 )
									ret := -0.500000
							if( ad_mf > -17767.7 )
								if( Negative_Money_Flow_Sum <= 8.28436e+07 )
									ret := 0.335206
								if( Negative_Money_Flow_Sum > 8.28436e+07 )
									ret := 0.055497
					if( ad_mf > 13287.9 )
						if( Money_Flow_Ratio <= 0.387273 )
							if( Negative_Money_Flow_Sum <= 7.75426e+07 )
								if( Raw_Money_Flow <= 3.75351e+06 )
									ret := -0.818182 // sell
								if( Raw_Money_Flow > 3.75351e+06 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 7.75426e+07 )
								if( MFI_High <= -56.2955 )
									ret := -0.320000
								if( MFI_High > -56.2955 )
									ret := -0.827586 // sell
						if( Money_Flow_Ratio > 0.387273 )
							if( ad <= 20850.8 )
								if( MFI_Low <= 25.0206 )
									ret := 0.142857
								if( MFI_Low > 25.0206 )
									ret := 0.695652
							if( ad > 20850.8 )
								ret := -0.588235
			if( Positive_Money_Flow > 6.74453e+06 )
				if( Negative_Money_Flow_Sum <= 1.3632e+07 )
					if( Negative_Money_Flow_Sum <= 8.91478e+06 )
						if( ad <= 7310.33 )
							if( Negative_Money_Flow_Sum <= 6.84517e+06 )
								if( Positive_Money_Flow <= 7.68556e+06 )
									ret := -0.108108
								if( Positive_Money_Flow > 7.68556e+06 )
									ret := 0.622222
							if( Negative_Money_Flow_Sum > 6.84517e+06 )
								if( ad_mf <= -2.9e-05 )
									ret := -0.464286
								if( ad_mf > -2.9e-05 )
									ret := -0.904762 // sell
						if( ad > 7310.33 )
							if( Money_Flow_Ratio <= 6.46813 )
								if( Typical_Price <= 189.327 )
									ret := 0.380952
								if( Typical_Price > 189.327 )
									ret := 0.809524 // buy
							if( Money_Flow_Ratio > 6.46813 )
								if( Raw_Money_Flow <= 7.82436e+06 )
									ret := 0.571429
								if( Raw_Money_Flow > 7.82436e+06 )
									ret := -0.529412
					if( Negative_Money_Flow_Sum > 8.91478e+06 )
						if( Raw_Money_Flow <= 7.74175e+06 )
							if( Raw_Money_Flow <= 7.07768e+06 )
								if( ad <= 22464.3 )
									ret := 0.652174
								if( ad > 22464.3 )
									ret := 0.133333
							if( Raw_Money_Flow > 7.07768e+06 )
								if( ad_mf <= -0.079647 )
									ret := 0.444444
								if( ad_mf > -0.079647 )
									ret := 0.911111 // buy
						if( Raw_Money_Flow > 7.74175e+06 )
							if( Typical_Price <= 235.613 )
								if( Positive_Money_Flow <= 8.38954e+06 )
									ret := -0.352941
								if( Positive_Money_Flow > 8.38954e+06 )
									ret := 0.562500
							if( Typical_Price > 235.613 )
								if( Typical_Price <= 298.919 )
									ret := 0.911111 // buy
								if( Typical_Price > 298.919 )
									ret := 0.352941
				if( Negative_Money_Flow_Sum > 1.3632e+07 )
					if( MFI_High <= -7.58809 )
						if( Negative_Money_Flow_Sum <= 2.70373e+07 )
							if( MFI_Low <= 47.6135 )
								if( ad <= 18884.6 )
									ret := -0.072165
								if( ad > 18884.6 )
									ret := -0.508475
							if( MFI_Low > 47.6135 )
								ret := 0.769231 // buy
						if( Negative_Money_Flow_Sum > 2.70373e+07 )
							if( Positive_Money_Flow_Sum <= 4.51886e+07 )
								if( Negative_Money_Flow_Sum <= 1.08562e+08 )
									ret := 0.114504
								if( Negative_Money_Flow_Sum > 1.08562e+08 )
									ret := -0.666667
							if( Positive_Money_Flow_Sum > 4.51886e+07 )
								if( ad_mf <= 23188.8 )
									ret := 0.497674
								if( ad_mf > 23188.8 )
									ret := 0.016667
					if( MFI_High > -7.58809 )
						if( MFI <= 79.0162 )
							if( Money_Flow_Ratio <= 3.02981 )
								if( Positive_Money_Flow_Sum <= 7.76853e+07 )
									ret := 0.166667
								if( Positive_Money_Flow_Sum > 7.76853e+07 )
									ret := -0.666667
							if( Money_Flow_Ratio > 3.02981 )
								if( ad_mf <= 13220.4 )
									ret := -0.363636
								if( ad_mf > 13220.4 )
									ret := -0.913043 // sell
						if( MFI > 79.0162 )
							if( Positive_Money_Flow <= 7.80773e+06 )
								ret := -0.304348
							if( Positive_Money_Flow > 7.80773e+06 )
								ret := 0.500000
		if( Raw_Money_Flow > 9.22990e+06 )
			if( Money_Flow_Ratio <= 0.385589 )
				if( Positive_Money_Flow <= 1.16158e+07 )
					if( Negative_Money_Flow <= 1.58408e+07 )
						if( Negative_Money_Flow <= 1.37853e+07 )
							if( MFI <= 25.4042 )
								if( mf <= -0.448609 )
									ret := 0.857143 // buy
								if( mf > -0.448609 )
									ret := -0.010230
							if( MFI > 25.4042 )
								if( Raw_Money_Flow <= 1.1371e+07 )
									ret := 0.833333 // buy
								if( Raw_Money_Flow > 1.1371e+07 )
									ret := 1.000000 // buy
						if( Negative_Money_Flow > 1.37853e+07 )
							if( MFI_Low <= -1.44562 )
								if( Typical_Price <= 233.149 )
									ret := 0.368421
								if( Typical_Price > 233.149 )
									ret := -0.222222
							if( MFI_Low > -1.44562 )
								if( ad <= -33476.9 )
									ret := 0.095238
								if( ad > -33476.9 )
									ret := 0.702381 // buy
					if( Negative_Money_Flow > 1.58408e+07 )
						if( Typical_Price <= 314.232 )
							if( MFI_Low <= 3.78014 )
								if( ad <= 7579.94 )
									ret := -0.078431
								if( ad > 7579.94 )
									ret := 0.606061
							if( MFI_Low > 3.78014 )
								if( mf <= -0.249815 )
									ret := -0.902439 // sell
								if( mf > -0.249815 )
									ret := -0.012987
						if( Typical_Price > 314.232 )
							if( mf <= -0.17762 )
								ret := -1.000000 // sell
							if( mf > -0.17762 )
								ret := -0.666667
				if( Positive_Money_Flow > 1.16158e+07 )
					if( ad <= -6727.63 )
						ret := 0.076923
					if( ad > -6727.63 )
						if( Negative_Money_Flow_Sum <= 1.26482e+08 )
							ret := 0.230769
						if( Negative_Money_Flow_Sum > 1.26482e+08 )
							if( MFI_High <= -60.1159 )
								ret := -0.600000
							if( MFI_High > -60.1159 )
								ret := -1.000000 // sell
			if( Money_Flow_Ratio > 0.385589 )
				if( Raw_Money_Flow <= 1.16576e+07 )
					if( Money_Flow_Ratio <= 0.660269 )
						if( ad_mf <= -32457.5 )
							if( Positive_Money_Flow_Sum <= 1.13526e+07 )
								ret := 0.714286 // buy
							if( Positive_Money_Flow_Sum > 1.13526e+07 )
								ret := -0.200000
						if( ad_mf > -32457.5 )
							if( Negative_Money_Flow_Sum <= 4.19513e+07 )
								if( Negative_Money_Flow_Sum <= 3.68649e+07 )
									ret := -0.519231
								if( Negative_Money_Flow_Sum > 3.68649e+07 )
									ret := 0.421053
							if( Negative_Money_Flow_Sum > 4.19513e+07 )
								if( ad <= -5972.82 )
									ret := -0.977273 // sell
								if( ad > -5972.82 )
									ret := -0.616667
					if( Money_Flow_Ratio > 0.660269 )
						if( Positive_Money_Flow_Sum <= 7.76011e+07 )
							if( MFI <= 67.5708 )
								if( MFI_High <= -13.0259 )
									ret := 0.064655
								if( MFI_High > -13.0259 )
									ret := 0.785714 // buy
							if( MFI > 67.5708 )
								if( MFI_Low <= 52.7598 )
									ret := -0.742857 // sell
								if( MFI_Low > 52.7598 )
									ret := -0.052632
						if( Positive_Money_Flow_Sum > 7.76011e+07 )
							if( ad <= 6091.34 )
								if( Negative_Money_Flow <= 9.77817e+06 )
									ret := 0.017544
								if( Negative_Money_Flow > 9.77817e+06 )
									ret := -0.512821
							if( ad > 6091.34 )
								if( Positive_Money_Flow_Sum <= 1.40259e+08 )
									ret := -0.698925
								if( Positive_Money_Flow_Sum > 1.40259e+08 )
									ret := -0.153846
				if( Raw_Money_Flow > 1.16576e+07 )
					if( MFI_High <= 12.5841 )
						if( MFI <= 54.8278 )
							if( ad_mf <= 1076.98 )
								if( mf <= -0.095582 )
									ret := -0.139186
								if( mf > -0.095582 )
									ret := 0.043933
							if( ad_mf > 1076.98 )
								if( Negative_Money_Flow_Sum <= 7.59841e+07 )
									ret := -0.106719
								if( Negative_Money_Flow_Sum > 7.59841e+07 )
									ret := -0.481283
						if( MFI > 54.8278 )
							if( MFI_Low <= 37.3256 )
								if( Money_Flow_Ratio <= 1.27809 )
									ret := 0.172414
								if( Money_Flow_Ratio > 1.27809 )
									ret := 0.537037
							if( MFI_Low > 37.3256 )
								if( Positive_Money_Flow_Sum <= 2.51056e+07 )
									ret := 0.388889
								if( Positive_Money_Flow_Sum > 2.51056e+07 )
									ret := -0.004991
					if( MFI_High > 12.5841 )
						if( MFI <= 96.9633 )
							if( ad_mf <= -0.381771 )
								ret := -1.000000 // sell
							if( ad_mf > -0.381771 )
								if( Positive_Money_Flow_Sum <= 9.57014e+07 )
									ret := -0.793103 // sell
								if( Positive_Money_Flow_Sum > 9.57014e+07 )
									ret := -0.312500
						if( MFI > 96.9633 )
							ret := 0.636364
	if( Typical_Price > 321.863 )
		if( ad <= 16728.4 )
			if( Typical_Price <= 630.188 )
				if( Negative_Money_Flow_Sum <= 2.18027e+08 )
					if( Negative_Money_Flow_Sum <= 1.49129e+08 )
						if( mf <= -0.042503 )
							if( Money_Flow_Ratio <= 1.68828 )
								if( Money_Flow_Ratio <= 0.405901 )
									ret := -0.004863
								if( Money_Flow_Ratio > 0.405901 )
									ret := -0.181745
							if( Money_Flow_Ratio > 1.68828 )
								if( mf <= -0.170777 )
									ret := 0.481928
								if( mf > -0.170777 )
									ret := 0.021886
						if( mf > -0.042503 )
							if( Positive_Money_Flow_Sum <= 1.12072e+08 )
								if( MFI_Low <= 75.8628 )
									ret := 0.033184
								if( MFI_Low > 75.8628 )
									ret := -0.733333 // sell
							if( Positive_Money_Flow_Sum > 1.12072e+08 )
								if( mf <= 0.405504 )
									ret := -0.103933
								if( mf > 0.405504 )
									ret := -0.734513 // sell
					if( Negative_Money_Flow_Sum > 1.49129e+08 )
						if( Positive_Money_Flow_Sum <= 1.94487e+07 )
							if( ad <= 3065.01 )
								if( Negative_Money_Flow <= 1.2152e+06 )
									ret := 1.000000 // buy
								if( Negative_Money_Flow > 1.2152e+06 )
									ret := 0.777778 // buy
							if( ad > 3065.01 )
								ret := -0.818182 // sell
						if( Positive_Money_Flow_Sum > 1.94487e+07 )
							if( Money_Flow_Ratio <= 1.09279 )
								if( Positive_Money_Flow_Sum <= 1.22476e+08 )
									ret := -0.501577
								if( Positive_Money_Flow_Sum > 1.22476e+08 )
									ret := 0.692308
							if( Money_Flow_Ratio > 1.09279 )
								if( mf <= 0.013146 )
									ret := -1.000000 // sell
								if( mf > 0.013146 )
									ret := -0.687500
				if( Negative_Money_Flow_Sum > 2.18027e+08 )
					if( MFI <= 32.7268 )
						if( MFI <= 4.51402 )
							if( MFI <= 3.29747 )
								ret := 0.437500
							if( MFI > 3.29747 )
								ret := 1.000000 // buy
						if( MFI > 4.51402 )
							if( ad_mf <= -9542.31 )
								if( MFI <= 16.1916 )
									ret := 0.972973 // buy
								if( MFI > 16.1916 )
									ret := 0.368421
							if( ad_mf > -9542.31 )
								if( MFI <= 16.9287 )
									ret := 0.096154
								if( MFI > 16.9287 )
									ret := 0.773585 // buy
					if( MFI > 32.7268 )
						if( Positive_Money_Flow_Sum <= 2.66172e+08 )
							ret := -0.722222 // sell
						if( Positive_Money_Flow_Sum > 2.66172e+08 )
							ret := 0.428571
			if( Typical_Price > 630.188 )
				if( Negative_Money_Flow_Sum <= 5.43483e+07 )
					if( Money_Flow_Ratio <= 1.92708 )
						if( ad_mf <= -4684.57 )
							if( MFI <= 64.5783 )
								if( Positive_Money_Flow <= 1.77005e+06 )
									ret := -0.320755
								if( Positive_Money_Flow > 1.77005e+06 )
									ret := 0.000000
							if( MFI > 64.5783 )
								ret := -0.800000 // sell
						if( ad_mf > -4684.57 )
							if( Raw_Money_Flow <= 5.55296e+06 )
								if( Negative_Money_Flow_Sum <= 5.18627e+07 )
									ret := 0.041494
								if( Negative_Money_Flow_Sum > 5.18627e+07 )
									ret := 0.642857
							if( Raw_Money_Flow > 5.55296e+06 )
								if( MFI_High <= -29.888 )
									ret := -0.555556
								if( MFI_High > -29.888 )
									ret := -0.064516
					if( Money_Flow_Ratio > 1.92708 )
						if( Typical_Price <= 657.437 )
							if( Money_Flow_Ratio <= 12.1116 )
								if( MFI <= 84.6648 )
									ret := 0.190083
								if( MFI > 84.6648 )
									ret := 0.611111
							if( Money_Flow_Ratio > 12.1116 )
								ret := -0.384615
						if( Typical_Price > 657.437 )
							if( Negative_Money_Flow <= 1.74952e+06 )
								if( MFI_High <= -0.047804 )
									ret := -0.024390
								if( MFI_High > -0.047804 )
									ret := -0.416667
							if( Negative_Money_Flow > 1.74952e+06 )
								if( ad_mf <= -5372.63 )
									ret := 0.562500
								if( ad_mf > -5372.63 )
									ret := 0.000000
				if( Negative_Money_Flow_Sum > 5.43483e+07 )
					if( Money_Flow_Ratio <= 1.40141 )
						if( Positive_Money_Flow_Sum <= 2.83692e+08 )
							if( Money_Flow_Ratio <= 1.14413 )
								if( Raw_Money_Flow <= 1.48203e+07 )
									ret := -0.269231
								if( Raw_Money_Flow > 1.48203e+07 )
									ret := 0.021505
							if( Money_Flow_Ratio > 1.14413 )
								if( Positive_Money_Flow_Sum <= 1.90596e+08 )
									ret := -0.343750
								if( Positive_Money_Flow_Sum > 1.90596e+08 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 2.83692e+08 )
							ret := 1.000000 // buy
					if( Money_Flow_Ratio > 1.40141 )
						if( ad_mf <= -17591 )
							if( Raw_Money_Flow <= 4.01427e+07 )
								ret := 0.300000
							if( Raw_Money_Flow > 4.01427e+07 )
								ret := -0.444444
						if( ad_mf > -17591 )
							if( Negative_Money_Flow <= 31975.4 )
								if( Typical_Price <= 669.632 )
									ret := -0.100000
								if( Typical_Price > 669.632 )
									ret := -0.880000 // sell
							if( Negative_Money_Flow > 31975.4 )
								if( ad <= -12624.5 )
									ret := -0.733333 // sell
								if( ad > -12624.5 )
									ret := -0.959677 // sell
		if( ad > 16728.4 )
			if( Money_Flow_Ratio <= 6.29527 )
				if( MFI_High <= -6.84921 )
					if( Raw_Money_Flow <= 4.02807e+07 )
						if( Positive_Money_Flow_Sum <= 7.28184e+07 )
							if( Negative_Money_Flow <= 3.1993e+07 )
								if( Positive_Money_Flow <= 1.88488e+07 )
									ret := -0.033019
								if( Positive_Money_Flow > 1.88488e+07 )
									ret := -0.328859
							if( Negative_Money_Flow > 3.1993e+07 )
								if( MFI_High <= -50.9582 )
									ret := -1.000000 // sell
								if( MFI_High > -50.9582 )
									ret := -0.684211
						if( Positive_Money_Flow_Sum > 7.28184e+07 )
							if( mf <= 0.070344 )
								if( Positive_Money_Flow_Sum <= 1.43028e+08 )
									ret := -0.352941
								if( Positive_Money_Flow_Sum > 1.43028e+08 )
									ret := 0.393939
							if( mf > 0.070344 )
								if( Negative_Money_Flow_Sum <= 1.17224e+08 )
									ret := -0.516556
								if( Negative_Money_Flow_Sum > 1.17224e+08 )
									ret := -0.980392 // sell
					if( Raw_Money_Flow > 4.02807e+07 )
						if( MFI <= 47.3 )
							if( ad <= 56062.9 )
								if( Money_Flow_Ratio <= 0.618681 )
									ret := 1.000000 // buy
								if( Money_Flow_Ratio > 0.618681 )
									ret := 0.571429
							if( ad > 56062.9 )
								if( MFI <= 22.0207 )
									ret := -0.777778 // sell
								if( MFI > 22.0207 )
									ret := 0.782609 // buy
						if( MFI > 47.3 )
							if( Positive_Money_Flow_Sum <= 3.24302e+08 )
								if( mf <= 0.257487 )
									ret := -0.525000
								if( mf > 0.257487 )
									ret := 0.176471
							if( Positive_Money_Flow_Sum > 3.24302e+08 )
								ret := 0.812500 // buy
				if( MFI_High > -6.84921 )
					if( MFI_Low <= 64.208 )
						if( mf <= 0.327139 )
							if( Typical_Price <= 431.83 )
								if( ad_mf <= 19192.7 )
									ret := -0.875000 // sell
								if( ad_mf > 19192.7 )
									ret := -0.072289
							if( Typical_Price > 431.83 )
								if( Positive_Money_Flow_Sum <= 1.90881e+08 )
									ret := 0.714286 // buy
								if( Positive_Money_Flow_Sum > 1.90881e+08 )
									ret := 0.076923
						if( mf > 0.327139 )
							if( mf <= 0.434352 )
								if( MFI_High <= -0.768921 )
									ret := 1.000000 // buy
								if( MFI_High > -0.768921 )
									ret := 0.611111
							if( mf > 0.434352 )
								ret := 0.000000
					if( MFI_Low > 64.208 )
						ret := -0.400000
			if( Money_Flow_Ratio > 6.29527 )
				if( Negative_Money_Flow_Sum <= 4.36221e+07 )
					if( ad_mf <= 82315.3 )
						if( Positive_Money_Flow_Sum <= 3.28038e+08 )
							if( Typical_Price <= 489.899 )
								if( Raw_Money_Flow <= 1.31983e+07 )
									ret := 0.125000
								if( Raw_Money_Flow > 1.31983e+07 )
									ret := -0.813953 // sell
							if( Typical_Price > 489.899 )
								ret := 0.000000
						if( Positive_Money_Flow_Sum > 3.28038e+08 )
							ret := 0.466667
					if( ad_mf > 82315.3 )
						if( mf <= 0.30114 )
							ret := -0.900000 // sell
						if( mf > 0.30114 )
							ret := -1.000000 // sell
				if( Negative_Money_Flow_Sum > 4.36221e+07 )
					ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_EPAM_15Min_9b330aca(mf, ad_mf, ad, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

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


