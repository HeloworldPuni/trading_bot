//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Stochastic_RSI
// ID_model: AAPL_1Min_2CS0_6478bdf8 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAPL_1Min_2CS0_6478bdf8", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAPL_1Min_6478bdf8(ad, mf, ad_mf, rsi1, smoothK_k, d_k, k, d, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( ad <= 270.277 )
		if( smoothK_k <= 10.461 )
			if( mf <= -0.31251 )
				if( rsi1 <= 18.5431 )
					if( ad_mf <= -142072 )
						if( smoothD_d <= 8.00827 )
							if( ad_mf <= -552474 )
								ret := 0.500000
							if( ad_mf > -552474 )
								if( smoothK_k <= -2.48356 )
									ret := 0.571429
								if( smoothK_k > -2.48356 )
									ret := 1.000000 // buy
						if( smoothD_d > 8.00827 )
							ret := 0.444444
					if( ad_mf > -142072 )
						if( mf <= -0.426963 )
							if( d <= 0.652855 )
								ret := -0.142857
							if( d > 0.652855 )
								if( d <= 5.72358 )
									ret := 0.846154 // buy
								if( d > 5.72358 )
									ret := 0.396552
						if( mf > -0.426963 )
							if( k <= 9.33435 )
								if( d_k <= 4.23635 )
									ret := 0.170455
								if( d_k > 4.23635 )
									ret := -0.214286
							if( k > 9.33435 )
								ret := 0.705882 // buy
				if( rsi1 > 18.5431 )
					if( smoothK_k <= -0.592559 )
						if( smoothK_k <= -1.0113 )
							if( k <= 0.225924 )
								if( k <= 0.039552 )
									ret := 0.161616
								if( k > 0.039552 )
									ret := -1.000000 // sell
							if( k > 0.225924 )
								if( rsi1 <= 19.9194 )
									ret := 0.769231 // buy
								if( rsi1 > 19.9194 )
									ret := 0.154762
						if( smoothK_k > -1.0113 )
							if( rsi1 <= 30.1703 )
								if( mf <= -0.391203 )
									ret := -0.384615
								if( mf > -0.391203 )
									ret := 0.714286 // buy
							if( rsi1 > 30.1703 )
								ret := -0.823529 // sell
					if( smoothK_k > -0.592559 )
						if( ad_mf <= 0.344532 )
							if( d_k <= -1.83759 )
								if( d_k <= -3.29688 )
									ret := 0.264706
								if( d_k > -3.29688 )
									ret := -0.153846
							if( d_k > -1.83759 )
								if( rsi1 <= 29.0986 )
									ret := 0.474708
								if( rsi1 > 29.0986 )
									ret := 0.210031
						if( ad_mf > 0.344532 )
							if( smoothD_d <= 2.03288 )
								if( ad_mf <= 0.490661 )
									ret := -0.315789
								if( ad_mf > 0.490661 )
									ret := 0.150000
							if( smoothD_d > 2.03288 )
								if( k <= 6.6852 )
									ret := 0.410714
								if( k > 6.6852 )
									ret := 0.076923
			if( mf > -0.31251 )
				if( rsi1 <= 42.346 )
					if( rsi1 <= 10.5045 )
						if( smoothD_d <= 0.787451 )
							if( ad_mf <= -12566.1 )
								if( ad_mf <= -121457 )
									ret := 0.823529 // buy
								if( ad_mf > -121457 )
									ret := 0.127273
							if( ad_mf > -12566.1 )
								if( k <= 0.332582 )
									ret := 0.550000
								if( k > 0.332582 )
									ret := 0.939394 // buy
						if( smoothD_d > 0.787451 )
							if( ad_mf <= -33186.3 )
								ret := 0.533333
							if( ad_mf > -33186.3 )
								if( d <= 6.30072 )
									ret := 0.055556
								if( d > 6.30072 )
									ret := -0.421053
					if( rsi1 > 10.5045 )
						if( ad <= -14064.4 )
							if( mf <= -0.288574 )
								if( smoothD_d <= 6.07765 )
									ret := -0.020833
								if( smoothD_d > 6.07765 )
									ret := -0.575000
							if( mf > -0.288574 )
								if( ad_mf <= -16558.5 )
									ret := 0.085999
								if( ad_mf > -16558.5 )
									ret := -0.463687
						if( ad > -14064.4 )
							if( rsi1 <= 34.0899 )
								if( rsi1 <= 15.9389 )
									ret := -0.057522
								if( rsi1 > 15.9389 )
									ret := 0.234168
							if( rsi1 > 34.0899 )
								if( ad <= -107.374 )
									ret := 0.167526
								if( ad > -107.374 )
									ret := 0.009732
				if( rsi1 > 42.346 )
					if( smoothD_d <= -1.71609 )
						if( ad <= -132673 )
							ret := -0.500000
						if( ad > -132673 )
							if( k <= 0.006191 )
								if( ad_mf <= -711.086 )
									ret := 0.625000
								if( ad_mf > -711.086 )
									ret := -0.270270
							if( k > 0.006191 )
								if( d_k <= -0.610125 )
									ret := 0.000000
								if( d_k > -0.610125 )
									ret := 0.743243 // buy
					if( smoothD_d > -1.71609 )
						if( smoothD_d <= 32.5488 )
							if( mf <= 0.353413 )
								if( smoothK_k <= 5.93944 )
									ret := -0.001377
								if( smoothK_k > 5.93944 )
									ret := 0.095318
							if( mf > 0.353413 )
								if( ad_mf <= -14011.5 )
									ret := 0.615385
								if( ad_mf > -14011.5 )
									ret := -0.225182
						if( smoothD_d > 32.5488 )
							if( ad <= -4181.86 )
								if( d <= 39.3835 )
									ret := 0.875000 // buy
								if( d > 39.3835 )
									ret := -0.272727
							if( ad > -4181.86 )
								if( rsi1 <= 55.5416 )
									ret := 0.395349
								if( rsi1 > 55.5416 )
									ret := -0.583333
		if( smoothK_k > 10.461 )
			if( k <= 90.2226 )
				if( rsi1 <= 34.1683 )
					if( d_k <= 1.32996 )
						if( ad <= -280190 )
							if( mf <= -0.313324 )
								if( smoothD_d <= 26.5941 )
									ret := 0.882353 // buy
								if( smoothD_d > 26.5941 )
									ret := -0.200000
							if( mf > -0.313324 )
								if( ad <= -479115 )
									ret := 0.233333
								if( ad > -479115 )
									ret := -0.858974 // sell
						if( ad > -280190 )
							if( smoothD_d <= 49.601 )
								if( ad <= -217655 )
									ret := 0.754717 // buy
								if( ad > -217655 )
									ret := 0.023285
							if( smoothD_d > 49.601 )
								if( ad_mf <= -379.35 )
									ret := 0.366667
								if( ad_mf > -379.35 )
									ret := -0.123457
					if( d_k > 1.32996 )
						if( ad_mf <= -423358 )
							if( d_k <= 6.3359 )
								if( ad <= -552234 )
									ret := -0.538462
								if( ad > -552234 )
									ret := -1.000000 // sell
							if( d_k > 6.3359 )
								ret := 0.352941
						if( ad_mf > -423358 )
							if( k <= 45.9221 )
								if( smoothD_d <= 40.9082 )
									ret := 0.215591
								if( smoothD_d > 40.9082 )
									ret := 0.061256
							if( k > 45.9221 )
								if( k <= 46.5293 )
									ret := 0.900000 // buy
								if( k > 46.5293 )
									ret := 0.331169
				if( rsi1 > 34.1683 )
					if( d_k <= 8.41805 )
						if( smoothD_d <= 61.1668 )
							if( ad_mf <= -6147.62 )
								if( d_k <= -3.21215 )
									ret := -0.029498
								if( d_k > -3.21215 )
									ret := -0.123320
							if( ad_mf > -6147.62 )
								if( smoothK_k <= 25.9401 )
									ret := 0.071092
								if( smoothK_k > 25.9401 )
									ret := -0.007251
						if( smoothD_d > 61.1668 )
							if( d_k <= -15.0434 )
								if( mf <= -0.180259 )
									ret := -0.040404
								if( mf > -0.180259 )
									ret := 0.279365
							if( d_k > -15.0434 )
								if( rsi1 <= 44.776 )
									ret := 0.089994
								if( rsi1 > 44.776 )
									ret := 0.006893
					if( d_k > 8.41805 )
						if( d <= 64.3318 )
							if( rsi1 <= 34.5348 )
								if( mf <= -0.088822 )
									ret := 0.659574
								if( mf > -0.088822 )
									ret := -0.026316
							if( rsi1 > 34.5348 )
								if( ad_mf <= -744508 )
									ret := 0.703704 // buy
								if( ad_mf > -744508 )
									ret := -0.019293
						if( d > 64.3318 )
							if( ad_mf <= -70297.3 )
								if( d_k <= 10.4634 )
									ret := -0.229391
								if( d_k > 10.4634 )
									ret := 0.019048
							if( ad_mf > -70297.3 )
								if( mf <= -0.04213 )
									ret := 0.072364
								if( mf > -0.04213 )
									ret := 0.180527
			if( k > 90.2226 )
				if( mf <= 0.339727 )
					if( ad <= -92303.2 )
						if( mf <= 0.278014 )
							if( d_k <= 1.97326 )
								if( d <= 75.5073 )
									ret := -0.666667
								if( d > 75.5073 )
									ret := -0.121535
							if( d_k > 1.97326 )
								if( rsi1 <= 70.3638 )
									ret := -0.602273
								if( rsi1 > 70.3638 )
									ret := 0.000000
						if( mf > 0.278014 )
							if( mf <= 0.30653 )
								ret := 0.650000
							if( mf > 0.30653 )
								ret := -0.083333
					if( ad > -92303.2 )
						if( rsi1 <= 40.9602 )
							if( smoothD_d <= 77.944 )
								if( mf <= -0.409078 )
									ret := 0.333333
								if( mf > -0.409078 )
									ret := -0.134328
							if( smoothD_d > 77.944 )
								if( rsi1 <= 38.0749 )
									ret := 0.024000
								if( rsi1 > 38.0749 )
									ret := 0.531250
						if( rsi1 > 40.9602 )
							if( d_k <= -4.15857 )
								if( ad <= -87359 )
									ret := 0.750000 // buy
								if( ad > -87359 )
									ret := -0.012706
							if( d_k > -4.15857 )
								if( d <= 95.5637 )
									ret := -0.165176
								if( d > 95.5637 )
									ret := -0.023088
				if( mf > 0.339727 )
					if( smoothD_d <= 89.3558 )
						if( smoothK_k <= 90.8161 )
							if( ad_mf <= -10715.1 )
								if( smoothK_k <= 88.8532 )
									ret := 0.333333
								if( smoothK_k > 88.8532 )
									ret := 0.615385
							if( ad_mf > -10715.1 )
								if( d_k <= -0.501464 )
									ret := -0.166667
								if( d_k > -0.501464 )
									ret := 0.294118
						if( smoothK_k > 90.8161 )
							if( smoothD_d <= 82.2322 )
								if( d_k <= -12.5766 )
									ret := -0.108108
								if( d_k > -12.5766 )
									ret := 0.416667
							if( smoothD_d > 82.2322 )
								if( k <= 98.2566 )
									ret := -0.563636
								if( k > 98.2566 )
									ret := -0.142857
					if( smoothD_d > 89.3558 )
						if( mf <= 0.55846 )
							if( smoothD_d <= 92.6176 )
								if( smoothK_k <= 88.5299 )
									ret := 0.241379
								if( smoothK_k > 88.5299 )
									ret := 0.530612
							if( smoothD_d > 92.6176 )
								if( d <= 99.3552 )
									ret := -0.027397
								if( d > 99.3552 )
									ret := 0.371429
						if( mf > 0.55846 )
							if( d <= 94.5009 )
								if( mf <= 0.65461 )
									ret := 0.000000
								if( mf > 0.65461 )
									ret := 0.352941
							if( d > 94.5009 )
								if( rsi1 <= 64.2427 )
									ret := 0.307692
								if( rsi1 > 64.2427 )
									ret := -0.371429
	if( ad > 270.277 )
		if( rsi1 <= 43.157 )
			if( rsi1 <= 42.4925 )
				if( ad <= 51591.3 )
					if( d_k <= -18.0633 )
						if( d <= 47.53 )
							if( k <= 55.3667 )
								if( mf <= 0.059155 )
									ret := 0.617978
								if( mf > 0.059155 )
									ret := 0.000000
							if( k > 55.3667 )
								if( ad_mf <= 2156.92 )
									ret := 0.518519
								if( ad_mf > 2156.92 )
									ret := 0.180328
						if( d > 47.53 )
							if( rsi1 <= 41.3218 )
								if( smoothK_k <= 89.9245 )
									ret := -0.054545
								if( smoothK_k > 89.9245 )
									ret := 0.500000
							if( rsi1 > 41.3218 )
								ret := -0.750000 // sell
					if( d_k > -18.0633 )
						if( mf <= -0.436555 )
							if( ad_mf <= 22335.3 )
								if( smoothK_k <= 34.066 )
									ret := -0.351852
								if( smoothK_k > 34.066 )
									ret := 0.036036
							if( ad_mf > 22335.3 )
								ret := 0.733333 // buy
						if( mf > -0.436555 )
							if( ad <= 3808.52 )
								if( smoothD_d <= 20.1159 )
									ret := 0.049390
								if( smoothD_d > 20.1159 )
									ret := 0.183636
							if( ad > 3808.52 )
								if( d_k <= -5.8985 )
									ret := -0.088578
								if( d_k > -5.8985 )
									ret := 0.025076
				if( ad > 51591.3 )
					if( smoothK_k <= 41.6375 )
						if( ad_mf <= 52790.6 )
							if( smoothK_k <= 10.7896 )
								if( rsi1 <= 33.7633 )
									ret := -0.250000
								if( rsi1 > 33.7633 )
									ret := 0.285714
							if( smoothK_k > 10.7896 )
								if( rsi1 <= 32.0308 )
									ret := 0.076923
								if( rsi1 > 32.0308 )
									ret := -0.893617 // sell
						if( ad_mf > 52790.6 )
							if( ad_mf <= 53330.9 )
								if( d_k <= -1.96648 )
									ret := 0.200000
								if( d_k > -1.96648 )
									ret := 0.880000 // buy
							if( ad_mf > 53330.9 )
								if( d <= 36.6034 )
									ret := -0.051376
								if( d > 36.6034 )
									ret := 0.238532
					if( smoothK_k > 41.6375 )
						if( k <= 65.4751 )
							if( d_k <= 2.90962 )
								if( rsi1 <= 33.8683 )
									ret := -0.530120
								if( rsi1 > 33.8683 )
									ret := -0.148265
							if( d_k > 2.90962 )
								if( ad <= 160049 )
									ret := -0.406593
								if( ad > 160049 )
									ret := -0.875000 // sell
						if( k > 65.4751 )
							if( ad <= 103738 )
								if( d_k <= -12.383 )
									ret := -0.185185
								if( d_k > -12.383 )
									ret := 0.318584
							if( ad > 103738 )
								if( smoothK_k <= 72.7398 )
									ret := -0.500000
								if( smoothK_k > 72.7398 )
									ret := 0.128205
			if( rsi1 > 42.4925 )
				if( d_k <= -10.113 )
					if( d_k <= -11.6778 )
						if( mf <= -0.043334 )
							if( ad <= 1866.17 )
								ret := -0.571429
							if( ad > 1866.17 )
								if( d <= 64.1932 )
									ret := 0.625000
								if( d > 64.1932 )
									ret := -0.250000
						if( mf > -0.043334 )
							if( d_k <= -13.5025 )
								if( mf <= 0.055632 )
									ret := -0.700000 // sell
								if( mf > 0.055632 )
									ret := -0.400000
							if( d_k > -13.5025 )
								ret := 0.133333
					if( d_k > -11.6778 )
						ret := -0.650000
				if( d_k > -10.113 )
					if( d_k <= -9.55863 )
						ret := 0.875000 // buy
					if( d_k > -9.55863 )
						if( ad <= 252962 )
							if( ad <= 22751.8 )
								if( ad_mf <= 11262 )
									ret := 0.187793
								if( ad_mf > 11262 )
									ret := -0.278689
							if( ad > 22751.8 )
								if( mf <= -0.057281 )
									ret := 0.151515
								if( mf > -0.057281 )
									ret := 0.440415
						if( ad > 252962 )
							ret := -0.571429
		if( rsi1 > 43.157 )
			if( ad <= 2557.91 )
				if( d <= 23.0062 )
					if( rsi1 <= 60.4832 )
						if( ad <= 1793.5 )
							if( k <= 1.53461 )
								if( rsi1 <= 46.0956 )
									ret := -0.538462
								if( rsi1 > 46.0956 )
									ret := 0.500000
							if( k > 1.53461 )
								if( ad_mf <= 1418.36 )
									ret := -0.314590
								if( ad_mf > 1418.36 )
									ret := -0.628821
						if( ad > 1793.5 )
							if( k <= 15.7265 )
								if( d <= 8.59155 )
									ret := 0.285714
								if( d > 8.59155 )
									ret := -0.500000
							if( k > 15.7265 )
								if( ad_mf <= 2516.81 )
									ret := 0.411111
								if( ad_mf > 2516.81 )
									ret := -0.615385
					if( rsi1 > 60.4832 )
						if( d_k <= 5.3567 )
							if( d <= 19.5154 )
								if( d <= 12.1525 )
									ret := -0.100000
								if( d > 12.1525 )
									ret := 0.509804
							if( d > 19.5154 )
								ret := -0.210526
						if( d_k > 5.3567 )
							if( ad <= 1110.14 )
								ret := -0.333333
							if( ad > 1110.14 )
								ret := -0.764706 // sell
				if( d > 23.0062 )
					if( d <= 56.1694 )
						if( d_k <= -2.26213 )
							if( rsi1 <= 67.4798 )
								if( ad_mf <= 1462.63 )
									ret := -0.143802
								if( ad_mf > 1462.63 )
									ret := 0.125301
							if( rsi1 > 67.4798 )
								if( ad_mf <= 2054.76 )
									ret := -0.316456
								if( ad_mf > 2054.76 )
									ret := -0.861111 // sell
						if( d_k > -2.26213 )
							if( ad_mf <= 1093.57 )
								if( ad <= 522.518 )
									ret := -0.145299
								if( ad > 522.518 )
									ret := 0.361257
							if( ad_mf > 1093.57 )
								if( ad <= 2488.5 )
									ret := -0.030151
								if( ad > 2488.5 )
									ret := -0.791667 // sell
					if( d > 56.1694 )
						if( rsi1 <= 49.0131 )
							if( k <= 74.3651 )
								if( smoothK_k <= 47.9962 )
									ret := 0.130435
								if( smoothK_k > 47.9962 )
									ret := -0.229885
							if( k > 74.3651 )
								if( smoothD_d <= 70.504 )
									ret := 0.552632
								if( smoothD_d > 70.504 )
									ret := 0.076923
						if( rsi1 > 49.0131 )
							if( mf <= 0.273677 )
								if( k <= 69.1113 )
									ret := -0.300917
								if( k > 69.1113 )
									ret := -0.173469
							if( mf > 0.273677 )
								if( d <= 83.1766 )
									ret := -0.141623
								if( d > 83.1766 )
									ret := 0.103578
			if( ad > 2557.91 )
				if( ad_mf <= 464964 )
					if( ad <= 340531 )
						if( rsi1 <= 63.6892 )
							if( ad <= 297574 )
								if( d_k <= 7.50209 )
									ret := -0.040438
								if( d_k > 7.50209 )
									ret := 0.038491
							if( ad > 297574 )
								if( mf <= 0.008547 )
									ret := -0.291667
								if( mf > 0.008547 )
									ret := 0.481481
						if( rsi1 > 63.6892 )
							if( d_k <= -0.006206 )
								if( ad <= 187620 )
									ret := -0.127839
								if( ad > 187620 )
									ret := 0.047706
							if( d_k > -0.006206 )
								if( ad_mf <= 2748.17 )
									ret := 0.625000
								if( ad_mf > 2748.17 )
									ret := -0.040368
					if( ad > 340531 )
						if( ad <= 348527 )
							if( rsi1 <= 57.898 )
								ret := -1.000000 // sell
							if( rsi1 > 57.898 )
								ret := -0.625000
						if( ad > 348527 )
							if( k <= 48.6886 )
								if( ad_mf <= 367559 )
									ret := 0.633333
								if( ad_mf > 367559 )
									ret := -0.250000
							if( k > 48.6886 )
								if( k <= 60.332 )
									ret := -0.891304 // sell
								if( k > 60.332 )
									ret := -0.200980
				if( ad_mf > 464964 )
					if( k <= 82.3887 )
						if( mf <= 0.761988 )
							if( d_k <= 4.11844 )
								if( ad <= 500139 )
									ret := 0.772727 // buy
								if( ad > 500139 )
									ret := 0.020649
							if( d_k > 4.11844 )
								if( d <= 33.2999 )
									ret := -0.928571 // sell
								if( d > 33.2999 )
									ret := -0.592593
						if( mf > 0.761988 )
							if( mf <= 0.928353 )
								if( d <= 47.7789 )
									ret := -1.000000 // sell
								if( d > 47.7789 )
									ret := -0.800000 // sell
							if( mf > 0.928353 )
								ret := -0.500000
					if( k > 82.3887 )
						if( smoothK_k <= 96.9965 )
							if( ad <= 1.20219e+06 )
								if( mf <= 0.209864 )
									ret := 0.060606
								if( mf > 0.209864 )
									ret := 0.690141
							if( ad > 1.20219e+06 )
								if( d_k <= -3.38239 )
									ret := -0.416667
								if( d_k > -3.38239 )
									ret := 0.250000
						if( smoothK_k > 96.9965 )
							if( d <= 99.9895 )
								if( ad_mf <= 634588 )
									ret := 0.888889 // buy
								if( ad_mf > 634588 )
									ret := 1.000000 // buy
							if( d > 99.9895 )
								ret := 0.833333 // buy
	
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
float op_operation = decision_tree_0_AAPL_1Min_6478bdf8(ad, mf, ad_mf, rsi1, smoothK_k, d_k, k, d, smoothD_d)

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


