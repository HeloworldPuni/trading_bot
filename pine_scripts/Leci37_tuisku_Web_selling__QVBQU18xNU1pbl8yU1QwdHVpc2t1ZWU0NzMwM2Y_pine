//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: APPS_15Min_2ST0_ee47303f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_APPS_15Min_2ST0_ee47303f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_APPS_15Min_ee47303f(rsi1, smoothK_k, d_k, k, d, smoothD_d, ema3, tema, ema2, ema12, ema13, ema1)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( rsi1 <= 43.0225 )
		if( ema3 <= 6.42108 )
			if( ema3 <= 1.60569 )
				if( ema12 <= -0.013537 )
					if( ema2 <= 1.50818 )
						if( ema12 <= -0.014604 )
							if( d <= 2.66903 )
								if( ema1 <= 1.262 )
									ret := 0.368421
								if( ema1 > 1.262 )
									ret := 0.655172
							if( d > 2.66903 )
								if( rsi1 <= 20.114 )
									ret := 0.690476
								if( rsi1 > 20.114 )
									ret := 0.911290 // buy
						if( ema12 > -0.014604 )
							if( ema13 <= -0.025896 )
								ret := -0.055556
							if( ema13 > -0.025896 )
								if( rsi1 <= 19.5204 )
									ret := 1.000000 // buy
								if( rsi1 > 19.5204 )
									ret := 0.543860
					if( ema2 > 1.50818 )
						if( rsi1 <= 20.612 )
							if( k <= 4.14662 )
								ret := 0.111111
							if( k > 4.14662 )
								ret := 0.772727 // buy
						if( rsi1 > 20.612 )
							if( d_k <= 6.82545 )
								if( d <= 6.57153 )
									ret := -0.133333
								if( d > 6.57153 )
									ret := 0.466667
							if( d_k > 6.82545 )
								if( smoothK_k <= 5.6806 )
									ret := -0.615385
								if( smoothK_k > 5.6806 )
									ret := -0.153846
				if( ema12 > -0.013537 )
					if( d <= 0.519614 )
						if( ema2 <= 0.715303 )
							ret := 0.076923
						if( ema2 > 0.715303 )
							if( d_k <= -0.001308 )
								ret := 1.000000 // buy
							if( d_k > -0.001308 )
								if( ema1 <= 1.48412 )
									ret := 0.593750
								if( ema1 > 1.48412 )
									ret := 0.941176 // buy
					if( d > 0.519614 )
						if( ema2 <= 1.23019 )
							if( ema1 <= 0.675844 )
								if( ema13 <= -0.014442 )
									ret := -0.793103 // sell
								if( ema13 > -0.014442 )
									ret := 0.196721
							if( ema1 > 0.675844 )
								if( rsi1 <= 5.47115 )
									ret := -0.358491
								if( rsi1 > 5.47115 )
									ret := 0.322156
						if( ema2 > 1.23019 )
							if( ema3 <= 1.2888 )
								if( ema2 <= 1.2798 )
									ret := 0.000000
								if( ema2 > 1.2798 )
									ret := -0.714286 // sell
							if( ema3 > 1.2888 )
								if( ema3 <= 1.58887 )
									ret := 0.163623
								if( ema3 > 1.58887 )
									ret := 0.604651
			if( ema3 > 1.60569 )
				if( d <= 44.407 )
					if( d <= 37.6847 )
						if( ema1 <= 6.15687 )
							if( rsi1 <= 11.9299 )
								if( tema <= 3.76771 )
									ret := 0.640000
								if( tema > 3.76771 )
									ret := 0.333333
							if( rsi1 > 11.9299 )
								if( rsi1 <= 33.7213 )
									ret := 0.149399
								if( rsi1 > 33.7213 )
									ret := 0.010975
						if( ema1 > 6.15687 )
							if( smoothK_k <= 2.05114 )
								if( ema13 <= -0.028926 )
									ret := -0.242424
								if( ema13 > -0.028926 )
									ret := 0.500000
							if( smoothK_k > 2.05114 )
								if( d <= 9.12223 )
									ret := 0.142857
								if( d > 9.12223 )
									ret := 0.648855
					if( d > 37.6847 )
						if( d <= 38.0514 )
							if( k <= 27.3357 )
								ret := -0.062500
							if( k > 27.3357 )
								if( k <= 38.6496 )
									ret := -0.950000 // sell
								if( k > 38.6496 )
									ret := -0.230769
						if( d > 38.0514 )
							if( d_k <= -14.2301 )
								if( smoothD_d <= 38.583 )
									ret := -0.711111 // sell
								if( smoothD_d > 38.583 )
									ret := -0.159091
							if( d_k > -14.2301 )
								if( smoothK_k <= 36.9966 )
									ret := -0.082938
								if( smoothK_k > 36.9966 )
									ret := 0.349650
				if( d > 44.407 )
					if( ema13 <= -0.110268 )
						if( tema <= 4.79435 )
							if( smoothD_d <= 63.0549 )
								if( rsi1 <= 30.6043 )
									ret := 0.920000 // buy
								if( rsi1 > 30.6043 )
									ret := 1.000000 // buy
							if( smoothD_d > 63.0549 )
								ret := -0.090909
						if( tema > 4.79435 )
							if( k <= 84.9178 )
								if( rsi1 <= 37.4982 )
									ret := 0.200000
								if( rsi1 > 37.4982 )
									ret := 1.000000 // buy
							if( k > 84.9178 )
								ret := -0.600000
					if( ema13 > -0.110268 )
						if( smoothD_d <= 42.168 )
							if( ema12 <= -0.007349 )
								if( d_k <= 16.2231 )
									ret := 0.796296 // buy
								if( d_k > 16.2231 )
									ret := 0.454545
							if( ema12 > -0.007349 )
								if( rsi1 <= 38.6046 )
									ret := -0.285714
								if( rsi1 > 38.6046 )
									ret := 0.458333
						if( smoothD_d > 42.168 )
							if( smoothD_d <= 58.3468 )
								if( d <= 57.2892 )
									ret := 0.170489
								if( d > 57.2892 )
									ret := -0.132143
							if( smoothD_d > 58.3468 )
								if( ema13 <= -0.101982 )
									ret := -0.448276
								if( ema13 > -0.101982 )
									ret := 0.247107
		if( ema3 > 6.42108 )
			if( ema3 <= 41.2585 )
				if( rsi1 <= 6.94651 )
					if( d_k <= 0.45845 )
						if( ema13 <= -0.770184 )
							ret := -1.000000 // sell
						if( ema13 > -0.770184 )
							ret := -0.350000
					if( d_k > 0.45845 )
						if( k <= 0.133922 )
							ret := 0.111111
						if( k > 0.133922 )
							ret := 0.000000
				if( rsi1 > 6.94651 )
					if( ema3 <= 40.0063 )
						if( rsi1 <= 17.8207 )
							if( ema12 <= -0.04684 )
								if( ema3 <= 14.0484 )
									ret := 0.577273
								if( ema3 > 14.0484 )
									ret := 0.227941
							if( ema12 > -0.04684 )
								if( k <= 5.8331 )
									ret := 0.285714
								if( k > 5.8331 )
									ret := -0.821429 // sell
						if( rsi1 > 17.8207 )
							if( ema3 <= 38.9454 )
								if( ema1 <= 34.6756 )
									ret := 0.050595
								if( ema1 > 34.6756 )
									ret := 0.213518
							if( ema3 > 38.9454 )
								if( smoothD_d <= -0.30721 )
									ret := 0.769231 // buy
								if( smoothD_d > -0.30721 )
									ret := -0.345946
					if( ema3 > 40.0063 )
						if( rsi1 <= 30.7746 )
							if( ema3 <= 41.1006 )
								if( smoothD_d <= 6.61891 )
									ret := 0.809524 // buy
								if( smoothD_d > 6.61891 )
									ret := 0.170732
							if( ema3 > 41.1006 )
								if( d <= 54.5624 )
									ret := 0.933333 // buy
								if( d > 54.5624 )
									ret := 1.000000 // buy
						if( rsi1 > 30.7746 )
							if( smoothK_k <= 18.1153 )
								if( d <= 18.6807 )
									ret := 0.826667 // buy
								if( d > 18.6807 )
									ret := -0.764706 // sell
							if( smoothK_k > 18.1153 )
								if( rsi1 <= 38.6983 )
									ret := -0.758621 // sell
								if( rsi1 > 38.6983 )
									ret := -0.036364
			if( ema3 > 41.2585 )
				if( d <= 0.93978 )
					if( ema13 <= -0.487389 )
						if( tema <= 85.2097 )
							if( tema <= 62.5686 )
								if( ema13 <= -1.56924 )
									ret := 0.444444
								if( ema13 > -1.56924 )
									ret := -0.789116 // sell
							if( tema > 62.5686 )
								if( ema1 <= 79.2561 )
									ret := 0.340000
								if( ema1 > 79.2561 )
									ret := -0.870968 // sell
						if( tema > 85.2097 )
							ret := 0.933333 // buy
					if( ema13 > -0.487389 )
						if( rsi1 <= 37.5832 )
							if( k <= 0.366752 )
								if( ema12 <= -0.242983 )
									ret := -0.516129
								if( ema12 > -0.242983 )
									ret := 0.366667
							if( k > 0.366752 )
								if( ema1 <= 49.2395 )
									ret := 1.000000 // buy
								if( ema1 > 49.2395 )
									ret := 0.433333
						if( rsi1 > 37.5832 )
							if( ema13 <= 0.186724 )
								ret := -0.500000
							if( ema13 > 0.186724 )
								ret := -0.750000 // sell
				if( d > 0.93978 )
					if( smoothK_k <= 5.30692 )
						if( ema3 <= 72.9693 )
							if( rsi1 <= 18.967 )
								if( ema3 <= 67.2021 )
									ret := 0.542636
								if( ema3 > 67.2021 )
									ret := -0.588235
							if( rsi1 > 18.967 )
								if( rsi1 <= 30.778 )
									ret := -0.177049
								if( rsi1 > 30.778 )
									ret := 0.160828
						if( ema3 > 72.9693 )
							if( rsi1 <= 17.2884 )
								if( ema3 <= 82.2328 )
									ret := -0.694444
								if( ema3 > 82.2328 )
									ret := 0.500000
							if( rsi1 > 17.2884 )
								if( rsi1 <= 30.4841 )
									ret := 0.584615
								if( rsi1 > 30.4841 )
									ret := 0.193050
					if( smoothK_k > 5.30692 )
						if( tema <= 72.4566 )
							if( ema12 <= -0.580966 )
								if( k <= 48.7676 )
									ret := 0.059603
								if( k > 48.7676 )
									ret := 0.547771
							if( ema12 > -0.580966 )
								if( d_k <= 27.5451 )
									ret := -0.055217
								if( d_k > 27.5451 )
									ret := 0.596774
						if( tema > 72.4566 )
							if( ema13 <= -1.70271 )
								if( ema1 <= 82.685 )
									ret := -0.151079
								if( ema1 > 82.685 )
									ret := 0.822222 // buy
							if( ema13 > -1.70271 )
								if( ema12 <= -0.451289 )
									ret := -0.395887
								if( ema12 > -0.451289 )
									ret := -0.144144
	if( rsi1 > 43.0225 )
		if( tema <= 86.2101 )
			if( ema1 <= 4.10999 )
				if( k <= 77.25 )
					if( ema13 <= -0.020344 )
						if( smoothD_d <= 42.8128 )
							if( d_k <= 7.15136 )
								if( rsi1 <= 48.7216 )
									ret := -0.419463
								if( rsi1 > 48.7216 )
									ret := 0.067568
							if( d_k > 7.15136 )
								if( ema2 <= 3.80865 )
									ret := 0.142857
								if( ema2 > 3.80865 )
									ret := 0.933333 // buy
						if( smoothD_d > 42.8128 )
							if( k <= 74.5527 )
								if( tema <= 3.80124 )
									ret := -0.761317 // sell
								if( tema > 3.80124 )
									ret := -0.285714
							if( k > 74.5527 )
								if( rsi1 <= 45.6122 )
									ret := 0.000000
								if( rsi1 > 45.6122 )
									ret := -0.730769 // sell
					if( ema13 > -0.020344 )
						if( ema13 <= 0.17055 )
							if( rsi1 <= 66.5777 )
								if( smoothD_d <= 47.9162 )
									ret := -0.047340
								if( smoothD_d > 47.9162 )
									ret := 0.092702
							if( rsi1 > 66.5777 )
								if( ema3 <= 1.56613 )
									ret := -0.497573
								if( ema3 > 1.56613 )
									ret := -0.223214
						if( ema13 > 0.17055 )
							if( ema1 <= 2.47912 )
								ret := -0.400000
							if( ema1 > 2.47912 )
								if( k <= 73.7872 )
									ret := -1.000000 // sell
								if( k > 73.7872 )
									ret := -0.909091 // sell
				if( k > 77.25 )
					if( d_k <= -5.73633 )
						if( k <= 79.4717 )
							if( rsi1 <= 54.3723 )
								if( rsi1 <= 53.4412 )
									ret := -0.486842
								if( rsi1 > 53.4412 )
									ret := 0.666667
							if( rsi1 > 54.3723 )
								if( d_k <= -17.5632 )
									ret := -0.419355
								if( d_k > -17.5632 )
									ret := -0.721311 // sell
						if( k > 79.4717 )
							if( ema13 <= -0.015302 )
								if( ema12 <= -0.026543 )
									ret := -1.000000 // sell
								if( ema12 > -0.026543 )
									ret := 0.152778
							if( ema13 > -0.015302 )
								if( rsi1 <= 46.0314 )
									ret := 0.631579
								if( rsi1 > 46.0314 )
									ret := -0.244607
					if( d_k > -5.73633 )
						if( tema <= 0.88986 )
							if( tema <= 0.705437 )
								if( ema2 <= 0.684956 )
									ret := -0.464286
								if( ema2 > 0.684956 )
									ret := 0.415094
							if( tema > 0.705437 )
								if( smoothD_d <= 91.0322 )
									ret := -0.327684
								if( smoothD_d > 91.0322 )
									ret := -0.852941 // sell
						if( tema > 0.88986 )
							if( tema <= 3.98966 )
								if( rsi1 <= 63.7693 )
									ret := 0.050601
								if( rsi1 > 63.7693 )
									ret := -0.110259
							if( tema > 3.98966 )
								if( k <= 87.524 )
									ret := -0.209302
								if( k > 87.524 )
									ret := -0.670455
			if( ema1 > 4.10999 )
				if( smoothK_k <= 14.4439 )
					if( ema13 <= 0.91972 )
						if( ema13 <= 0.412794 )
							if( ema3 <= 84.5997 )
								if( ema13 <= -0.002691 )
									ret := 0.024201
								if( ema13 > -0.002691 )
									ret := 0.128553
							if( ema3 > 84.5997 )
								if( ema2 <= 84.723 )
									ret := -0.923077 // sell
								if( ema2 > 84.723 )
									ret := -0.407407
						if( ema13 > 0.412794 )
							if( d_k <= 10.7894 )
								if( rsi1 <= 51.8769 )
									ret := 0.063492
								if( rsi1 > 51.8769 )
									ret := -0.441748
							if( d_k > 10.7894 )
								if( ema2 <= 34.3843 )
									ret := -0.296296
								if( ema2 > 34.3843 )
									ret := 0.280899
					if( ema13 > 0.91972 )
						if( smoothK_k <= 5.45718 )
							if( ema3 <= 57.0623 )
								if( ema13 <= 0.990551 )
									ret := 0.666667
								if( ema13 > 0.990551 )
									ret := 0.974359 // buy
							if( ema3 > 57.0623 )
								if( ema13 <= 1.4892 )
									ret := 0.428571
								if( ema13 > 1.4892 )
									ret := 0.000000
						if( smoothK_k > 5.45718 )
							if( ema13 <= 1.07596 )
								ret := 0.687500
							if( ema13 > 1.07596 )
								if( ema2 <= 76.0191 )
									ret := 0.193548
								if( ema2 > 76.0191 )
									ret := -0.571429
				if( smoothK_k > 14.4439 )
					if( ema12 <= 0.384161 )
						if( k <= 27.3755 )
							if( smoothK_k <= 24.1614 )
								if( ema13 <= 0.08681 )
									ret := -0.157895
								if( ema13 > 0.08681 )
									ret := -0.024472
							if( smoothK_k > 24.1614 )
								if( ema12 <= 0.04483 )
									ret := -0.486486
								if( ema12 > 0.04483 )
									ret := -0.923077 // sell
						if( k > 27.3755 )
							if( ema1 <= 5.46537 )
								if( d_k <= 2.33143 )
									ret := -0.033749
								if( d_k > 2.33143 )
									ret := 0.251695
							if( ema1 > 5.46537 )
								if( ema3 <= 83.5916 )
									ret := -0.049980
								if( ema3 > 83.5916 )
									ret := 0.237805
					if( ema12 > 0.384161 )
						if( ema12 <= 0.795204 )
							if( tema <= 50.7744 )
								if( d <= 51.3717 )
									ret := 0.400000
								if( d > 51.3717 )
									ret := -0.024272
							if( tema > 50.7744 )
								if( ema13 <= 1.25735 )
									ret := 0.225906
								if( ema13 > 1.25735 )
									ret := -0.070485
						if( ema12 > 0.795204 )
							if( ema2 <= 70.7574 )
								if( d <= 61.618 )
									ret := -0.615385
								if( d > 61.618 )
									ret := 0.129288
							if( ema2 > 70.7574 )
								if( ema3 <= 82.8663 )
									ret := -0.306233
								if( ema3 > 82.8663 )
									ret := 0.923077 // buy
		if( tema > 86.2101 )
			if( ema2 <= 94.1278 )
				if( k <= 68.9349 )
					if( d <= 23.3776 )
						if( ema3 <= 92.8572 )
							if( ema3 <= 89.3763 )
								if( ema1 <= 87.7009 )
									ret := -0.307692
								if( ema1 > 87.7009 )
									ret := 0.255814
							if( ema3 > 89.3763 )
								if( d <= 10.0481 )
									ret := -0.777778 // sell
								if( d > 10.0481 )
									ret := -0.583333
						if( ema3 > 92.8572 )
							ret := 0.500000
					if( d > 23.3776 )
						if( tema <= 93.6245 )
							if( smoothK_k <= 19.5325 )
								if( smoothK_k <= 6.49977 )
									ret := -0.444444
								if( smoothK_k > 6.49977 )
									ret := -0.883721 // sell
							if( smoothK_k > 19.5325 )
								if( d_k <= 6.98641 )
									ret := -0.398907
								if( d_k > 6.98641 )
									ret := -0.609756
						if( tema > 93.6245 )
							ret := 0.304348
				if( k > 68.9349 )
					if( ema2 <= 86.6682 )
						if( d <= 84.7896 )
							if( smoothK_k <= 72.2919 )
								ret := -0.526316
							if( smoothK_k > 72.2919 )
								if( smoothD_d <= 78.4137 )
									ret := 0.000000
								if( smoothD_d > 78.4137 )
									ret := 0.666667
						if( d > 84.7896 )
							if( rsi1 <= 79.0088 )
								if( smoothK_k <= 95.2853 )
									ret := -0.581818
								if( smoothK_k > 95.2853 )
									ret := 0.100000
							if( rsi1 > 79.0088 )
								if( ema2 <= 85.2935 )
									ret := -0.565217
								if( ema2 > 85.2935 )
									ret := -0.838710 // sell
					if( ema2 > 86.6682 )
						if( tema <= 88.4658 )
							if( k <= 85.2631 )
								if( rsi1 <= 48.2107 )
									ret := 0.880000 // buy
								if( rsi1 > 48.2107 )
									ret := 0.509804
							if( k > 85.2631 )
								if( k <= 94.306 )
									ret := 0.177778
								if( k > 94.306 )
									ret := -0.400000
						if( tema > 88.4658 )
							if( ema12 <= 0.934059 )
								if( d_k <= -0.006152 )
									ret := -0.573770
								if( d_k > -0.006152 )
									ret := -0.168317
							if( ema12 > 0.934059 )
								if( ema2 <= 87.6755 )
									ret := -0.384615
								if( ema2 > 87.6755 )
									ret := 0.622222
			if( ema2 > 94.1278 )
				if( d_k <= -1.00776 )
					if( d_k <= -8.21107 )
						ret := -0.714286 // sell
					if( d_k > -8.21107 )
						ret := -1.000000 // sell
				if( d_k > -1.00776 )
					ret := 0.045455
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

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
float op_operation = decision_tree_0_APPS_15Min_ee47303f(rsi1, smoothK_k, d_k, k, d, smoothD_d, ema3, tema, ema2, ema12, ema13, ema1)

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


