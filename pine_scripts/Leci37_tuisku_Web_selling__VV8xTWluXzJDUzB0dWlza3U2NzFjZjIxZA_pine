//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Stochastic_RSI
// ID_model: U_1Min_2CS0_671cf21d Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_2CS0_671cf21d", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_671cf21d(ad_mf, mf, ad, rsi1, d, k, smoothD_d, d_k, smoothK_k)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ad_mf <= 89.4038 )
		if( rsi1 <= 49.7892 )
			if( ad <= -3342.89 )
				if( rsi1 <= 28.5007 )
					if( ad <= -245282 )
						if( mf <= -0.477574 )
							ret := 0.571429
						if( mf > -0.477574 )
							if( ad <= -293527 )
								ret := 1.000000 // buy
							if( ad > -293527 )
								ret := 0.714286 // buy
					if( ad > -245282 )
						if( ad <= -3880.19 )
							if( ad <= -3928.07 )
								if( k <= 0.144788 )
									ret := -0.031603
								if( k > 0.144788 )
									ret := 0.115412
							if( ad > -3928.07 )
								if( smoothK_k <= 30.6598 )
									ret := -0.625000
								if( smoothK_k > 30.6598 )
									ret := -1.000000 // sell
						if( ad > -3880.19 )
							if( ad <= -3461.93 )
								if( d <= 21.3873 )
									ret := 0.365079
								if( d > 21.3873 )
									ret := 0.703704 // buy
							if( ad > -3461.93 )
								if( ad_mf <= -3441.99 )
									ret := -0.625000
								if( ad_mf > -3441.99 )
									ret := 0.352941
				if( rsi1 > 28.5007 )
					if( k <= 34.7371 )
						if( ad <= -6044.5 )
							if( ad_mf <= -6149.51 )
								if( ad <= -151414 )
									ret := 0.642857
								if( ad > -151414 )
									ret := 0.024621
							if( ad_mf > -6149.51 )
								if( mf <= 0.013914 )
									ret := 0.722222 // buy
								if( mf > 0.013914 )
									ret := 0.375000
						if( ad > -6044.5 )
							if( ad_mf <= -5852.32 )
								if( smoothD_d <= -0.870065 )
									ret := 0.000000
								if( smoothD_d > -0.870065 )
									ret := -0.442857
							if( ad_mf > -5852.32 )
								if( mf <= -0.276905 )
									ret := 0.213115
								if( mf > -0.276905 )
									ret := -0.115900
					if( k > 34.7371 )
						if( ad <= -19258.2 )
							if( ad_mf <= -521608 )
								ret := 1.000000 // buy
							if( ad_mf > -521608 )
								if( mf <= 0.364607 )
									ret := 0.155193
								if( mf > 0.364607 )
									ret := -0.750000 // sell
						if( ad > -19258.2 )
							if( ad_mf <= -18066.2 )
								if( mf <= 0.177017 )
									ret := -0.362319
								if( mf > 0.177017 )
									ret := 1.000000 // buy
							if( ad_mf > -18066.2 )
								if( d <= 94.5662 )
									ret := 0.068360
								if( d > 94.5662 )
									ret := -0.222222
			if( ad > -3342.89 )
				if( d <= 47.1783 )
					if( d_k <= 2.66075 )
						if( ad_mf <= -2994.08 )
							if( k <= 47.0148 )
								if( ad_mf <= -3060.71 )
									ret := 0.400000
								if( ad_mf > -3060.71 )
									ret := 0.727273 // buy
							if( k > 47.0148 )
								if( mf <= -0.138888 )
									ret := -0.500000
								if( mf > -0.138888 )
									ret := 0.000000
						if( ad_mf > -2994.08 )
							if( mf <= -0.561643 )
								if( smoothD_d <= 17.1694 )
									ret := 0.629032
								if( smoothD_d > 17.1694 )
									ret := -0.037037
							if( mf > -0.561643 )
								if( d_k <= -22.2547 )
									ret := -0.279412
								if( d_k > -22.2547 )
									ret := 0.088459
					if( d_k > 2.66075 )
						if( smoothK_k <= 25.2503 )
							if( smoothD_d <= 37.3778 )
								if( mf <= -0.154395 )
									ret := 0.289130
								if( mf > -0.154395 )
									ret := 0.174559
							if( smoothD_d > 37.3778 )
								if( ad_mf <= -0.377111 )
									ret := 0.240000
								if( ad_mf > -0.377111 )
									ret := 0.587786
						if( smoothK_k > 25.2503 )
							if( rsi1 <= 42.3481 )
								if( ad_mf <= -0.28187 )
									ret := -0.013514
								if( ad_mf > -0.28187 )
									ret := -0.324324
							if( rsi1 > 42.3481 )
								if( rsi1 <= 43.0467 )
									ret := 0.620690
								if( rsi1 > 43.0467 )
									ret := 0.145161
				if( d > 47.1783 )
					if( ad <= -1577.54 )
						if( smoothK_k <= 88.2625 )
							if( rsi1 <= 36.8107 )
								if( d_k <= -10.0773 )
									ret := 0.347826
								if( d_k > -10.0773 )
									ret := -0.173913
							if( rsi1 > 36.8107 )
								if( ad <= -1706.7 )
									ret := 0.278302
								if( ad > -1706.7 )
									ret := -0.225000
						if( smoothK_k > 88.2625 )
							if( k <= 95.3572 )
								if( k <= 93.7382 )
									ret := -0.333333
								if( k > 93.7382 )
									ret := -0.800000 // sell
							if( k > 95.3572 )
								ret := 0.000000
					if( ad > -1577.54 )
						if( d_k <= 17.5859 )
							if( d_k <= 13.2862 )
								if( k <= 46.2166 )
									ret := 0.000000
								if( k > 46.2166 )
									ret := 0.292002
							if( d_k > 13.2862 )
								if( smoothK_k <= 57.3479 )
									ret := 0.187817
								if( smoothK_k > 57.3479 )
									ret := -0.296296
						if( d_k > 17.5859 )
							if( smoothD_d <= 58.0019 )
								if( smoothD_d <= 51.8347 )
									ret := 0.376147
								if( smoothD_d > 51.8347 )
									ret := 0.689394
							if( smoothD_d > 58.0019 )
								if( d <= 65.682 )
									ret := -0.250000
								if( d > 65.682 )
									ret := 0.462687
		if( rsi1 > 49.7892 )
			if( ad <= -271.61 )
				if( ad_mf <= -101430 )
					if( d_k <= 12.8742 )
						if( rsi1 <= 53.306 )
							if( ad_mf <= -114033 )
								if( ad_mf <= -121565 )
									ret := 0.095238
								if( ad_mf > -121565 )
									ret := 1.000000 // buy
							if( ad_mf > -114033 )
								if( d <= 58.9392 )
									ret := -1.000000 // sell
								if( d > 58.9392 )
									ret := 0.000000
						if( rsi1 > 53.306 )
							if( ad_mf <= -291499 )
								if( d_k <= 3.93917 )
									ret := 0.300000
								if( d_k > 3.93917 )
									ret := -0.666667
							if( ad_mf > -291499 )
								if( d_k <= 10.7303 )
									ret := 0.710145 // buy
								if( d_k > 10.7303 )
									ret := 0.000000
					if( d_k > 12.8742 )
						if( d <= 65.3021 )
							if( ad <= -127802 )
								if( ad <= -287759 )
									ret := -0.750000 // sell
								if( ad > -287759 )
									ret := 0.900000 // buy
							if( ad > -127802 )
								ret := -0.714286 // sell
						if( d > 65.3021 )
							if( k <= 55.8659 )
								ret := -1.000000 // sell
							if( k > 55.8659 )
								ret := -0.750000 // sell
				if( ad_mf > -101430 )
					if( ad_mf <= -88746.9 )
						if( d_k <= 3.98617 )
							if( mf <= 0.11629 )
								if( mf <= -0.132333 )
									ret := -0.571429
								if( mf > -0.132333 )
									ret := 0.000000
							if( mf > 0.11629 )
								ret := -0.800000 // sell
						if( d_k > 3.98617 )
							if( d_k <= 14.1289 )
								if( rsi1 <= 65.0706 )
									ret := -1.000000 // sell
								if( rsi1 > 65.0706 )
									ret := -0.750000 // sell
							if( d_k > 14.1289 )
								ret := -0.500000
					if( ad_mf > -88746.9 )
						if( rsi1 <= 59.2763 )
							if( k <= 34.1886 )
								if( mf <= 0.150903 )
									ret := 0.093966
								if( mf > 0.150903 )
									ret := -0.115288
							if( k > 34.1886 )
								if( d_k <= -13.1605 )
									ret := -0.003802
								if( d_k > -13.1605 )
									ret := 0.164692
						if( rsi1 > 59.2763 )
							if( ad_mf <= -41878.4 )
								if( smoothD_d <= 50.6973 )
									ret := -0.272727
								if( smoothD_d > 50.6973 )
									ret := 0.319549
							if( ad_mf > -41878.4 )
								if( ad_mf <= -41342.5 )
									ret := -0.900000 // sell
								if( ad_mf > -41342.5 )
									ret := 0.038339
			if( ad > -271.61 )
				if( d_k <= -4.88933 )
					if( k <= 22.3034 )
						if( ad_mf <= -0.07773 )
							if( rsi1 <= 65.9063 )
								if( smoothD_d <= 3.9449 )
									ret := -0.560000
								if( smoothD_d > 3.9449 )
									ret := -0.851064 // sell
							if( rsi1 > 65.9063 )
								ret := 0.166667
						if( ad_mf > -0.07773 )
							if( smoothD_d <= 3.13301 )
								if( smoothD_d <= 1.36658 )
									ret := -0.200000
								if( smoothD_d > 1.36658 )
									ret := 0.857143 // buy
							if( smoothD_d > 3.13301 )
								if( d <= 7.81578 )
									ret := -0.857143 // sell
								if( d > 7.81578 )
									ret := -0.093750
					if( k > 22.3034 )
						if( ad_mf <= 62.1442 )
							if( rsi1 <= 50.6323 )
								if( rsi1 <= 50.3824 )
									ret := -0.017422
								if( rsi1 > 50.3824 )
									ret := 0.647059
							if( rsi1 > 50.6323 )
								if( d <= 92.8425 )
									ret := -0.161792
								if( d > 92.8425 )
									ret := 0.288889
						if( ad_mf > 62.1442 )
							if( ad_mf <= 75.3358 )
								ret := 1.000000 // buy
							if( ad_mf > 75.3358 )
								ret := 0.200000
				if( d_k > -4.88933 )
					if( ad_mf <= 0.200881 )
						if( d_k <= 5.34567 )
							if( rsi1 <= 77.8494 )
								if( d_k <= 2.36758 )
									ret := -0.065094
								if( d_k > 2.36758 )
									ret := -0.194012
							if( rsi1 > 77.8494 )
								if( d <= 98.4527 )
									ret := 0.263158
								if( d > 98.4527 )
									ret := -0.146067
						if( d_k > 5.34567 )
							if( rsi1 <= 61.5651 )
								if( mf <= 0.173925 )
									ret := 0.027619
								if( mf > 0.173925 )
									ret := 0.178922
							if( rsi1 > 61.5651 )
								if( smoothD_d <= 75.0217 )
									ret := -0.010453
								if( smoothD_d > 75.0217 )
									ret := -0.220588
					if( ad_mf > 0.200881 )
						if( k <= 38.5072 )
							if( smoothD_d <= 30.6269 )
								if( mf <= -0.20333 )
									ret := 0.154545
								if( mf > -0.20333 )
									ret := -0.555556
							if( smoothD_d > 30.6269 )
								if( d_k <= -1.40308 )
									ret := -0.900000 // sell
								if( d_k > -1.40308 )
									ret := -0.232558
						if( k > 38.5072 )
							if( ad <= 57.5723 )
								if( mf <= -0.762173 )
									ret := -0.636364
								if( mf > -0.762173 )
									ret := 0.143791
							if( ad > 57.5723 )
								if( rsi1 <= 68.8976 )
									ret := 0.235294
								if( rsi1 > 68.8976 )
									ret := 0.944444 // buy
	if( ad_mf > 89.4038 )
		if( ad_mf <= 4288.68 )
			if( d_k <= -2.34248 )
				if( rsi1 <= 57.1752 )
					if( ad_mf <= 1679.49 )
						if( ad_mf <= 109.677 )
							if( ad_mf <= 96.311 )
								ret := -0.500000
							if( ad_mf > 96.311 )
								if( d_k <= -21.7327 )
									ret := -0.750000 // sell
								if( d_k > -21.7327 )
									ret := -1.000000 // sell
						if( ad_mf > 109.677 )
							if( ad <= 864.678 )
								if( mf <= 0.306914 )
									ret := -0.063694
								if( mf > 0.306914 )
									ret := 0.459459
							if( ad > 864.678 )
								if( rsi1 <= 46.6866 )
									ret := -0.125000
								if( rsi1 > 46.6866 )
									ret := -0.318182
					if( ad_mf > 1679.49 )
						if( ad <= 3870.64 )
							if( ad_mf <= 2546.11 )
								if( rsi1 <= 45.2783 )
									ret := 0.276860
								if( rsi1 > 45.2783 )
									ret := 0.036000
							if( ad_mf > 2546.11 )
								if( smoothK_k <= 39.491 )
									ret := -0.106195
								if( smoothK_k > 39.491 )
									ret := 0.100649
						if( ad > 3870.64 )
							if( ad <= 4094.74 )
								if( smoothD_d <= 33.0773 )
									ret := -0.577320
								if( smoothD_d > 33.0773 )
									ret := -0.166667
							if( ad > 4094.74 )
								if( d <= 45.9959 )
									ret := 0.235294
								if( d > 45.9959 )
									ret := -0.566667
				if( rsi1 > 57.1752 )
					if( ad <= 455.596 )
						if( ad <= 292.906 )
							if( smoothK_k <= 74.6707 )
								if( k <= 48.5394 )
									ret := 0.000000
								if( k > 48.5394 )
									ret := -0.846154 // sell
							if( smoothK_k > 74.6707 )
								if( mf <= -0.175236 )
									ret := -0.500000
								if( mf > -0.175236 )
									ret := 0.222222
						if( ad > 292.906 )
							if( d_k <= -4.16411 )
								if( smoothD_d <= 72.3909 )
									ret := 0.675000
								if( smoothD_d > 72.3909 )
									ret := 0.166667
							if( d_k > -4.16411 )
								if( rsi1 <= 59.9967 )
									ret := -0.700000 // sell
								if( rsi1 > 59.9967 )
									ret := 0.166667
					if( ad > 455.596 )
						if( ad_mf <= 2837.23 )
							if( ad_mf <= 1897.82 )
								if( ad <= 1265.84 )
									ret := -0.331183
								if( ad > 1265.84 )
									ret := -0.026217
							if( ad_mf > 1897.82 )
								if( d <= 92.9237 )
									ret := -0.424658
								if( d > 92.9237 )
									ret := -0.111111
						if( ad_mf > 2837.23 )
							if( ad <= 3699.2 )
								if( ad_mf <= 2963.54 )
									ret := 0.536585
								if( ad_mf > 2963.54 )
									ret := 0.016393
							if( ad > 3699.2 )
								if( mf <= 0.10832 )
									ret := -0.240964
								if( mf > 0.10832 )
									ret := -0.535211
			if( d_k > -2.34248 )
				if( ad_mf <= 600.913 )
					if( ad_mf <= 358.952 )
						if( ad_mf <= 323.06 )
							if( ad_mf <= 221.765 )
								if( mf <= 0.0152 )
									ret := -0.067416
								if( mf > 0.0152 )
									ret := 0.373134
							if( ad_mf > 221.765 )
								if( d <= 12.3957 )
									ret := 0.500000
								if( d > 12.3957 )
									ret := -0.274074
						if( ad_mf > 323.06 )
							if( smoothK_k <= 87.0124 )
								if( mf <= 0.334581 )
									ret := 0.222222
								if( mf > 0.334581 )
									ret := 1.000000 // buy
							if( smoothK_k > 87.0124 )
								if( ad <= 350.949 )
									ret := 0.750000 // buy
								if( ad > 350.949 )
									ret := 1.000000 // buy
					if( ad_mf > 358.952 )
						if( ad <= 409.024 )
							if( k <= 97.1031 )
								if( smoothD_d <= 87.666 )
									ret := -0.647887
								if( smoothD_d > 87.666 )
									ret := -0.125000
							if( k > 97.1031 )
								ret := 0.750000 // buy
						if( ad > 409.024 )
							if( ad_mf <= 453.168 )
								if( d_k <= 14.5846 )
									ret := 0.052632
								if( d_k > 14.5846 )
									ret := 0.600000
							if( ad_mf > 453.168 )
								if( smoothD_d <= 51.8213 )
									ret := -0.185185
								if( smoothD_d > 51.8213 )
									ret := -0.500000
				if( ad_mf > 600.913 )
					if( mf <= -0.100678 )
						if( ad <= 1365.9 )
							if( ad <= 672.104 )
								if( rsi1 <= 45.8715 )
									ret := 0.785714 // buy
								if( rsi1 > 45.8715 )
									ret := 0.307692
							if( ad > 672.104 )
								if( mf <= -0.273916 )
									ret := 0.368421
								if( mf > -0.273916 )
									ret := 0.102804
						if( ad > 1365.9 )
							if( d <= 76.3448 )
								if( k <= 7.47413 )
									ret := 0.185430
								if( k > 7.47413 )
									ret := -0.151282
							if( d > 76.3448 )
								if( ad_mf <= 4232.16 )
									ret := 0.166667
								if( ad_mf > 4232.16 )
									ret := -1.000000 // sell
					if( mf > -0.100678 )
						if( ad <= 2581.12 )
							if( ad_mf <= 2549.05 )
								if( ad_mf <= 1057.85 )
									ret := 0.008147
								if( ad_mf > 1057.85 )
									ret := -0.104575
							if( ad_mf > 2549.05 )
								if( d_k <= 6.81154 )
									ret := -0.758621 // sell
								if( d_k > 6.81154 )
									ret := 0.000000
						if( ad > 2581.12 )
							if( ad <= 4210.74 )
								if( ad_mf <= 4127.19 )
									ret := 0.016272
								if( ad_mf > 4127.19 )
									ret := 0.333333
							if( ad > 4210.74 )
								if( smoothD_d <= 89.0861 )
									ret := -0.486486
								if( smoothD_d > 89.0861 )
									ret := 0.272727
		if( ad_mf > 4288.68 )
			if( mf <= -0.430281 )
				if( ad_mf <= 27139.7 )
					if( rsi1 <= 32.8857 )
						if( ad_mf <= 9895.25 )
							if( rsi1 <= 25.1802 )
								if( ad_mf <= 5952.26 )
									ret := 0.166667
								if( ad_mf > 5952.26 )
									ret := 1.000000 // buy
							if( rsi1 > 25.1802 )
								ret := 0.000000
						if( ad_mf > 9895.25 )
							if( smoothD_d <= 12.3341 )
								if( smoothD_d <= 8.34939 )
									ret := 0.000000
								if( smoothD_d > 8.34939 )
									ret := -0.500000
							if( smoothD_d > 12.3341 )
								if( smoothD_d <= 19.4051 )
									ret := 0.500000
								if( smoothD_d > 19.4051 )
									ret := 0.000000
					if( rsi1 > 32.8857 )
						if( ad_mf <= 6653.55 )
							if( ad_mf <= 6194.02 )
								if( smoothD_d <= 82.9709 )
									ret := 0.611111
								if( smoothD_d > 82.9709 )
									ret := -0.250000
							if( ad_mf > 6194.02 )
								ret := -0.600000
						if( ad_mf > 6653.55 )
							if( d_k <= -5.02486 )
								if( d_k <= -11.2447 )
									ret := 0.680000
								if( d_k > -11.2447 )
									ret := -0.333333
							if( d_k > -5.02486 )
								if( d <= 55.7794 )
									ret := 0.962963 // buy
								if( d > 55.7794 )
									ret := 0.444444
				if( ad_mf > 27139.7 )
					if( d <= 50.5881 )
						if( ad_mf <= 29222.5 )
							ret := 1.000000 // buy
						if( ad_mf > 29222.5 )
							if( mf <= -0.475969 )
								ret := 0.714286 // buy
							if( mf > -0.475969 )
								ret := 0.200000
					if( d > 50.5881 )
						ret := 1.000000 // buy
			if( mf > -0.430281 )
				if( rsi1 <= 67.8064 )
					if( ad_mf <= 255823 )
						if( d <= 97.025 )
							if( rsi1 <= 27.2471 )
								if( d <= 24.64 )
									ret := 0.191315
								if( d > 24.64 )
									ret := -0.172185
							if( rsi1 > 27.2471 )
								if( mf <= 0.115695 )
									ret := -0.007776
								if( mf > 0.115695 )
									ret := 0.050722
						if( d > 97.025 )
							if( ad <= 4612.47 )
								if( d <= 97.8317 )
									ret := -0.250000
								if( d > 97.8317 )
									ret := -0.888889 // sell
							if( ad > 4612.47 )
								if( ad <= 5125.82 )
									ret := 0.368421
								if( ad > 5125.82 )
									ret := -0.161049
					if( ad_mf > 255823 )
						if( rsi1 <= 34.5868 )
							ret := 0.142857
						if( rsi1 > 34.5868 )
							if( ad_mf <= 519331 )
								if( smoothD_d <= 27.4362 )
									ret := -0.888889 // sell
								if( smoothD_d > 27.4362 )
									ret := -0.083333
							if( ad_mf > 519331 )
								if( mf <= 0.377698 )
									ret := -0.958333 // sell
								if( mf > 0.377698 )
									ret := -0.500000
				if( rsi1 > 67.8064 )
					if( ad <= 74002.8 )
						if( d_k <= -0.907862 )
							if( ad_mf <= 54533.9 )
								if( smoothD_d <= 85.6484 )
									ret := 0.267070
								if( smoothD_d > 85.6484 )
									ret := 0.124814
							if( ad_mf > 54533.9 )
								if( d <= 50.5483 )
									ret := -0.384615
								if( d > 50.5483 )
									ret := 0.669811
						if( d_k > -0.907862 )
							if( ad <= 69466.8 )
								if( ad <= 52165 )
									ret := 0.036697
								if( ad > 52165 )
									ret := -0.360000
							if( ad > 69466.8 )
								if( rsi1 <= 69.7508 )
									ret := 0.250000
								if( rsi1 > 69.7508 )
									ret := 0.882353 // buy
					if( ad > 74002.8 )
						if( mf <= 0.213433 )
							if( smoothD_d <= 86.7634 )
								if( ad <= 77833.6 )
									ret := -0.428571
								if( ad > 77833.6 )
									ret := 0.532258
							if( smoothD_d > 86.7634 )
								if( ad <= 103307 )
									ret := -0.714286 // sell
								if( ad > 103307 )
									ret := 0.166667
						if( mf > 0.213433 )
							if( d_k <= -23.8498 )
								if( k <= 66.4987 )
									ret := 0.250000
								if( k > 66.4987 )
									ret := 1.000000 // buy
							if( d_k > -23.8498 )
								if( mf <= 0.465686 )
									ret := -0.376963
								if( mf > 0.465686 )
									ret := 0.019231
	
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
float op_operation = decision_tree_0_U_1Min_671cf21d(ad_mf, mf, ad, rsi1, d, k, smoothD_d, d_k, smoothK_k)

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


