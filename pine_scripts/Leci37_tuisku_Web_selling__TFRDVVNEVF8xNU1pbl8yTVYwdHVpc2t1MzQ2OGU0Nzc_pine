//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Vortex_Indicator
// ID_model: LTCUSDT_15Min_2MV0_3468e477 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_LTCUSDT_15Min_2MV0_3468e477", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_LTCUSDT_15Min_3468e477(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Money_Flow_Ratio <= 0.799772 )
		if( Raw_Money_Flow <= 1.10648e+06 )
			if( Typical_Price <= 90.6653 )
				if( Positive_Money_Flow_Sum <= 9.47351e+06 )
					if( Positive_Money_Flow_Sum <= 7.50145e+06 )
						if( Negative_Money_Flow <= 502687 )
							if( Negative_Money_Flow_Sum <= 1.89308e+06 )
								if( Positive_Money_Flow <= 56400.7 )
									ret := 0.068208
								if( Positive_Money_Flow > 56400.7 )
									ret := -0.018203
							if( Negative_Money_Flow_Sum > 1.89308e+06 )
								if( Typical_Price <= 68.8527 )
									ret := 0.117941
								if( Typical_Price > 68.8527 )
									ret := 0.058513
						if( Negative_Money_Flow > 502687 )
							if( VIP <= 0.704073 )
								if( Money_Flow_Ratio <= 0.226857 )
									ret := 0.128205
								if( Money_Flow_Ratio > 0.226857 )
									ret := -0.166667
							if( VIP > 0.704073 )
								if( Positive_Money_Flow_Sum <= 725882 )
									ret := -0.235772
								if( Positive_Money_Flow_Sum > 725882 )
									ret := 0.191184
					if( Positive_Money_Flow_Sum > 7.50145e+06 )
						if( Typical_Price <= 84.391 )
							if( VIP <= 0.880828 )
								if( Positive_Money_Flow_Sum <= 8.94125e+06 )
									ret := 0.487805
								if( Positive_Money_Flow_Sum > 8.94125e+06 )
									ret := -0.588235
							if( VIP > 0.880828 )
								if( Raw_Money_Flow <= 384812 )
									ret := -0.142857
								if( Raw_Money_Flow > 384812 )
									ret := 0.695652
						if( Typical_Price > 84.391 )
							if( VIM <= 1.10913 )
								if( Negative_Money_Flow <= 257772 )
									ret := -0.555556
								if( Negative_Money_Flow > 257772 )
									ret := 0.166667
							if( VIM > 1.10913 )
								if( MFI <= 29.3057 )
									ret := 0.000000
								if( MFI > 29.3057 )
									ret := 0.827586 // buy
				if( Positive_Money_Flow_Sum > 9.47351e+06 )
					if( Negative_Money_Flow <= 448851 )
						if( Typical_Price <= 87.7517 )
							if( MFI_High <= -51.5235 )
								if( MFI_Low <= 3.9571 )
									ret := -0.250000
								if( MFI_Low > 3.9571 )
									ret := 1.000000 // buy
							if( MFI_High > -51.5235 )
								if( VIM <= 1.00889 )
									ret := 0.500000
								if( VIM > 1.00889 )
									ret := -0.766667 // sell
						if( Typical_Price > 87.7517 )
							if( VIP_VIM <= -0.108689 )
								if( MFI_Low <= 19.1208 )
									ret := 0.200000
								if( MFI_Low > 19.1208 )
									ret := 1.000000 // buy
							if( VIP_VIM > -0.108689 )
								ret := -0.750000 // sell
					if( Negative_Money_Flow > 448851 )
						if( Positive_Money_Flow_Sum <= 1.21153e+07 )
							if( Positive_Money_Flow_Sum <= 1.0645e+07 )
								if( MFI <= 38.908 )
									ret := 0.384615
								if( MFI > 38.908 )
									ret := -0.750000 // sell
							if( Positive_Money_Flow_Sum > 1.0645e+07 )
								if( MFI_Low <= 23.721 )
									ret := 1.000000 // buy
								if( MFI_Low > 23.721 )
									ret := 0.750000 // buy
						if( Positive_Money_Flow_Sum > 1.21153e+07 )
							if( Positive_Money_Flow <= 59441 )
								if( Negative_Money_Flow <= 869537 )
									ret := 0.500000
								if( Negative_Money_Flow > 869537 )
									ret := -0.500000
							if( Positive_Money_Flow > 59441 )
								ret := -1.000000 // sell
			if( Typical_Price > 90.6653 )
				if( Money_Flow_Ratio <= 0.650407 )
					if( Typical_Price <= 100.843 )
						if( VIM <= 1.17446 )
							if( Negative_Money_Flow_Sum <= 2.09583e+07 )
								if( Raw_Money_Flow <= 346371 )
									ret := 0.092920
								if( Raw_Money_Flow > 346371 )
									ret := -0.060804
							if( Negative_Money_Flow_Sum > 2.09583e+07 )
								if( Typical_Price <= 93.2673 )
									ret := 1.000000 // buy
								if( Typical_Price > 93.2673 )
									ret := 0.647059
						if( VIM > 1.17446 )
							if( Negative_Money_Flow_Sum <= 1.76778e+07 )
								if( Negative_Money_Flow_Sum <= 1.16925e+07 )
									ret := 0.094030
								if( Negative_Money_Flow_Sum > 1.16925e+07 )
									ret := 0.483333
							if( Negative_Money_Flow_Sum > 1.76778e+07 )
								if( Negative_Money_Flow_Sum <= 2.2069e+07 )
									ret := -0.589744
								if( Negative_Money_Flow_Sum > 2.2069e+07 )
									ret := 0.190476
					if( Typical_Price > 100.843 )
						if( VIP <= 0.924462 )
							if( Money_Flow_Ratio <= 0.635043 )
								if( Money_Flow_Ratio <= 0.167699 )
									ret := -0.888889 // sell
								if( Money_Flow_Ratio > 0.167699 )
									ret := -0.257143
							if( Money_Flow_Ratio > 0.635043 )
								ret := 0.571429
						if( VIP > 0.924462 )
							if( Negative_Money_Flow_Sum <= 7.11464e+06 )
								if( VIP_VIM <= -0.166033 )
									ret := -0.500000
								if( VIP_VIM > -0.166033 )
									ret := -0.033333
							if( Negative_Money_Flow_Sum > 7.11464e+06 )
								if( Negative_Money_Flow_Sum <= 1.30497e+07 )
									ret := 0.785714 // buy
								if( Negative_Money_Flow_Sum > 1.30497e+07 )
									ret := 0.000000
				if( Money_Flow_Ratio > 0.650407 )
					if( Raw_Money_Flow <= 142773 )
						if( VIM <= 1.11956 )
							if( Negative_Money_Flow_Sum <= 1.17914e+06 )
								ret := 0.500000
							if( Negative_Money_Flow_Sum > 1.17914e+06 )
								ret := 0.000000
						if( VIM > 1.11956 )
							if( Raw_Money_Flow <= 91999.5 )
								ret := 0.500000
							if( Raw_Money_Flow > 91999.5 )
								ret := 1.000000 // buy
					if( Raw_Money_Flow > 142773 )
						if( VIM <= 1.09556 )
							if( VIP_VIM <= -0.185037 )
								if( MFI_Low <= 23.1492 )
									ret := 0.722222 // buy
								if( MFI_Low > 23.1492 )
									ret := 0.076923
							if( VIP_VIM > -0.185037 )
								if( Positive_Money_Flow_Sum <= 6.77442e+06 )
									ret := -0.134513
								if( Positive_Money_Flow_Sum > 6.77442e+06 )
									ret := 0.254237
						if( VIM > 1.09556 )
							if( Negative_Money_Flow_Sum <= 1.30795e+07 )
								if( Negative_Money_Flow_Sum <= 1.23253e+07 )
									ret := -0.243421
								if( Negative_Money_Flow_Sum > 1.23253e+07 )
									ret := 0.500000
							if( Negative_Money_Flow_Sum > 1.30795e+07 )
								if( VIP_VIM <= -0.18759 )
									ret := -1.000000 // sell
								if( VIP_VIM > -0.18759 )
									ret := -0.500000
		if( Raw_Money_Flow > 1.10648e+06 )
			if( VIP <= 0.804989 )
				if( MFI_High <= -54.8997 )
					if( Raw_Money_Flow <= 8.46515e+06 )
						if( Positive_Money_Flow_Sum <= 2.71876e+06 )
							if( Typical_Price <= 98.5767 )
								if( Raw_Money_Flow <= 1.25496e+06 )
									ret := 0.026316
								if( Raw_Money_Flow > 1.25496e+06 )
									ret := 0.382166
							if( Typical_Price > 98.5767 )
								if( VIM <= 1.20892 )
									ret := -0.375000
								if( VIM > 1.20892 )
									ret := -0.857143 // sell
						if( Positive_Money_Flow_Sum > 2.71876e+06 )
							if( Typical_Price <= 99.7398 )
								if( MFI_Low <= 1.68599 )
									ret := 0.173307
								if( MFI_Low > 1.68599 )
									ret := -0.099602
							if( Typical_Price > 99.7398 )
								if( Negative_Money_Flow_Sum <= 4.91813e+07 )
									ret := -0.792453 // sell
								if( Negative_Money_Flow_Sum > 4.91813e+07 )
									ret := 1.000000 // buy
					if( Raw_Money_Flow > 8.46515e+06 )
						if( Negative_Money_Flow_Sum <= 4.23245e+07 )
							if( VIM <= 1.20207 )
								if( Typical_Price <= 93.2616 )
									ret := 1.000000 // buy
								if( Typical_Price > 93.2616 )
									ret := 0.750000 // buy
							if( VIM > 1.20207 )
								if( Negative_Money_Flow_Sum <= 2.41952e+07 )
									ret := -0.600000
								if( Negative_Money_Flow_Sum > 2.41952e+07 )
									ret := 0.900000 // buy
						if( Negative_Money_Flow_Sum > 4.23245e+07 )
							if( Raw_Money_Flow <= 1.42293e+07 )
								ret := 0.200000
							if( Raw_Money_Flow > 1.42293e+07 )
								ret := -1.000000 // sell
				if( MFI_High > -54.8997 )
					if( Typical_Price <= 47.7339 )
						if( Raw_Money_Flow <= 1.28822e+06 )
							ret := 0.400000
						if( Raw_Money_Flow > 1.28822e+06 )
							if( VIM <= 1.17262 )
								ret := -0.857143 // sell
							if( VIM > 1.17262 )
								ret := -0.285714
					if( Typical_Price > 47.7339 )
						if( Typical_Price <= 80.1259 )
							if( VIP <= 0.796757 )
								if( Positive_Money_Flow_Sum <= 1.78686e+07 )
									ret := 0.634204
								if( Positive_Money_Flow_Sum > 1.78686e+07 )
									ret := 0.942857 // buy
							if( VIP > 0.796757 )
								if( VIP <= 0.798419 )
									ret := -0.363636
								if( VIP > 0.798419 )
									ret := 0.477273
						if( Typical_Price > 80.1259 )
							if( Positive_Money_Flow <= 1.74559e+06 )
								if( Typical_Price <= 80.3023 )
									ret := -0.714286 // sell
								if( Typical_Price > 80.3023 )
									ret := 0.473945
							if( Positive_Money_Flow > 1.74559e+06 )
								if( Typical_Price <= 89.1433 )
									ret := 0.222222
								if( Typical_Price > 89.1433 )
									ret := -0.392857
			if( VIP > 0.804989 )
				if( Positive_Money_Flow_Sum <= 3.56566e+07 )
					if( Typical_Price <= 98.2636 )
						if( Money_Flow_Ratio <= 0.441207 )
							if( Positive_Money_Flow <= 1.79902e+06 )
								if( VIM <= 1.03454 )
									ret := -0.509091
								if( VIM > 1.03454 )
									ret := 0.005310
							if( Positive_Money_Flow > 1.79902e+06 )
								if( Raw_Money_Flow <= 2.14193e+06 )
									ret := 0.933333 // buy
								if( Raw_Money_Flow > 2.14193e+06 )
									ret := 0.222222
						if( Money_Flow_Ratio > 0.441207 )
							if( VIP_VIM <= -0.290966 )
								if( Negative_Money_Flow <= 2.2091e+06 )
									ret := 0.457143
								if( Negative_Money_Flow > 2.2091e+06 )
									ret := -0.312500
							if( VIP_VIM > -0.290966 )
								if( Negative_Money_Flow_Sum <= 2.13246e+07 )
									ret := 0.188693
								if( Negative_Money_Flow_Sum > 2.13246e+07 )
									ret := -0.108108
					if( Typical_Price > 98.2636 )
						if( Negative_Money_Flow_Sum <= 1.03437e+07 )
							if( Negative_Money_Flow <= 1.83053e+06 )
								if( Positive_Money_Flow <= 1.39412e+06 )
									ret := -0.148936
								if( Positive_Money_Flow > 1.39412e+06 )
									ret := 0.800000 // buy
							if( Negative_Money_Flow > 1.83053e+06 )
								if( Typical_Price <= 101.977 )
									ret := 0.444444
								if( Typical_Price > 101.977 )
									ret := 1.000000 // buy
						if( Negative_Money_Flow_Sum > 1.03437e+07 )
							if( VIM <= 1.08971 )
								if( Positive_Money_Flow_Sum <= 1.10578e+07 )
									ret := -0.754098 // sell
								if( Positive_Money_Flow_Sum > 1.10578e+07 )
									ret := -0.380952
							if( VIM > 1.08971 )
								if( Positive_Money_Flow <= 2.33425e+06 )
									ret := 0.044118
								if( Positive_Money_Flow > 2.33425e+06 )
									ret := -0.730769 // sell
				if( Positive_Money_Flow_Sum > 3.56566e+07 )
					ret := 1.000000 // buy
	if( Money_Flow_Ratio > 0.799772 )
		if( Positive_Money_Flow <= 257034 )
			if( Positive_Money_Flow_Sum <= 2.59006e+07 )
				if( MFI <= 67.5231 )
					if( Negative_Money_Flow_Sum <= 3.48358e+06 )
						if( VIP <= 0.868805 )
							if( Negative_Money_Flow_Sum <= 2.27267e+06 )
								if( Negative_Money_Flow_Sum <= 1.65089e+06 )
									ret := -0.087336
								if( Negative_Money_Flow_Sum > 1.65089e+06 )
									ret := -0.431373
							if( Negative_Money_Flow_Sum > 2.27267e+06 )
								if( Typical_Price <= 61.8034 )
									ret := 0.636364
								if( Typical_Price > 61.8034 )
									ret := -0.084211
						if( VIP > 0.868805 )
							if( Typical_Price <= 64.7183 )
								if( Negative_Money_Flow <= 193689 )
									ret := 0.052876
								if( Negative_Money_Flow > 193689 )
									ret := 0.199115
							if( Typical_Price > 64.7183 )
								if( Typical_Price <= 85.503 )
									ret := 0.026545
								if( Typical_Price > 85.503 )
									ret := -0.056854
					if( Negative_Money_Flow_Sum > 3.48358e+06 )
						if( Raw_Money_Flow <= 505090 )
							if( Negative_Money_Flow_Sum <= 3.94344e+06 )
								if( Negative_Money_Flow_Sum <= 3.69645e+06 )
									ret := 0.213158
								if( Negative_Money_Flow_Sum > 3.69645e+06 )
									ret := -0.154639
							if( Negative_Money_Flow_Sum > 3.94344e+06 )
								if( Typical_Price <= 88.1271 )
									ret := 0.293283
								if( Typical_Price > 88.1271 )
									ret := 0.093682
						if( Raw_Money_Flow > 505090 )
							if( MFI_High <= -15.1865 )
								if( Money_Flow_Ratio <= 1.67664 )
									ret := 0.067246
								if( Money_Flow_Ratio > 1.67664 )
									ret := -0.224913
							if( MFI_High > -15.1865 )
								if( Negative_Money_Flow <= 1.69183e+06 )
									ret := 0.419355
								if( Negative_Money_Flow > 1.69183e+06 )
									ret := -0.204545
				if( MFI > 67.5231 )
					if( Typical_Price <= 68.24 )
						if( Negative_Money_Flow <= 1.2333e+06 )
							if( Raw_Money_Flow <= 784263 )
								if( Positive_Money_Flow_Sum <= 9.09609e+06 )
									ret := -0.080560
								if( Positive_Money_Flow_Sum > 9.09609e+06 )
									ret := 0.383838
							if( Raw_Money_Flow > 784263 )
								if( VIM <= 0.872732 )
									ret := 0.096774
								if( VIM > 0.872732 )
									ret := 0.814815 // buy
						if( Negative_Money_Flow > 1.2333e+06 )
							if( VIM <= 0.7199 )
								if( Typical_Price <= 63.1017 )
									ret := -1.000000 // sell
								if( Typical_Price > 63.1017 )
									ret := 0.400000
							if( VIM > 0.7199 )
								if( Money_Flow_Ratio <= 2.30451 )
									ret := -0.400000
								if( Money_Flow_Ratio > 2.30451 )
									ret := -0.933333 // sell
					if( Typical_Price > 68.24 )
						if( Negative_Money_Flow_Sum <= 7.65474e+06 )
							if( Positive_Money_Flow_Sum <= 1.60993e+07 )
								if( Negative_Money_Flow <= 1.00309e+06 )
									ret := 0.038205
								if( Negative_Money_Flow > 1.00309e+06 )
									ret := -0.211896
							if( Positive_Money_Flow_Sum > 1.60993e+07 )
								if( VIP_VIM <= 0.434103 )
									ret := 0.512195
								if( VIP_VIM > 0.434103 )
									ret := 0.136000
						if( Negative_Money_Flow_Sum > 7.65474e+06 )
							if( Raw_Money_Flow <= 2.09916e+06 )
								if( MFI_Low <= 49.1076 )
									ret := -0.050000
								if( MFI_Low > 49.1076 )
									ret := -0.725000 // sell
							if( Raw_Money_Flow > 2.09916e+06 )
								if( VIP_VIM <= 0.314435 )
									ret := 0.875000 // buy
								if( VIP_VIM > 0.314435 )
									ret := 0.200000
			if( Positive_Money_Flow_Sum > 2.59006e+07 )
				if( Typical_Price <= 105.552 )
					if( Typical_Price <= 81.1917 )
						if( MFI_High <= -7.0919 )
							if( Typical_Price <= 79.7653 )
								if( Typical_Price <= 60.1546 )
									ret := 0.250000
								if( Typical_Price > 60.1546 )
									ret := -0.954545 // sell
							if( Typical_Price > 79.7653 )
								ret := 0.500000
						if( MFI_High > -7.0919 )
							if( Positive_Money_Flow_Sum <= 5.00523e+07 )
								if( VIP <= 1.35943 )
									ret := 1.000000 // buy
								if( VIP > 1.35943 )
									ret := 0.166667
							if( Positive_Money_Flow_Sum > 5.00523e+07 )
								if( VIP_VIM <= 0.798022 )
									ret := -1.000000 // sell
								if( VIP_VIM > 0.798022 )
									ret := -0.250000
					if( Typical_Price > 81.1917 )
						if( Typical_Price <= 95.0332 )
							if( Positive_Money_Flow_Sum <= 4.88061e+07 )
								if( VIP <= 1.1104 )
									ret := -0.500000
								if( VIP > 1.1104 )
									ret := 0.658824
							if( Positive_Money_Flow_Sum > 4.88061e+07 )
								if( Typical_Price <= 94.1678 )
									ret := -0.846154 // sell
								if( Typical_Price > 94.1678 )
									ret := 0.785714 // buy
						if( Typical_Price > 95.0332 )
							if( Negative_Money_Flow_Sum <= 9.49923e+06 )
								if( MFI_High <= -0.937027 )
									ret := -0.200000
								if( MFI_High > -0.937027 )
									ret := 0.583333
							if( Negative_Money_Flow_Sum > 9.49923e+06 )
								if( Negative_Money_Flow_Sum <= 3.24509e+07 )
									ret := 0.868132 // buy
								if( Negative_Money_Flow_Sum > 3.24509e+07 )
									ret := 0.307692
				if( Typical_Price > 105.552 )
					if( Positive_Money_Flow_Sum <= 3.47648e+07 )
						if( MFI <= 53.5059 )
							ret := -0.428571
						if( MFI > 53.5059 )
							if( VIP <= 1.20591 )
								if( Positive_Money_Flow_Sum <= 2.95086e+07 )
									ret := 0.500000
								if( Positive_Money_Flow_Sum > 2.95086e+07 )
									ret := 1.000000 // buy
							if( VIP > 1.20591 )
								ret := 0.200000
					if( Positive_Money_Flow_Sum > 3.47648e+07 )
						if( Positive_Money_Flow_Sum <= 5.17745e+07 )
							if( Raw_Money_Flow <= 4.76043e+06 )
								if( Positive_Money_Flow_Sum <= 4.22798e+07 )
									ret := -0.571429
								if( Positive_Money_Flow_Sum > 4.22798e+07 )
									ret := -1.000000 // sell
							if( Raw_Money_Flow > 4.76043e+06 )
								ret := 0.000000
						if( Positive_Money_Flow_Sum > 5.17745e+07 )
							ret := -1.000000 // sell
		if( Positive_Money_Flow > 257034 )
			if( Money_Flow_Ratio <= 15.0791 )
				if( Typical_Price <= 107.815 )
					if( Raw_Money_Flow <= 7.9129e+06 )
						if( Typical_Price <= 75.4491 )
							if( VIP_VIM <= 0.497596 )
								if( Raw_Money_Flow <= 1.42663e+06 )
									ret := 0.008632
								if( Raw_Money_Flow > 1.42663e+06 )
									ret := 0.183442
							if( VIP_VIM > 0.497596 )
								if( Positive_Money_Flow <= 1.25129e+06 )
									ret := -0.087362
								if( Positive_Money_Flow > 1.25129e+06 )
									ret := -0.374603
						if( Typical_Price > 75.4491 )
							if( Positive_Money_Flow_Sum <= 4.41314e+06 )
								if( VIP <= 1.07469 )
									ret := -0.196559
								if( VIP > 1.07469 )
									ret := -0.053440
							if( Positive_Money_Flow_Sum > 4.41314e+06 )
								if( VIP <= 0.929871 )
									ret := 0.213333
								if( VIP > 0.929871 )
									ret := -0.042758
					if( Raw_Money_Flow > 7.9129e+06 )
						if( MFI <= 69.6262 )
							if( Negative_Money_Flow_Sum <= 1.6827e+07 )
								ret := 0.000000
							if( Negative_Money_Flow_Sum > 1.6827e+07 )
								ret := -1.000000 // sell
						if( MFI > 69.6262 )
							if( VIP_VIM <= 0.88139 )
								if( Raw_Money_Flow <= 8.06994e+06 )
									ret := 0.250000
								if( Raw_Money_Flow > 8.06994e+06 )
									ret := 0.838235 // buy
							if( VIP_VIM > 0.88139 )
								if( Raw_Money_Flow <= 8.69294e+06 )
									ret := 0.500000
								if( Raw_Money_Flow > 8.69294e+06 )
									ret := -1.000000 // sell
				if( Typical_Price > 107.815 )
					if( Positive_Money_Flow <= 1.57154e+06 )
						if( Typical_Price <= 108.748 )
							ret := -0.800000 // sell
						if( Typical_Price > 108.748 )
							if( VIM <= 0.999349 )
								if( VIM <= 0.889781 )
									ret := 1.000000 // buy
								if( VIM > 0.889781 )
									ret := 0.750000 // buy
							if( VIM > 0.999349 )
								ret := -0.333333
					if( Positive_Money_Flow > 1.57154e+06 )
						if( VIM <= 0.925331 )
							if( Negative_Money_Flow_Sum <= 7.24682e+06 )
								ret := -0.166667
							if( Negative_Money_Flow_Sum > 7.24682e+06 )
								if( Money_Flow_Ratio <= 1.82308 )
									ret := -0.789474 // sell
								if( Money_Flow_Ratio > 1.82308 )
									ret := -1.000000 // sell
						if( VIM > 0.925331 )
							if( Positive_Money_Flow <= 1.73497e+06 )
								ret := -1.000000 // sell
							if( Positive_Money_Flow > 1.73497e+06 )
								if( VIP <= 1.04545 )
									ret := -0.100000
								if( VIP > 1.04545 )
									ret := -0.750000 // sell
			if( Money_Flow_Ratio > 15.0791 )
				if( Money_Flow_Ratio <= 127.392 )
					if( Positive_Money_Flow_Sum <= 4.79662e+06 )
						if( Negative_Money_Flow_Sum <= 178427 )
							if( Typical_Price <= 88.9098 )
								ret := 0.000000
							if( Typical_Price > 88.9098 )
								ret := 0.500000
						if( Negative_Money_Flow_Sum > 178427 )
							if( Money_Flow_Ratio <= 17.276 )
								ret := -0.200000
							if( Money_Flow_Ratio > 17.276 )
								ret := -1.000000 // sell
					if( Positive_Money_Flow_Sum > 4.79662e+06 )
						if( VIP_VIM <= 0.53593 )
							ret := -0.666667
						if( VIP_VIM > 0.53593 )
							if( Money_Flow_Ratio <= 21.554 )
								if( VIP_VIM <= 0.702339 )
									ret := 0.400000
								if( VIP_VIM > 0.702339 )
									ret := 0.800000 // buy
							if( Money_Flow_Ratio > 21.554 )
								if( Positive_Money_Flow_Sum <= 6.10557e+06 )
									ret := 0.888889 // buy
								if( Positive_Money_Flow_Sum > 6.10557e+06 )
									ret := 0.163636
				if( Money_Flow_Ratio > 127.392 )
					ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_LTCUSDT_15Min_3468e477(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, VIP, VIP_VIM, VIM)

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


