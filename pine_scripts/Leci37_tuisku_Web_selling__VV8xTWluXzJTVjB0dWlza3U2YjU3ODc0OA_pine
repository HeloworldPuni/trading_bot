//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: U_1Min_2SV0_6b578748 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_2SV0_6b578748", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_6b578748(rsi1, d, k, smoothD_d, d_k, smoothK_k, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( rsi1 <= 51.1698 )
		if( VIP_VIM <= -0.83057 )
			if( rsi1 <= 46.6329 )
				if( VIM <= 5.82952 )
					if( smoothD_d <= 78.5911 )
						if( d <= 75.2917 )
							if( k <= 0.136386 )
								if( d <= 6.2e-05 )
									ret := 0.273684
								if( d > 6.2e-05 )
									ret := -0.123457
							if( k > 0.136386 )
								if( d <= 66.9253 )
									ret := 0.215408
								if( d > 66.9253 )
									ret := 0.750000 // buy
						if( d > 75.2917 )
							ret := -0.545455
					if( smoothD_d > 78.5911 )
						if( k <= 77.2806 )
							ret := 0.875000 // buy
						if( k > 77.2806 )
							ret := 1.000000 // buy
				if( VIM > 5.82952 )
					if( d <= 71.6185 )
						if( k <= 6.92259 )
							if( d_k <= 12.6427 )
								if( d_k <= 7.75384 )
									ret := 0.683673
								if( d_k > 7.75384 )
									ret := 0.966667 // buy
							if( d_k > 12.6427 )
								ret := 0.181818
						if( k > 6.92259 )
							if( smoothK_k <= 7.27748 )
								if( VIP <= 8.02632 )
									ret := -0.466667
								if( VIP > 8.02632 )
									ret := 0.090909
							if( smoothK_k > 7.27748 )
								if( VIP_VIM <= -0.972001 )
									ret := 0.351899
								if( VIP_VIM > -0.972001 )
									ret := 0.716981 // buy
					if( d > 71.6185 )
						if( VIP <= 9.24091 )
							ret := 0.000000
						if( VIP > 9.24091 )
							if( rsi1 <= 44.7663 )
								ret := -0.777778 // sell
							if( rsi1 > 44.7663 )
								ret := -0.250000
			if( rsi1 > 46.6329 )
				if( VIP <= 7.59917 )
					if( d_k <= -5.65747 )
						if( d_k <= -9.4404 )
							if( smoothK_k <= 67.0794 )
								ret := 0.076923
							if( smoothK_k > 67.0794 )
								ret := 0.454545
						if( d_k > -9.4404 )
							ret := -0.750000 // sell
					if( d_k > -5.65747 )
						if( smoothD_d <= 30.3399 )
							if( smoothK_k <= 29.0326 )
								if( k <= 11.9913 )
									ret := 0.545455
								if( k > 11.9913 )
									ret := 0.071429
							if( smoothK_k > 29.0326 )
								ret := 0.800000 // buy
						if( smoothD_d > 30.3399 )
							if( VIM <= 3.75907 )
								if( k <= 65.8078 )
									ret := 0.176471
								if( k > 65.8078 )
									ret := 0.545455
							if( VIM > 3.75907 )
								if( smoothD_d <= 63.4155 )
									ret := -0.260870
								if( smoothD_d > 63.4155 )
									ret := 0.230769
				if( VIP > 7.59917 )
					if( smoothD_d <= 6.40513 )
						ret := 0.692308
					if( smoothD_d > 6.40513 )
						if( VIM <= 9.77036 )
							ret := -1.000000 // sell
						if( VIM > 9.77036 )
							if( k <= 72.2483 )
								if( rsi1 <= 49.8729 )
									ret := -0.475410
								if( rsi1 > 49.8729 )
									ret := -0.166667
							if( k > 72.2483 )
								ret := 0.052632
		if( VIP_VIM > -0.83057 )
			if( VIM <= 1.41658 )
				if( VIP_VIM <= 0.175444 )
					if( smoothK_k <= 0.176014 )
						if( d_k <= 11.1059 )
							if( rsi1 <= 13.8477 )
								if( VIP_VIM <= -0.778633 )
									ret := -0.065217
								if( VIP_VIM > -0.778633 )
									ret := 0.590000
							if( rsi1 > 13.8477 )
								if( VIP <= 1.0279 )
									ret := -0.029381
								if( VIP > 1.0279 )
									ret := 0.525000
						if( d_k > 11.1059 )
							if( VIM <= 1.18745 )
								if( d <= 21.6239 )
									ret := 0.209125
								if( d > 21.6239 )
									ret := -0.164948
							if( VIM > 1.18745 )
								if( d <= 13.0603 )
									ret := 0.793103 // buy
								if( d > 13.0603 )
									ret := 0.384956
					if( smoothK_k > 0.176014 )
						if( k <= 74.4511 )
							if( d_k <= 17.2607 )
								if( k <= 4.15049 )
									ret := -0.182336
								if( k > 4.15049 )
									ret := -0.040653
							if( d_k > 17.2607 )
								if( k <= 6.15301 )
									ret := -0.264706
								if( k > 6.15301 )
									ret := 0.095156
						if( k > 74.4511 )
							if( smoothK_k <= 86.21 )
								if( VIM <= 1.07418 )
									ret := 0.178702
								if( VIM > 1.07418 )
									ret := 0.031052
							if( smoothK_k > 86.21 )
								if( VIM <= 1.28848 )
									ret := -0.052158
								if( VIM > 1.28848 )
									ret := 0.395833
				if( VIP_VIM > 0.175444 )
					if( rsi1 <= 40.3433 )
						if( rsi1 <= 38.2406 )
							if( smoothD_d <= 34.7673 )
								ret := 0.500000
							if( smoothD_d > 34.7673 )
								ret := -0.200000
						if( rsi1 > 38.2406 )
							ret := -0.692308
					if( rsi1 > 40.3433 )
						if( smoothD_d <= 59.7771 )
							if( rsi1 <= 49.9805 )
								if( smoothK_k <= 11.6195 )
									ret := 0.056604
								if( smoothK_k > 11.6195 )
									ret := 0.664430
							if( rsi1 > 49.9805 )
								if( k <= 11.9815 )
									ret := 0.714286 // buy
								if( k > 11.9815 )
									ret := 0.019048
						if( smoothD_d > 59.7771 )
							if( smoothD_d <= 85.3875 )
								if( VIM <= 1.35701 )
									ret := -0.157895
								if( VIM > 1.35701 )
									ret := 0.888889 // buy
							if( smoothD_d > 85.3875 )
								if( VIM <= 0.937965 )
									ret := 0.826087 // buy
								if( VIM > 0.937965 )
									ret := 0.300000
			if( VIM > 1.41658 )
				if( smoothD_d <= 42.1174 )
					if( d_k <= -22.9888 )
						if( VIP <= 1.32638 )
							ret := -0.166667
						if( VIP > 1.32638 )
							if( k <= 61.4065 )
								if( smoothK_k <= 53.6775 )
									ret := -0.968750 // sell
								if( smoothK_k > 53.6775 )
									ret := -0.777778 // sell
							if( k > 61.4065 )
								if( VIP <= 1.76024 )
									ret := -1.000000 // sell
								if( VIP > 1.76024 )
									ret := -0.100000
					if( d_k > -22.9888 )
						if( smoothD_d <= 2.45981 )
							if( rsi1 <= 35.0401 )
								if( d <= 0.626119 )
									ret := 0.458333
								if( d > 0.626119 )
									ret := -0.016706
							if( rsi1 > 35.0401 )
								if( rsi1 <= 49.6666 )
									ret := -0.375439
								if( rsi1 > 49.6666 )
									ret := 0.129032
						if( smoothD_d > 2.45981 )
							if( VIP <= 10.5658 )
								if( rsi1 <= 27.9549 )
									ret := 0.334740
								if( rsi1 > 27.9549 )
									ret := 0.078168
							if( VIP > 10.5658 )
								if( VIM <= 19.5317 )
									ret := 0.485232
								if( VIM > 19.5317 )
									ret := 0.130233
				if( smoothD_d > 42.1174 )
					if( rsi1 <= 36.9337 )
						if( d_k <= 12.1315 )
							if( VIP <= 1.49172 )
								if( VIM <= 1.50261 )
									ret := 0.738095 // buy
								if( VIM > 1.50261 )
									ret := 0.242857
							if( VIP > 1.49172 )
								if( VIP <= 3.03333 )
									ret := 0.804348 // buy
								if( VIP > 3.03333 )
									ret := 0.465116
						if( d_k > 12.1315 )
							if( smoothD_d <= 82.1629 )
								if( smoothD_d <= 62.2039 )
									ret := 0.031008
								if( smoothD_d > 62.2039 )
									ret := 0.710843 // buy
							if( smoothD_d > 82.1629 )
								ret := -0.666667
					if( rsi1 > 36.9337 )
						if( VIM <= 4.15594 )
							if( k <= 88.7623 )
								if( VIM <= 1.4408 )
									ret := -0.266667
								if( VIM > 1.4408 )
									ret := 0.125604
							if( k > 88.7623 )
								if( VIP <= 3.17221 )
									ret := 0.504237
								if( VIP > 3.17221 )
									ret := -0.351351
						if( VIM > 4.15594 )
							if( rsi1 <= 48.4897 )
								if( d_k <= 24.3667 )
									ret := 0.518456
								if( d_k > 24.3667 )
									ret := -0.419355
							if( rsi1 > 48.4897 )
								if( d <= 84.6284 )
									ret := 0.162963
								if( d > 84.6284 )
									ret := -0.318841
	if( rsi1 > 51.1698 )
		if( VIM <= 1.00196 )
			if( VIM <= 0.750945 )
				if( d_k <= -6.89777 )
					if( smoothD_d <= 88.6673 )
						if( d_k <= -32.3022 )
							if( rsi1 <= 75.7654 )
								ret := 1.000000 // buy
							if( rsi1 > 75.7654 )
								ret := 0.785714 // buy
						if( d_k > -32.3022 )
							if( smoothK_k <= 95.8625 )
								if( d <= 86.5563 )
									ret := 0.286908
								if( d > 86.5563 )
									ret := 0.666667
							if( smoothK_k > 95.8625 )
								if( VIM <= 0.584183 )
									ret := 0.666667
								if( VIM > 0.584183 )
									ret := -0.207692
					if( smoothD_d > 88.6673 )
						if( d_k <= -7.17212 )
							ret := 0.222222
						if( d_k > -7.17212 )
							ret := 1.000000 // buy
				if( d_k > -6.89777 )
					if( VIP <= 1.4095 )
						if( rsi1 <= 73.8061 )
							if( VIP <= 1.23021 )
								if( d_k <= 7.19078 )
									ret := -0.016129
								if( d_k > 7.19078 )
									ret := -0.467391
							if( VIP > 1.23021 )
								if( k <= 70.3477 )
									ret := -0.005650
								if( k > 70.3477 )
									ret := 0.269675
						if( rsi1 > 73.8061 )
							if( smoothK_k <= 63.8613 )
								if( VIP <= 1.30107 )
									ret := 0.401639
								if( VIP > 1.30107 )
									ret := 0.032864
							if( smoothK_k > 63.8613 )
								if( smoothK_k <= 65.8805 )
									ret := -0.787879 // sell
								if( smoothK_k > 65.8805 )
									ret := -0.103864
					if( VIP > 1.4095 )
						if( k <= 77.03 )
							if( rsi1 <= 81.9862 )
								if( smoothD_d <= 78.6594 )
									ret := -0.333333
								if( smoothD_d > 78.6594 )
									ret := -0.950000 // sell
							if( rsi1 > 81.9862 )
								if( rsi1 <= 85.0777 )
									ret := 0.363636
								if( rsi1 > 85.0777 )
									ret := -0.069767
						if( k > 77.03 )
							if( d_k <= 2.86744 )
								if( k <= 93.9841 )
									ret := 0.373333
								if( k > 93.9841 )
									ret := 0.099220
							if( d_k > 2.86744 )
								if( VIP_VIM <= 0.815612 )
									ret := 0.092593
								if( VIP_VIM > 0.815612 )
									ret := 0.506098
			if( VIM > 0.750945 )
				if( smoothK_k <= 22.1016 )
					if( d <= 15.6995 )
						if( smoothK_k <= 10.6311 )
							if( smoothD_d <= -0.267076 )
								if( VIP_VIM <= 0.350581 )
									ret := 0.233083
								if( VIP_VIM > 0.350581 )
									ret := -0.421053
							if( smoothD_d > -0.267076 )
								if( smoothD_d <= 8.22722 )
									ret := -0.319481
								if( smoothD_d > 8.22722 )
									ret := -0.057613
						if( smoothK_k > 10.6311 )
							if( d <= 11.6759 )
								if( rsi1 <= 52.9062 )
									ret := -0.333333
								if( rsi1 > 52.9062 )
									ret := 0.533708
							if( d > 11.6759 )
								if( VIM <= 0.929954 )
									ret := 0.368932
								if( VIM > 0.929954 )
									ret := -0.278481
					if( d > 15.6995 )
						if( k <= 24.7798 )
							if( VIP_VIM <= 0.628414 )
								if( VIM <= 0.940823 )
									ret := -0.287892
								if( VIM > 0.940823 )
									ret := -0.108696
							if( VIP_VIM > 0.628414 )
								ret := 0.833333 // buy
						if( k > 24.7798 )
							if( smoothD_d <= 28.9767 )
								if( k <= 25.0054 )
									ret := -0.607143
								if( k > 25.0054 )
									ret := -1.000000 // sell
							if( smoothD_d > 28.9767 )
								ret := -0.230769
				if( smoothK_k > 22.1016 )
					if( VIP <= 1.59053 )
						if( d <= 26.3001 )
							if( smoothK_k <= 32.0757 )
								if( VIP <= 1.17532 )
									ret := 0.452174
								if( VIP > 1.17532 )
									ret := -0.086420
							if( smoothK_k > 32.0757 )
								if( rsi1 <= 62.788 )
									ret := -0.309211
								if( rsi1 > 62.788 )
									ret := 0.363636
						if( d > 26.3001 )
							if( k <= 49.0998 )
								if( smoothD_d <= 57.1265 )
									ret := -0.052736
								if( smoothD_d > 57.1265 )
									ret := -0.340299
							if( k > 49.0998 )
								if( smoothD_d <= 96.6692 )
									ret := 0.014636
								if( smoothD_d > 96.6692 )
									ret := 0.242424
					if( VIP > 1.59053 )
						if( rsi1 <= 76.631 )
							if( k <= 71.172 )
								if( smoothD_d <= 43.5705 )
									ret := -0.500000
								if( smoothD_d > 43.5705 )
									ret := 0.083333
							if( k > 71.172 )
								if( k <= 88.2178 )
									ret := -0.813559 // sell
								if( k > 88.2178 )
									ret := -0.345455
						if( rsi1 > 76.631 )
							if( d <= 72.6617 )
								ret := -0.714286 // sell
							if( d > 72.6617 )
								if( VIP <= 1.77803 )
									ret := 0.583333
								if( VIP > 1.77803 )
									ret := -0.058824
		if( VIM > 1.00196 )
			if( smoothD_d <= 87.6724 )
				if( d <= 3.70988 )
					if( smoothK_k <= -1.32113 )
						if( VIM <= 1.3102 )
							ret := 0.909091 // buy
						if( VIM > 1.3102 )
							ret := 0.636364
					if( smoothK_k > -1.32113 )
						if( VIP <= 1.41268 )
							ret := -0.428571
						if( VIP > 1.41268 )
							if( VIP <= 2.00516 )
								ret := 1.000000 // buy
							if( VIP > 2.00516 )
								ret := -0.076923
				if( d > 3.70988 )
					if( VIP <= 8.28184 )
						if( smoothD_d <= 70.0745 )
							if( k <= 30.9849 )
								if( VIP <= 1.14843 )
									ret := -0.303644
								if( VIP > 1.14843 )
									ret := -0.004801
							if( k > 30.9849 )
								if( smoothD_d <= 50.431 )
									ret := -0.285276
								if( smoothD_d > 50.431 )
									ret := -0.178082
						if( smoothD_d > 70.0745 )
							if( smoothD_d <= 80.1906 )
								if( VIP <= 1.05006 )
									ret := 0.396694
								if( VIP > 1.05006 )
									ret := -0.056258
							if( smoothD_d > 80.1906 )
								if( d_k <= 15.359 )
									ret := -0.192386
								if( d_k > 15.359 )
									ret := 1.000000 // buy
					if( VIP > 8.28184 )
						if( d <= 47.6444 )
							if( VIP <= 36.909 )
								if( d_k <= 2.67315 )
									ret := -0.649718
								if( d_k > 2.67315 )
									ret := -0.129630
							if( VIP > 36.909 )
								if( smoothK_k <= 48.0127 )
									ret := 0.157895
								if( smoothK_k > 48.0127 )
									ret := -0.857143 // sell
						if( d > 47.6444 )
							if( k <= 63.3822 )
								if( smoothD_d <= 68.9289 )
									ret := 0.138211
								if( smoothD_d > 68.9289 )
									ret := -0.555556
							if( k > 63.3822 )
								if( VIM <= 11.0804 )
									ret := -0.605691
								if( VIM > 11.0804 )
									ret := -0.158730
			if( smoothD_d > 87.6724 )
				if( d_k <= -2.40709 )
					if( VIP_VIM <= 0.199955 )
						if( k <= 99.1913 )
							if( smoothD_d <= 91.4625 )
								if( VIP_VIM <= 0.091049 )
									ret := -0.797872 // sell
								if( VIP_VIM > 0.091049 )
									ret := -0.416667
							if( smoothD_d > 91.4625 )
								if( VIM <= 2.79697 )
									ret := -0.636364
								if( VIM > 2.79697 )
									ret := 0.250000
						if( k > 99.1913 )
							if( rsi1 <= 54.2002 )
								if( rsi1 <= 53.7238 )
									ret := -0.350000
								if( rsi1 > 53.7238 )
									ret := 0.923077 // buy
							if( rsi1 > 54.2002 )
								if( VIP_VIM <= -0.296271 )
									ret := -0.800000 // sell
								if( VIP_VIM > -0.296271 )
									ret := -0.215686
					if( VIP_VIM > 0.199955 )
						if( smoothD_d <= 93.3067 )
							if( VIP <= 1.9805 )
								if( VIM <= 1.31303 )
									ret := 0.945946 // buy
								if( VIM > 1.31303 )
									ret := 0.307692
							if( VIP > 1.9805 )
								if( smoothD_d <= 89.1279 )
									ret := -0.560000
								if( smoothD_d > 89.1279 )
									ret := -0.012195
						if( smoothD_d > 93.3067 )
							if( k <= 99.9802 )
								ret := -0.153846
							if( k > 99.9802 )
								if( smoothD_d <= 93.787 )
									ret := -0.666667
								if( smoothD_d > 93.787 )
									ret := -0.952381 // sell
				if( d_k > -2.40709 )
					if( VIP_VIM <= 1.25401 )
						if( d <= 97.0478 )
							if( smoothK_k <= 94.9901 )
								if( VIP <= 4.11646 )
									ret := 0.248175
								if( VIP > 4.11646 )
									ret := -0.065217
							if( smoothK_k > 94.9901 )
								if( VIP_VIM <= 0.028931 )
									ret := 0.600000
								if( VIP_VIM > 0.028931 )
									ret := 1.000000 // buy
						if( d > 97.0478 )
							if( k <= 97.6717 )
								if( smoothD_d <= 95.929 )
									ret := -0.339869
								if( smoothD_d > 95.929 )
									ret := -0.888889 // sell
							if( k > 97.6717 )
								if( VIM <= 6.41758 )
									ret := -0.066667
								if( VIM > 6.41758 )
									ret := 0.766667 // buy
					if( VIP_VIM > 1.25401 )
						if( VIP_VIM <= 1.68251 )
							if( smoothD_d <= 95.1239 )
								if( smoothK_k <= 86.8166 )
									ret := 0.800000 // buy
								if( smoothK_k > 86.8166 )
									ret := 0.125000
							if( smoothD_d > 95.1239 )
								if( smoothK_k <= 95.9403 )
									ret := 1.000000 // buy
								if( smoothK_k > 95.9403 )
									ret := 0.923077 // buy
						if( VIP_VIM > 1.68251 )
							if( rsi1 <= 79.9603 )
								ret := -0.187500
							if( rsi1 > 79.9603 )
								ret := 0.500000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_U_1Min_6b578748(rsi1, d, k, smoothD_d, d_k, smoothK_k, VIP, VIP_VIM, VIM)

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


