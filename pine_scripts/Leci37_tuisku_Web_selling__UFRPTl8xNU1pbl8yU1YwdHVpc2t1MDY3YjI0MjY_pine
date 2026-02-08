//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: PTON_15Min_2SV0_067b2426 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PTON_15Min_2SV0_067b2426", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PTON_15Min_067b2426(d, d_k, smoothK_k, k, rsi1, smoothD_d, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( smoothK_k <= 2.76599 )
		if( VIP_VIM <= -0.670587 )
			if( d <= 2.87387 )
				if( VIP_VIM <= -1.30099 )
					if( VIP <= 0.321077 )
						ret := -1.000000 // sell
					if( VIP > 0.321077 )
						ret := -0.833333 // sell
				if( VIP_VIM > -1.30099 )
					if( VIM <= 1.38116 )
						if( VIP_VIM <= -0.759077 )
							if( smoothD_d <= -1.28183 )
								if( d_k <= 0.004063 )
									ret := 0.736842 // buy
								if( d_k > 0.004063 )
									ret := 0.950000 // buy
							if( smoothD_d > -1.28183 )
								ret := 0.300000
						if( VIP_VIM > -0.759077 )
							if( VIP_VIM <= -0.735807 )
								if( d_k <= 0.08537 )
									ret := -0.590909
								if( d_k > 0.08537 )
									ret := 0.333333
							if( VIP_VIM > -0.735807 )
								if( VIP_VIM <= -0.676148 )
									ret := 0.387597
								if( VIP_VIM > -0.676148 )
									ret := -0.222222
					if( VIM > 1.38116 )
						if( rsi1 <= 17.3857 )
							if( VIP <= 0.846535 )
								if( k <= 1.46858 )
									ret := 0.000000
								if( k > 1.46858 )
									ret := 0.492063
							if( VIP > 0.846535 )
								ret := -0.611111
						if( rsi1 > 17.3857 )
							if( VIP <= 0.764987 )
								if( VIP <= 0.668876 )
									ret := -0.118421
								if( VIP > 0.668876 )
									ret := -0.562500
							if( VIP > 0.764987 )
								if( rsi1 <= 22.8041 )
									ret := 0.040000
								if( rsi1 > 22.8041 )
									ret := 0.428571
			if( d > 2.87387 )
				if( d <= 15.8117 )
					if( d_k <= 7.49343 )
						if( rsi1 <= 8.79979 )
							if( smoothD_d <= 0.896775 )
								ret := -0.388889
							if( smoothD_d > 0.896775 )
								if( d_k <= 4.32738 )
									ret := -1.000000 // sell
								if( d_k > 4.32738 )
									ret := -0.500000
						if( rsi1 > 8.79979 )
							if( d_k <= 6.95663 )
								if( d_k <= 2.30909 )
									ret := -0.258333
								if( d_k > 2.30909 )
									ret := 0.072539
							if( d_k > 6.95663 )
								if( VIM <= 1.38761 )
									ret := -0.909091 // sell
								if( VIM > 1.38761 )
									ret := -0.666667
					if( d_k > 7.49343 )
						if( smoothK_k <= -1.32388 )
							if( k <= 0.158139 )
								if( rsi1 <= 25.4348 )
									ret := 0.500000
								if( rsi1 > 25.4348 )
									ret := -0.272727
							if( k > 0.158139 )
								if( smoothK_k <= -2.65184 )
									ret := 1.000000 // buy
								if( smoothK_k > -2.65184 )
									ret := 0.695652
						if( smoothK_k > -1.32388 )
							if( smoothK_k <= 0.642781 )
								ret := -0.687500
							if( smoothK_k > 0.642781 )
								ret := 0.461538
				if( d > 15.8117 )
					if( smoothK_k <= 2.06009 )
						if( d <= 20.096 )
							if( smoothK_k <= -1.81497 )
								ret := -0.692308
							if( smoothK_k > -1.81497 )
								ret := -0.913043 // sell
						if( d > 20.096 )
							if( rsi1 <= 21.8752 )
								if( d_k <= 27.3968 )
									ret := -0.941176 // sell
								if( d_k > 27.3968 )
									ret := -0.461538
							if( rsi1 > 21.8752 )
								if( VIP_VIM <= -0.701181 )
									ret := 0.384615
								if( VIP_VIM > -0.701181 )
									ret := -0.555556
					if( smoothK_k > 2.06009 )
						ret := 0.666667
		if( VIP_VIM > -0.670587 )
			if( rsi1 <= 20.0808 )
				if( k <= 1.09129 )
					if( d_k <= 16.597 )
						if( VIM <= 1.8159 )
							if( d_k <= 0.798379 )
								if( smoothK_k <= -2.31614 )
									ret := 0.211765
								if( smoothK_k > -2.31614 )
									ret := 0.947368 // buy
							if( d_k > 0.798379 )
								if( d_k <= 1.87199 )
									ret := 0.940000 // buy
								if( d_k > 1.87199 )
									ret := 0.757225 // buy
						if( VIM > 1.8159 )
							ret := -0.500000
					if( d_k > 16.597 )
						ret := -0.454545
				if( k > 1.09129 )
					if( k <= 3.84464 )
						if( smoothK_k <= -0.01628 )
							if( k <= 2.91076 )
								if( smoothD_d <= 5.47138 )
									ret := 0.223776
								if( smoothD_d > 5.47138 )
									ret := -0.523810
							if( k > 2.91076 )
								ret := 0.923077 // buy
						if( smoothK_k > -0.01628 )
							if( rsi1 <= 14.1382 )
								if( VIM <= 1.3001 )
									ret := -0.954545 // sell
								if( VIM > 1.3001 )
									ret := -0.307692
							if( rsi1 > 14.1382 )
								if( smoothK_k <= 0.31813 )
									ret := -0.333333
								if( smoothK_k > 0.31813 )
									ret := 0.476190
					if( k > 3.84464 )
						if( d_k <= -2.00097 )
							ret := -0.150000
						if( d_k > -2.00097 )
							if( d <= 4.5712 )
								if( d <= 3.38354 )
									ret := 0.843750 // buy
								if( d > 3.38354 )
									ret := 0.605263
							if( d > 4.5712 )
								if( VIM <= 1.27084 )
									ret := -0.357143
								if( VIM > 1.27084 )
									ret := 0.479167
			if( rsi1 > 20.0808 )
				if( smoothD_d <= 13.7405 )
					if( VIP <= 0.766586 )
						if( VIM <= 1.35732 )
							if( VIM <= 1.13018 )
								ret := 0.640000
							if( VIM > 1.13018 )
								if( smoothD_d <= 6.58448 )
									ret := -0.108280
								if( smoothD_d > 6.58448 )
									ret := 0.264706
						if( VIM > 1.35732 )
							if( rsi1 <= 28.8746 )
								if( smoothD_d <= 1.75104 )
									ret := -0.961538 // sell
								if( smoothD_d > 1.75104 )
									ret := -0.578947
							if( rsi1 > 28.8746 )
								ret := 0.250000
					if( VIP > 0.766586 )
						if( VIP <= 1.37909 )
							if( d <= 15.2718 )
								if( k <= 4.42821 )
									ret := 0.061553
								if( k > 4.42821 )
									ret := 0.225968
							if( d > 15.2718 )
								if( VIP_VIM <= -0.178418 )
									ret := -0.527273
								if( VIP_VIM > -0.178418 )
									ret := -0.191489
						if( VIP > 1.37909 )
							if( k <= 5.1216 )
								if( d <= 1.26633 )
									ret := 0.693878
								if( d > 1.26633 )
									ret := 0.149068
							if( k > 5.1216 )
								if( rsi1 <= 47.9485 )
									ret := 0.481481
								if( rsi1 > 47.9485 )
									ret := 1.000000 // buy
				if( smoothD_d > 13.7405 )
					if( smoothD_d <= 25.6735 )
						if( rsi1 <= 38.2048 )
							if( VIP <= 0.745156 )
								if( smoothK_k <= -2.9312 )
									ret := 0.368421
								if( smoothK_k > -2.9312 )
									ret := 0.853659 // buy
							if( VIP > 0.745156 )
								if( rsi1 <= 30.7451 )
									ret := 0.338710
								if( rsi1 > 30.7451 )
									ret := -0.175676
						if( rsi1 > 38.2048 )
							if( d <= 23.5738 )
								if( VIP <= 0.980739 )
									ret := 0.692308
								if( VIP > 0.980739 )
									ret := 0.233010
							if( d > 23.5738 )
								if( rsi1 <= 52.8774 )
									ret := 0.851351 // buy
								if( rsi1 > 52.8774 )
									ret := 0.200000
					if( smoothD_d > 25.6735 )
						if( VIP <= 0.889318 )
							if( k <= 2.34242 )
								if( smoothD_d <= 26.7299 )
									ret := -1.000000 // sell
								if( smoothD_d > 26.7299 )
									ret := -0.826087 // sell
							if( k > 2.34242 )
								ret := -0.181818
						if( VIP > 0.889318 )
							if( k <= 3.43921 )
								if( VIM <= 1.08311 )
									ret := 0.900000 // buy
								if( VIM > 1.08311 )
									ret := 0.666667
							if( k > 3.43921 )
								if( smoothD_d <= 29.6695 )
									ret := 0.100000
								if( smoothD_d > 29.6695 )
									ret := -0.300000
	if( smoothK_k > 2.76599 )
		if( VIP <= 1.33046 )
			if( rsi1 <= 46.2862 )
				if( d <= 6.70995 )
					if( rsi1 <= 27.0665 )
						if( VIP_VIM <= -0.565155 )
							if( d <= 6.57125 )
								if( k <= 7.79016 )
									ret := 0.250000
								if( k > 7.79016 )
									ret := -0.185430
							if( d > 6.57125 )
								ret := -0.782609 // sell
						if( VIP_VIM > -0.565155 )
							if( d_k <= -1.98158 )
								if( rsi1 <= 25.706 )
									ret := 0.063492
								if( rsi1 > 25.706 )
									ret := 0.714286 // buy
							if( d_k > -1.98158 )
								if( smoothD_d <= 3.4245 )
									ret := -0.458333
								if( smoothD_d > 3.4245 )
									ret := 0.062500
					if( rsi1 > 27.0665 )
						if( VIP_VIM <= -0.535778 )
							if( rsi1 <= 38.3589 )
								if( k <= 6.63455 )
									ret := -0.029412
								if( k > 6.63455 )
									ret := -0.607843
							if( rsi1 > 38.3589 )
								ret := 0.052632
						if( VIP_VIM > -0.535778 )
							if( VIP <= 0.939103 )
								if( VIP <= 0.722044 )
									ret := 0.689655
								if( VIP > 0.722044 )
									ret := -0.266369
							if( VIP > 0.939103 )
								if( d <= 5.88402 )
									ret := 0.341772
								if( d > 5.88402 )
									ret := -0.188525
				if( d > 6.70995 )
					if( smoothD_d <= 79.1148 )
						if( d <= 7.49573 )
							if( k <= 6.23874 )
								ret := -0.588235
							if( k > 6.23874 )
								if( rsi1 <= 22.6129 )
									ret := -0.117647
								if( rsi1 > 22.6129 )
									ret := 0.369697
						if( d > 7.49573 )
							if( smoothK_k <= 91.602 )
								if( k <= 83.0207 )
									ret := 0.034688
								if( k > 83.0207 )
									ret := -0.242358
							if( smoothK_k > 91.602 )
								if( smoothK_k <= 94.2744 )
									ret := 0.655556
								if( smoothK_k > 94.2744 )
									ret := -0.086957
					if( smoothD_d > 79.1148 )
						if( k <= 87.0526 )
							if( d <= 94.2907 )
								if( VIM <= 0.999846 )
									ret := 0.656716
								if( VIM > 0.999846 )
									ret := 0.264402
							if( d > 94.2907 )
								ret := -0.884615 // sell
						if( k > 87.0526 )
							if( VIP <= 1.06993 )
								if( smoothK_k <= 87.2328 )
									ret := -0.231156
								if( smoothK_k > 87.2328 )
									ret := 0.174404
							if( VIP > 1.06993 )
								if( VIP_VIM <= -0.165403 )
									ret := 0.083333
								if( VIP_VIM > -0.165403 )
									ret := -0.740000 // sell
			if( rsi1 > 46.2862 )
				if( VIM <= 1.09071 )
					if( smoothK_k <= 6.95888 )
						if( smoothD_d <= 14.15 )
							if( VIP_VIM <= -0.130277 )
								ret := 0.823529 // buy
							if( VIP_VIM > -0.130277 )
								if( rsi1 <= 61.0655 )
									ret := -0.021898
								if( rsi1 > 61.0655 )
									ret := -0.456790
						if( smoothD_d > 14.15 )
							if( VIP <= 1.10939 )
								if( VIP_VIM <= 0.11932 )
									ret := -0.580000
								if( VIP_VIM > 0.11932 )
									ret := 0.347826
							if( VIP > 1.10939 )
								if( rsi1 <= 59.0009 )
									ret := -0.333333
								if( rsi1 > 59.0009 )
									ret := -0.771429 // sell
					if( smoothK_k > 6.95888 )
						if( VIP <= 0.991145 )
							if( smoothK_k <= 12.4179 )
								if( VIP_VIM <= -0.11762 )
									ret := 0.809524 // buy
								if( VIP_VIM > -0.11762 )
									ret := 0.108108
							if( smoothK_k > 12.4179 )
								if( smoothD_d <= 14.4494 )
									ret := -0.396947
								if( smoothD_d > 14.4494 )
									ret := -0.105044
						if( VIP > 0.991145 )
							if( VIP_VIM <= 0.582751 )
								if( rsi1 <= 71.9789 )
									ret := 0.021108
								if( rsi1 > 71.9789 )
									ret := -0.068486
							if( VIP_VIM > 0.582751 )
								if( d <= 36.853 )
									ret := -0.833333 // sell
								if( d > 36.853 )
									ret := 0.141463
				if( VIM > 1.09071 )
					if( smoothD_d <= 12.6695 )
						if( k <= 12.6849 )
							if( smoothD_d <= 1.81699 )
								if( smoothD_d <= 1.16409 )
									ret := -0.090909
								if( smoothD_d > 1.16409 )
									ret := -0.454545
							if( smoothD_d > 1.81699 )
								if( smoothK_k <= 3.38382 )
									ret := 0.100000
								if( smoothK_k > 3.38382 )
									ret := 0.500000
						if( k > 12.6849 )
							if( k <= 20.1453 )
								if( d_k <= -3.79426 )
									ret := -0.615385
								if( d_k > -3.79426 )
									ret := 0.298507
							if( k > 20.1453 )
								if( k <= 23.6722 )
									ret := 0.567164
								if( k > 23.6722 )
									ret := 0.131783
					if( smoothD_d > 12.6695 )
						if( rsi1 <= 52.0733 )
							if( k <= 50.6154 )
								if( k <= 8.29769 )
									ret := -0.812500 // sell
								if( k > 8.29769 )
									ret := -0.148679
							if( k > 50.6154 )
								if( smoothD_d <= 52.3781 )
									ret := 0.323718
								if( smoothD_d > 52.3781 )
									ret := -0.025057
						if( rsi1 > 52.0733 )
							if( d <= 41.1913 )
								if( smoothD_d <= 31.8403 )
									ret := -0.260128
								if( smoothD_d > 31.8403 )
									ret := -0.492308
							if( d > 41.1913 )
								if( smoothD_d <= 66.2296 )
									ret := -0.020112
								if( smoothD_d > 66.2296 )
									ret := -0.230916
		if( VIP > 1.33046 )
			if( d_k <= 15.1352 )
				if( smoothD_d <= 24.0002 )
					if( rsi1 <= 58.8364 )
						if( VIP_VIM <= 0.14382 )
							if( smoothD_d <= 2.98955 )
								if( VIM <= 1.85344 )
									ret := 0.096774
								if( VIM > 1.85344 )
									ret := 0.641304
							if( smoothD_d > 2.98955 )
								if( smoothD_d <= 9.39786 )
									ret := -0.200581
								if( smoothD_d > 9.39786 )
									ret := 0.171254
						if( VIP_VIM > 0.14382 )
							if( k <= 12.2996 )
								if( VIM <= 1.18132 )
									ret := -0.655172
								if( VIM > 1.18132 )
									ret := -0.268817
							if( k > 12.2996 )
								if( k <= 12.8008 )
									ret := 0.727273 // buy
								if( k > 12.8008 )
									ret := -0.030303
					if( rsi1 > 58.8364 )
						if( smoothD_d <= 22.14 )
							if( rsi1 <= 60.9707 )
								if( d_k <= -13.716 )
									ret := -0.840000 // sell
								if( d_k > -13.716 )
									ret := -0.376344
							if( rsi1 > 60.9707 )
								if( VIP <= 2.03445 )
									ret := -0.012931
								if( VIP > 2.03445 )
									ret := -0.700000 // sell
						if( smoothD_d > 22.14 )
							if( rsi1 <= 67.3967 )
								if( smoothK_k <= 28.5612 )
									ret := -0.312500
								if( smoothK_k > 28.5612 )
									ret := 0.769231 // buy
							if( rsi1 > 67.3967 )
								ret := 0.705882 // buy
				if( smoothD_d > 24.0002 )
					if( VIP_VIM <= 0.275683 )
						if( k <= 61.02 )
							if( d_k <= -21.0417 )
								if( d_k <= -22.3945 )
									ret := 0.611111
								if( d_k > -22.3945 )
									ret := 1.000000 // buy
							if( d_k > -21.0417 )
								if( k <= 17.0503 )
									ret := -0.631579
								if( k > 17.0503 )
									ret := -0.082389
						if( k > 61.02 )
							if( k <= 66.158 )
								if( d <= 77.1091 )
									ret := -0.461690
								if( d > 77.1091 )
									ret := 0.521739
							if( k > 66.158 )
								if( k <= 96.7403 )
									ret := -0.140902
								if( k > 96.7403 )
									ret := -0.394286
					if( VIP_VIM > 0.275683 )
						if( rsi1 <= 50.5543 )
							if( d <= 77.4401 )
								if( VIP_VIM <= 0.293614 )
									ret := 0.578947
								if( VIP_VIM > 0.293614 )
									ret := -0.003937
							if( d > 77.4401 )
								if( VIP_VIM <= 0.298816 )
									ret := 0.090909
								if( VIP_VIM > 0.298816 )
									ret := 0.644444
						if( rsi1 > 50.5543 )
							if( d_k <= -0.343515 )
								if( smoothK_k <= 96.6594 )
									ret := -0.109606
								if( smoothK_k > 96.6594 )
									ret := -0.301294
							if( d_k > -0.343515 )
								if( smoothD_d <= 28.0938 )
									ret := -0.644444
								if( smoothD_d > 28.0938 )
									ret := -0.000280
			if( d_k > 15.1352 )
				if( k <= 9.93992 )
					if( k <= 8.92491 )
						if( smoothK_k <= 3.62166 )
							ret := 0.636364
						if( smoothK_k > 3.62166 )
							if( smoothK_k <= 5.21308 )
								ret := 0.153846
							if( smoothK_k > 5.21308 )
								ret := 0.428571
					if( k > 8.92491 )
						if( smoothD_d <= 27.3833 )
							ret := 1.000000 // buy
						if( smoothD_d > 27.3833 )
							ret := 0.764706 // buy
				if( k > 9.93992 )
					if( VIM <= 1.54382 )
						if( rsi1 <= 62.0499 )
							if( k <= 10.9673 )
								ret := -0.600000
							if( k > 10.9673 )
								if( rsi1 <= 46.368 )
									ret := 0.147436
								if( rsi1 > 46.368 )
									ret := 0.451713
						if( rsi1 > 62.0499 )
							if( k <= 52.9163 )
								if( d_k <= 16.4237 )
									ret := -0.411765
								if( d_k > 16.4237 )
									ret := 0.186667
							if( k > 52.9163 )
								if( VIP_VIM <= 0.629833 )
									ret := -0.695652
								if( VIP_VIM > 0.629833 )
									ret := 0.142857
					if( VIM > 1.54382 )
						if( VIP_VIM <= 0.319884 )
							if( VIP <= 1.4609 )
								if( smoothD_d <= 27.9058 )
									ret := 0.400000
								if( smoothD_d > 27.9058 )
									ret := -0.492063
							if( VIP > 1.4609 )
								if( rsi1 <= 35.8495 )
									ret := 0.653465
								if( rsi1 > 35.8495 )
									ret := -0.086538
						if( VIP_VIM > 0.319884 )
							if( k <= 55.6482 )
								if( d <= 45.8006 )
									ret := 0.105263
								if( d > 45.8006 )
									ret := -0.304348
							if( k > 55.6482 )
								if( d_k <= 17.9432 )
									ret := -1.000000 // sell
								if( d_k > 17.9432 )
									ret := -0.777778 // sell
	
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
float op_operation = decision_tree_0_PTON_15Min_067b2426(d, d_k, smoothK_k, k, rsi1, smoothD_d, VIP, VIP_VIM, VIM)

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


