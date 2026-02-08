//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Money_Flow_Index
// ID_model: APPS_15Min_2BM0_340c2de3 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_APPS_15Min_2BM0_340c2de3", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_APPS_15Min_340c2de3(bullPower, bbp, bearPower, bbm, BBPower_Color, Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( bullPower <= -0.003281 )
		if( Positive_Money_Flow_Sum <= 1.30045e+07 )
			if( Negative_Money_Flow_Sum <= 28722.1 )
				if( Negative_Money_Flow <= 1834.8 )
					if( Positive_Money_Flow_Sum <= 274184 )
						if( bearPower <= -0.005066 )
							if( Negative_Money_Flow_Sum <= 11106.1 )
								if( MFI_Low <= 54.2489 )
									ret := 0.133333
								if( MFI_Low > 54.2489 )
									ret := 0.666667
							if( Negative_Money_Flow_Sum > 11106.1 )
								if( Typical_Price <= 3.65866 )
									ret := 0.788000 // buy
								if( Typical_Price > 3.65866 )
									ret := 0.000000
						if( bearPower > -0.005066 )
							if( Raw_Money_Flow <= 532.057 )
								if( Negative_Money_Flow <= 24.5679 )
									ret := 0.076923
								if( Negative_Money_Flow > 24.5679 )
									ret := -0.466667
							if( Raw_Money_Flow > 532.057 )
								ret := 0.785714 // buy
					if( Positive_Money_Flow_Sum > 274184 )
						if( Negative_Money_Flow <= 287.545 )
							ret := 0.529412
						if( Negative_Money_Flow > 287.545 )
							if( Raw_Money_Flow <= 1284.44 )
								ret := -0.642857
							if( Raw_Money_Flow > 1284.44 )
								ret := 0.416667
				if( Negative_Money_Flow > 1834.8 )
					if( Typical_Price <= 0.913317 )
						if( Money_Flow_Ratio <= 1.02822 )
							ret := 0.823529 // buy
						if( Money_Flow_Ratio > 1.02822 )
							ret := 1.000000 // buy
					if( Typical_Price > 0.913317 )
						if( MFI_High <= 19.1752 )
							if( MFI_High <= 17.8632 )
								if( MFI_Low <= 15.5489 )
									ret := -0.266667
								if( MFI_Low > 15.5489 )
									ret := 0.224138
							if( MFI_High > 17.8632 )
								ret := -1.000000 // sell
						if( MFI_High > 19.1752 )
							ret := 0.769231 // buy
			if( Negative_Money_Flow_Sum > 28722.1 )
				if( Raw_Money_Flow <= 42683.7 )
					if( bullPower <= -0.009152 )
						if( Typical_Price <= 3.43681 )
							if( Positive_Money_Flow_Sum <= 473374 )
								if( bbp <= -0.039263 )
									ret := 0.404478
								if( bbp > -0.039263 )
									ret := 0.172892
							if( Positive_Money_Flow_Sum > 473374 )
								if( bullPower <= -0.033437 )
									ret := 0.889706 // buy
								if( bullPower > -0.033437 )
									ret := 0.578616
						if( Typical_Price > 3.43681 )
							if( Negative_Money_Flow_Sum <= 3.97793e+06 )
								if( Positive_Money_Flow <= 12.5954 )
									ret := 0.185293
								if( Positive_Money_Flow > 12.5954 )
									ret := 0.002738
							if( Negative_Money_Flow_Sum > 3.97793e+06 )
								if( Positive_Money_Flow_Sum <= 609965 )
									ret := 0.187675
								if( Positive_Money_Flow_Sum > 609965 )
									ret := 0.367512
					if( bullPower > -0.009152 )
						if( MFI_High <= -5.33859 )
							if( MFI_Low <= 11.8648 )
								if( Positive_Money_Flow_Sum <= 32073.6 )
									ret := 0.153535
								if( Positive_Money_Flow_Sum > 32073.6 )
									ret := -0.046794
							if( MFI_Low > 11.8648 )
								if( MFI_Low <= 25.2434 )
									ret := 0.264220
								if( MFI_Low > 25.2434 )
									ret := 0.133333
						if( MFI_High > -5.33859 )
							if( Money_Flow_Ratio <= 3.65349 )
								if( Positive_Money_Flow_Sum <= 467476 )
									ret := 0.000000
								if( Positive_Money_Flow_Sum > 467476 )
									ret := -0.731707 // sell
							if( Money_Flow_Ratio > 3.65349 )
								if( MFI_Low <= 71.437 )
									ret := 0.174419
								if( MFI_Low > 71.437 )
									ret := -0.750000 // sell
				if( Raw_Money_Flow > 42683.7 )
					if( Positive_Money_Flow <= 454884 )
						if( Negative_Money_Flow_Sum <= 675764 )
							if( Raw_Money_Flow <= 85908.2 )
								if( Positive_Money_Flow_Sum <= 48785.8 )
									ret := 0.529412
								if( Positive_Money_Flow_Sum > 48785.8 )
									ret := -0.013115
							if( Raw_Money_Flow > 85908.2 )
								if( Raw_Money_Flow <= 111175 )
									ret := -0.405018
								if( Raw_Money_Flow > 111175 )
									ret := -0.027027
						if( Negative_Money_Flow_Sum > 675764 )
							if( MFI_Low <= 3.17636 )
								if( Positive_Money_Flow_Sum <= 22790.5 )
									ret := -0.230769
								if( Positive_Money_Flow_Sum > 22790.5 )
									ret := 0.133758
							if( MFI_Low > 3.17636 )
								if( Negative_Money_Flow_Sum <= 813789 )
									ret := 0.419162
								if( Negative_Money_Flow_Sum > 813789 )
									ret := 0.015115
					if( Positive_Money_Flow > 454884 )
						if( Negative_Money_Flow_Sum <= 2.0279e+07 )
							if( Negative_Money_Flow_Sum <= 2.93096e+06 )
								if( MFI <= 50.2126 )
									ret := 0.630303
								if( MFI > 50.2126 )
									ret := 0.288136
							if( Negative_Money_Flow_Sum > 2.93096e+06 )
								if( bbp <= -0.416858 )
									ret := 0.347368
								if( bbp > -0.416858 )
									ret := 0.125298
						if( Negative_Money_Flow_Sum > 2.0279e+07 )
							if( Positive_Money_Flow_Sum <= 1.2078e+07 )
								if( Money_Flow_Ratio <= 0.437161 )
									ret := -0.239286
								if( Money_Flow_Ratio > 0.437161 )
									ret := 0.500000
							if( Positive_Money_Flow_Sum > 1.2078e+07 )
								if( bullPower <= -0.260515 )
									ret := 0.800000 // buy
								if( bullPower > -0.260515 )
									ret := 0.157895
		if( Positive_Money_Flow_Sum > 1.30045e+07 )
			if( Negative_Money_Flow_Sum <= 2.17072e+07 )
				if( MFI <= 79.8224 )
					if( Positive_Money_Flow_Sum <= 4.33916e+07 )
						if( MFI_Low <= 55.5095 )
							if( Positive_Money_Flow_Sum <= 1.35409e+07 )
								if( bbm <= 0.118128 )
									ret := 0.259259
								if( bbm > 0.118128 )
									ret := -0.584906
							if( Positive_Money_Flow_Sum > 1.35409e+07 )
								if( MFI_High <= -35.9217 )
									ret := 0.657895
								if( MFI_High > -35.9217 )
									ret := 0.223404
						if( MFI_Low > 55.5095 )
							if( Negative_Money_Flow_Sum <= 9.47191e+06 )
								if( Negative_Money_Flow_Sum <= 6.17574e+06 )
									ret := -0.820000 // sell
								if( Negative_Money_Flow_Sum > 6.17574e+06 )
									ret := -0.315789
							if( Negative_Money_Flow_Sum > 9.47191e+06 )
								if( Negative_Money_Flow_Sum <= 9.67465e+06 )
									ret := 0.866667 // buy
								if( Negative_Money_Flow_Sum > 9.67465e+06 )
									ret := 0.294118
					if( Positive_Money_Flow_Sum > 4.33916e+07 )
						if( Negative_Money_Flow <= 257455 )
							ret := -0.375000
						if( Negative_Money_Flow > 257455 )
							ret := -1.000000 // sell
				if( MFI > 79.8224 )
					if( Positive_Money_Flow_Sum <= 1.46913e+07 )
						ret := -0.500000
					if( Positive_Money_Flow_Sum > 1.46913e+07 )
						if( Money_Flow_Ratio <= 6.6651 )
							if( bearPower <= -0.083549 )
								if( Negative_Money_Flow <= 1014.84 )
									ret := 0.454545
								if( Negative_Money_Flow > 1014.84 )
									ret := 0.850000 // buy
							if( bearPower > -0.083549 )
								if( Typical_Price <= 43.7783 )
									ret := 0.192308
								if( Typical_Price > 43.7783 )
									ret := 1.000000 // buy
						if( Money_Flow_Ratio > 6.6651 )
							if( Typical_Price <= 17.9367 )
								ret := -0.476190
							if( Typical_Price > 17.9367 )
								if( Positive_Money_Flow <= 6723.84 )
									ret := 0.370370
								if( Positive_Money_Flow > 6723.84 )
									ret := 0.694915
			if( Negative_Money_Flow_Sum > 2.17072e+07 )
				if( bbm <= 2.28301 )
					if( Negative_Money_Flow_Sum <= 3.4619e+08 )
						if( MFI_High <= -30.6093 )
							if( Raw_Money_Flow <= 2.71555e+07 )
								if( MFI_Low <= -5.9831 )
									ret := 0.298077
								if( MFI_Low > -5.9831 )
									ret := -0.084426
							if( Raw_Money_Flow > 2.71555e+07 )
								if( Money_Flow_Ratio <= 0.396921 )
									ret := -0.666667
								if( Money_Flow_Ratio > 0.396921 )
									ret := 0.100000
						if( MFI_High > -30.6093 )
							if( MFI <= 76.5194 )
								if( Positive_Money_Flow_Sum <= 1.55887e+08 )
									ret := 0.098121
								if( Positive_Money_Flow_Sum > 1.55887e+08 )
									ret := 0.909091 // buy
							if( MFI > 76.5194 )
								if( bbp <= -1.10995 )
									ret := -0.375000
								if( bbp > -1.10995 )
									ret := -0.928571 // sell
					if( Negative_Money_Flow_Sum > 3.4619e+08 )
						if( Raw_Money_Flow <= 2.22778e+07 )
							ret := -0.888889 // sell
						if( Raw_Money_Flow > 2.22778e+07 )
							ret := -1.000000 // sell
				if( bbm > 2.28301 )
					if( Positive_Money_Flow <= 1.34919e+07 )
						if( Raw_Money_Flow <= 2.54773e+07 )
							if( Typical_Price <= 67.5599 )
								ret := 0.416667
							if( Typical_Price > 67.5599 )
								ret := 0.842105 // buy
						if( Raw_Money_Flow > 2.54773e+07 )
							ret := -0.111111
					if( Positive_Money_Flow > 1.34919e+07 )
						ret := 0.933333 // buy
	if( bullPower > -0.003281 )
		if( BBPower_Color <= 0.5 )
			if( MFI_Low <= 46.7878 )
				if( Raw_Money_Flow <= 1.02859e+06 )
					if( Positive_Money_Flow <= 15.4177 )
						if( Negative_Money_Flow <= 1.25529 )
							if( MFI_High <= -39.2464 )
								if( Raw_Money_Flow <= 42235.1 )
									ret := -0.355932
								if( Raw_Money_Flow > 42235.1 )
									ret := 0.020833
							if( MFI_High > -39.2464 )
								if( bullPower <= 0.019712 )
									ret := -0.050000
								if( bullPower > 0.019712 )
									ret := 0.705882 // buy
						if( Negative_Money_Flow > 1.25529 )
							if( bbp <= 0.008109 )
								if( Negative_Money_Flow <= 65831.8 )
									ret := 0.121661
								if( Negative_Money_Flow > 65831.8 )
									ret := 0.013658
							if( bbp > 0.008109 )
								if( bbm <= 0.092464 )
									ret := 0.240833
								if( bbm > 0.092464 )
									ret := 0.031315
					if( Positive_Money_Flow > 15.4177 )
						if( MFI_Low <= 15.4221 )
							if( Positive_Money_Flow <= 48186.7 )
								if( Raw_Money_Flow <= 62084.4 )
									ret := -0.316427
								if( Raw_Money_Flow > 62084.4 )
									ret := 0.155556
							if( Positive_Money_Flow > 48186.7 )
								if( bearPower <= -0.018698 )
									ret := 0.019309
								if( bearPower > -0.018698 )
									ret := -0.252174
						if( MFI_Low > 15.4221 )
							if( bbp <= -0.000129 )
								if( bullPower <= -0.002841 )
									ret := -0.428571
								if( bullPower > -0.002841 )
									ret := 0.005250
							if( bbp > -0.000129 )
								if( Positive_Money_Flow <= 308162 )
									ret := -0.179027
								if( Positive_Money_Flow > 308162 )
									ret := 0.108696
				if( Raw_Money_Flow > 1.02859e+06 )
					if( bbp <= -2.57575 )
						if( Typical_Price <= 76.0297 )
							ret := 1.000000 // buy
						if( Typical_Price > 76.0297 )
							if( Negative_Money_Flow <= 5.99784e+07 )
								ret := 0.230769
							if( Negative_Money_Flow > 5.99784e+07 )
								ret := 1.000000 // buy
					if( bbp > -2.57575 )
						if( Money_Flow_Ratio <= 0.697392 )
							if( MFI_Low <= 20.7103 )
								if( bearPower <= -0.059328 )
									ret := -0.123410
								if( bearPower > -0.059328 )
									ret := 0.331169
							if( MFI_Low > 20.7103 )
								if( bbp <= -0.146618 )
									ret := 0.066667
								if( bbp > -0.146618 )
									ret := 0.960000 // buy
						if( Money_Flow_Ratio > 0.697392 )
							if( Positive_Money_Flow <= 7.39368e+06 )
								if( MFI_Low <= 24.2088 )
									ret := -0.381166
								if( MFI_Low > 24.2088 )
									ret := -0.169217
							if( Positive_Money_Flow > 7.39368e+06 )
								if( Typical_Price <= 72.6041 )
									ret := 0.418478
								if( Typical_Price > 72.6041 )
									ret := -0.375000
			if( MFI_Low > 46.7878 )
				if( Positive_Money_Flow_Sum <= 5.31356e+07 )
					if( bullPower <= 0.016152 )
						if( Raw_Money_Flow <= 18290.8 )
							if( Positive_Money_Flow <= 596.233 )
								if( Money_Flow_Ratio <= 4.17025 )
									ret := 0.298828
								if( Money_Flow_Ratio > 4.17025 )
									ret := 0.439506
							if( Positive_Money_Flow > 596.233 )
								if( bearPower <= 0.002591 )
									ret := 0.194379
								if( bearPower > 0.002591 )
									ret := -0.290323
						if( Raw_Money_Flow > 18290.8 )
							if( Negative_Money_Flow_Sum <= 566954 )
								if( bbp <= -0.041629 )
									ret := 0.813953 // buy
								if( bbp > -0.041629 )
									ret := 0.103152
							if( Negative_Money_Flow_Sum > 566954 )
								if( bearPower <= -0.034893 )
									ret := -0.049020
								if( bearPower > -0.034893 )
									ret := -0.365079
					if( bullPower > 0.016152 )
						if( Negative_Money_Flow_Sum <= 20832.1 )
							if( bbm <= 0.012552 )
								ret := -1.000000 // sell
							if( bbm > 0.012552 )
								if( Typical_Price <= 1.33675 )
									ret := -1.000000 // sell
								if( Typical_Price > 1.33675 )
									ret := -0.288462
						if( Negative_Money_Flow_Sum > 20832.1 )
							if( Negative_Money_Flow_Sum <= 305889 )
								if( MFI_High <= 15.9048 )
									ret := 0.118056
								if( MFI_High > 15.9048 )
									ret := 0.557143
							if( Negative_Money_Flow_Sum > 305889 )
								if( Negative_Money_Flow <= 2.18411e+06 )
									ret := -0.034305
								if( Negative_Money_Flow > 2.18411e+06 )
									ret := -0.377246
				if( Positive_Money_Flow_Sum > 5.31356e+07 )
					if( Positive_Money_Flow <= 511785 )
						if( Typical_Price <= 87.5152 )
							if( Typical_Price <= 57.7068 )
								if( bearPower <= -0.223379 )
									ret := 0.238095
								if( bearPower > -0.223379 )
									ret := 0.842105 // buy
							if( Typical_Price > 57.7068 )
								if( Money_Flow_Ratio <= 2.2328 )
									ret := 0.555556
								if( Money_Flow_Ratio > 2.2328 )
									ret := 0.922222 // buy
						if( Typical_Price > 87.5152 )
							ret := 0.000000
					if( Positive_Money_Flow > 511785 )
						if( MFI_Low <= 55.4256 )
							if( bullPower <= 0.051338 )
								ret := -0.294118
							if( bullPower > 0.051338 )
								if( bearPower <= -0.254008 )
									ret := 0.800000 // buy
								if( bearPower > -0.254008 )
									ret := 0.250000
						if( MFI_Low > 55.4256 )
							if( Raw_Money_Flow <= 3.08564e+06 )
								ret := -0.933333 // sell
							if( Raw_Money_Flow > 3.08564e+06 )
								if( MFI_Low <= 57.753 )
									ret := 0.333333
								if( MFI_Low > 57.753 )
									ret := -0.388889
		if( BBPower_Color > 0.5 )
			if( Raw_Money_Flow <= 13656.4 )
				if( bbp <= 0.032469 )
					if( MFI <= 64.4123 )
						if( Positive_Money_Flow_Sum <= 43922.9 )
							if( MFI <= 11.0627 )
								if( Raw_Money_Flow <= 485.101 )
									ret := -0.911765 // sell
								if( Raw_Money_Flow > 485.101 )
									ret := -0.656250
							if( MFI > 11.0627 )
								if( bbm <= 0.004978 )
									ret := -0.479087
								if( bbm > 0.004978 )
									ret := -0.162362
						if( Positive_Money_Flow_Sum > 43922.9 )
							if( Money_Flow_Ratio <= 1.2408 )
								if( Typical_Price <= 0.708578 )
									ret := 0.806452 // buy
								if( Typical_Price > 0.708578 )
									ret := -0.029784
							if( Money_Flow_Ratio > 1.2408 )
								if( Positive_Money_Flow_Sum <= 107702 )
									ret := -0.098446
								if( Positive_Money_Flow_Sum > 107702 )
									ret := -0.349614
					if( MFI > 64.4123 )
						if( Positive_Money_Flow_Sum <= 34470.6 )
							if( MFI_Low <= 52.7574 )
								if( Positive_Money_Flow_Sum <= 30405.3 )
									ret := 0.461538
								if( Positive_Money_Flow_Sum > 30405.3 )
									ret := -0.400000
							if( MFI_Low > 52.7574 )
								if( MFI_High <= 12.9379 )
									ret := -0.516129
								if( MFI_High > 12.9379 )
									ret := 0.555556
						if( Positive_Money_Flow_Sum > 34470.6 )
							if( Positive_Money_Flow_Sum <= 204028 )
								if( MFI_Low <= 75.6165 )
									ret := 0.009960
								if( MFI_Low > 75.6165 )
									ret := 0.750000 // buy
							if( Positive_Money_Flow_Sum > 204028 )
								if( Raw_Money_Flow <= 2858.96 )
									ret := 0.011494
								if( Raw_Money_Flow > 2858.96 )
									ret := 0.354115
				if( bbp > 0.032469 )
					if( MFI_High <= -41.2106 )
						if( Positive_Money_Flow <= 2.44903 )
							if( bbm <= 0.0854 )
								if( Negative_Money_Flow_Sum <= 4.5466e+06 )
									ret := -0.535912
								if( Negative_Money_Flow_Sum > 4.5466e+06 )
									ret := -0.117117
							if( bbm > 0.0854 )
								ret := 0.384615
						if( Positive_Money_Flow > 2.44903 )
							if( Negative_Money_Flow_Sum <= 4.8335e+06 )
								if( bearPower <= 0.132607 )
									ret := -0.674142
								if( bearPower > 0.132607 )
									ret := -0.354430
							if( Negative_Money_Flow_Sum > 4.8335e+06 )
								if( bullPower <= 0.058332 )
									ret := 0.084507
								if( bullPower > 0.058332 )
									ret := -0.472492
					if( MFI_High > -41.2106 )
						if( Typical_Price <= 3.93685 )
							if( Raw_Money_Flow <= 4699.35 )
								if( bearPower <= 0.043692 )
									ret := -0.393300
								if( bearPower > 0.043692 )
									ret := -0.837438 // sell
							if( Raw_Money_Flow > 4699.35 )
								if( MFI <= 95.999 )
									ret := -0.111349
								if( MFI > 95.999 )
									ret := -0.730769 // sell
						if( Typical_Price > 3.93685 )
							if( bullPower <= 0.082576 )
								if( MFI_Low <= 60.8351 )
									ret := -0.140957
								if( MFI_Low > 60.8351 )
									ret := 0.281734
							if( bullPower > 0.082576 )
								if( bbm <= 0.1708 )
									ret := -0.281410
								if( bbm > 0.1708 )
									ret := 0.210526
			if( Raw_Money_Flow > 13656.4 )
				if( Positive_Money_Flow <= 48.0641 )
					if( Typical_Price <= 80.1774 )
						if( bullPower <= 1.37273 )
							if( Money_Flow_Ratio <= 1.92107 )
								if( Negative_Money_Flow_Sum <= 35573.6 )
									ret := 0.621622
								if( Negative_Money_Flow_Sum > 35573.6 )
									ret := -0.018490
							if( Money_Flow_Ratio > 1.92107 )
								if( MFI <= 90.1075 )
									ret := 0.071093
								if( MFI > 90.1075 )
									ret := -0.105105
						if( bullPower > 1.37273 )
							if( MFI_High <= 8.00915 )
								if( bbm <= 0.669724 )
									ret := 0.000000
								if( bbm > 0.669724 )
									ret := 0.482759
							if( MFI_High > 8.00915 )
								ret := -0.583333
					if( Typical_Price > 80.1774 )
						if( Negative_Money_Flow <= 205821 )
							if( bearPower <= -0.113371 )
								ret := -0.466667
							if( bearPower > -0.113371 )
								if( bearPower <= 0.04189 )
									ret := 0.444444
								if( bearPower > 0.04189 )
									ret := 0.123288
						if( Negative_Money_Flow > 205821 )
							if( MFI_High <= -32.8178 )
								if( Positive_Money_Flow_Sum <= 5.80594e+07 )
									ret := -0.258065
								if( Positive_Money_Flow_Sum > 5.80594e+07 )
									ret := -1.000000 // sell
							if( MFI_High > -32.8178 )
								if( MFI_Low <= 45.5377 )
									ret := -0.082353
								if( MFI_Low > 45.5377 )
									ret := -0.342105
				if( Positive_Money_Flow > 48.0641 )
					if( bbm <= 0.993396 )
						if( MFI_Low <= 21.159 )
							if( Negative_Money_Flow_Sum <= 311323 )
								if( bullPower <= 0.148237 )
									ret := -0.641176
								if( bullPower > 0.148237 )
									ret := -0.050000
							if( Negative_Money_Flow_Sum > 311323 )
								if( Money_Flow_Ratio <= 0.003358 )
									ret := 0.866667 // buy
								if( Money_Flow_Ratio > 0.003358 )
									ret := -0.151123
						if( MFI_Low > 21.159 )
							if( bbp <= 0.066492 )
								if( Positive_Money_Flow <= 46238.3 )
									ret := 0.129100
								if( Positive_Money_Flow > 46238.3 )
									ret := -0.013982
							if( bbp > 0.066492 )
								if( Raw_Money_Flow <= 22895.8 )
									ret := -0.337043
								if( Raw_Money_Flow > 22895.8 )
									ret := -0.060061
					if( bbm > 0.993396 )
						if( Positive_Money_Flow <= 3.12222e+06 )
							if( Positive_Money_Flow_Sum <= 1.98323e+06 )
								if( Positive_Money_Flow_Sum <= 1.30336e+06 )
									ret := -0.142857
								if( Positive_Money_Flow_Sum > 1.30336e+06 )
									ret := 0.542857
							if( Positive_Money_Flow_Sum > 1.98323e+06 )
								if( bbm <= 1.8 )
									ret := -0.454545
								if( bbm > 1.8 )
									ret := -0.950000 // sell
						if( Positive_Money_Flow > 3.12222e+06 )
							if( Typical_Price <= 86.8037 )
								if( MFI <= 38.4463 )
									ret := -0.655172
								if( MFI > 38.4463 )
									ret := 0.204655
							if( Typical_Price > 86.8037 )
								if( bbm <= 1.1232 )
									ret := 0.428571
								if( bbm > 1.1232 )
									ret := -0.548387
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_APPS_15Min_340c2de3(bullPower, bbp, bearPower, bbm, BBPower_Color, Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum)

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


