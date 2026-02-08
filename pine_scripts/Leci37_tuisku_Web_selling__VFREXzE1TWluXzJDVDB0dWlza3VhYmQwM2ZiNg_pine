//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Triple_EMA
// ID_model: TTD_15Min_2CT0_abd03fb6 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TTD_15Min_2CT0_abd03fb6", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TTD_15Min_abd03fb6(ad_mf, mf, ad, ema2, ema1, ema12, ema3, ema13, tema)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( ad_mf <= 0.225411 )
		if( ad <= -9350.2 )
			if( ema12 <= 1.38095 )
				if( tema <= 51.5021 )
					if( ad <= -9681.9 )
						if( mf <= 0.047081 )
							if( ema13 <= 0.61692 )
								if( ema12 <= -0.375171 )
									ret := 0.013986
								if( ema12 > -0.375171 )
									ret := 0.195641
							if( ema13 > 0.61692 )
								if( tema <= 47.4291 )
									ret := -0.814815 // sell
								if( tema > 47.4291 )
									ret := -0.034483
						if( mf > 0.047081 )
							if( ema13 <= 0.989545 )
								if( mf <= 0.177593 )
									ret := -0.086751
								if( mf > 0.177593 )
									ret := 0.111959
							if( ema13 > 0.989545 )
								if( ema3 <= 43.5911 )
									ret := 0.735294 // buy
								if( ema3 > 43.5911 )
									ret := 0.217391
					if( ad > -9681.9 )
						if( ema12 <= 0.028036 )
							ret := 0.947368 // buy
						if( ema12 > 0.028036 )
							ret := 0.615385
				if( tema > 51.5021 )
					if( ema3 <= 356.045 )
						if( ema1 <= 63.5907 )
							if( ad <= -10478.5 )
								if( mf <= 0.192744 )
									ret := 0.049724
								if( mf > 0.192744 )
									ret := -0.175153
							if( ad > -10478.5 )
								if( ema1 <= 54.3305 )
									ret := 0.024390
								if( ema1 > 54.3305 )
									ret := -0.423729
						if( ema1 > 63.5907 )
							if( ad_mf <= -11351.8 )
								if( mf <= -0.43425 )
									ret := -0.225204
								if( mf > -0.43425 )
									ret := -0.037278
							if( ad_mf > -11351.8 )
								if( ad <= -9514.45 )
									ret := -0.217323
								if( ad > -9514.45 )
									ret := -0.657534
					if( ema3 > 356.045 )
						if( ema12 <= -14.9139 )
							if( mf <= -0.212295 )
								ret := -0.454545
							if( mf > -0.212295 )
								ret := -1.000000 // sell
						if( ema12 > -14.9139 )
							if( mf <= 0.046574 )
								if( mf <= -0.092361 )
									ret := 0.027778
								if( mf > -0.092361 )
									ret := 0.268534
							if( mf > 0.046574 )
								if( ad <= -14645.2 )
									ret := 0.150289
								if( ad > -14645.2 )
									ret := -0.375661
			if( ema12 > 1.38095 )
				if( tema <= 611.556 )
					if( ad <= -333471 )
						if( tema <= 66.6456 )
							ret := 0.636364
						if( tema > 66.6456 )
							if( ad <= -489360 )
								ret := 0.823529 // buy
							if( ad > -489360 )
								ret := 1.000000 // buy
					if( ad > -333471 )
						if( ad <= -73732.3 )
							if( ad <= -159921 )
								if( ad <= -211476 )
									ret := -0.285714
								if( ad > -211476 )
									ret := 0.826087 // buy
							if( ad > -159921 )
								if( tema <= 176.82 )
									ret := 0.321429
								if( tema > 176.82 )
									ret := -0.431034
						if( ad > -73732.3 )
							if( ad <= -68373.1 )
								if( mf <= 0.26021 )
									ret := 0.923077 // buy
								if( mf > 0.26021 )
									ret := 0.666667
							if( ad > -68373.1 )
								if( tema <= 72.0127 )
									ret := 0.900000 // buy
								if( tema > 72.0127 )
									ret := 0.216185
				if( tema > 611.556 )
					if( ema1 <= 706.422 )
						if( ad <= -23514.1 )
							if( mf <= -0.010081 )
								ret := -0.888889 // sell
							if( mf > -0.010081 )
								if( ema2 <= 625.994 )
									ret := -0.500000
								if( ema2 > 625.994 )
									ret := 0.324324
						if( ad > -23514.1 )
							if( mf <= 0.033935 )
								ret := -1.000000 // sell
							if( mf > 0.033935 )
								if( ema12 <= 3.41016 )
									ret := -0.272727
								if( ema12 > 3.41016 )
									ret := -0.771429 // sell
					if( ema1 > 706.422 )
						if( ema1 <= 779.841 )
							if( ad_mf <= -18921.1 )
								if( ad <= -26302.7 )
									ret := 0.607143
								if( ad > -26302.7 )
									ret := -0.333333
							if( ad_mf > -18921.1 )
								if( ad <= -13212.7 )
									ret := 0.886364 // buy
								if( ad > -13212.7 )
									ret := -0.222222
						if( ema1 > 779.841 )
							if( ema12 <= 5.94229 )
								if( ema1 <= 866.875 )
									ret := 0.053191
								if( ema1 > 866.875 )
									ret := -0.566667
							if( ema12 > 5.94229 )
								if( ema13 <= 20.0985 )
									ret := -0.838710 // sell
								if( ema13 > 20.0985 )
									ret := 0.066667
		if( ad > -9350.2 )
			if( ad <= -422.084 )
				if( ad <= -452.046 )
					if( ema13 <= -0.331614 )
						if( ema2 <= 85.7705 )
							if( ema12 <= -0.207155 )
								if( ema12 <= -0.371404 )
									ret := 0.473592
								if( ema12 > -0.371404 )
									ret := 0.321825
							if( ema12 > -0.207155 )
								if( mf <= 0.104615 )
									ret := 0.140152
								if( mf > 0.104615 )
									ret := -0.377778
						if( ema2 > 85.7705 )
							if( mf <= 0.384922 )
								if( ad_mf <= -728.482 )
									ret := 0.074130
								if( ad_mf > -728.482 )
									ret := 0.344937
							if( mf > 0.384922 )
								if( ema12 <= -0.800415 )
									ret := 0.896552 // buy
								if( ema12 > -0.800415 )
									ret := 0.200000
					if( ema13 > -0.331614 )
						if( ema2 <= 784.246 )
							if( ema12 <= -0.263071 )
								if( mf <= -0.184409 )
									ret := 0.333333
								if( mf > -0.184409 )
									ret := -0.442623
							if( ema12 > -0.263071 )
								if( ad <= -1798.54 )
									ret := 0.122594
								if( ad > -1798.54 )
									ret := 0.062055
						if( ema2 > 784.246 )
							if( ad <= -807.518 )
								if( ema13 <= 2.98844 )
									ret := 0.356322
								if( ema13 > 2.98844 )
									ret := -0.156250
							if( ad > -807.518 )
								if( ema2 <= 822.668 )
									ret := -0.888889 // sell
								if( ema2 > 822.668 )
									ret := 0.000000
				if( ad > -452.046 )
					if( mf <= -0.398644 )
						ret := -0.545455
					if( mf > -0.398644 )
						if( ema1 <= 63.8707 )
							if( ad <= -448.602 )
								ret := 0.444444
							if( ad > -448.602 )
								if( ema1 <= 49.9934 )
									ret := 0.722222 // buy
								if( ema1 > 49.9934 )
									ret := 0.952381 // buy
						if( ema1 > 63.8707 )
							if( ad_mf <= -434.524 )
								if( tema <= 581.006 )
									ret := -0.135593
								if( tema > 581.006 )
									ret := 0.785714 // buy
							if( ad_mf > -434.524 )
								if( ema1 <= 92.5335 )
									ret := 0.904762 // buy
								if( ema1 > 92.5335 )
									ret := 0.540541
			if( ad > -422.084 )
				if( ema2 <= 282.682 )
					if( ad_mf <= 0.006666 )
						if( ema1 <= 278.511 )
							if( ema3 <= 273.789 )
								if( ema13 <= -0.384395 )
									ret := 0.097371
								if( ema13 > -0.384395 )
									ret := -0.070547
							if( ema3 > 273.789 )
								if( ema12 <= -0.300921 )
									ret := 0.769231 // buy
								if( ema12 > -0.300921 )
									ret := 0.047619
						if( ema1 > 278.511 )
							if( ema12 <= -0.14167 )
								ret := -1.000000 // sell
							if( ema12 > -0.14167 )
								if( tema <= 280.603 )
									ret := -0.166667
								if( tema > 280.603 )
									ret := -0.666667
					if( ad_mf > 0.006666 )
						if( ema12 <= 0.078632 )
							if( ema13 <= -1.19919 )
								if( ema1 <= 56.7205 )
									ret := -0.500000
								if( ema1 > 56.7205 )
									ret := 0.552000
							if( ema13 > -1.19919 )
								if( ema2 <= 198.807 )
									ret := 0.164013
								if( ema2 > 198.807 )
									ret := -0.131805
						if( ema12 > 0.078632 )
							if( ema12 <= 0.087139 )
								if( ema2 <= 59.4551 )
									ret := -0.366667
								if( ema2 > 59.4551 )
									ret := -0.791667 // sell
							if( ema12 > 0.087139 )
								if( tema <= 47.878 )
									ret := 0.355932
								if( tema > 47.878 )
									ret := -0.141197
				if( ema2 > 282.682 )
					if( ema13 <= -1.45513 )
						if( tema <= 450.852 )
							if( ad <= -220.556 )
								if( mf <= -0.200564 )
									ret := -1.000000 // sell
								if( mf > -0.200564 )
									ret := 0.416667
							if( ad > -220.556 )
								if( ema2 <= 302.079 )
									ret := 0.095238
								if( ema2 > 302.079 )
									ret := 0.625954
						if( tema > 450.852 )
							if( ema12 <= -5.89748 )
								if( ema13 <= -12.5873 )
									ret := -0.529412
								if( ema13 > -12.5873 )
									ret := 0.692308
							if( ema12 > -5.89748 )
								if( ema12 <= -3.44941 )
									ret := -0.801724 // sell
								if( ema12 > -3.44941 )
									ret := -0.250000
					if( ema13 > -1.45513 )
						if( ema2 <= 937.436 )
							if( tema <= 285.436 )
								if( ema13 <= -0.109959 )
									ret := 0.705882 // buy
								if( ema13 > -0.109959 )
									ret := 1.000000 // buy
							if( tema > 285.436 )
								if( ema12 <= 3.06736 )
									ret := 0.238275
								if( ema12 > 3.06736 )
									ret := -0.148649
						if( ema2 > 937.436 )
							if( ema13 <= 4.01148 )
								ret := -0.823529 // sell
							if( ema13 > 4.01148 )
								ret := -0.363636
	if( ad_mf > 0.225411 )
		if( ema13 <= 2.24638 )
			if( ema1 <= 43.8134 )
				if( ema13 <= -0.574791 )
					if( ad_mf <= 279458 )
						if( mf <= -0.211311 )
							if( mf <= -0.254534 )
								ret := 0.666667
							if( mf > -0.254534 )
								ret := 1.000000 // buy
						if( mf > -0.211311 )
							if( tema <= 39.8468 )
								if( ema12 <= -0.358672 )
									ret := 1.000000 // buy
								if( ema12 > -0.358672 )
									ret := 0.533333
							if( tema > 39.8468 )
								if( ema2 <= 43.012 )
									ret := 0.454545
								if( ema2 > 43.012 )
									ret := 0.000000
					if( ad_mf > 279458 )
						ret := 0.100000
				if( ema13 > -0.574791 )
					if( ad_mf <= 89.0051 )
						if( ema13 <= -0.086193 )
							if( mf <= -0.320674 )
								ret := -0.764706 // sell
							if( mf > -0.320674 )
								if( ema1 <= 34.6142 )
									ret := 1.000000 // buy
								if( ema1 > 34.6142 )
									ret := -0.500000
						if( ema13 > -0.086193 )
							if( mf <= -0.239478 )
								ret := -1.000000 // sell
							if( mf > -0.239478 )
								ret := -0.545455
					if( ad_mf > 89.0051 )
						if( ad <= 389364 )
							if( mf <= -0.412158 )
								if( ad <= 620.709 )
									ret := 0.913043 // buy
								if( ad > 620.709 )
									ret := 0.416667
							if( mf > -0.412158 )
								if( ema12 <= 0.114744 )
									ret := -0.029967
								if( ema12 > 0.114744 )
									ret := 0.115942
						if( ad > 389364 )
							if( ema13 <= 0.154925 )
								ret := 0.769231 // buy
							if( ema13 > 0.154925 )
								ret := 1.000000 // buy
			if( ema1 > 43.8134 )
				if( ad_mf <= 1817.14 )
					if( ad_mf <= 500.207 )
						if( ema1 <= 764.982 )
							if( ema13 <= -0.121365 )
								if( ad_mf <= 459.94 )
									ret := 0.047108
								if( ad_mf > 459.94 )
									ret := 0.579545
							if( ema13 > -0.121365 )
								if( ema3 <= 652.483 )
									ret := -0.076585
								if( ema3 > 652.483 )
									ret := 0.727273 // buy
						if( ema1 > 764.982 )
							if( ema1 <= 806.38 )
								if( ema3 <= 792.292 )
									ret := -0.967742 // sell
								if( ema3 > 792.292 )
									ret := -0.777778 // sell
							if( ema1 > 806.38 )
								if( ema12 <= 0.519634 )
									ret := -0.206897
								if( ema12 > 0.519634 )
									ret := 0.333333
					if( ad_mf > 500.207 )
						if( ema12 <= -0.557999 )
							if( ad_mf <= 625.592 )
								if( mf <= 0.172962 )
									ret := 0.635514
								if( mf > 0.172962 )
									ret := -0.409091
							if( ad_mf > 625.592 )
								if( tema <= 457.124 )
									ret := 0.167702
								if( tema > 457.124 )
									ret := -0.340426
						if( ema12 > -0.557999 )
							if( mf <= 0.375735 )
								if( ad_mf <= 625.443 )
									ret := -0.362924
								if( ad_mf > 625.443 )
									ret := -0.113313
							if( mf > 0.375735 )
								if( ema3 <= 235.206 )
									ret := -0.571031
								if( ema3 > 235.206 )
									ret := 0.071429
				if( ad_mf > 1817.14 )
					if( mf <= 0.55331 )
						if( ad <= 581690 )
							if( tema <= 43.7249 )
								if( ema1 <= 43.9705 )
									ret := -0.153846
								if( ema1 > 43.9705 )
									ret := 0.743590 // buy
							if( tema > 43.7249 )
								if( ad <= 24176.6 )
									ret := -0.010555
								if( ad > 24176.6 )
									ret := -0.065036
						if( ad > 581690 )
							if( ema13 <= -0.829886 )
								if( ema1 <= 63.7038 )
									ret := 0.909091 // buy
								if( ema1 > 63.7038 )
									ret := 1.000000 // buy
							if( ema13 > -0.829886 )
								if( mf <= 0.464405 )
									ret := 0.017964
								if( mf > 0.464405 )
									ret := 0.781250 // buy
					if( mf > 0.55331 )
						if( ema1 <= 47.6747 )
							if( ema2 <= 46.007 )
								ret := -0.562500
							if( ema2 > 46.007 )
								ret := -0.923077 // sell
						if( ema1 > 47.6747 )
							if( ema13 <= -0.351178 )
								if( ema1 <= 81.2529 )
									ret := -0.948718 // sell
								if( ema1 > 81.2529 )
									ret := -0.297872
							if( ema13 > -0.351178 )
								if( mf <= 0.756482 )
									ret := -0.113861
								if( mf > 0.756482 )
									ret := -0.424000
		if( ema13 > 2.24638 )
			if( ema3 <= 206.346 )
				if( ad <= 2641.77 )
					if( ema3 <= 190.938 )
						if( ad <= 1449.55 )
							if( tema <= 172.772 )
								if( ema12 <= 1.39796 )
									ret := 0.714286 // buy
								if( ema12 > 1.39796 )
									ret := 0.363636
							if( tema > 172.772 )
								ret := 0.000000
						if( ad > 1449.55 )
							if( ema12 <= 2.08888 )
								ret := -0.461538
							if( ema12 > 2.08888 )
								ret := 0.066667
					if( ema3 > 190.938 )
						if( ad_mf <= 1878.66 )
							ret := -0.533333
						if( ad_mf > 1878.66 )
							ret := -0.944444 // sell
				if( ad > 2641.77 )
					if( ema2 <= 81.4297 )
						if( ema3 <= 44.9676 )
							ret := -0.208333
						if( ema3 > 44.9676 )
							if( ad <= 427693 )
								if( ema12 <= 1.38929 )
									ret := 0.622642
								if( ema12 > 1.38929 )
									ret := 0.850394 // buy
							if( ad > 427693 )
								if( mf <= 0.526983 )
									ret := -0.205882
								if( mf > 0.526983 )
									ret := 0.900000 // buy
					if( ema2 > 81.4297 )
						if( ad_mf <= 321354 )
							if( mf <= 0.259022 )
								if( mf <= 0.131526 )
									ret := 0.050420
								if( mf > 0.131526 )
									ret := 0.569672
							if( mf > 0.259022 )
								if( ema12 <= 4.07612 )
									ret := 0.157182
								if( ema12 > 4.07612 )
									ret := -0.535714
						if( ad_mf > 321354 )
							if( tema <= 98.7694 )
								ret := 0.700000 // buy
							if( tema > 98.7694 )
								ret := 1.000000 // buy
			if( ema3 > 206.346 )
				if( tema <= 845.323 )
					if( ema2 <= 836.168 )
						if( mf <= -0.058377 )
							if( ema2 <= 584.281 )
								if( ema13 <= 3.05649 )
									ret := -0.148649
								if( ema13 > 3.05649 )
									ret := -0.614583
							if( ema2 > 584.281 )
								if( ema3 <= 661.106 )
									ret := 0.255814
								if( ema3 > 661.106 )
									ret := -0.309524
						if( mf > -0.058377 )
							if( mf <= -0.033125 )
								if( ad_mf <= 2392.31 )
									ret := 0.941176 // buy
								if( ad_mf > 2392.31 )
									ret := 0.294118
							if( mf > -0.033125 )
								if( ad_mf <= 226.223 )
									ret := -0.666667
								if( ad_mf > 226.223 )
									ret := -0.007197
					if( ema2 > 836.168 )
						ret := 0.809524 // buy
				if( tema > 845.323 )
					if( ad <= 13214.6 )
						if( ad <= 526 )
							if( mf <= 0.012937 )
								ret := -1.000000 // sell
							if( mf > 0.012937 )
								ret := -0.714286 // sell
						if( ad > 526 )
							if( mf <= 0.108309 )
								if( mf <= -0.027381 )
									ret := -0.357143
								if( mf > -0.027381 )
									ret := 0.304348
							if( mf > 0.108309 )
								if( ema1 <= 893.589 )
									ret := -0.480000
								if( ema1 > 893.589 )
									ret := -0.152174
					if( ad > 13214.6 )
						if( ema13 <= 4.15947 )
							ret := -0.300000
						if( ema13 > 4.15947 )
							if( ema1 <= 860.697 )
								ret := -0.562500
							if( ema1 > 860.697 )
								if( ema2 <= 863.506 )
									ret := -1.000000 // sell
								if( ema2 > 863.506 )
									ret := -0.736842 // sell
	
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
float op_operation = decision_tree_0_TTD_15Min_abd03fb6(ad_mf, mf, ad, ema2, ema1, ema12, ema3, ema13, tema)

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


