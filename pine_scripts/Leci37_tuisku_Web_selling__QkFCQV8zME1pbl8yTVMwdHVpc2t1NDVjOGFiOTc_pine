//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Stochastic_RSI
// ID_model: BABA_30Min_2MS0_45c8ab97 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_BABA_30Min_2MS0_45c8ab97", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_BABA_30Min_45c8ab97(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, rsi1, smoothK_k, d_k, k, d, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( Positive_Money_Flow_Sum <= 6.19676e+07 )
		if( rsi1 <= 80.5179 )
			if( Typical_Price <= 88.8708 )
				if( smoothK_k <= 5.23658 )
					if( MFI_High <= -76.439 )
						if( Negative_Money_Flow <= 1.75804e+08 )
							if( smoothD_d <= -1.00367 )
								if( MFI_High <= -79.4877 )
									ret := -0.555556
								if( MFI_High > -79.4877 )
									ret := -0.080000
							if( smoothD_d > -1.00367 )
								if( Money_Flow_Ratio <= 0.031553 )
									ret := 0.062992
								if( Money_Flow_Ratio > 0.031553 )
									ret := 0.714286 // buy
						if( Negative_Money_Flow > 1.75804e+08 )
							if( Raw_Money_Flow <= 2.98733e+08 )
								if( d <= 5.42661 )
									ret := 1.000000 // buy
								if( d > 5.42661 )
									ret := 0.777778 // buy
							if( Raw_Money_Flow > 2.98733e+08 )
								ret := 0.222222
					if( MFI_High > -76.439 )
						if( Positive_Money_Flow <= 3386.5 )
							if( MFI <= 33.6551 )
								if( smoothD_d <= 6.70916 )
									ret := -0.480663
								if( smoothD_d > 6.70916 )
									ret := 0.111111
							if( MFI > 33.6551 )
								if( d <= 7.55831 )
									ret := -0.148515
								if( d > 7.55831 )
									ret := 0.928571 // buy
						if( Positive_Money_Flow > 3386.5 )
							if( d_k <= -2.51939 )
								if( MFI_High <= -34.6907 )
									ret := 0.621622
								if( MFI_High > -34.6907 )
									ret := 0.000000
							if( d_k > -2.51939 )
								if( MFI <= 10.5249 )
									ret := -0.545455
								if( MFI > 10.5249 )
									ret := -0.014493
				if( smoothK_k > 5.23658 )
					if( Raw_Money_Flow <= 3.95248e+07 )
						if( Typical_Price <= 70.0203 )
							if( rsi1 <= 67.8251 )
								if( Negative_Money_Flow_Sum <= 1.77569e+08 )
									ret := 0.636905
								if( Negative_Money_Flow_Sum > 1.77569e+08 )
									ret := 0.037037
							if( rsi1 > 67.8251 )
								if( rsi1 <= 69.2151 )
									ret := -1.000000 // sell
								if( rsi1 > 69.2151 )
									ret := -0.095238
						if( Typical_Price > 70.0203 )
							if( MFI_High <= -18.1587 )
								if( Positive_Money_Flow_Sum <= 3.39254e+06 )
									ret := -0.062635
								if( Positive_Money_Flow_Sum > 3.39254e+06 )
									ret := 0.179894
							if( MFI_High > -18.1587 )
								if( MFI_Low <= 52.4222 )
									ret := -0.183280
								if( MFI_Low > 52.4222 )
									ret := 0.099125
					if( Raw_Money_Flow > 3.95248e+07 )
						if( Negative_Money_Flow <= 6.80597e+07 )
							if( MFI_High <= -75.0543 )
								if( Negative_Money_Flow_Sum <= 1.74729e+08 )
									ret := 0.800000 // buy
								if( Negative_Money_Flow_Sum > 1.74729e+08 )
									ret := -0.200000
							if( MFI_High > -75.0543 )
								if( Typical_Price <= 81.0077 )
									ret := -0.737705 // sell
								if( Typical_Price > 81.0077 )
									ret := 0.200000
						if( Negative_Money_Flow > 6.80597e+07 )
							if( Negative_Money_Flow_Sum <= 1.22431e+08 )
								if( MFI_High <= -71.9473 )
									ret := 0.517241
								if( MFI_High > -71.9473 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 1.22431e+08 )
								if( Negative_Money_Flow_Sum <= 1.50995e+08 )
									ret := -0.566667
								if( Negative_Money_Flow_Sum > 1.50995e+08 )
									ret := 0.060606
			if( Typical_Price > 88.8708 )
				if( d_k <= -5.51304 )
					if( Negative_Money_Flow <= 3.84539e+06 )
						if( Money_Flow_Ratio <= 1.83011 )
							if( rsi1 <= 61.2994 )
								if( Positive_Money_Flow_Sum <= 3.19973e+06 )
									ret := 0.321678
								if( Positive_Money_Flow_Sum > 3.19973e+06 )
									ret := -0.078261
							if( rsi1 > 61.2994 )
								if( smoothD_d <= 75.3766 )
									ret := -0.160000
								if( smoothD_d > 75.3766 )
									ret := -0.490196
						if( Money_Flow_Ratio > 1.83011 )
							if( d <= 29.098 )
								if( MFI_High <= -0.533612 )
									ret := -0.769841 // sell
								if( MFI_High > -0.533612 )
									ret := -0.071429
							if( d > 29.098 )
								if( Negative_Money_Flow_Sum <= 1.89472e+07 )
									ret := -0.182418
								if( Negative_Money_Flow_Sum > 1.89472e+07 )
									ret := 1.000000 // buy
					if( Negative_Money_Flow > 3.84539e+06 )
						if( Negative_Money_Flow <= 1.3212e+07 )
							if( Typical_Price <= 125.235 )
								if( smoothK_k <= 69.34 )
									ret := -0.938462 // sell
								if( smoothK_k > 69.34 )
									ret := -0.368421
							if( Typical_Price > 125.235 )
								if( Money_Flow_Ratio <= 1.83135 )
									ret := -0.390244
								if( Money_Flow_Ratio > 1.83135 )
									ret := 0.272727
						if( Negative_Money_Flow > 1.3212e+07 )
							if( MFI <= 5.84295 )
								if( Raw_Money_Flow <= 2.42001e+08 )
									ret := -0.080000
								if( Raw_Money_Flow > 2.42001e+08 )
									ret := -0.611765
							if( MFI > 5.84295 )
								if( rsi1 <= 39.6511 )
									ret := 0.295455
								if( rsi1 > 39.6511 )
									ret := -0.200000
				if( d_k > -5.51304 )
					if( Positive_Money_Flow_Sum <= 1.71169e+07 )
						if( Raw_Money_Flow <= 3.83851e+08 )
							if( MFI_High <= -17.8975 )
								if( k <= 45.5297 )
									ret := 0.000747
								if( k > 45.5297 )
									ret := -0.111070
							if( MFI_High > -17.8975 )
								if( Positive_Money_Flow_Sum <= 5.60013e+06 )
									ret := 0.541284
								if( Positive_Money_Flow_Sum > 5.60013e+06 )
									ret := 0.105417
						if( Raw_Money_Flow > 3.83851e+08 )
							if( smoothK_k <= 51.4485 )
								if( Typical_Price <= 232.912 )
									ret := -0.375000
								if( Typical_Price > 232.912 )
									ret := 0.222222
							if( smoothK_k > 51.4485 )
								if( rsi1 <= 42.6178 )
									ret := 0.894737 // buy
								if( rsi1 > 42.6178 )
									ret := -0.320000
					if( Positive_Money_Flow_Sum > 1.71169e+07 )
						if( d <= 18.0311 )
							if( MFI <= 5.09158 )
								if( Negative_Money_Flow <= 1.50368e+08 )
									ret := 0.416667
								if( Negative_Money_Flow > 1.50368e+08 )
									ret := -0.185984
							if( MFI > 5.09158 )
								if( Typical_Price <= 101.356 )
									ret := 0.000000
								if( Typical_Price > 101.356 )
									ret := -0.432836
						if( d > 18.0311 )
							if( k <= 7.92498 )
								if( MFI_Low <= 7.86448 )
									ret := 0.666667
								if( MFI_Low > 7.86448 )
									ret := -0.500000
							if( k > 7.92498 )
								if( Positive_Money_Flow_Sum <= 2.88206e+07 )
									ret := -0.143916
								if( Positive_Money_Flow_Sum > 2.88206e+07 )
									ret := -0.020889
		if( rsi1 > 80.5179 )
			if( MFI <= 10.2969 )
				if( MFI <= 4.07616 )
					if( rsi1 <= 82.705 )
						ret := 0.545455
					if( rsi1 > 82.705 )
						if( k <= 96.2653 )
							if( k <= 91.3717 )
								ret := 0.000000
							if( k > 91.3717 )
								ret := -0.111111
						if( k > 96.2653 )
							ret := 0.111111
				if( MFI > 4.07616 )
					if( Typical_Price <= 170.38 )
						if( Typical_Price <= 76.437 )
							ret := -0.411765
						if( Typical_Price > 76.437 )
							if( d_k <= -4.35009 )
								ret := -0.083333
							if( d_k > -4.35009 )
								ret := 0.444444
					if( Typical_Price > 170.38 )
						if( Negative_Money_Flow <= 184665 )
							ret := -0.285714
						if( Negative_Money_Flow > 184665 )
							if( smoothD_d <= 89.1912 )
								ret := -0.545455
							if( smoothD_d > 89.1912 )
								ret := -0.954545 // sell
			if( MFI > 10.2969 )
				if( Negative_Money_Flow_Sum <= 4.95628e+06 )
					if( Typical_Price <= 96.7725 )
						if( MFI_Low <= 64.6611 )
							if( Money_Flow_Ratio <= 4.41749 )
								ret := -0.058824
							if( Money_Flow_Ratio > 4.41749 )
								ret := -0.842105 // sell
						if( MFI_Low > 64.6611 )
							if( Typical_Price <= 74.9067 )
								ret := -0.090909
							if( Typical_Price > 74.9067 )
								if( Positive_Money_Flow_Sum <= 2.93719e+07 )
									ret := 0.868421 // buy
								if( Positive_Money_Flow_Sum > 2.93719e+07 )
									ret := 0.200000
					if( Typical_Price > 96.7725 )
						if( MFI_Low <= 73.2155 )
							if( Typical_Price <= 161.12 )
								if( smoothK_k <= 90.8901 )
									ret := -0.800000 // sell
								if( smoothK_k > 90.8901 )
									ret := -0.428571
							if( Typical_Price > 161.12 )
								if( d <= 92.5366 )
									ret := 0.125000
								if( d > 92.5366 )
									ret := -0.222222
						if( MFI_Low > 73.2155 )
							ret := -0.954545 // sell
				if( Negative_Money_Flow_Sum > 4.95628e+06 )
					if( Negative_Money_Flow_Sum <= 2.24905e+07 )
						if( smoothD_d <= 94.2952 )
							if( Positive_Money_Flow_Sum <= 3.71186e+07 )
								if( Positive_Money_Flow_Sum <= 2.75706e+07 )
									ret := 0.597156
								if( Positive_Money_Flow_Sum > 2.75706e+07 )
									ret := 0.905405 // buy
							if( Positive_Money_Flow_Sum > 3.71186e+07 )
								if( d_k <= 0.042474 )
									ret := 0.137931
								if( d_k > 0.042474 )
									ret := 0.620690
						if( smoothD_d > 94.2952 )
							if( MFI <= 59.1437 )
								if( d <= 98.3321 )
									ret := 0.230769
								if( d > 98.3321 )
									ret := 0.863636 // buy
							if( MFI > 59.1437 )
								if( MFI_Low <= 64.2185 )
									ret := -0.238095
								if( MFI_Low > 64.2185 )
									ret := 0.600000
					if( Negative_Money_Flow_Sum > 2.24905e+07 )
						if( Positive_Money_Flow_Sum <= 5.03047e+07 )
							if( k <= 99.7542 )
								if( Money_Flow_Ratio <= 0.747359 )
									ret := 0.455696
								if( Money_Flow_Ratio > 0.747359 )
									ret := 0.089744
							if( k > 99.7542 )
								ret := -0.411765
						if( Positive_Money_Flow_Sum > 5.03047e+07 )
							if( smoothK_k <= 93.1232 )
								if( Raw_Money_Flow <= 1.87411e+07 )
									ret := -0.882353 // sell
								if( Raw_Money_Flow > 1.87411e+07 )
									ret := -0.285714
							if( smoothK_k > 93.1232 )
								ret := -0.111111
	if( Positive_Money_Flow_Sum > 6.19676e+07 )
		if( MFI_Low <= -4.59777 )
			if( k <= 47.8368 )
				if( Negative_Money_Flow_Sum <= 5.4323e+09 )
					if( Positive_Money_Flow <= 2.63044e+06 )
						if( Negative_Money_Flow <= 3.26004e+06 )
							if( Typical_Price <= 89.9725 )
								if( Negative_Money_Flow_Sum <= 5.7971e+08 )
									ret := -0.285714
								if( Negative_Money_Flow_Sum > 5.7971e+08 )
									ret := 0.280000
							if( Typical_Price > 89.9725 )
								if( Positive_Money_Flow <= 99816.3 )
									ret := 0.600917
								if( Positive_Money_Flow > 99816.3 )
									ret := 0.360784
						if( Negative_Money_Flow > 3.26004e+06 )
							if( Negative_Money_Flow <= 7.41121e+07 )
								if( Negative_Money_Flow_Sum <= 1.97905e+09 )
									ret := -0.025641
								if( Negative_Money_Flow_Sum > 1.97905e+09 )
									ret := 0.640000
							if( Negative_Money_Flow > 7.41121e+07 )
								if( rsi1 <= 50.8327 )
									ret := 0.291587
								if( rsi1 > 50.8327 )
									ret := -0.104167
					if( Positive_Money_Flow > 2.63044e+06 )
						if( Positive_Money_Flow_Sum <= 4.26686e+08 )
							if( Negative_Money_Flow_Sum <= 6.75389e+08 )
								if( Typical_Price <= 129.663 )
									ret := 0.606557
								if( Typical_Price > 129.663 )
									ret := -0.142857
							if( Negative_Money_Flow_Sum > 6.75389e+08 )
								if( Negative_Money_Flow <= 598285 )
									ret := -0.047337
								if( Negative_Money_Flow > 598285 )
									ret := -0.700000 // sell
						if( Positive_Money_Flow_Sum > 4.26686e+08 )
							if( Raw_Money_Flow <= 1.87331e+08 )
								ret := 0.166667
							if( Raw_Money_Flow > 1.87331e+08 )
								if( k <= 6.38672 )
									ret := 0.400000
								if( k > 6.38672 )
									ret := 0.944444 // buy
				if( Negative_Money_Flow_Sum > 5.4323e+09 )
					if( d_k <= 0.246563 )
						ret := 0.666667
					if( d_k > 0.246563 )
						ret := 1.000000 // buy
			if( k > 47.8368 )
				if( Positive_Money_Flow_Sum <= 1.75627e+08 )
					if( Raw_Money_Flow <= 7.83702e+08 )
						if( Negative_Money_Flow <= 6.44933e+08 )
							if( Negative_Money_Flow <= 4.3906e+08 )
								if( MFI_Low <= -12.2671 )
									ret := -0.392405
								if( MFI_Low > -12.2671 )
									ret := 0.177474
							if( Negative_Money_Flow > 4.3906e+08 )
								if( Negative_Money_Flow <= 5.346e+08 )
									ret := 1.000000 // buy
								if( Negative_Money_Flow > 5.346e+08 )
									ret := 0.583333
						if( Negative_Money_Flow > 6.44933e+08 )
							if( Typical_Price <= 170.426 )
								ret := -1.000000 // sell
							if( Typical_Price > 170.426 )
								ret := -0.909091 // sell
					if( Raw_Money_Flow > 7.83702e+08 )
						if( Raw_Money_Flow <= 1.06617e+09 )
							if( smoothD_d <= 65.7855 )
								ret := 0.571429
							if( smoothD_d > 65.7855 )
								if( Positive_Money_Flow_Sum <= 7.59388e+07 )
									ret := 0.846154 // buy
								if( Positive_Money_Flow_Sum > 7.59388e+07 )
									ret := 1.000000 // buy
						if( Raw_Money_Flow > 1.06617e+09 )
							if( Negative_Money_Flow_Sum <= 1.27916e+09 )
								ret := -0.900000 // sell
							if( Negative_Money_Flow_Sum > 1.27916e+09 )
								ret := 0.733333 // buy
				if( Positive_Money_Flow_Sum > 1.75627e+08 )
					if( Positive_Money_Flow_Sum <= 4.48616e+08 )
						if( Positive_Money_Flow <= 66231.2 )
							if( rsi1 <= 22.8396 )
								ret := 0.944444 // buy
							if( rsi1 > 22.8396 )
								if( MFI_High <= -71.8367 )
									ret := -0.823529 // sell
								if( MFI_High > -71.8367 )
									ret := -0.217822
						if( Positive_Money_Flow > 66231.2 )
							if( MFI_Low <= -9.66499 )
								ret := 0.090909
							if( MFI_Low > -9.66499 )
								if( Typical_Price <= 215.802 )
									ret := -0.815385 // sell
								if( Typical_Price > 215.802 )
									ret := 0.083333
					if( Positive_Money_Flow_Sum > 4.48616e+08 )
						if( Negative_Money_Flow_Sum <= 5.27048e+09 )
							if( MFI_Low <= -5.89407 )
								ret := 0.882353 // buy
							if( MFI_Low > -5.89407 )
								ret := 0.300000
						if( Negative_Money_Flow_Sum > 5.27048e+09 )
							ret := -0.100000
		if( MFI_Low > -4.59777 )
			if( Raw_Money_Flow <= 1.32061e+06 )
				if( rsi1 <= 72.6979 )
					if( Typical_Price <= 125.063 )
						if( Money_Flow_Ratio <= 172.468 )
							if( Positive_Money_Flow <= 298182 )
								if( MFI <= 23.3803 )
									ret := -0.134091
								if( MFI > 23.3803 )
									ret := 0.056303
							if( Positive_Money_Flow > 298182 )
								if( rsi1 <= 65.1198 )
									ret := -0.022265
								if( rsi1 > 65.1198 )
									ret := -0.236776
						if( Money_Flow_Ratio > 172.468 )
							if( d_k <= -3.23767 )
								ret := -0.363636
							if( d_k > -3.23767 )
								if( MFI_High <= 19.8259 )
									ret := 0.753846 // buy
								if( MFI_High > 19.8259 )
									ret := 0.000000
					if( Typical_Price > 125.063 )
						if( rsi1 <= 69.0764 )
							if( smoothK_k <= 87.7626 )
								if( Negative_Money_Flow_Sum <= 2.04531e+09 )
									ret := 0.109780
								if( Negative_Money_Flow_Sum > 2.04531e+09 )
									ret := 0.437870
							if( smoothK_k > 87.7626 )
								if( Typical_Price <= 138.246 )
									ret := -0.466667
								if( Typical_Price > 138.246 )
									ret := -0.006165
						if( rsi1 > 69.0764 )
							if( d_k <= -16.5484 )
								if( d_k <= -19.6861 )
									ret := 0.478261
								if( d_k > -19.6861 )
									ret := 0.863636 // buy
							if( d_k > -16.5484 )
								if( Negative_Money_Flow_Sum <= 1.06663e+07 )
									ret := -0.307692
								if( Negative_Money_Flow_Sum > 1.06663e+07 )
									ret := 0.242500
				if( rsi1 > 72.6979 )
					if( rsi1 <= 73.3341 )
						if( MFI_Low <= 52.7907 )
							if( Raw_Money_Flow <= 606144 )
								if( k <= 64.3117 )
									ret := -0.454545
								if( k > 64.3117 )
									ret := 0.225000
							if( Raw_Money_Flow > 606144 )
								if( Typical_Price <= 168.251 )
									ret := -0.761905 // sell
								if( Typical_Price > 168.251 )
									ret := 0.200000
						if( MFI_Low > 52.7907 )
							if( Negative_Money_Flow_Sum <= 1.27907e+07 )
								ret := 0.000000
							if( Negative_Money_Flow_Sum > 1.27907e+07 )
								if( Typical_Price <= 87.4033 )
									ret := -0.857143 // sell
								if( Typical_Price > 87.4033 )
									ret := -0.461538
					if( rsi1 > 73.3341 )
						if( Positive_Money_Flow_Sum <= 4.77071e+08 )
							if( d <= 95.9216 )
								if( Positive_Money_Flow_Sum <= 3.98628e+08 )
									ret := 0.062147
								if( Positive_Money_Flow_Sum > 3.98628e+08 )
									ret := 0.380597
							if( d > 95.9216 )
								if( rsi1 <= 74.2127 )
									ret := -0.615385
								if( rsi1 > 74.2127 )
									ret := -0.071429
						if( Positive_Money_Flow_Sum > 4.77071e+08 )
							if( Typical_Price <= 94.7722 )
								if( rsi1 <= 79.0503 )
									ret := -0.586957
								if( rsi1 > 79.0503 )
									ret := -0.183908
							if( Typical_Price > 94.7722 )
								if( MFI_High <= 3.28393 )
									ret := -0.126126
								if( MFI_High > 3.28393 )
									ret := 0.067327
			if( Raw_Money_Flow > 1.32061e+06 )
				if( Money_Flow_Ratio <= 3.41435 )
					if( Positive_Money_Flow_Sum <= 1.83809e+09 )
						if( MFI <= 35.0047 )
							if( d_k <= 8.57656 )
								if( rsi1 <= 48.469 )
									ret := 0.035723
								if( rsi1 > 48.469 )
									ret := -0.089028
							if( d_k > 8.57656 )
								if( d <= 85.6218 )
									ret := 0.149153
								if( d > 85.6218 )
									ret := -0.305556
						if( MFI > 35.0047 )
							if( d_k <= 20.2801 )
								if( MFI_Low <= 56.3872 )
									ret := -0.027438
								if( MFI_Low > 56.3872 )
									ret := 0.128878
							if( d_k > 20.2801 )
								if( Money_Flow_Ratio <= 1.45666 )
									ret := 0.199612
								if( Money_Flow_Ratio > 1.45666 )
									ret := -0.028986
					if( Positive_Money_Flow_Sum > 1.83809e+09 )
						if( smoothD_d <= 94.9969 )
							if( Raw_Money_Flow <= 1.6397e+08 )
								if( Typical_Price <= 205.237 )
									ret := 0.409142
								if( Typical_Price > 205.237 )
									ret := 0.050943
							if( Raw_Money_Flow > 1.6397e+08 )
								if( MFI <= 26.6121 )
									ret := 0.804878 // buy
								if( MFI > 26.6121 )
									ret := 0.013041
						if( smoothD_d > 94.9969 )
							if( MFI <= 44.732 )
								if( rsi1 <= 31.6563 )
									ret := -0.400000
								if( rsi1 > 31.6563 )
									ret := -1.000000 // sell
							if( MFI > 44.732 )
								if( rsi1 <= 53.2109 )
									ret := 0.700000 // buy
								if( rsi1 > 53.2109 )
									ret := -0.220588
				if( Money_Flow_Ratio > 3.41435 )
					if( Positive_Money_Flow <= 5.84026e+07 )
						if( Money_Flow_Ratio <= 100.878 )
							if( Positive_Money_Flow <= 5533.37 )
								if( rsi1 <= 68.5934 )
									ret := -0.103338
								if( rsi1 > 68.5934 )
									ret := 0.091222
							if( Positive_Money_Flow > 5533.37 )
								if( Typical_Price <= 195.028 )
									ret := -0.083736
								if( Typical_Price > 195.028 )
									ret := -0.412338
						if( Money_Flow_Ratio > 100.878 )
							if( Raw_Money_Flow <= 2.69157e+06 )
								if( Raw_Money_Flow <= 2.42174e+06 )
									ret := -0.229299
								if( Raw_Money_Flow > 2.42174e+06 )
									ret := 0.473684
							if( Raw_Money_Flow > 2.69157e+06 )
								if( smoothD_d <= 91.6512 )
									ret := -0.570681
								if( smoothD_d > 91.6512 )
									ret := -0.208333
					if( Positive_Money_Flow > 5.84026e+07 )
						if( rsi1 <= 63.76 )
							if( d <= 33.1093 )
								if( Positive_Money_Flow_Sum <= 1.10445e+08 )
									ret := 0.818182 // buy
								if( Positive_Money_Flow_Sum > 1.10445e+08 )
									ret := -0.301090
							if( d > 33.1093 )
								if( rsi1 <= 56.0582 )
									ret := 0.048601
								if( rsi1 > 56.0582 )
									ret := -0.179039
						if( rsi1 > 63.76 )
							if( MFI <= 99.1325 )
								if( Negative_Money_Flow_Sum <= 6.51034e+06 )
									ret := 0.286260
								if( Negative_Money_Flow_Sum > 6.51034e+06 )
									ret := -0.012195
							if( MFI > 99.1325 )
								if( Money_Flow_Ratio <= 482.548 )
									ret := 0.354212
								if( Money_Flow_Ratio > 482.548 )
									ret := -0.081633
	
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
float op_operation = decision_tree_0_BABA_30Min_45c8ab97(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, rsi1, smoothK_k, d_k, k, d, smoothD_d)

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


