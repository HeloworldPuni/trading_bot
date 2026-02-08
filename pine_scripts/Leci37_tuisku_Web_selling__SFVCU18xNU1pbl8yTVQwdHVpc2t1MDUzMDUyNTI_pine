//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Triple_EMA
// ID_model: HUBS_15Min_2MT0_05305252 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_HUBS_15Min_2MT0_05305252", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_HUBS_15Min_05305252(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=0.7, min_samples_leaf=7,min_samples_split=10, random_state=843828734)
	if( MFI <= 32.247 )
		if( Negative_Money_Flow_Sum <= 7.8341e+07 )
			if( Negative_Money_Flow_Sum <= 7.00323e+07 )
				if( Positive_Money_Flow_Sum <= 1.18504e+07 )
					if( Raw_Money_Flow <= 3.5494e+06 )
						if( Positive_Money_Flow_Sum <= 2.42266e+06 )
							if( ema13 <= 0.417558 )
								if( ema13 <= -1.32285 )
									ret := 0.714286 // buy
								if( ema13 > -1.32285 )
									ret := 0.263081
							if( ema13 > 0.417558 )
								if( MFI_Low <= -1.67535 )
									ret := -0.923077 // sell
								if( MFI_Low > -1.67535 )
									ret := -0.187500
						if( Positive_Money_Flow_Sum > 2.42266e+06 )
							if( tema <= 88.9698 )
								if( Negative_Money_Flow_Sum <= 4.22001e+07 )
									ret := -0.004808
								if( Negative_Money_Flow_Sum > 4.22001e+07 )
									ret := -1.000000 // sell
							if( tema > 88.9698 )
								if( ema1 <= 126.256 )
									ret := 0.281667
								if( ema1 > 126.256 )
									ret := 0.108108
					if( Raw_Money_Flow > 3.5494e+06 )
						if( tema <= 347.252 )
							if( ema1 <= 85.4466 )
								if( Raw_Money_Flow <= 8.57017e+06 )
									ret := -0.158730
								if( Raw_Money_Flow > 8.57017e+06 )
									ret := 0.466667
							if( ema1 > 85.4466 )
								if( MFI_High <= -71.6515 )
									ret := -0.027027
								if( MFI_High > -71.6515 )
									ret := 0.519185
						if( tema > 347.252 )
							if( Negative_Money_Flow_Sum <= 5.5561e+07 )
								if( ema12 <= -1.51008 )
									ret := -0.580645
								if( ema12 > -1.51008 )
									ret := -0.020833
							if( Negative_Money_Flow_Sum > 5.5561e+07 )
								if( Negative_Money_Flow_Sum <= 6.54666e+07 )
									ret := 0.428571
								if( Negative_Money_Flow_Sum > 6.54666e+07 )
									ret := -0.100000
				if( Positive_Money_Flow_Sum > 1.18504e+07 )
					if( Negative_Money_Flow <= 1.70417e+07 )
						if( ema12 <= -0.955844 )
							if( Raw_Money_Flow <= 1.77125e+06 )
								if( ema1 <= 219.925 )
									ret := -0.041096
								if( ema1 > 219.925 )
									ret := -0.611111
							if( Raw_Money_Flow > 1.77125e+06 )
								if( ema3 <= 176.543 )
									ret := -0.191304
								if( ema3 > 176.543 )
									ret := 0.070243
						if( ema12 > -0.955844 )
							if( Negative_Money_Flow_Sum <= 4.08728e+07 )
								if( Positive_Money_Flow_Sum <= 1.27421e+07 )
									ret := -0.242604
								if( Positive_Money_Flow_Sum > 1.27421e+07 )
									ret := 0.081535
							if( Negative_Money_Flow_Sum > 4.08728e+07 )
								if( Typical_Price <= 508.717 )
									ret := 0.277516
								if( Typical_Price > 508.717 )
									ret := -0.084967
					if( Negative_Money_Flow > 1.70417e+07 )
						if( Money_Flow_Ratio <= 0.239817 )
							if( Negative_Money_Flow <= 2.34987e+07 )
								ret := 1.000000 // buy
							if( Negative_Money_Flow > 2.34987e+07 )
								ret := 0.250000
						if( Money_Flow_Ratio > 0.239817 )
							if( Raw_Money_Flow <= 3.10822e+07 )
								if( ema3 <= 540.217 )
									ret := -0.640288
								if( ema3 > 540.217 )
									ret := 0.142857
							if( Raw_Money_Flow > 3.10822e+07 )
								ret := 0.347826
			if( Negative_Money_Flow_Sum > 7.00323e+07 )
				if( ema3 <= 623.302 )
					if( ema3 <= 281.83 )
						if( MFI_High <= -60.9581 )
							if( Positive_Money_Flow_Sum <= 1.15422e+07 )
								ret := -0.083333
							if( Positive_Money_Flow_Sum > 1.15422e+07 )
								if( Typical_Price <= 181.686 )
									ret := -0.500000
								if( Typical_Price > 181.686 )
									ret := -0.923077 // sell
						if( MFI_High > -60.9581 )
							if( Negative_Money_Flow_Sum <= 7.19757e+07 )
								if( ema12 <= -1.20133 )
									ret := 0.333333
								if( ema12 > -1.20133 )
									ret := -0.818182 // sell
							if( Negative_Money_Flow_Sum > 7.19757e+07 )
								if( Negative_Money_Flow_Sum <= 7.60829e+07 )
									ret := 0.916667 // buy
								if( Negative_Money_Flow_Sum > 7.60829e+07 )
									ret := -0.500000
					if( ema3 > 281.83 )
						if( ema12 <= 1.39888 )
							if( ema3 <= 389.485 )
								if( ema12 <= -2.97669 )
									ret := 0.125000
								if( ema12 > -2.97669 )
									ret := 0.764706 // buy
							if( ema3 > 389.485 )
								if( MFI_Low <= 11.7564 )
									ret := 0.439739
								if( MFI_Low > 11.7564 )
									ret := -0.500000
						if( ema12 > 1.39888 )
							if( Negative_Money_Flow <= 11394.6 )
								ret := -0.307692
							if( Negative_Money_Flow > 11394.6 )
								ret := 0.066667
				if( ema3 > 623.302 )
					if( Raw_Money_Flow <= 8.66520e+06 )
						ret := -0.166667
					if( Raw_Money_Flow > 8.66520e+06 )
						ret := -0.916667 // sell
		if( Negative_Money_Flow_Sum > 7.8341e+07 )
			if( Negative_Money_Flow_Sum <= 8.04349e+07 )
				if( Positive_Money_Flow_Sum <= 1.42396e+07 )
					if( ema1 <= 372.843 )
						ret := 0.666667
					if( ema1 > 372.843 )
						ret := 0.181818
				if( Positive_Money_Flow_Sum > 1.42396e+07 )
					if( Negative_Money_Flow <= 7.79594e+06 )
						if( Typical_Price <= 502.491 )
							if( MFI <= 18.4422 )
								ret := -1.000000 // sell
							if( MFI > 18.4422 )
								if( Raw_Money_Flow <= 2.54485e+06 )
									ret := -0.105263
								if( Raw_Money_Flow > 2.54485e+06 )
									ret := -0.770833 // sell
						if( Typical_Price > 502.491 )
							ret := 0.000000
					if( Negative_Money_Flow > 7.79594e+06 )
						if( tema <= 337.258 )
							ret := 0.555556
						if( tema > 337.258 )
							ret := -0.200000
			if( Negative_Money_Flow_Sum > 8.04349e+07 )
				if( Negative_Money_Flow_Sum <= 1.44066e+08 )
					if( Money_Flow_Ratio <= 0.254247 )
						if( Positive_Money_Flow_Sum <= 2.25861e+07 )
							if( Typical_Price <= 268.818 )
								if( ema2 <= 259.976 )
									ret := -0.175732
								if( ema2 > 259.976 )
									ret := -0.800000 // sell
							if( Typical_Price > 268.818 )
								if( Negative_Money_Flow <= 2.6214e+07 )
									ret := -0.002342
								if( Negative_Money_Flow > 2.6214e+07 )
									ret := 0.348485
						if( Positive_Money_Flow_Sum > 2.25861e+07 )
							if( ema1 <= 449.323 )
								if( Positive_Money_Flow <= 126802 )
									ret := -0.396040
								if( Positive_Money_Flow > 126802 )
									ret := -0.855072 // sell
							if( ema1 > 449.323 )
								if( ema2 <= 598.239 )
									ret := -0.008929
								if( ema2 > 598.239 )
									ret := -0.461538
					if( Money_Flow_Ratio > 0.254247 )
						if( Positive_Money_Flow <= 583775 )
							if( ema12 <= -4.12535 )
								if( Negative_Money_Flow_Sum <= 8.92661e+07 )
									ret := -0.307692
								if( Negative_Money_Flow_Sum > 8.92661e+07 )
									ret := 0.618321
							if( ema12 > -4.12535 )
								if( ema3 <= 316.125 )
									ret := 0.355030
								if( ema3 > 316.125 )
									ret := 0.029190
						if( Positive_Money_Flow > 583775 )
							if( Positive_Money_Flow_Sum <= 2.35663e+07 )
								if( Money_Flow_Ratio <= 0.271275 )
									ret := 0.437500
								if( Money_Flow_Ratio > 0.271275 )
									ret := 1.000000 // buy
							if( Positive_Money_Flow_Sum > 2.35663e+07 )
								if( Negative_Money_Flow_Sum <= 8.55107e+07 )
									ret := 0.363636
								if( Negative_Money_Flow_Sum > 8.55107e+07 )
									ret := -0.146341
				if( Negative_Money_Flow_Sum > 1.44066e+08 )
					if( Negative_Money_Flow_Sum <= 1.92075e+08 )
						if( tema <= 483.273 )
							if( Positive_Money_Flow_Sum <= 1.07552e+07 )
								if( Negative_Money_Flow <= 1.27461e+07 )
									ret := 0.222222
								if( Negative_Money_Flow > 1.27461e+07 )
									ret := -1.000000 // sell
							if( Positive_Money_Flow_Sum > 1.07552e+07 )
								if( Positive_Money_Flow_Sum <= 7.50646e+07 )
									ret := 0.555336
								if( Positive_Money_Flow_Sum > 7.50646e+07 )
									ret := -0.526316
						if( tema > 483.273 )
							if( tema <= 640.506 )
								if( Typical_Price <= 630.361 )
									ret := 0.017429
								if( Typical_Price > 630.361 )
									ret := -0.656250
							if( tema > 640.506 )
								if( Raw_Money_Flow <= 1.49897e+06 )
									ret := -0.818182 // sell
								if( Raw_Money_Flow > 1.49897e+06 )
									ret := 0.405714
					if( Negative_Money_Flow_Sum > 1.92075e+08 )
						if( Negative_Money_Flow_Sum <= 3.7677e+08 )
							if( ema13 <= -11.5857 )
								if( ema1 <= 730.926 )
									ret := 0.365854
								if( ema1 > 730.926 )
									ret := -0.714286 // sell
							if( ema13 > -11.5857 )
								if( Typical_Price <= 688.254 )
									ret := -0.155949
								if( Typical_Price > 688.254 )
									ret := -0.705128 // sell
						if( Negative_Money_Flow_Sum > 3.7677e+08 )
							if( Money_Flow_Ratio <= 0.188495 )
								if( ema13 <= -21.7243 )
									ret := -0.769231 // sell
								if( ema13 > -21.7243 )
									ret := 0.564286
							if( Money_Flow_Ratio > 0.188495 )
								if( ema2 <= 639.964 )
									ret := -0.456522
								if( ema2 > 639.964 )
									ret := 0.900000 // buy
	if( MFI > 32.247 )
		if( Positive_Money_Flow_Sum <= 1.61131e+08 )
			if( Negative_Money_Flow <= 1.9093e+07 )
				if( Raw_Money_Flow <= 1.56572e+06 )
					if( Negative_Money_Flow_Sum <= 1.32208e+08 )
						if( MFI_Low <= 32.309 )
							if( Positive_Money_Flow_Sum <= 7.07314e+06 )
								if( Raw_Money_Flow <= 487886 )
									ret := 0.025723
								if( Raw_Money_Flow > 487886 )
									ret := -0.122974
							if( Positive_Money_Flow_Sum > 7.07314e+06 )
								if( tema <= 188.877 )
									ret := 0.126992
								if( tema > 188.877 )
									ret := -0.074685
						if( MFI_Low > 32.309 )
							if( Money_Flow_Ratio <= 51.9021 )
								if( ema13 <= 13.3566 )
									ret := 0.103404
								if( ema13 > 13.3566 )
									ret := -0.818182 // sell
							if( Money_Flow_Ratio > 51.9021 )
								ret := 0.958333 // buy
					if( Negative_Money_Flow_Sum > 1.32208e+08 )
						if( MFI <= 39.168 )
							if( Raw_Money_Flow <= 72187.4 )
								ret := 0.615385
							if( Raw_Money_Flow > 72187.4 )
								if( Positive_Money_Flow_Sum <= 9.03334e+07 )
									ret := 0.909091 // buy
								if( Positive_Money_Flow_Sum > 9.03334e+07 )
									ret := 1.000000 // buy
						if( MFI > 39.168 )
							if( Positive_Money_Flow_Sum <= 1.2964e+08 )
								ret := 0.533333
							if( Positive_Money_Flow_Sum > 1.2964e+08 )
								if( Negative_Money_Flow_Sum <= 1.53266e+08 )
									ret := 0.625000
								if( Negative_Money_Flow_Sum > 1.53266e+08 )
									ret := -0.666667
				if( Raw_Money_Flow > 1.56572e+06 )
					if( Negative_Money_Flow_Sum <= 7.51118e+07 )
						if( Negative_Money_Flow_Sum <= 6.38e+07 )
							if( Negative_Money_Flow_Sum <= 4.90754e+07 )
								if( ema13 <= -3.01069 )
									ret := -0.173460
								if( ema13 > -3.01069 )
									ret := 0.011549
							if( Negative_Money_Flow_Sum > 4.90754e+07 )
								if( Money_Flow_Ratio <= 0.496182 )
									ret := -0.431818
								if( Money_Flow_Ratio > 0.496182 )
									ret := 0.126667
						if( Negative_Money_Flow_Sum > 6.38e+07 )
							if( MFI_Low <= 33.1741 )
								if( ema1 <= 457.162 )
									ret := 0.097479
								if( ema1 > 457.162 )
									ret := -0.218487
							if( MFI_Low > 33.1741 )
								if( Raw_Money_Flow <= 1.0385e+07 )
									ret := -0.495798
								if( Raw_Money_Flow > 1.0385e+07 )
									ret := -0.044554
					if( Negative_Money_Flow_Sum > 7.51118e+07 )
						if( Negative_Money_Flow_Sum <= 1.53297e+08 )
							if( ema12 <= -1.06867 )
								if( Positive_Money_Flow <= 6.96875e+07 )
									ret := 0.226558
								if( Positive_Money_Flow > 6.96875e+07 )
									ret := -0.928571 // sell
							if( ema12 > -1.06867 )
								if( Positive_Money_Flow_Sum <= 1.16689e+08 )
									ret := 0.103059
								if( Positive_Money_Flow_Sum > 1.16689e+08 )
									ret := -0.071930
						if( Negative_Money_Flow_Sum > 1.53297e+08 )
							if( ema13 <= -12.4053 )
								ret := 0.866667 // buy
							if( ema13 > -12.4053 )
								if( MFI <= 46.3086 )
									ret := -0.170483
								if( MFI > 46.3086 )
									ret := -0.657143
			if( Negative_Money_Flow > 1.9093e+07 )
				if( Positive_Money_Flow_Sum <= 9.82936e+07 )
					if( ema2 <= 631.217 )
						if( Positive_Money_Flow_Sum <= 4.2403e+07 )
							if( MFI_Low <= 18.0122 )
								if( ema13 <= -2.01618 )
									ret := -0.666667
								if( ema13 > -2.01618 )
									ret := 0.359375
							if( MFI_Low > 18.0122 )
								if( Positive_Money_Flow_Sum <= 3.0972e+07 )
									ret := 0.264706
								if( Positive_Money_Flow_Sum > 3.0972e+07 )
									ret := 0.800000 // buy
						if( Positive_Money_Flow_Sum > 4.2403e+07 )
							if( Negative_Money_Flow <= 6.7454e+07 )
								if( ema12 <= 1.64797 )
									ret := 0.044917
								if( ema12 > 1.64797 )
									ret := -0.417582
							if( Negative_Money_Flow > 6.7454e+07 )
								ret := 0.894737 // buy
					if( ema2 > 631.217 )
						if( Negative_Money_Flow_Sum <= 1.13875e+08 )
							if( Negative_Money_Flow_Sum <= 6.29726e+07 )
								if( Negative_Money_Flow_Sum <= 5.48272e+07 )
									ret := 0.777778 // buy
								if( Negative_Money_Flow_Sum > 5.48272e+07 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 6.29726e+07 )
								if( Negative_Money_Flow <= 3.54718e+07 )
									ret := -0.090909
								if( Negative_Money_Flow > 3.54718e+07 )
									ret := 0.521739
						if( Negative_Money_Flow_Sum > 1.13875e+08 )
							if( Typical_Price <= 679.605 )
								ret := 0.769231 // buy
							if( Typical_Price > 679.605 )
								ret := 1.000000 // buy
				if( Positive_Money_Flow_Sum > 9.82936e+07 )
					if( tema <= 469.736 )
						if( ema3 <= 317.636 )
							ret := 0.333333
						if( ema3 > 317.636 )
							if( Negative_Money_Flow <= 2.21966e+07 )
								if( MFI_Low <= 34.6594 )
									ret := 0.416667
								if( MFI_Low > 34.6594 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow > 2.21966e+07 )
								if( Negative_Money_Flow_Sum <= 6.01551e+07 )
									ret := 0.700000 // buy
								if( Negative_Money_Flow_Sum > 6.01551e+07 )
									ret := 0.985294 // buy
					if( tema > 469.736 )
						if( Negative_Money_Flow_Sum <= 1.86993e+08 )
							if( ema13 <= -10.1187 )
								ret := -0.500000
							if( ema13 > -10.1187 )
								if( ema12 <= 0.997442 )
									ret := 0.625000
								if( ema12 > 0.997442 )
									ret := 0.151899
						if( Negative_Money_Flow_Sum > 1.86993e+08 )
							if( ema13 <= -7.23265 )
								if( Negative_Money_Flow <= 3.10689e+07 )
									ret := -0.083333
								if( Negative_Money_Flow > 3.10689e+07 )
									ret := 0.933333 // buy
							if( ema13 > -7.23265 )
								if( MFI <= 36.219 )
									ret := -0.235294
								if( MFI > 36.219 )
									ret := -0.850000 // sell
		if( Positive_Money_Flow_Sum > 1.61131e+08 )
			if( ema13 <= -1.95859 )
				if( Raw_Money_Flow <= 7.23873e+06 )
					if( MFI_High <= -6.17378 )
						if( ema1 <= 652.48 )
							if( Positive_Money_Flow_Sum <= 1.69712e+08 )
								ret := 0.913043 // buy
							if( Positive_Money_Flow_Sum > 1.69712e+08 )
								if( Positive_Money_Flow <= 82192.6 )
									ret := 0.680000
								if( Positive_Money_Flow > 82192.6 )
									ret := -0.142857
						if( ema1 > 652.48 )
							ret := 1.000000 // buy
					if( MFI_High > -6.17378 )
						if( Positive_Money_Flow_Sum <= 1.84947e+08 )
							ret := -0.600000
						if( Positive_Money_Flow_Sum > 1.84947e+08 )
							if( Typical_Price <= 545.046 )
								ret := 0.583333
							if( Typical_Price > 545.046 )
								ret := -0.071429
				if( Raw_Money_Flow > 7.23873e+06 )
					if( Negative_Money_Flow_Sum <= 1.39502e+08 )
						if( Typical_Price <= 592.855 )
							if( ema3 <= 483 )
								if( ema2 <= 461.278 )
									ret := 0.120000
								if( ema2 > 461.278 )
									ret := -0.857143 // sell
							if( ema3 > 483 )
								if( ema12 <= -2.9664 )
									ret := 0.839286 // buy
								if( ema12 > -2.9664 )
									ret := 0.333333
						if( Typical_Price > 592.855 )
							if( Negative_Money_Flow_Sum <= 8.9893e+07 )
								if( ema12 <= -2.55713 )
									ret := -0.117647
								if( ema12 > -2.55713 )
									ret := -0.769231 // sell
							if( Negative_Money_Flow_Sum > 8.9893e+07 )
								if( Money_Flow_Ratio <= 1.57759 )
									ret := -0.642857
								if( Money_Flow_Ratio > 1.57759 )
									ret := 0.575758
					if( Negative_Money_Flow_Sum > 1.39502e+08 )
						if( Negative_Money_Flow <= 6.71483e+07 )
							if( MFI_High <= -27.1204 )
								if( ema12 <= -2.94842 )
									ret := 0.250000
								if( ema12 > -2.94842 )
									ret := -0.463415
							if( MFI_High > -27.1204 )
								if( Negative_Money_Flow <= 3.97778e+06 )
									ret := -0.352941
								if( Negative_Money_Flow > 3.97778e+06 )
									ret := -0.800000 // sell
						if( Negative_Money_Flow > 6.71483e+07 )
							ret := 1.000000 // buy
			if( ema13 > -1.95859 )
				if( MFI_Low <= 71.17 )
					if( Negative_Money_Flow_Sum <= 1.64126e+08 )
						if( Raw_Money_Flow <= 256221 )
							if( MFI <= 73.032 )
								if( Negative_Money_Flow <= 102867 )
									ret := -0.480000
								if( Negative_Money_Flow > 102867 )
									ret := 0.545455
							if( MFI > 73.032 )
								if( tema <= 483.959 )
									ret := -0.914286 // sell
								if( tema > 483.959 )
									ret := -0.490196
						if( Raw_Money_Flow > 256221 )
							if( Positive_Money_Flow_Sum <= 1.73573e+08 )
								if( ema13 <= 10.2557 )
									ret := -0.376176
								if( ema13 > 10.2557 )
									ret := 0.384615
							if( Positive_Money_Flow_Sum > 1.73573e+08 )
								if( MFI_High <= -15.903 )
									ret := 0.195876
								if( MFI_High > -15.903 )
									ret := -0.106698
					if( Negative_Money_Flow_Sum > 1.64126e+08 )
						if( Negative_Money_Flow_Sum <= 4.87982e+08 )
							if( Raw_Money_Flow <= 6.11263e+06 )
								ret := 0.150000
							if( Raw_Money_Flow > 6.11263e+06 )
								if( Positive_Money_Flow_Sum <= 1.66051e+08 )
									ret := -0.111111
								if( Positive_Money_Flow_Sum > 1.66051e+08 )
									ret := -0.753247 // sell
						if( Negative_Money_Flow_Sum > 4.87982e+08 )
							if( Raw_Money_Flow <= 4.41795e+07 )
								ret := -0.454545
							if( Raw_Money_Flow > 4.41795e+07 )
								if( ema13 <= 14.1771 )
									ret := 0.777778 // buy
								if( ema13 > 14.1771 )
									ret := 1.000000 // buy
				if( MFI_Low > 71.17 )
					if( tema <= 538.695 )
						if( Negative_Money_Flow <= 36209.6 )
							if( Positive_Money_Flow_Sum <= 2.76497e+08 )
								if( Typical_Price <= 503.411 )
									ret := 0.447368
								if( Typical_Price > 503.411 )
									ret := -0.130435
							if( Positive_Money_Flow_Sum > 2.76497e+08 )
								ret := -0.272727
						if( Negative_Money_Flow > 36209.6 )
							if( Positive_Money_Flow <= 302458 )
								if( MFI_Low <= 74.5115 )
									ret := 0.812500 // buy
								if( MFI_Low > 74.5115 )
									ret := 0.533333
							if( Positive_Money_Flow > 302458 )
								ret := 1.000000 // buy
					if( tema > 538.695 )
						if( MFI_High <= 12.3428 )
							ret := -0.105263
						if( MFI_High > 12.3428 )
							if( Negative_Money_Flow_Sum <= 3.67832e+07 )
								ret := -0.600000
							if( Negative_Money_Flow_Sum > 3.67832e+07 )
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


//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


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
float op_operation = decision_tree_0_HUBS_15Min_05305252(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, ema12, ema3, ema13, tema, ema1, ema2)

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


