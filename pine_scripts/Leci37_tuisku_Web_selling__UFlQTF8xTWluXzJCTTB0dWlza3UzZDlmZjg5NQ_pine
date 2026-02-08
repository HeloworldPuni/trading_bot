//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Money_Flow_Index
// ID_model: PYPL_1Min_2BM0_3d9ff895 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PYPL_1Min_2BM0_3d9ff895", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PYPL_1Min_3d9ff895(bearPower, bbm, bbp, bullPower, BBPower_Color, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( bearPower <= 0.024444 )
		if( Raw_Money_Flow <= 145440 )
			if( bbp <= -0.021202 )
				if( Negative_Money_Flow <= 110.142 )
					if( bbp <= -0.066806 )
						if( Money_Flow_Ratio <= 0.603454 )
							if( MFI_Low <= -10.4463 )
								if( MFI <= 4.73895 )
									ret := 0.133333
								if( MFI > 4.73895 )
									ret := -0.419355
							if( MFI_Low > -10.4463 )
								if( Positive_Money_Flow <= 77790.7 )
									ret := 0.339492
								if( Positive_Money_Flow > 77790.7 )
									ret := 0.630137
						if( Money_Flow_Ratio > 0.603454 )
							if( Money_Flow_Ratio <= 1.39328 )
								if( Negative_Money_Flow_Sum <= 248564 )
									ret := 0.279070
								if( Negative_Money_Flow_Sum > 248564 )
									ret := -0.161290
							if( Money_Flow_Ratio > 1.39328 )
								if( Raw_Money_Flow <= 20534 )
									ret := 0.595238
								if( Raw_Money_Flow > 20534 )
									ret := 0.129630
					if( bbp > -0.066806 )
						if( bearPower <= -0.030685 )
							if( MFI_Low <= 53.4812 )
								if( Negative_Money_Flow_Sum <= 575928 )
									ret := -0.097087
								if( Negative_Money_Flow_Sum > 575928 )
									ret := 0.194444
							if( MFI_Low > 53.4812 )
								if( Positive_Money_Flow <= 24678.3 )
									ret := 0.000000
								if( Positive_Money_Flow > 24678.3 )
									ret := -0.709677 // sell
						if( bearPower > -0.030685 )
							if( MFI <= 19.2359 )
								if( Positive_Money_Flow <= 82592.8 )
									ret := -0.102564
								if( Positive_Money_Flow > 82592.8 )
									ret := -1.000000 // sell
							if( MFI > 19.2359 )
								if( Negative_Money_Flow_Sum <= 48393 )
									ret := 0.875000 // buy
								if( Negative_Money_Flow_Sum > 48393 )
									ret := 0.169145
				if( Negative_Money_Flow > 110.142 )
					if( MFI <= 44.5242 )
						if( Money_Flow_Ratio <= 0.629344 )
							if( Positive_Money_Flow_Sum <= 306975 )
								if( MFI <= 30.8824 )
									ret := 0.226667
								if( MFI > 30.8824 )
									ret := 0.436364
							if( Positive_Money_Flow_Sum > 306975 )
								if( Raw_Money_Flow <= 7577.84 )
									ret := -0.043478
								if( Raw_Money_Flow > 7577.84 )
									ret := 0.624769
						if( Money_Flow_Ratio > 0.629344 )
							if( Negative_Money_Flow <= 37979.2 )
								if( bbp <= -0.037658 )
									ret := 0.330357
								if( bbp > -0.037658 )
									ret := -0.285714
							if( Negative_Money_Flow > 37979.2 )
								if( Negative_Money_Flow_Sum <= 296328 )
									ret := -0.555556
								if( Negative_Money_Flow_Sum > 296328 )
									ret := 0.066116
					if( MFI > 44.5242 )
						if( bearPower <= -0.144718 )
							if( Negative_Money_Flow <= 14147.6 )
								if( MFI_High <= -24.9086 )
									ret := -0.214286
								if( MFI_High > -24.9086 )
									ret := 0.729730 // buy
							if( Negative_Money_Flow > 14147.6 )
								if( Negative_Money_Flow <= 53334.1 )
									ret := 0.873134 // buy
								if( Negative_Money_Flow > 53334.1 )
									ret := 0.567164
						if( bearPower > -0.144718 )
							if( Negative_Money_Flow_Sum <= 301050 )
								if( Negative_Money_Flow <= 6428.06 )
									ret := 0.884615 // buy
								if( Negative_Money_Flow > 6428.06 )
									ret := 0.495441
							if( Negative_Money_Flow_Sum > 301050 )
								if( MFI <= 91.6744 )
									ret := 0.283937
								if( MFI > 91.6744 )
									ret := 0.659341
			if( bbp > -0.021202 )
				if( BBPower_Color <= 0.5 )
					if( MFI_Low <= 2.71566 )
						if( bbp <= 0.046075 )
							if( bbp <= -0.012882 )
								if( Raw_Money_Flow <= 16882 )
									ret := -0.100000
								if( Raw_Money_Flow > 16882 )
									ret := 0.294118
							if( bbp > -0.012882 )
								if( Raw_Money_Flow <= 48478.7 )
									ret := -0.305785
								if( Raw_Money_Flow > 48478.7 )
									ret := 0.181818
						if( bbp > 0.046075 )
							if( Positive_Money_Flow <= 64682 )
								ret := -1.000000 // sell
							if( Positive_Money_Flow > 64682 )
								ret := -0.500000
					if( MFI_Low > 2.71566 )
						if( Positive_Money_Flow_Sum <= 360489 )
							if( Raw_Money_Flow <= 19390.6 )
								if( Negative_Money_Flow_Sum <= 103761 )
									ret := 0.584615
								if( Negative_Money_Flow_Sum > 103761 )
									ret := 0.148026
							if( Raw_Money_Flow > 19390.6 )
								if( Positive_Money_Flow_Sum <= 153483 )
									ret := 0.333333
								if( Positive_Money_Flow_Sum > 153483 )
									ret := -0.057007
						if( Positive_Money_Flow_Sum > 360489 )
							if( Positive_Money_Flow <= 25138.2 )
								if( Typical_Price <= 66.2982 )
									ret := 0.224747
								if( Typical_Price > 66.2982 )
									ret := 0.566667
							if( Positive_Money_Flow > 25138.2 )
								if( bbm <= 0.021137 )
									ret := 0.250000
								if( bbm > 0.021137 )
									ret := -0.115385
				if( BBPower_Color > 0.5 )
					if( Negative_Money_Flow <= 9948.53 )
						if( bbp <= 0.080758 )
							if( bullPower <= 0.12322 )
								if( bbm <= 0.181648 )
									ret := -0.017146
								if( bbm > 0.181648 )
									ret := 1.000000 // buy
							if( bullPower > 0.12322 )
								if( Raw_Money_Flow <= 54606.9 )
									ret := -0.750000 // sell
								if( Raw_Money_Flow > 54606.9 )
									ret := -1.000000 // sell
						if( bbp > 0.080758 )
							if( Negative_Money_Flow_Sum <= 768404 )
								if( Negative_Money_Flow_Sum <= 613356 )
									ret := -0.230769
								if( Negative_Money_Flow_Sum > 613356 )
									ret := 0.500000
							if( Negative_Money_Flow_Sum > 768404 )
								if( Typical_Price <= 63.4683 )
									ret := -0.517241
								if( Typical_Price > 63.4683 )
									ret := -0.904762 // sell
					if( Negative_Money_Flow > 9948.53 )
						if( Money_Flow_Ratio <= 63.9802 )
							if( Positive_Money_Flow_Sum <= 140771 )
								if( bullPower <= 0.044502 )
									ret := 0.246575
								if( bullPower > 0.044502 )
									ret := 1.000000 // buy
							if( Positive_Money_Flow_Sum > 140771 )
								if( Positive_Money_Flow_Sum <= 363789 )
									ret := -0.068841
								if( Positive_Money_Flow_Sum > 363789 )
									ret := 0.139860
						if( Money_Flow_Ratio > 63.9802 )
							if( bbp <= 0.047418 )
								if( bearPower <= -0.001014 )
									ret := 0.500000
								if( bearPower > -0.001014 )
									ret := 0.000000
							if( bbp > 0.047418 )
								ret := 1.000000 // buy
		if( Raw_Money_Flow > 145440 )
			if( Negative_Money_Flow <= 1.05512e+06 )
				if( Positive_Money_Flow <= 5.43516e+07 )
					if( Negative_Money_Flow_Sum <= 2.07589e+06 )
						if( BBPower_Color <= 0.5 )
							if( MFI_High <= -53.468 )
								if( Raw_Money_Flow <= 230508 )
									ret := -0.210145
								if( Raw_Money_Flow > 230508 )
									ret := 0.253521
							if( MFI_High > -53.468 )
								if( Typical_Price <= 71.2629 )
									ret := 0.348866
								if( Typical_Price > 71.2629 )
									ret := -0.015267
						if( BBPower_Color > 0.5 )
							if( bullPower <= 0.400457 )
								if( Positive_Money_Flow_Sum <= 1.69791e+07 )
									ret := 0.024242
								if( Positive_Money_Flow_Sum > 1.69791e+07 )
									ret := -0.475000
							if( bullPower > 0.400457 )
								if( Negative_Money_Flow_Sum <= 1.25775e+06 )
									ret := 0.634146
								if( Negative_Money_Flow_Sum > 1.25775e+06 )
									ret := -1.000000 // sell
					if( Negative_Money_Flow_Sum > 2.07589e+06 )
						if( bbm <= 0.095307 )
							if( Positive_Money_Flow_Sum <= 2.96088e+07 )
								if( Positive_Money_Flow_Sum <= 1.886e+07 )
									ret := 0.011125
								if( Positive_Money_Flow_Sum > 1.886e+07 )
									ret := -0.197970
							if( Positive_Money_Flow_Sum > 2.96088e+07 )
								if( Positive_Money_Flow <= 8.77004e+06 )
									ret := 0.231504
								if( Positive_Money_Flow > 8.77004e+06 )
									ret := -0.238095
						if( bbm > 0.095307 )
							if( Positive_Money_Flow_Sum <= 3.97841e+06 )
								if( bbp <= -0.228697 )
									ret := 0.127273
								if( bbp > -0.228697 )
									ret := -0.318471
							if( Positive_Money_Flow_Sum > 3.97841e+06 )
								if( Negative_Money_Flow <= 534.953 )
									ret := 0.077437
								if( Negative_Money_Flow > 534.953 )
									ret := 0.320084
				if( Positive_Money_Flow > 5.43516e+07 )
					if( bbm <= 0.030471 )
						if( Raw_Money_Flow <= 6.50872e+07 )
							ret := 0.000000
						if( Raw_Money_Flow > 6.50872e+07 )
							if( Negative_Money_Flow_Sum <= 3.27885e+07 )
								ret := -0.833333 // sell
							if( Negative_Money_Flow_Sum > 3.27885e+07 )
								if( MFI <= 70.6626 )
									ret := -0.500000
								if( MFI > 70.6626 )
									ret := -0.250000
					if( bbm > 0.030471 )
						if( Typical_Price <= 71.8498 )
							if( Typical_Price <= 60.2422 )
								ret := -0.750000 // sell
							if( Typical_Price > 60.2422 )
								ret := -1.000000 // sell
						if( Typical_Price > 71.8498 )
							ret := -0.571429
			if( Negative_Money_Flow > 1.05512e+06 )
				if( Negative_Money_Flow_Sum <= 2.86622e+07 )
					if( Positive_Money_Flow_Sum <= 1.51641e+07 )
						if( bullPower <= -0.261807 )
							if( Negative_Money_Flow_Sum <= 1.92875e+07 )
								if( MFI_Low <= 10.3614 )
									ret := 0.500000
								if( MFI_Low > 10.3614 )
									ret := -0.750000 // sell
							if( Negative_Money_Flow_Sum > 1.92875e+07 )
								if( bbm <= 0.191967 )
									ret := -0.769231 // sell
								if( bbm > 0.191967 )
									ret := -1.000000 // sell
						if( bullPower > -0.261807 )
							if( Raw_Money_Flow <= 1.05763e+07 )
								if( bbm <= 0.382708 )
									ret := 0.108974
								if( bbm > 0.382708 )
									ret := -0.400000
							if( Raw_Money_Flow > 1.05763e+07 )
								if( bearPower <= -0.03403 )
									ret := -0.410526
								if( bearPower > -0.03403 )
									ret := 0.666667
					if( Positive_Money_Flow_Sum > 1.51641e+07 )
						if( Positive_Money_Flow_Sum <= 3.37798e+07 )
							if( MFI_High <= -38.3023 )
								if( Negative_Money_Flow <= 4.01758e+06 )
									ret := -0.588889
								if( Negative_Money_Flow > 4.01758e+06 )
									ret := 0.291667
							if( MFI_High > -38.3023 )
								if( MFI <= 56.6192 )
									ret := 0.117457
								if( MFI > 56.6192 )
									ret := -0.094198
						if( Positive_Money_Flow_Sum > 3.37798e+07 )
							if( Negative_Money_Flow_Sum <= 2.75386e+07 )
								if( Money_Flow_Ratio <= 7.88182 )
									ret := 0.431373
								if( Money_Flow_Ratio > 7.88182 )
									ret := -0.636364
							if( Negative_Money_Flow_Sum > 2.75386e+07 )
								if( Raw_Money_Flow <= 2.77754e+06 )
									ret := 0.142857
								if( Raw_Money_Flow > 2.77754e+06 )
									ret := -0.866667 // sell
				if( Negative_Money_Flow_Sum > 2.86622e+07 )
					if( MFI <= 46.4518 )
						if( Negative_Money_Flow_Sum <= 8.9827e+07 )
							if( bearPower <= -0.661936 )
								if( MFI <= 4.29383 )
									ret := -0.866667 // sell
								if( MFI > 4.29383 )
									ret := -0.176471
							if( bearPower > -0.661936 )
								if( Money_Flow_Ratio <= 0.650982 )
									ret := 0.199214
								if( Money_Flow_Ratio > 0.650982 )
									ret := 0.494624
						if( Negative_Money_Flow_Sum > 8.9827e+07 )
							if( bbm <= 0.057221 )
								if( Typical_Price <= 71.265 )
									ret := -0.565217
								if( Typical_Price > 71.265 )
									ret := 0.416667
							if( bbm > 0.057221 )
								if( MFI_High <= -37.2414 )
									ret := 0.669811
								if( MFI_High > -37.2414 )
									ret := -1.000000 // sell
					if( MFI > 46.4518 )
						if( Typical_Price <= 72.6442 )
							if( bearPower <= -0.117778 )
								if( Typical_Price <= 62.6537 )
									ret := 0.363636
								if( Typical_Price > 62.6537 )
									ret := -0.629310
							if( bearPower > -0.117778 )
								if( Negative_Money_Flow_Sum <= 2.99047e+07 )
									ret := -0.714286 // sell
								if( Negative_Money_Flow_Sum > 2.99047e+07 )
									ret := 0.233010
						if( Typical_Price > 72.6442 )
							if( Raw_Money_Flow <= 7.59661e+06 )
								if( MFI_Low <= 27.2325 )
									ret := 0.000000
								if( MFI_Low > 27.2325 )
									ret := 0.825000 // buy
							if( Raw_Money_Flow > 7.59661e+06 )
								if( MFI_High <= -26.8504 )
									ret := 0.500000
								if( MFI_High > -26.8504 )
									ret := -0.250000
	if( bearPower > 0.024444 )
		if( Raw_Money_Flow <= 210633 )
			if( bbp <= 0.161757 )
				if( BBPower_Color <= 0.5 )
					if( MFI_High <= -7.55865 )
						if( bbm <= 1.6e-05 )
							if( Positive_Money_Flow_Sum <= 798127 )
								if( Negative_Money_Flow_Sum <= 904630 )
									ret := -0.141414
								if( Negative_Money_Flow_Sum > 904630 )
									ret := 0.625000
							if( Positive_Money_Flow_Sum > 798127 )
								if( bbp <= 0.06111 )
									ret := -0.500000
								if( bbp > 0.06111 )
									ret := -1.000000 // sell
						if( bbm > 1.6e-05 )
							if( Negative_Money_Flow_Sum <= 3.417e+06 )
								if( Typical_Price <= 67.6983 )
									ret := 0.102564
								if( Typical_Price > 67.6983 )
									ret := 0.743590 // buy
							if( Negative_Money_Flow_Sum > 3.417e+06 )
								ret := -1.000000 // sell
					if( MFI_High > -7.55865 )
						if( Raw_Money_Flow <= 73769.9 )
							if( MFI_High <= -3.76921 )
								if( Money_Flow_Ratio <= 3.1758 )
									ret := 0.680000
								if( Money_Flow_Ratio > 3.1758 )
									ret := -1.000000 // sell
							if( MFI_High > -3.76921 )
								if( Positive_Money_Flow_Sum <= 4.408e+06 )
									ret := 0.892857 // buy
								if( Positive_Money_Flow_Sum > 4.408e+06 )
									ret := -0.200000
						if( Raw_Money_Flow > 73769.9 )
							if( MFI_High <= -3.27357 )
								ret := 1.000000 // buy
							if( MFI_High > -3.27357 )
								if( Negative_Money_Flow_Sum <= 194425 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow_Sum > 194425 )
									ret := 0.333333
				if( BBPower_Color > 0.5 )
					if( Positive_Money_Flow <= 15665.3 )
						if( Positive_Money_Flow <= 14.7809 )
							if( Positive_Money_Flow_Sum <= 80094.1 )
								if( Negative_Money_Flow <= 3153 )
									ret := 0.000000
								if( Negative_Money_Flow > 3153 )
									ret := 0.684211
							if( Positive_Money_Flow_Sum > 80094.1 )
								if( bearPower <= 0.044299 )
									ret := -0.078998
								if( bearPower > 0.044299 )
									ret := -0.223278
						if( Positive_Money_Flow > 14.7809 )
							if( Positive_Money_Flow_Sum <= 574889 )
								if( Negative_Money_Flow_Sum <= 92422.5 )
									ret := -0.015385
								if( Negative_Money_Flow_Sum > 92422.5 )
									ret := -0.452381
							if( Positive_Money_Flow_Sum > 574889 )
								if( Positive_Money_Flow_Sum <= 650686 )
									ret := 0.393939
								if( Positive_Money_Flow_Sum > 650686 )
									ret := -0.220513
					if( Positive_Money_Flow > 15665.3 )
						if( MFI <= 40.2274 )
							if( bearPower <= 0.069904 )
								if( bbm <= 0.052262 )
									ret := -0.165414
								if( bbm > 0.052262 )
									ret := -0.909091 // sell
							if( bearPower > 0.069904 )
								if( Typical_Price <= 64.288 )
									ret := -1.000000 // sell
								if( Typical_Price > 64.288 )
									ret := -0.541667
						if( MFI > 40.2274 )
							if( MFI_High <= -38.1979 )
								if( bearPower <= 0.04298 )
									ret := 0.800000 // buy
								if( bearPower > 0.04298 )
									ret := -0.041667
							if( MFI_High > -38.1979 )
								if( Typical_Price <= 61.0086 )
									ret := -0.225410
								if( Typical_Price > 61.0086 )
									ret := 0.003444
			if( bbp > 0.161757 )
				if( Typical_Price <= 68.7214 )
					if( Positive_Money_Flow <= 695.106 )
						if( Typical_Price <= 60.955 )
							if( MFI <= 46.1596 )
								if( bullPower <= 0.121171 )
									ret := -1.000000 // sell
								if( bullPower > 0.121171 )
									ret := -0.500000
							if( MFI > 46.1596 )
								if( MFI <= 66.9156 )
									ret := 0.000000
								if( MFI > 66.9156 )
									ret := -0.645833
						if( Typical_Price > 60.955 )
							if( bbm <= 0.17225 )
								if( Typical_Price <= 62.69 )
									ret := 0.265625
								if( Typical_Price > 62.69 )
									ret := -0.186528
							if( bbm > 0.17225 )
								ret := 1.000000 // buy
					if( Positive_Money_Flow > 695.106 )
						if( BBPower_Color <= 0.5 )
							if( Money_Flow_Ratio <= 0.648617 )
								if( Typical_Price <= 65.7783 )
									ret := -0.900000 // sell
								if( Typical_Price > 65.7783 )
									ret := -0.142857
							if( Money_Flow_Ratio > 0.648617 )
								if( Negative_Money_Flow_Sum <= 759756 )
									ret := -0.169231
								if( Negative_Money_Flow_Sum > 759756 )
									ret := 0.764706 // buy
						if( BBPower_Color > 0.5 )
							if( Positive_Money_Flow <= 5807.76 )
								if( Negative_Money_Flow <= 16062.1 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow > 16062.1 )
									ret := -0.500000
							if( Positive_Money_Flow > 5807.76 )
								if( Positive_Money_Flow_Sum <= 1.32413e+06 )
									ret := -0.417636
								if( Positive_Money_Flow_Sum > 1.32413e+06 )
									ret := -0.708920 // sell
				if( Typical_Price > 68.7214 )
					if( MFI_High <= -31.9138 )
						if( Typical_Price <= 78.4487 )
							if( Positive_Money_Flow_Sum <= 183034 )
								if( bullPower <= 0.142294 )
									ret := -0.466667
								if( bullPower > 0.142294 )
									ret := 0.500000
							if( Positive_Money_Flow_Sum > 183034 )
								if( Typical_Price <= 69.8189 )
									ret := -0.521739
								if( Typical_Price > 69.8189 )
									ret := -0.829268 // sell
						if( Typical_Price > 78.4487 )
							if( bbm <= 0.001126 )
								if( Positive_Money_Flow <= 30354.6 )
									ret := -0.666667
								if( Positive_Money_Flow > 30354.6 )
									ret := 0.000000
							if( bbm > 0.001126 )
								if( Positive_Money_Flow_Sum <= 633381 )
									ret := 1.000000 // buy
								if( Positive_Money_Flow_Sum > 633381 )
									ret := 0.166667
					if( MFI_High > -31.9138 )
						if( Positive_Money_Flow_Sum <= 934690 )
							if( Positive_Money_Flow_Sum <= 310522 )
								if( Positive_Money_Flow_Sum <= 257337 )
									ret := 0.101266
								if( Positive_Money_Flow_Sum > 257337 )
									ret := -0.532258
							if( Positive_Money_Flow_Sum > 310522 )
								if( Negative_Money_Flow_Sum <= 85510.4 )
									ret := 0.593750
								if( Negative_Money_Flow_Sum > 85510.4 )
									ret := 0.099206
						if( Positive_Money_Flow_Sum > 934690 )
							if( Typical_Price <= 69.3967 )
								if( Raw_Money_Flow <= 39580.1 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 39580.1 )
									ret := 0.000000
							if( Typical_Price > 69.3967 )
								if( Positive_Money_Flow <= 837.345 )
									ret := -0.032258
								if( Positive_Money_Flow > 837.345 )
									ret := -0.513043
		if( Raw_Money_Flow > 210633 )
			if( bbp <= 0.613483 )
				if( Negative_Money_Flow_Sum <= 4.10759e+07 )
					if( Money_Flow_Ratio <= 7.38614 )
						if( Negative_Money_Flow_Sum <= 2.85626e+07 )
							if( Negative_Money_Flow_Sum <= 2.09377e+06 )
								if( Positive_Money_Flow_Sum <= 469084 )
									ret := -0.520000
								if( Positive_Money_Flow_Sum > 469084 )
									ret := 0.138346
							if( Negative_Money_Flow_Sum > 2.09377e+06 )
								if( Positive_Money_Flow_Sum <= 8.93722e+07 )
									ret := -0.006650
								if( Positive_Money_Flow_Sum > 8.93722e+07 )
									ret := -0.574468
						if( Negative_Money_Flow_Sum > 2.85626e+07 )
							if( bbp <= 0.243157 )
								if( Typical_Price <= 69.3778 )
									ret := -0.173913
								if( Typical_Price > 69.3778 )
									ret := 0.368421
							if( bbp > 0.243157 )
								if( Typical_Price <= 66.2111 )
									ret := -0.064516
								if( Typical_Price > 66.2111 )
									ret := 0.638889
					if( Money_Flow_Ratio > 7.38614 )
						if( MFI_High <= 18.5599 )
							if( Typical_Price <= 63.0287 )
								if( Positive_Money_Flow_Sum <= 9.63355e+07 )
									ret := 0.135266
								if( Positive_Money_Flow_Sum > 9.63355e+07 )
									ret := -0.750000 // sell
							if( Typical_Price > 63.0287 )
								if( Positive_Money_Flow_Sum <= 1.82049e+06 )
									ret := 0.363636
								if( Positive_Money_Flow_Sum > 1.82049e+06 )
									ret := -0.269982
						if( MFI_High > 18.5599 )
							if( Positive_Money_Flow_Sum <= 2.16018e+07 )
								ret := 0.000000
							if( Positive_Money_Flow_Sum > 2.16018e+07 )
								ret := 1.000000 // buy
				if( Negative_Money_Flow_Sum > 4.10759e+07 )
					if( Typical_Price <= 66.7458 )
						if( MFI_High <= -17.7619 )
							if( bbm <= 0.023844 )
								if( bearPower <= 0.097337 )
									ret := -0.111111
								if( bearPower > 0.097337 )
									ret := -0.750000 // sell
							if( bbm > 0.023844 )
								if( Negative_Money_Flow_Sum <= 1.00085e+08 )
									ret := -0.782609 // sell
								if( Negative_Money_Flow_Sum > 1.00085e+08 )
									ret := -0.250000
						if( MFI_High > -17.7619 )
							ret := 1.000000 // buy
					if( Typical_Price > 66.7458 )
						if( bearPower <= 0.062175 )
							if( bearPower <= 0.058109 )
								if( Raw_Money_Flow <= 5.93155e+06 )
									ret := -0.650000
								if( Raw_Money_Flow > 5.93155e+06 )
									ret := 0.000000
							if( bearPower > 0.058109 )
								ret := 0.250000
						if( bearPower > 0.062175 )
							if( bullPower <= 0.372944 )
								if( bbp <= 0.464747 )
									ret := -1.000000 // sell
								if( bbp > 0.464747 )
									ret := -0.714286 // sell
							if( bullPower > 0.372944 )
								ret := 0.000000
			if( bbp > 0.613483 )
				if( Typical_Price <= 72.2242 )
					if( MFI_High <= 15.6028 )
						if( Money_Flow_Ratio <= 4.29266 )
							if( Negative_Money_Flow_Sum <= 1.22982e+07 )
								if( bbm <= 0.391017 )
									ret := -0.489362
								if( bbm > 0.391017 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 1.22982e+07 )
								if( Raw_Money_Flow <= 1.72405e+07 )
									ret := 0.657895
								if( Raw_Money_Flow > 1.72405e+07 )
									ret := -1.000000 // sell
						if( Money_Flow_Ratio > 4.29266 )
							if( Positive_Money_Flow <= 4.04004e+06 )
								if( Positive_Money_Flow <= 1.76258e+06 )
									ret := 0.695652
								if( Positive_Money_Flow > 1.76258e+06 )
									ret := -0.025000
							if( Positive_Money_Flow > 4.04004e+06 )
								if( MFI_High <= 15.1798 )
									ret := 0.817391 // buy
								if( MFI_High > 15.1798 )
									ret := 0.000000
					if( MFI_High > 15.6028 )
						if( Positive_Money_Flow <= 4.51707e+06 )
							if( bullPower <= 0.546882 )
								ret := -0.500000
							if( bullPower > 0.546882 )
								if( Money_Flow_Ratio <= 24.1274 )
									ret := -0.750000 // sell
								if( Money_Flow_Ratio > 24.1274 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow > 4.51707e+06 )
							if( Money_Flow_Ratio <= 24.694 )
								ret := -0.857143 // sell
							if( Money_Flow_Ratio > 24.694 )
								if( Typical_Price <= 65.9128 )
									ret := 0.764706 // buy
								if( Typical_Price > 65.9128 )
									ret := -0.428571
				if( Typical_Price > 72.2242 )
					if( Positive_Money_Flow_Sum <= 3.30934e+07 )
						if( MFI_Low <= 46.7691 )
							if( Money_Flow_Ratio <= 0.736561 )
								ret := -0.500000
							if( Money_Flow_Ratio > 0.736561 )
								ret := 0.200000
						if( MFI_Low > 46.7691 )
							if( bullPower <= 0.394921 )
								ret := -0.200000
							if( bullPower > 0.394921 )
								if( Positive_Money_Flow_Sum <= 1.47383e+06 )
									ret := -0.500000
								if( Positive_Money_Flow_Sum > 1.47383e+06 )
									ret := -1.000000 // sell
					if( Positive_Money_Flow_Sum > 3.30934e+07 )
						if( Positive_Money_Flow <= 9.54257e+06 )
							if( MFI_High <= 4.81626 )
								if( bearPower <= 0.241356 )
									ret := 0.750000 // buy
								if( bearPower > 0.241356 )
									ret := -0.500000
							if( MFI_High > 4.81626 )
								if( MFI <= 99.523 )
									ret := 0.937500 // buy
								if( MFI > 99.523 )
									ret := 0.250000
						if( Positive_Money_Flow > 9.54257e+06 )
							if( Typical_Price <= 72.8468 )
								ret := -0.500000
							if( Typical_Price > 72.8468 )
								ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0


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
float op_operation = decision_tree_0_PYPL_1Min_3d9ff895(bearPower, bbm, bbp, bullPower, BBPower_Color, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

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


