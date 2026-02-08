//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Vortex_Indicator
// ID_model: TRXUSDT_30Min_2MV0_c0acde27 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TRXUSDT_30Min_2MV0_c0acde27", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TRXUSDT_30Min_c0acde27(Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow, VIP_VIM, VIM, VIP)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Typical_Price <= 0.064558 )
		if( VIP_VIM <= -0.134931 )
			if( Negative_Money_Flow_Sum <= 3.59736e+06 )
				if( Positive_Money_Flow_Sum <= 3.1406e+06 )
					if( MFI_High <= -55.8173 )
						if( Positive_Money_Flow_Sum <= 312818 )
							ret := 0.800000 // buy
						if( Positive_Money_Flow_Sum > 312818 )
							if( Typical_Price <= 0.060511 )
								if( Negative_Money_Flow_Sum <= 2.78084e+06 )
									ret := 0.000000
								if( Negative_Money_Flow_Sum > 2.78084e+06 )
									ret := -0.340426
							if( Typical_Price > 0.060511 )
								if( Money_Flow_Ratio <= 0.309323 )
									ret := -1.000000 // sell
								if( Money_Flow_Ratio > 0.309323 )
									ret := -0.750000 // sell
					if( MFI_High > -55.8173 )
						if( Raw_Money_Flow <= 926857 )
							if( MFI <= 37.0354 )
								if( VIP_VIM <= -0.269675 )
									ret := 0.267045
								if( VIP_VIM > -0.269675 )
									ret := 0.055556
							if( MFI > 37.0354 )
								if( Positive_Money_Flow_Sum <= 2.32123e+06 )
									ret := -0.070615
								if( Positive_Money_Flow_Sum > 2.32123e+06 )
									ret := 0.157143
						if( Raw_Money_Flow > 926857 )
							if( Negative_Money_Flow <= 1.16334e+06 )
								if( Money_Flow_Ratio <= 0.75273 )
									ret := -0.875000 // sell
								if( Money_Flow_Ratio > 0.75273 )
									ret := -0.250000
							if( Negative_Money_Flow > 1.16334e+06 )
								if( Raw_Money_Flow <= 1.3849e+06 )
									ret := 0.600000
								if( Raw_Money_Flow > 1.3849e+06 )
									ret := -0.250000
				if( Positive_Money_Flow_Sum > 3.1406e+06 )
					if( Positive_Money_Flow <= 195144 )
						if( Positive_Money_Flow_Sum <= 3.22779e+06 )
							ret := 0.750000 // buy
						if( Positive_Money_Flow_Sum > 3.22779e+06 )
							if( Negative_Money_Flow_Sum <= 3.39576e+06 )
								if( Raw_Money_Flow <= 299968 )
									ret := 0.166667
								if( Raw_Money_Flow > 299968 )
									ret := 0.000000
							if( Negative_Money_Flow_Sum > 3.39576e+06 )
								ret := -0.500000
					if( Positive_Money_Flow > 195144 )
						if( MFI <= 51.9824 )
							ret := 0.250000
						if( MFI > 51.9824 )
							if( Negative_Money_Flow_Sum <= 3.02973e+06 )
								if( Raw_Money_Flow <= 498095 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 498095 )
									ret := 0.500000
							if( Negative_Money_Flow_Sum > 3.02973e+06 )
								ret := 1.000000 // buy
			if( Negative_Money_Flow_Sum > 3.59736e+06 )
				if( Positive_Money_Flow_Sum <= 1.0763e+07 )
					if( Typical_Price <= 0.058473 )
						if( Negative_Money_Flow_Sum <= 1.81618e+07 )
							if( MFI <= 34.8896 )
								if( Negative_Money_Flow_Sum <= 6.45222e+06 )
									ret := 0.163399
								if( Negative_Money_Flow_Sum > 6.45222e+06 )
									ret := 0.351187
							if( MFI > 34.8896 )
								if( Positive_Money_Flow_Sum <= 9.98484e+06 )
									ret := 0.155051
								if( Positive_Money_Flow_Sum > 9.98484e+06 )
									ret := 0.515625
						if( Negative_Money_Flow_Sum > 1.81618e+07 )
							if( Raw_Money_Flow <= 1.15389e+06 )
								if( Negative_Money_Flow <= 441450 )
									ret := -0.234568
								if( Negative_Money_Flow > 441450 )
									ret := 0.659574
							if( Raw_Money_Flow > 1.15389e+06 )
								if( VIP <= 0.662581 )
									ret := 0.793103 // buy
								if( VIP > 0.662581 )
									ret := 0.504950
					if( Typical_Price > 0.058473 )
						if( VIP <= 0.717588 )
							if( Money_Flow_Ratio <= 0.179253 )
								if( Raw_Money_Flow <= 1.30107e+06 )
									ret := 0.045455
								if( Raw_Money_Flow > 1.30107e+06 )
									ret := 0.613333
							if( Money_Flow_Ratio > 0.179253 )
								if( VIM <= 1.2083 )
									ret := -0.702703 // sell
								if( VIM > 1.2083 )
									ret := -0.072727
						if( VIP > 0.717588 )
							if( Typical_Price <= 0.064388 )
								if( MFI_High <= -40.6592 )
									ret := 0.188679
								if( MFI_High > -40.6592 )
									ret := 0.054820
							if( Typical_Price > 0.064388 )
								if( Negative_Money_Flow_Sum <= 4.47811e+06 )
									ret := -0.166667
								if( Negative_Money_Flow_Sum > 4.47811e+06 )
									ret := 0.592105
				if( Positive_Money_Flow_Sum > 1.0763e+07 )
					if( Negative_Money_Flow_Sum <= 4.54002e+07 )
						if( MFI_Low <= 11.3045 )
							if( Negative_Money_Flow <= 5.10677e+06 )
								if( MFI_Low <= 4.93478 )
									ret := 0.447368
								if( MFI_Low > 4.93478 )
									ret := -0.228571
							if( Negative_Money_Flow > 5.10677e+06 )
								if( Typical_Price <= 0.029287 )
									ret := -0.250000
								if( Typical_Price > 0.029287 )
									ret := -1.000000 // sell
						if( MFI_Low > 11.3045 )
							if( MFI <= 50.6778 )
								if( MFI_Low <= 21.4675 )
									ret := 0.086022
								if( MFI_Low > 21.4675 )
									ret := 0.328054
							if( MFI > 50.6778 )
								if( MFI_Low <= 41.4227 )
									ret := -0.336134
								if( MFI_Low > 41.4227 )
									ret := 0.450000
					if( Negative_Money_Flow_Sum > 4.54002e+07 )
						if( Negative_Money_Flow <= 1.55299e+07 )
							if( VIP <= 0.841638 )
								if( Typical_Price <= 0.063097 )
									ret := 0.549356
								if( Typical_Price > 0.063097 )
									ret := -0.227273
							if( VIP > 0.841638 )
								if( Typical_Price <= 0.046175 )
									ret := -0.466667
								if( Typical_Price > 0.046175 )
									ret := 0.344444
						if( Negative_Money_Flow > 1.55299e+07 )
							if( VIP_VIM <= -0.613229 )
								ret := -0.750000 // sell
							if( VIP_VIM > -0.613229 )
								ret := -1.000000 // sell
		if( VIP_VIM > -0.134931 )
			if( Negative_Money_Flow <= 562348 )
				if( Money_Flow_Ratio <= 2.87256 )
					if( Positive_Money_Flow_Sum <= 3.88098e+06 )
						if( Money_Flow_Ratio <= 0.65989 )
							if( VIP_VIM <= -0.089836 )
								if( Raw_Money_Flow <= 325598 )
									ret := 0.231579
								if( Raw_Money_Flow > 325598 )
									ret := -0.075630
							if( VIP_VIM > -0.089836 )
								if( Typical_Price <= 0.0288 )
									ret := 0.009174
								if( Typical_Price > 0.0288 )
									ret := -0.302239
						if( Money_Flow_Ratio > 0.65989 )
							if( Typical_Price <= 0.025202 )
								if( Positive_Money_Flow_Sum <= 1.51345e+06 )
									ret := 0.561404
								if( Positive_Money_Flow_Sum > 1.51345e+06 )
									ret := 0.088235
							if( Typical_Price > 0.025202 )
								if( Negative_Money_Flow_Sum <= 5.27033e+06 )
									ret := -0.003405
								if( Negative_Money_Flow_Sum > 5.27033e+06 )
									ret := 0.833333 // buy
					if( Positive_Money_Flow_Sum > 3.88098e+06 )
						if( MFI_High <= -35.4756 )
							if( Positive_Money_Flow_Sum <= 1.52891e+07 )
								if( VIP_VIM <= -0.087644 )
									ret := 0.135266
								if( VIP_VIM > -0.087644 )
									ret := 0.378924
							if( Positive_Money_Flow_Sum > 1.52891e+07 )
								if( Positive_Money_Flow_Sum <= 2.67107e+07 )
									ret := -0.268817
								if( Positive_Money_Flow_Sum > 2.67107e+07 )
									ret := 0.652174
						if( MFI_High > -35.4756 )
							if( Typical_Price <= 0.026165 )
								if( Negative_Money_Flow <= 385812 )
									ret := 0.382353
								if( Negative_Money_Flow > 385812 )
									ret := -0.052632
							if( Typical_Price > 0.026165 )
								if( Negative_Money_Flow_Sum <= 2.40865e+06 )
									ret := 0.237052
								if( Negative_Money_Flow_Sum > 2.40865e+06 )
									ret := 0.052878
				if( Money_Flow_Ratio > 2.87256 )
					if( Positive_Money_Flow <= 1.5527e+07 )
						if( Typical_Price <= 0.042676 )
							if( VIM <= 0.712537 )
								if( Positive_Money_Flow_Sum <= 1.08188e+07 )
									ret := -0.025641
								if( Positive_Money_Flow_Sum > 1.08188e+07 )
									ret := -0.801980 // sell
							if( VIM > 0.712537 )
								if( VIM <= 0.887825 )
									ret := -0.108571
								if( VIM > 0.887825 )
									ret := 0.531250
						if( Typical_Price > 0.042676 )
							if( Negative_Money_Flow_Sum <= 1.24842e+07 )
								if( Raw_Money_Flow <= 1.65847e+06 )
									ret := 0.067568
								if( Raw_Money_Flow > 1.65847e+06 )
									ret := -0.175589
							if( Negative_Money_Flow_Sum > 1.24842e+07 )
								if( Negative_Money_Flow_Sum <= 1.61374e+07 )
									ret := 0.656250
								if( Negative_Money_Flow_Sum > 1.61374e+07 )
									ret := -0.473684
					if( Positive_Money_Flow > 1.5527e+07 )
						ret := -1.000000 // sell
			if( Negative_Money_Flow > 562348 )
				if( Negative_Money_Flow_Sum <= 1.61955e+07 )
					if( VIP_VIM <= 0.193499 )
						if( MFI_High <= -44.6824 )
							if( Typical_Price <= 0.059818 )
								if( Positive_Money_Flow_Sum <= 2.20895e+06 )
									ret := 0.166667
								if( Positive_Money_Flow_Sum > 2.20895e+06 )
									ret := -0.647059
							if( Typical_Price > 0.059818 )
								if( Negative_Money_Flow_Sum <= 6.62614e+06 )
									ret := -0.142857
								if( Negative_Money_Flow_Sum > 6.62614e+06 )
									ret := 0.428571
						if( MFI_High > -44.6824 )
							if( Negative_Money_Flow_Sum <= 3.40472e+06 )
								if( Positive_Money_Flow_Sum <= 6.17861e+06 )
									ret := 0.005525
								if( Positive_Money_Flow_Sum > 6.17861e+06 )
									ret := -0.800000 // sell
							if( Negative_Money_Flow_Sum > 3.40472e+06 )
								if( VIP <= 1.1147 )
									ret := 0.152840
								if( VIP > 1.1147 )
									ret := -0.378378
					if( VIP_VIM > 0.193499 )
						if( MFI_Low <= 52.2056 )
							if( VIP_VIM <= 0.65995 )
								if( Negative_Money_Flow_Sum <= 6.90403e+06 )
									ret := 0.216480
								if( Negative_Money_Flow_Sum > 6.90403e+06 )
									ret := 0.375516
							if( VIP_VIM > 0.65995 )
								ret := -0.833333 // sell
						if( MFI_Low > 52.2056 )
							if( Raw_Money_Flow <= 1.21065e+06 )
								if( Money_Flow_Ratio <= 3.6184 )
									ret := -0.133971
								if( Money_Flow_Ratio > 3.6184 )
									ret := 0.270833
							if( Raw_Money_Flow > 1.21065e+06 )
								if( Positive_Money_Flow_Sum <= 4.33732e+07 )
									ret := 0.377432
								if( Positive_Money_Flow_Sum > 4.33732e+07 )
									ret := -0.681818
				if( Negative_Money_Flow_Sum > 1.61955e+07 )
					if( Typical_Price <= 0.05614 )
						if( Raw_Money_Flow <= 1.50541e+07 )
							if( Negative_Money_Flow_Sum <= 1.64975e+07 )
								if( MFI_High <= -30.3049 )
									ret := 0.000000
								if( MFI_High > -30.3049 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 1.64975e+07 )
								if( Negative_Money_Flow_Sum <= 1.7301e+07 )
									ret := 0.771429 // buy
								if( Negative_Money_Flow_Sum > 1.7301e+07 )
									ret := 0.090468
						if( Raw_Money_Flow > 1.50541e+07 )
							if( MFI_High <= -26.5361 )
								ret := -1.000000 // sell
							if( MFI_High > -26.5361 )
								ret := -0.500000
					if( Typical_Price > 0.05614 )
						if( VIP <= 1.23012 )
							if( Raw_Money_Flow <= 7.24321e+06 )
								if( Positive_Money_Flow_Sum <= 1.17446e+07 )
									ret := -0.689655
								if( Positive_Money_Flow_Sum > 1.17446e+07 )
									ret := -0.251701
							if( Raw_Money_Flow > 7.24321e+06 )
								if( VIP_VIM <= 0.13448 )
									ret := 0.750000 // buy
								if( VIP_VIM > 0.13448 )
									ret := -0.562500
						if( VIP > 1.23012 )
							if( Negative_Money_Flow <= 4.48319e+06 )
								if( VIM <= 0.764267 )
									ret := 1.000000 // buy
								if( VIM > 0.764267 )
									ret := 0.500000
							if( Negative_Money_Flow > 4.48319e+06 )
								if( VIP <= 1.24285 )
									ret := 0.600000
								if( VIP > 1.24285 )
									ret := -0.142857
	if( Typical_Price > 0.064558 )
		if( Positive_Money_Flow_Sum <= 7.39298e+06 )
			if( Negative_Money_Flow <= 1.67349e+06 )
				if( Negative_Money_Flow_Sum <= 2.22244e+07 )
					if( Raw_Money_Flow <= 449230 )
						if( VIM <= 1.38422 )
							if( VIP_VIM <= -0.045913 )
								if( Positive_Money_Flow_Sum <= 4.275e+06 )
									ret := 0.020514
								if( Positive_Money_Flow_Sum > 4.275e+06 )
									ret := 0.149457
							if( VIP_VIM > -0.045913 )
								if( VIP <= 1.17086 )
									ret := -0.043805
								if( VIP > 1.17086 )
									ret := 0.057722
						if( VIM > 1.38422 )
							if( Typical_Price <= 0.083336 )
								if( MFI_Low <= 2.51151 )
									ret := 0.769231 // buy
								if( MFI_Low > 2.51151 )
									ret := -0.375000
							if( Typical_Price > 0.083336 )
								if( Positive_Money_Flow_Sum <= 2.25563e+06 )
									ret := -0.081081
								if( Positive_Money_Flow_Sum > 2.25563e+06 )
									ret := 0.400000
					if( Raw_Money_Flow > 449230 )
						if( Negative_Money_Flow_Sum <= 1.03159e+07 )
							if( MFI <= 18.7141 )
								if( Negative_Money_Flow_Sum <= 4.8252e+06 )
									ret := -0.659091
								if( Negative_Money_Flow_Sum > 4.8252e+06 )
									ret := -0.208459
							if( MFI > 18.7141 )
								if( Positive_Money_Flow <= 1.82998e+06 )
									ret := -0.053797
								if( Positive_Money_Flow > 1.82998e+06 )
									ret := 0.300813
						if( Negative_Money_Flow_Sum > 1.03159e+07 )
							if( MFI_High <= -45.8169 )
								if( Positive_Money_Flow <= 2.83034e+06 )
									ret := 0.015656
								if( Positive_Money_Flow > 2.83034e+06 )
									ret := -1.000000 // sell
							if( MFI_High > -45.8169 )
								if( VIP_VIM <= -0.147872 )
									ret := 0.654676
								if( VIP_VIM > -0.147872 )
									ret := 0.033333
				if( Negative_Money_Flow_Sum > 2.22244e+07 )
					if( Negative_Money_Flow_Sum <= 2.26289e+07 )
						if( VIP <= 0.789036 )
							ret := -1.000000 // sell
						if( VIP > 0.789036 )
							ret := -0.500000
					if( Negative_Money_Flow_Sum > 2.26289e+07 )
						if( MFI_High <= -62.7956 )
							if( Negative_Money_Flow_Sum <= 2.56717e+07 )
								if( MFI_Low <= -12.6595 )
									ret := -0.250000
								if( MFI_Low > -12.6595 )
									ret := 0.931034 // buy
							if( Negative_Money_Flow_Sum > 2.56717e+07 )
								if( VIM <= 1.40353 )
									ret := -0.040541
								if( VIM > 1.40353 )
									ret := -0.700000 // sell
						if( MFI_High > -62.7956 )
							if( VIM <= 1.33614 )
								if( MFI_Low <= -2.00483 )
									ret := -1.000000 // sell
								if( MFI_Low > -2.00483 )
									ret := -0.562500
							if( VIM > 1.33614 )
								if( Positive_Money_Flow <= 1.01043e+06 )
									ret := 0.833333 // buy
								if( Positive_Money_Flow > 1.01043e+06 )
									ret := -0.428571
			if( Negative_Money_Flow > 1.67349e+06 )
				if( MFI_Low <= -10.182 )
					if( VIP_VIM <= -0.715633 )
						if( Negative_Money_Flow_Sum <= 4.44925e+07 )
							if( VIP_VIM <= -0.878346 )
								if( Raw_Money_Flow <= 1.92226e+06 )
									ret := -0.625000
								if( Raw_Money_Flow > 1.92226e+06 )
									ret := 0.281250
							if( VIP_VIM > -0.878346 )
								if( Positive_Money_Flow_Sum <= 903063 )
									ret := 0.200000
								if( Positive_Money_Flow_Sum > 903063 )
									ret := -0.641509
						if( Negative_Money_Flow_Sum > 4.44925e+07 )
							if( Negative_Money_Flow_Sum <= 8.03267e+07 )
								if( MFI <= 7.85084 )
									ret := 0.933333 // buy
								if( MFI > 7.85084 )
									ret := 0.500000
							if( Negative_Money_Flow_Sum > 8.03267e+07 )
								if( Negative_Money_Flow <= 6.79938e+06 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow > 6.79938e+06 )
									ret := -0.250000
					if( VIP_VIM > -0.715633 )
						if( Money_Flow_Ratio <= 0.049337 )
							ret := -0.500000
						if( Money_Flow_Ratio > 0.049337 )
							if( MFI_High <= -70.5718 )
								if( Negative_Money_Flow_Sum <= 3.73589e+07 )
									ret := 0.428571
								if( Negative_Money_Flow_Sum > 3.73589e+07 )
									ret := 0.904762 // buy
							if( MFI_High > -70.5718 )
								ret := 0.000000
				if( MFI_Low > -10.182 )
					if( Negative_Money_Flow_Sum <= 2.02735e+07 )
						if( Negative_Money_Flow <= 6.92907e+06 )
							if( Raw_Money_Flow <= 2.64218e+06 )
								if( Negative_Money_Flow <= 2.49554e+06 )
									ret := -0.117871
								if( Negative_Money_Flow > 2.49554e+06 )
									ret := 0.263158
							if( Raw_Money_Flow > 2.64218e+06 )
								if( Typical_Price <= 0.080488 )
									ret := -0.443182
								if( Typical_Price > 0.080488 )
									ret := -0.064516
						if( Negative_Money_Flow > 6.92907e+06 )
							if( Raw_Money_Flow <= 9.08689e+06 )
								if( Positive_Money_Flow_Sum <= 6.06485e+06 )
									ret := 1.000000 // buy
								if( Positive_Money_Flow_Sum > 6.06485e+06 )
									ret := 0.500000
							if( Raw_Money_Flow > 9.08689e+06 )
								ret := -0.200000
					if( Negative_Money_Flow_Sum > 2.02735e+07 )
						if( VIP_VIM <= -0.699927 )
							if( MFI_Low <= -4.3684 )
								if( VIP_VIM <= -0.719944 )
									ret := -0.325000
								if( VIP_VIM > -0.719944 )
									ret := 0.625000
							if( MFI_Low > -4.3684 )
								if( Negative_Money_Flow <= 2.5504e+06 )
									ret := 1.000000 // buy
								if( Negative_Money_Flow > 2.5504e+06 )
									ret := 0.555556
						if( VIP_VIM > -0.699927 )
							if( Negative_Money_Flow_Sum <= 2.42285e+07 )
								if( VIM <= 1.1415 )
									ret := 0.400000
								if( VIM > 1.1415 )
									ret := -0.736842 // sell
							if( Negative_Money_Flow_Sum > 2.42285e+07 )
								if( MFI_High <= -59.337 )
									ret := -0.405941
								if( MFI_High > -59.337 )
									ret := 0.777778 // buy
		if( Positive_Money_Flow_Sum > 7.39298e+06 )
			if( MFI_High <= -13.6764 )
				if( Typical_Price <= 0.12043 )
					if( Positive_Money_Flow_Sum <= 2.11676e+08 )
						if( VIP_VIM <= 0.02781 )
							if( Negative_Money_Flow_Sum <= 1.82764e+08 )
								if( Positive_Money_Flow <= 1.31689e+06 )
									ret := 0.118831
								if( Positive_Money_Flow > 1.31689e+06 )
									ret := 0.021114
							if( Negative_Money_Flow_Sum > 1.82764e+08 )
								if( MFI_Low <= 18.8402 )
									ret := 0.780822 // buy
								if( MFI_Low > 18.8402 )
									ret := -0.687500
						if( VIP_VIM > 0.02781 )
							if( Negative_Money_Flow_Sum <= 8.46237e+06 )
								if( Raw_Money_Flow <= 2.85972e+06 )
									ret := 0.042200
								if( Raw_Money_Flow > 2.85972e+06 )
									ret := -0.481481
							if( Negative_Money_Flow_Sum > 8.46237e+06 )
								if( Positive_Money_Flow <= 1.88667e+07 )
									ret := 0.178784
								if( Positive_Money_Flow > 1.88667e+07 )
									ret := -0.472222
					if( Positive_Money_Flow_Sum > 2.11676e+08 )
						if( Negative_Money_Flow <= 1.53004e+07 )
							if( Typical_Price <= 0.078391 )
								ret := -0.750000 // sell
							if( Typical_Price > 0.078391 )
								ret := -1.000000 // sell
						if( Negative_Money_Flow > 1.53004e+07 )
							ret := -0.600000
				if( Typical_Price > 0.12043 )
					if( MFI <= 32.075 )
						if( VIM <= 1.20066 )
							if( Positive_Money_Flow_Sum <= 8.12073e+06 )
								if( VIM <= 1.13213 )
									ret := 0.923077 // buy
								if( VIM > 1.13213 )
									ret := -0.111111
							if( Positive_Money_Flow_Sum > 8.12073e+06 )
								if( Negative_Money_Flow_Sum <= 4.57601e+07 )
									ret := -0.170732
								if( Negative_Money_Flow_Sum > 4.57601e+07 )
									ret := -0.632558
						if( VIM > 1.20066 )
							if( MFI_Low <= 6.31804 )
								if( Negative_Money_Flow_Sum <= 1.06982e+08 )
									ret := -0.171429
								if( Negative_Money_Flow_Sum > 1.06982e+08 )
									ret := 0.684211
							if( MFI_Low > 6.31804 )
								if( Positive_Money_Flow_Sum <= 8.58317e+07 )
									ret := -0.517647
								if( Positive_Money_Flow_Sum > 8.58317e+07 )
									ret := 1.000000 // buy
					if( MFI > 32.075 )
						if( Negative_Money_Flow_Sum <= 1.51468e+08 )
							if( Positive_Money_Flow <= 9.11199e+06 )
								if( MFI_High <= -38.5294 )
									ret := -0.153846
								if( MFI_High > -38.5294 )
									ret := 0.068146
							if( Positive_Money_Flow > 9.11199e+06 )
								if( Positive_Money_Flow_Sum <= 2.00092e+08 )
									ret := -0.413669
								if( Positive_Money_Flow_Sum > 2.00092e+08 )
									ret := 0.675000
						if( Negative_Money_Flow_Sum > 1.51468e+08 )
							if( Positive_Money_Flow_Sum <= 2.3021e+08 )
								if( Positive_Money_Flow_Sum <= 8.68823e+07 )
									ret := 0.200000
								if( Positive_Money_Flow_Sum > 8.68823e+07 )
									ret := 0.824742 // buy
							if( Positive_Money_Flow_Sum > 2.3021e+08 )
								if( MFI_High <= -27.8828 )
									ret := -0.200000
								if( MFI_High > -27.8828 )
									ret := -1.000000 // sell
			if( MFI_High > -13.6764 )
				if( VIM <= 0.552591 )
					if( Positive_Money_Flow_Sum <= 2.25316e+07 )
						if( Positive_Money_Flow_Sum <= 8.58736e+06 )
							if( Positive_Money_Flow_Sum <= 8.36896e+06 )
								if( Negative_Money_Flow_Sum <= 936574 )
									ret := 0.750000 // buy
								if( Negative_Money_Flow_Sum > 936574 )
									ret := -0.200000
							if( Positive_Money_Flow_Sum > 8.36896e+06 )
								ret := 1.000000 // buy
						if( Positive_Money_Flow_Sum > 8.58736e+06 )
							if( Raw_Money_Flow <= 7.4008e+06 )
								if( Positive_Money_Flow_Sum <= 2.19834e+07 )
									ret := -0.149606
								if( Positive_Money_Flow_Sum > 2.19834e+07 )
									ret := 1.000000 // buy
							if( Raw_Money_Flow > 7.4008e+06 )
								if( VIM <= 0.448139 )
									ret := -1.000000 // sell
								if( VIM > 0.448139 )
									ret := -0.500000
					if( Positive_Money_Flow_Sum > 2.25316e+07 )
						if( Typical_Price <= 0.134042 )
							if( VIP <= 1.32172 )
								if( MFI_High <= 7.80622 )
									ret := -1.000000 // sell
								if( MFI_High > 7.80622 )
									ret := -0.750000 // sell
							if( VIP > 1.32172 )
								if( VIP <= 1.3982 )
									ret := -0.258065
								if( VIP > 1.3982 )
									ret := -0.731343 // sell
						if( Typical_Price > 0.134042 )
							if( VIM <= 0.510135 )
								if( VIP_VIM <= 0.882827 )
									ret := -1.000000 // sell
								if( VIP_VIM > 0.882827 )
									ret := 0.000000
							if( VIM > 0.510135 )
								ret := 1.000000 // buy
				if( VIM > 0.552591 )
					if( Negative_Money_Flow_Sum <= 2.95739e+06 )
						if( Positive_Money_Flow_Sum <= 2.12275e+07 )
							if( Raw_Money_Flow <= 591924 )
								if( VIP <= 1.09945 )
									ret := -0.571429
								if( VIP > 1.09945 )
									ret := -0.085616
							if( Raw_Money_Flow > 591924 )
								if( VIP <= 1.2857 )
									ret := 0.294118
								if( VIP > 1.2857 )
									ret := 0.100394
						if( Positive_Money_Flow_Sum > 2.12275e+07 )
							if( VIP <= 1.26059 )
								if( Positive_Money_Flow_Sum <= 2.41842e+07 )
									ret := 1.000000 // buy
								if( Positive_Money_Flow_Sum > 2.41842e+07 )
									ret := -0.250000
							if( VIP > 1.26059 )
								if( Positive_Money_Flow <= 1.10195e+06 )
									ret := 0.000000
								if( Positive_Money_Flow > 1.10195e+06 )
									ret := -0.717391 // sell
					if( Negative_Money_Flow_Sum > 2.95739e+06 )
						if( Positive_Money_Flow <= 3.43857e+07 )
							if( Raw_Money_Flow <= 1.10182e+07 )
								if( MFI <= 74.1895 )
									ret := -0.006632
								if( MFI > 74.1895 )
									ret := -0.132241
							if( Raw_Money_Flow > 1.10182e+07 )
								if( VIP <= 1.30045 )
									ret := 0.051903
								if( VIP > 1.30045 )
									ret := 0.500000
						if( Positive_Money_Flow > 3.43857e+07 )
							if( Negative_Money_Flow_Sum <= 4.7566e+07 )
								ret := 0.000000
							if( Negative_Money_Flow_Sum > 4.7566e+07 )
								ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_TRXUSDT_30Min_c0acde27(Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow, VIP_VIM, VIM, VIP)

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


