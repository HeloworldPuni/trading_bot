//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Triple_EMA
// ID_model: XRPUSDT_5Min_2MT0_3c271153 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_XRPUSDT_5Min_2MT0_3c271153", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_XRPUSDT_5Min_3c271153(Positive_Money_Flow_Sum, MFI, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, MFI_High, Typical_Price, Positive_Money_Flow, Negative_Money_Flow_Sum, ema2, tema, ema12, ema3, ema1, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( ema13 <= -0.001804 )
		if( Negative_Money_Flow_Sum <= 2.78059e+07 )
			if( ema13 <= -0.00486 )
				if( Negative_Money_Flow <= 798718 )
					if( Money_Flow_Ratio <= 0.173143 )
						if( Positive_Money_Flow_Sum <= 3.87003e+06 )
							if( ema13 <= -0.006832 )
								if( MFI_High <= -68.6892 )
									ret := -1.000000 // sell
								if( MFI_High > -68.6892 )
									ret := -0.800000 // sell
							if( ema13 > -0.006832 )
								if( MFI_High <= -66.1396 )
									ret := -0.171429
								if( MFI_High > -66.1396 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 3.87003e+06 )
							ret := 0.600000
					if( Money_Flow_Ratio > 0.173143 )
						if( ema13 <= -0.00626 )
							if( MFI_Low <= 14.1813 )
								if( Money_Flow_Ratio <= 0.31698 )
									ret := 0.601449
								if( Money_Flow_Ratio > 0.31698 )
									ret := 0.088710
							if( MFI_Low > 14.1813 )
								if( tema <= 0.556636 )
									ret := -0.125000
								if( tema > 0.556636 )
									ret := 0.940000 // buy
						if( ema13 > -0.00626 )
							if( Positive_Money_Flow_Sum <= 5.39515e+06 )
								if( Typical_Price <= 0.575521 )
									ret := -0.390805
								if( Typical_Price > 0.575521 )
									ret := 0.125000
							if( Positive_Money_Flow_Sum > 5.39515e+06 )
								if( ema2 <= 0.514086 )
									ret := 0.700000 // buy
								if( ema2 > 0.514086 )
									ret := 0.105263
				if( Negative_Money_Flow > 798718 )
					if( Raw_Money_Flow <= 1.71824e+06 )
						if( Money_Flow_Ratio <= 0.309341 )
							if( ema1 <= 0.647765 )
								if( MFI_High <= -66.2753 )
									ret := 0.892308 // buy
								if( MFI_High > -66.2753 )
									ret := 0.363636
							if( ema1 > 0.647765 )
								ret := -0.384615
						if( Money_Flow_Ratio > 0.309341 )
							if( tema <= 0.553908 )
								ret := 0.076923
							if( tema > 0.553908 )
								if( ema13 <= -0.006318 )
									ret := 0.583333
								if( ema13 > -0.006318 )
									ret := 0.915254 // buy
					if( Raw_Money_Flow > 1.71824e+06 )
						if( MFI <= 11.0977 )
							if( ema1 <= 0.54149 )
								if( MFI_Low <= -10.5431 )
									ret := 0.410256
								if( MFI_Low > -10.5431 )
									ret := -0.636364
							if( ema1 > 0.54149 )
								if( Raw_Money_Flow <= 2.76896e+06 )
									ret := 0.960000 // buy
								if( Raw_Money_Flow > 2.76896e+06 )
									ret := 0.661538
						if( MFI > 11.0977 )
							if( Raw_Money_Flow <= 2.04889e+06 )
								if( ema13 <= -0.005373 )
									ret := -0.614286
								if( ema13 > -0.005373 )
									ret := 0.080000
							if( Raw_Money_Flow > 2.04889e+06 )
								if( ema12 <= -0.005443 )
									ret := -1.000000 // sell
								if( ema12 > -0.005443 )
									ret := 0.278937
			if( ema13 > -0.00486 )
				if( ema1 <= 0.554901 )
					if( Typical_Price <= 0.437217 )
						if( MFI_Low <= -2.75904 )
							ret := 0.428571
						if( MFI_Low > -2.75904 )
							if( ema2 <= 0.418372 )
								ret := 1.000000 // buy
							if( ema2 > 0.418372 )
								if( ema12 <= -0.00115 )
									ret := -0.314286
								if( ema12 > -0.00115 )
									ret := -0.857143 // sell
					if( Typical_Price > 0.437217 )
						if( Negative_Money_Flow <= 1.03832e+06 )
							if( Positive_Money_Flow <= 806585 )
								if( ema3 <= 0.444212 )
									ret := 0.888889 // buy
								if( ema3 > 0.444212 )
									ret := 0.059558
							if( Positive_Money_Flow > 806585 )
								if( Positive_Money_Flow_Sum <= 4.52158e+06 )
									ret := 0.447566
								if( Positive_Money_Flow_Sum > 4.52158e+06 )
									ret := 0.158389
						if( Negative_Money_Flow > 1.03832e+06 )
							if( tema <= 0.467881 )
								if( ema3 <= 0.447659 )
									ret := 0.727273 // buy
								if( ema3 > 0.447659 )
									ret := -0.387097
							if( tema > 0.467881 )
								if( Typical_Price <= 0.548524 )
									ret := 0.321644
								if( Typical_Price > 0.548524 )
									ret := 0.023438
				if( ema1 > 0.554901 )
					if( Negative_Money_Flow_Sum <= 1.6404e+07 )
						if( MFI_High <= -42.5375 )
							if( MFI_High <= -44.9159 )
								if( ema12 <= -0.001439 )
									ret := 0.130117
								if( ema12 > -0.001439 )
									ret := 0.037493
							if( MFI_High > -44.9159 )
								if( MFI_High <= -43.4643 )
									ret := 0.426696
								if( MFI_High > -43.4643 )
									ret := 0.189781
						if( MFI_High > -42.5375 )
							if( tema <= 0.65236 )
								if( Raw_Money_Flow <= 387946 )
									ret := -0.404959
								if( Raw_Money_Flow > 387946 )
									ret := 0.042525
							if( tema > 0.65236 )
								if( Raw_Money_Flow <= 1.76417e+06 )
									ret := -0.420074
								if( Raw_Money_Flow > 1.76417e+06 )
									ret := 0.157895
					if( Negative_Money_Flow_Sum > 1.6404e+07 )
						if( Raw_Money_Flow <= 7.73276e+06 )
							if( MFI_Low <= -13.5669 )
								ret := 0.875000 // buy
							if( MFI_Low > -13.5669 )
								if( Money_Flow_Ratio <= 0.180192 )
									ret := -0.386598
								if( Money_Flow_Ratio > 0.180192 )
									ret := -0.064806
						if( Raw_Money_Flow > 7.73276e+06 )
							if( ema13 <= -0.003444 )
								ret := 1.000000 // buy
							if( ema13 > -0.003444 )
								ret := 0.500000
		if( Negative_Money_Flow_Sum > 2.78059e+07 )
			if( Negative_Money_Flow <= 4.8535e+06 )
				if( Typical_Price <= 0.622708 )
					if( ema12 <= -0.007097 )
						if( Positive_Money_Flow <= 7.98399e+06 )
							if( Positive_Money_Flow <= 2.3074e+06 )
								ret := 0.380952
							if( Positive_Money_Flow > 2.3074e+06 )
								if( ema3 <= 0.510587 )
									ret := 0.000000
								if( ema3 > 0.510587 )
									ret := -0.786667 // sell
						if( Positive_Money_Flow > 7.98399e+06 )
							if( ema1 <= 0.580253 )
								if( ema13 <= -0.032724 )
									ret := 0.636364
								if( ema13 > -0.032724 )
									ret := -0.416667
							if( ema1 > 0.580253 )
								ret := 1.000000 // buy
					if( ema12 > -0.007097 )
						if( Positive_Money_Flow_Sum <= 1.01786e+07 )
							if( Positive_Money_Flow_Sum <= 8.17902e+06 )
								if( ema12 <= -0.003354 )
									ret := 0.060440
								if( ema12 > -0.003354 )
									ret := 0.627737
							if( Positive_Money_Flow_Sum > 8.17902e+06 )
								if( MFI_High <= -54.8846 )
									ret := -0.557971
								if( MFI_High > -54.8846 )
									ret := 0.764706 // buy
						if( Positive_Money_Flow_Sum > 1.01786e+07 )
							if( Typical_Price <= 0.4223 )
								if( Money_Flow_Ratio <= 0.389132 )
									ret := -1.000000 // sell
								if( Money_Flow_Ratio > 0.389132 )
									ret := -0.777778 // sell
							if( Typical_Price > 0.4223 )
								if( tema <= 0.596254 )
									ret := 0.666121
								if( tema > 0.596254 )
									ret := 0.257848
				if( Typical_Price > 0.622708 )
					if( ema12 <= -0.000462 )
						if( MFI_High <= -46.594 )
							if( MFI_High <= -53.7605 )
								if( ema13 <= -0.007719 )
									ret := -0.384615
								if( ema13 > -0.007719 )
									ret := 0.067485
							if( MFI_High > -53.7605 )
								if( MFI_Low <= 11.2933 )
									ret := 0.711111 // buy
								if( MFI_Low > 11.2933 )
									ret := 0.220000
						if( MFI_High > -46.594 )
							if( MFI_Low <= 32.0065 )
								if( ema1 <= 0.684973 )
									ret := -0.305882
								if( ema1 > 0.684973 )
									ret := -0.771739 // sell
							if( MFI_Low > 32.0065 )
								ret := 0.888889 // buy
					if( ema12 > -0.000462 )
						ret := 0.900000 // buy
			if( Negative_Money_Flow > 4.8535e+06 )
				if( MFI_High <= -41.3779 )
					if( Positive_Money_Flow_Sum <= 2.57418e+07 )
						if( ema13 <= -0.008727 )
							if( Raw_Money_Flow <= 1.39987e+07 )
								if( Raw_Money_Flow <= 9.96607e+06 )
									ret := 0.447917
								if( Raw_Money_Flow > 9.96607e+06 )
									ret := -0.531250
							if( Raw_Money_Flow > 1.39987e+07 )
								if( ema1 <= 0.528207 )
									ret := 0.285714
								if( ema1 > 0.528207 )
									ret := 0.962963 // buy
						if( ema13 > -0.008727 )
							if( MFI <= 27.8999 )
								if( MFI_High <= -74.6066 )
									ret := 0.090909
								if( MFI_High > -74.6066 )
									ret := 0.823789 // buy
							if( MFI > 27.8999 )
								ret := 0.160000
					if( Positive_Money_Flow_Sum > 2.57418e+07 )
						if( ema1 <= 0.541957 )
							ret := 0.888889 // buy
						if( ema1 > 0.541957 )
							ret := 1.000000 // buy
				if( MFI_High > -41.3779 )
					if( ema12 <= -0.008144 )
						ret := -1.000000 // sell
					if( ema12 > -0.008144 )
						if( tema <= 0.556768 )
							ret := 0.928571 // buy
						if( tema > 0.556768 )
							ret := 0.300000
	if( ema13 > -0.001804 )
		if( ema2 <= 0.630546 )
			if( Negative_Money_Flow_Sum <= 5.3467e+06 )
				if( Negative_Money_Flow_Sum <= 5.24151e+06 )
					if( Negative_Money_Flow <= 538017 )
						if( Positive_Money_Flow <= 280268 )
							if( MFI <= 50.1065 )
								if( tema <= 0.495119 )
									ret := 0.006713
								if( tema > 0.495119 )
									ret := -0.065167
							if( MFI > 50.1065 )
								if( Positive_Money_Flow_Sum <= 8.77809e+06 )
									ret := 0.016968
								if( Positive_Money_Flow_Sum > 8.77809e+06 )
									ret := -0.142574
						if( Positive_Money_Flow > 280268 )
							if( Positive_Money_Flow_Sum <= 1.34126e+07 )
								if( MFI_High <= -0.860377 )
									ret := -0.067275
								if( MFI_High > -0.860377 )
									ret := -0.180197
							if( Positive_Money_Flow_Sum > 1.34126e+07 )
								if( MFI <= 88.0559 )
									ret := 0.211813
								if( MFI > 88.0559 )
									ret := -0.228111
					if( Negative_Money_Flow > 538017 )
						if( Negative_Money_Flow_Sum <= 1.66358e+06 )
							if( ema13 <= 0.002039 )
								if( Negative_Money_Flow <= 549224 )
									ret := 0.272727
								if( Negative_Money_Flow > 549224 )
									ret := -0.312000
							if( ema13 > 0.002039 )
								if( Negative_Money_Flow <= 707012 )
									ret := 0.434783
								if( Negative_Money_Flow > 707012 )
									ret := -0.315789
						if( Negative_Money_Flow_Sum > 1.66358e+06 )
							if( ema3 <= 0.604922 )
								if( MFI <= 68.1217 )
									ret := 0.036757
								if( MFI > 68.1217 )
									ret := 0.157030
							if( ema3 > 0.604922 )
								if( ema3 <= 0.626082 )
									ret := -0.060316
								if( ema3 > 0.626082 )
									ret := 0.159864
				if( Negative_Money_Flow_Sum > 5.24151e+06 )
					if( Positive_Money_Flow_Sum <= 3.83556e+06 )
						if( MFI_Low <= 12.2389 )
							if( Positive_Money_Flow <= 535833 )
								if( MFI_High <= -50.5711 )
									ret := -0.082803
								if( MFI_High > -50.5711 )
									ret := -0.612903
							if( Positive_Money_Flow > 535833 )
								ret := -0.857143 // sell
						if( MFI_Low > 12.2389 )
							if( Negative_Money_Flow <= 1.53133e+06 )
								if( ema12 <= -0.000278 )
									ret := 0.112676
								if( ema12 > -0.000278 )
									ret := 0.469565
							if( Negative_Money_Flow > 1.53133e+06 )
								ret := -0.625000
					if( Positive_Money_Flow_Sum > 3.83556e+06 )
						if( Positive_Money_Flow_Sum <= 4.04208e+06 )
							if( ema3 <= 0.532504 )
								ret := -0.684211
							if( ema3 > 0.532504 )
								if( ema13 <= -0.00064 )
									ret := -0.800000 // sell
								if( ema13 > -0.00064 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 4.04208e+06 )
							if( Positive_Money_Flow_Sum <= 2.95869e+07 )
								if( Positive_Money_Flow_Sum <= 1.04779e+07 )
									ret := -0.137353
								if( Positive_Money_Flow_Sum > 1.04779e+07 )
									ret := -0.478632
							if( Positive_Money_Flow_Sum > 2.95869e+07 )
								ret := 0.625000
			if( Negative_Money_Flow_Sum > 5.3467e+06 )
				if( ema1 <= 0.63234 )
					if( ema13 <= 0.000939 )
						if( Positive_Money_Flow_Sum <= 1.68836e+07 )
							if( Money_Flow_Ratio <= 0.467323 )
								if( Negative_Money_Flow_Sum <= 2.3381e+07 )
									ret := 0.008438
								if( Negative_Money_Flow_Sum > 2.3381e+07 )
									ret := -0.719101 // sell
							if( Money_Flow_Ratio > 0.467323 )
								if( MFI_High <= -40.9344 )
									ret := 0.135479
								if( MFI_High > -40.9344 )
									ret := 0.048856
						if( Positive_Money_Flow_Sum > 1.68836e+07 )
							if( ema2 <= 0.454938 )
								ret := -1.000000 // sell
							if( ema2 > 0.454938 )
								if( ema13 <= -0.000636 )
									ret := 0.526104
								if( ema13 > -0.000636 )
									ret := 0.179963
					if( ema13 > 0.000939 )
						if( ema2 <= 0.498365 )
							if( ema2 <= 0.426092 )
								if( Positive_Money_Flow <= 680446 )
									ret := 0.535714
								if( Positive_Money_Flow > 680446 )
									ret := 1.000000 // buy
							if( ema2 > 0.426092 )
								if( Positive_Money_Flow <= 5.73253e+06 )
									ret := 0.207018
								if( Positive_Money_Flow > 5.73253e+06 )
									ret := -1.000000 // sell
						if( ema2 > 0.498365 )
							if( MFI_Low <= 27.8082 )
								if( Money_Flow_Ratio <= 0.902502 )
									ret := 0.118211
								if( Money_Flow_Ratio > 0.902502 )
									ret := 0.626667
							if( MFI_Low > 27.8082 )
								if( MFI <= 68.4397 )
									ret := -0.059325
								if( MFI > 68.4397 )
									ret := 0.065519
				if( ema1 > 0.63234 )
					if( Money_Flow_Ratio <= 3.04353 )
						if( Raw_Money_Flow <= 3.09726e+06 )
							ret := 0.000000
						if( Raw_Money_Flow > 3.09726e+06 )
							if( MFI_Low <= 50.0887 )
								ret := -0.300000
							if( MFI_Low > 50.0887 )
								ret := -1.000000 // sell
					if( Money_Flow_Ratio > 3.04353 )
						if( Money_Flow_Ratio <= 3.55897 )
							ret := -1.000000 // sell
						if( Money_Flow_Ratio > 3.55897 )
							ret := -0.857143 // sell
		if( ema2 > 0.630546 )
			if( Positive_Money_Flow_Sum <= 2.18722e+07 )
				if( Raw_Money_Flow <= 565030 )
					if( Positive_Money_Flow <= 74282.3 )
						if( Positive_Money_Flow_Sum <= 1.53812e+06 )
							if( MFI_Low <= 1.51549 )
								if( Money_Flow_Ratio <= 0.246587 )
									ret := 0.111111
								if( Money_Flow_Ratio > 0.246587 )
									ret := 0.900000 // buy
							if( MFI_Low > 1.51549 )
								if( Negative_Money_Flow_Sum <= 3.23657e+06 )
									ret := -0.156398
								if( Negative_Money_Flow_Sum > 3.23657e+06 )
									ret := -0.493827
						if( Positive_Money_Flow_Sum > 1.53812e+06 )
							if( MFI <= 60.7285 )
								if( ema13 <= 0.000733 )
									ret := 0.053583
								if( ema13 > 0.000733 )
									ret := 0.370879
							if( MFI > 60.7285 )
								if( MFI <= 61.2037 )
									ret := -0.600000
								if( MFI > 61.2037 )
									ret := -0.008803
					if( Positive_Money_Flow > 74282.3 )
						if( MFI_High <= -22.4568 )
							if( MFI_High <= -42.3395 )
								if( MFI_Low <= 13.5393 )
									ret := -0.172414
								if( MFI_Low > 13.5393 )
									ret := 0.242678
							if( MFI_High > -42.3395 )
								if( ema12 <= -0.000355 )
									ret := -0.375862
								if( ema12 > -0.000355 )
									ret := -0.145203
						if( MFI_High > -22.4568 )
							if( MFI_Low <= 38.6104 )
								if( Negative_Money_Flow_Sum <= 4.84907e+06 )
									ret := 0.100000
								if( Negative_Money_Flow_Sum > 4.84907e+06 )
									ret := 1.000000 // buy
							if( MFI_Low > 38.6104 )
								if( Raw_Money_Flow <= 561376 )
									ret := -0.019802
								if( Raw_Money_Flow > 561376 )
									ret := 0.692308
				if( Raw_Money_Flow > 565030 )
					if( Money_Flow_Ratio <= 1.09219 )
						if( Positive_Money_Flow_Sum <= 1.27525e+07 )
							if( MFI <= 48.0376 )
								if( Positive_Money_Flow_Sum <= 1.00495e+07 )
									ret := -0.072042
								if( Positive_Money_Flow_Sum > 1.00495e+07 )
									ret := -0.429787
							if( MFI > 48.0376 )
								if( MFI_Low <= 28.2815 )
									ret := 0.657895
								if( MFI_Low > 28.2815 )
									ret := 0.018270
						if( Positive_Money_Flow_Sum > 1.27525e+07 )
							if( ema3 <= 0.710531 )
								if( MFI_Low <= 24.2031 )
									ret := 0.675862
								if( MFI_Low > 24.2031 )
									ret := 0.151852
							if( ema3 > 0.710531 )
								ret := -0.913043 // sell
					if( Money_Flow_Ratio > 1.09219 )
						if( ema13 <= 0.004668 )
							if( Money_Flow_Ratio <= 1.12209 )
								if( Raw_Money_Flow <= 852282 )
									ret := -0.118421
								if( Raw_Money_Flow > 852282 )
									ret := -0.719298 // sell
							if( Money_Flow_Ratio > 1.12209 )
								if( ema12 <= 0.00069 )
									ret := -0.069959
								if( ema12 > 0.00069 )
									ret := -0.241108
						if( ema13 > 0.004668 )
							if( Money_Flow_Ratio <= 5.14867 )
								if( Typical_Price <= 0.687698 )
									ret := 0.712000 // buy
								if( Typical_Price > 0.687698 )
									ret := 0.166667
							if( Money_Flow_Ratio > 5.14867 )
								ret := -0.833333 // sell
			if( Positive_Money_Flow_Sum > 2.18722e+07 )
				if( Positive_Money_Flow_Sum <= 1.78555e+08 )
					if( Typical_Price <= 0.657559 )
						if( MFI_Low <= 43.7956 )
							if( ema12 <= 0.002196 )
								if( Positive_Money_Flow <= 1.13537e+06 )
									ret := 0.500000
								if( Positive_Money_Flow > 1.13537e+06 )
									ret := 0.062500
							if( ema12 > 0.002196 )
								if( ema1 <= 0.645675 )
									ret := -0.545455
								if( ema1 > 0.645675 )
									ret := -1.000000 // sell
						if( MFI_Low > 43.7956 )
							if( MFI_Low <= 64.9269 )
								if( Negative_Money_Flow_Sum <= 1.40453e+07 )
									ret := -0.540881
								if( Negative_Money_Flow_Sum > 1.40453e+07 )
									ret := -0.274725
							if( MFI_Low > 64.9269 )
								if( Positive_Money_Flow <= 6.941e+06 )
									ret := 0.473684
								if( Positive_Money_Flow > 6.941e+06 )
									ret := -1.000000 // sell
					if( Typical_Price > 0.657559 )
						if( Typical_Price <= 0.733083 )
							if( ema13 <= 0.005531 )
								if( Raw_Money_Flow <= 1.83125e+06 )
									ret := -0.779310 // sell
								if( Raw_Money_Flow > 1.83125e+06 )
									ret := -0.330189
							if( ema13 > 0.005531 )
								if( Positive_Money_Flow_Sum <= 7.76458e+07 )
									ret := -0.818859 // sell
								if( Positive_Money_Flow_Sum > 7.76458e+07 )
									ret := -0.487179
						if( Typical_Price > 0.733083 )
							if( tema <= 0.737443 )
								ret := 0.600000
							if( tema > 0.737443 )
								ret := -0.333333
				if( Positive_Money_Flow_Sum > 1.78555e+08 )
					if( Raw_Money_Flow <= 2.09626e+07 )
						ret := 0.952381 // buy
					if( Raw_Money_Flow > 2.09626e+07 )
						ret := 0.230769
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_XRPUSDT_5Min_3c271153(Positive_Money_Flow_Sum, MFI, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, MFI_High, Typical_Price, Positive_Money_Flow, Negative_Money_Flow_Sum, ema2, tema, ema12, ema3, ema1, ema13)

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


