//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: LYFT_1Min_2SV0_93e22e16 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_LYFT_1Min_2SV0_93e22e16", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_LYFT_1Min_93e22e16(d, d_k, smoothK_k, k, rsi1, smoothD_d, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( smoothK_k <= 8.84789 )
		if( rsi1 <= 54.8634 )
			if( d <= 32.5576 )
				if( VIM <= 2.61613 )
					if( VIP <= 0.950595 )
						if( VIM <= 1.48509 )
							if( smoothK_k <= 8.32699 )
								if( d_k <= -0.010653 )
									ret := -0.038314
								if( d_k > -0.010653 )
									ret := 0.068772
							if( smoothK_k > 8.32699 )
								if( VIM <= 1.17876 )
									ret := 0.555556
								if( VIM > 1.17876 )
									ret := 0.052288
						if( VIM > 1.48509 )
							if( smoothK_k <= 7.95732 )
								if( d_k <= -0.538527 )
									ret := 0.660000
								if( d_k > -0.538527 )
									ret := 0.129794
							if( smoothK_k > 7.95732 )
								ret := -0.800000 // sell
					if( VIP > 0.950595 )
						if( smoothK_k <= -2.69578 )
							if( VIM <= 0.938156 )
								if( VIM <= 0.915548 )
									ret := 0.333333
								if( VIM > 0.915548 )
									ret := -0.538462
							if( VIM > 0.938156 )
								if( k <= 0.00526 )
									ret := 0.272388
								if( k > 0.00526 )
									ret := 0.578947
						if( smoothK_k > -2.69578 )
							if( rsi1 <= 38.0524 )
								if( d_k <= 3.28439 )
									ret := 0.539568
								if( d_k > 3.28439 )
									ret := 0.036082
							if( rsi1 > 38.0524 )
								if( rsi1 <= 40.9741 )
									ret := -0.192893
								if( rsi1 > 40.9741 )
									ret := 0.144330
				if( VIM > 2.61613 )
					if( smoothK_k <= 5.99986 )
						if( rsi1 <= 39.9756 )
							if( rsi1 <= 8.29191 )
								ret := -0.266667
							if( rsi1 > 8.29191 )
								if( rsi1 <= 33.4202 )
									ret := 0.465116
								if( rsi1 > 33.4202 )
									ret := 0.710938 // buy
						if( rsi1 > 39.9756 )
							if( smoothD_d <= -0.509312 )
								if( d_k <= -0.776328 )
									ret := -0.444444
								if( d_k > -0.776328 )
									ret := -0.733333 // sell
							if( smoothD_d > -0.509312 )
								if( smoothD_d <= 8.94652 )
									ret := 0.416667
								if( smoothD_d > 8.94652 )
									ret := -0.076923
					if( smoothK_k > 5.99986 )
						if( VIM <= 19.9216 )
							if( smoothK_k <= 6.12442 )
								ret := 1.000000 // buy
							if( smoothK_k > 6.12442 )
								if( k <= 10.1383 )
									ret := 0.548780
								if( k > 10.1383 )
									ret := 0.750000 // buy
						if( VIM > 19.9216 )
							ret := 0.052632
			if( d > 32.5576 )
				if( k <= 10.0778 )
					if( smoothD_d <= 33.4303 )
						if( rsi1 <= 40.523 )
							ret := 0.363636
						if( rsi1 > 40.523 )
							if( d <= 35.1117 )
								if( d_k <= 26.6084 )
									ret := -0.666667
								if( d_k > 26.6084 )
									ret := -0.964286 // sell
							if( d > 35.1117 )
								ret := -0.375000
					if( smoothD_d > 33.4303 )
						if( smoothK_k <= 3.97116 )
							ret := -0.666667
						if( smoothK_k > 3.97116 )
							if( rsi1 <= 38.8705 )
								ret := -1.000000 // sell
							if( rsi1 > 38.8705 )
								ret := -0.900000 // sell
				if( k > 10.0778 )
					if( d_k <= 26.5309 )
						if( VIP_VIM <= -0.086134 )
							ret := 0.285714
						if( VIP_VIM > -0.086134 )
							ret := 0.650000
					if( d_k > 26.5309 )
						if( d <= 41.9495 )
							ret := 0.000000
						if( d > 41.9495 )
							ret := -0.100000
		if( rsi1 > 54.8634 )
			if( k <= 4.49192 )
				if( VIP <= 1.03387 )
					ret := 0.117647
				if( VIP > 1.03387 )
					if( k <= 2.36145 )
						if( d_k <= 1.7266 )
							if( smoothK_k <= -1.21207 )
								if( d_k <= 0.328315 )
									ret := -0.823529 // sell
								if( d_k > 0.328315 )
									ret := -0.333333
							if( smoothK_k > -1.21207 )
								ret := -1.000000 // sell
						if( d_k > 1.7266 )
							if( rsi1 <= 59.5629 )
								if( smoothK_k <= -2.781 )
									ret := 0.083333
								if( smoothK_k > -2.781 )
									ret := -0.440000
							if( rsi1 > 59.5629 )
								if( VIP <= 1.27286 )
									ret := -0.787234 // sell
								if( VIP > 1.27286 )
									ret := 0.300000
					if( k > 2.36145 )
						if( k <= 4.40843 )
							if( smoothD_d <= -1.24693 )
								ret := -0.928571 // sell
							if( smoothD_d > -1.24693 )
								if( VIM <= 0.87189 )
									ret := -0.513514
								if( VIM > 0.87189 )
									ret := 0.121212
						if( k > 4.40843 )
							ret := -1.000000 // sell
			if( k > 4.49192 )
				if( smoothK_k <= 7.68743 )
					if( d_k <= 20.0023 )
						if( k <= 9.45511 )
							if( VIP_VIM <= 0.17601 )
								if( VIM <= 0.94206 )
									ret := -0.666667
								if( VIM > 0.94206 )
									ret := -0.107527
							if( VIP_VIM > 0.17601 )
								if( VIP <= 1.23654 )
									ret := 0.238806
								if( VIP > 1.23654 )
									ret := -0.558140
						if( k > 9.45511 )
							if( d_k <= -2.21809 )
								if( d_k <= -3.87922 )
									ret := 0.300000
								if( d_k > -3.87922 )
									ret := 1.000000 // buy
							if( d_k > -2.21809 )
								if( VIM <= 1.1013 )
									ret := 0.426829
								if( VIM > 1.1013 )
									ret := -0.600000
					if( d_k > 20.0023 )
						if( smoothD_d <= 27.6192 )
							if( k <= 7.63176 )
								if( rsi1 <= 61.7938 )
									ret := -0.666667
								if( rsi1 > 61.7938 )
									ret := -1.000000 // sell
							if( k > 7.63176 )
								ret := -0.500000
						if( smoothD_d > 27.6192 )
							ret := 0.700000 // buy
				if( smoothK_k > 7.68743 )
					if( VIP <= 1.08166 )
						if( VIP_VIM <= 0.126395 )
							if( k <= 11.4089 )
								ret := -1.000000 // sell
							if( k > 11.4089 )
								ret := -0.700000 // sell
						if( VIP_VIM > 0.126395 )
							ret := -0.588235
					if( VIP > 1.08166 )
						if( VIP <= 1.22921 )
							if( d_k <= 7.91595 )
								if( VIP_VIM <= 0.28112 )
									ret := -0.300000
								if( VIP_VIM > 0.28112 )
									ret := 0.500000
							if( d_k > 7.91595 )
								ret := 0.300000
						if( VIP > 1.22921 )
							if( d_k <= 9.72605 )
								ret := -0.350000
							if( d_k > 9.72605 )
								ret := -0.800000 // sell
	if( smoothK_k > 8.84789 )
		if( smoothK_k <= 90.2353 )
			if( rsi1 <= 54.1333 )
				if( VIP <= 1.10651 )
					if( smoothK_k <= 48.1277 )
						if( rsi1 <= 14.0086 )
							if( d <= 12.0525 )
								if( VIP <= 0.651579 )
									ret := 0.960000 // buy
								if( VIP > 0.651579 )
									ret := 0.666667
							if( d > 12.0525 )
								if( VIM <= 1.31168 )
									ret := -0.114286
								if( VIM > 1.31168 )
									ret := 0.622222
						if( rsi1 > 14.0086 )
							if( VIP <= 0.942914 )
								if( rsi1 <= 39.8492 )
									ret := -0.032500
								if( rsi1 > 39.8492 )
									ret := -0.130196
							if( VIP > 0.942914 )
								if( smoothD_d <= 5.72283 )
									ret := -0.295302
								if( smoothD_d > 5.72283 )
									ret := 0.023516
					if( smoothK_k > 48.1277 )
						if( smoothD_d <= 33.2865 )
							if( VIM <= 0.96844 )
								ret := -0.600000
							if( VIM > 0.96844 )
								if( smoothD_d <= 26.9981 )
									ret := -0.120690
								if( smoothD_d > 26.9981 )
									ret := 0.377510
						if( smoothD_d > 33.2865 )
							if( VIM <= 1.40289 )
								if( rsi1 <= 38.6962 )
									ret := 0.110861
								if( rsi1 > 38.6962 )
									ret := -0.014180
							if( VIM > 1.40289 )
								if( d <= 52.5158 )
									ret := -0.023810
								if( d > 52.5158 )
									ret := 0.470588
				if( VIP > 1.10651 )
					if( rsi1 <= 43.3143 )
						if( k <= 15.9925 )
							if( VIP <= 11.7878 )
								if( rsi1 <= 42.0919 )
									ret := -0.214286
								if( rsi1 > 42.0919 )
									ret := 0.333333
							if( VIP > 11.7878 )
								ret := 0.916667 // buy
						if( k > 15.9925 )
							if( d_k <= 15.3114 )
								if( VIM <= 11.0537 )
									ret := 0.257616
								if( VIM > 11.0537 )
									ret := 0.675325
							if( d_k > 15.3114 )
								if( k <= 30.9981 )
									ret := 0.329480
								if( k > 30.9981 )
									ret := 0.617450
					if( rsi1 > 43.3143 )
						if( smoothD_d <= 75.2004 )
							if( VIM <= 8.52962 )
								if( k <= 71.5385 )
									ret := 0.077442
								if( k > 71.5385 )
									ret := -0.155393
							if( VIM > 8.52962 )
								if( VIP <= 160.407 )
									ret := 0.301759
								if( VIP > 160.407 )
									ret := -0.293333
						if( smoothD_d > 75.2004 )
							if( VIP_VIM <= -1.25744 )
								if( smoothK_k <= 81.8531 )
									ret := -0.684211
								if( smoothK_k > 81.8531 )
									ret := -0.111111
							if( VIP_VIM > -1.25744 )
								if( smoothD_d <= 85.3498 )
									ret := 0.471449
								if( smoothD_d > 85.3498 )
									ret := 0.092357
			if( rsi1 > 54.1333 )
				if( VIP <= 1.39472 )
					if( VIM <= 1.06082 )
						if( smoothD_d <= 68.264 )
							if( VIP <= 1.1618 )
								if( k <= 17.8148 )
									ret := -0.210863
								if( k > 17.8148 )
									ret := 0.008853
							if( VIP > 1.1618 )
								if( smoothK_k <= 31.1937 )
									ret := -0.281984
								if( smoothK_k > 31.1937 )
									ret := -0.064041
						if( smoothD_d > 68.264 )
							if( d <= 75.8084 )
								if( k <= 75.0665 )
									ret := 0.087218
								if( k > 75.0665 )
									ret := 0.282051
							if( d > 75.8084 )
								if( smoothD_d <= 86.6112 )
									ret := -0.035277
								if( smoothD_d > 86.6112 )
									ret := 0.069503
					if( VIM > 1.06082 )
						if( d <= 88.6154 )
							if( smoothK_k <= 32.7088 )
								if( d_k <= -7.93075 )
									ret := 0.611111
								if( d_k > -7.93075 )
									ret := -0.173333
							if( smoothK_k > 32.7088 )
								if( smoothD_d <= 47.7027 )
									ret := -0.632911
								if( smoothD_d > 47.7027 )
									ret := -0.316667
						if( d > 88.6154 )
							if( smoothK_k <= 85.7194 )
								if( k <= 86.8831 )
									ret := 0.444444
								if( k > 86.8831 )
									ret := 1.000000 // buy
							if( smoothK_k > 85.7194 )
								ret := 0.133333
				if( VIP > 1.39472 )
					if( smoothD_d <= 58.198 )
						if( rsi1 <= 55.3562 )
							if( d <= 60.4178 )
								if( d_k <= -16.0874 )
									ret := 0.378378
								if( d_k > -16.0874 )
									ret := -0.098291
							if( d > 60.4178 )
								ret := -0.904762 // sell
						if( rsi1 > 55.3562 )
							if( d <= 57.5519 )
								if( VIP <= 2.85615 )
									ret := -0.442291
								if( VIP > 2.85615 )
									ret := -0.204126
							if( d > 57.5519 )
								if( smoothK_k <= 51.1481 )
									ret := -0.200000
								if( smoothK_k > 51.1481 )
									ret := -0.627907
					if( smoothD_d > 58.198 )
						if( smoothK_k <= 49.8961 )
							if( smoothD_d <= 63.7083 )
								if( k <= 51.1227 )
									ret := -0.132075
								if( k > 51.1227 )
									ret := 0.733333 // buy
							if( smoothD_d > 63.7083 )
								if( VIP <= 1.55646 )
									ret := 0.583333
								if( VIP > 1.55646 )
									ret := 0.944444 // buy
						if( smoothK_k > 49.8961 )
							if( VIP <= 19.5451 )
								if( d_k <= 11.45 )
									ret := -0.158562
								if( d_k > 11.45 )
									ret := 0.149533
							if( VIP > 19.5451 )
								if( VIP <= 1746.5 )
									ret := -0.625000
								if( VIP > 1746.5 )
									ret := 0.833333 // buy
		if( smoothK_k > 90.2353 )
			if( rsi1 <= 87.4363 )
				if( rsi1 <= 35.4136 )
					if( smoothK_k <= 93.2932 )
						if( k <= 94.0241 )
							ret := -0.235294
						if( k > 94.0241 )
							if( d_k <= -4.6218 )
								if( k <= 95.7546 )
									ret := -0.307692
								if( k > 95.7546 )
									ret := -0.818182 // sell
							if( d_k > -4.6218 )
								if( smoothK_k <= 91.9245 )
									ret := -0.850000 // sell
								if( smoothK_k > 91.9245 )
									ret := -1.000000 // sell
					if( smoothK_k > 93.2932 )
						if( VIM <= 1.21477 )
							ret := 0.533333
						if( VIM > 1.21477 )
							if( k <= 97.6913 )
								ret := -0.111111
							if( k > 97.6913 )
								ret := -0.777778 // sell
				if( rsi1 > 35.4136 )
					if( d_k <= 2.24533 )
						if( d <= 99.8968 )
							if( k <= 95.3881 )
								if( smoothD_d <= 87.8867 )
									ret := -0.097107
								if( smoothD_d > 87.8867 )
									ret := -0.249730
							if( k > 95.3881 )
								if( VIM <= 0.646316 )
									ret := -0.353774
								if( VIM > 0.646316 )
									ret := -0.032059
						if( d > 99.8968 )
							if( VIM <= 0.958958 )
								if( VIP <= 1.10768 )
									ret := 0.640625
								if( VIP > 1.10768 )
									ret := 0.168399
							if( VIM > 0.958958 )
								if( VIP_VIM <= 0.043882 )
									ret := -0.145161
								if( VIP_VIM > 0.043882 )
									ret := -0.563107
					if( d_k > 2.24533 )
						if( smoothD_d <= 93.3593 )
							if( k <= 93.5448 )
								ret := 0.187500
							if( k > 93.5448 )
								ret := -0.789474 // sell
						if( smoothD_d > 93.3593 )
							if( smoothK_k <= 90.5499 )
								if( VIP_VIM <= 0.491108 )
									ret := 0.156863
								if( VIP_VIM > 0.491108 )
									ret := -0.761905 // sell
							if( smoothK_k > 90.5499 )
								if( VIM <= 0.602067 )
									ret := -0.666667
								if( VIM > 0.602067 )
									ret := 0.241667
			if( rsi1 > 87.4363 )
				if( k <= 97.7171 )
					if( smoothD_d <= 87.086 )
						ret := -0.181818
					if( smoothD_d > 87.086 )
						if( d <= 97.7021 )
							if( d <= 95.3202 )
								if( smoothK_k <= 92.1614 )
									ret := -0.636364
								if( smoothK_k > 92.1614 )
									ret := -0.935484 // sell
							if( d > 95.3202 )
								if( rsi1 <= 89.0496 )
									ret := -0.652174
								if( rsi1 > 89.0496 )
									ret := -0.192308
						if( d > 97.7021 )
							if( smoothK_k <= 93.4368 )
								ret := -0.727273 // sell
							if( smoothK_k > 93.4368 )
								ret := -1.000000 // sell
				if( k > 97.7171 )
					if( VIP_VIM <= 0.699327 )
						if( VIP <= 1.33094 )
							if( VIM <= 0.734415 )
								if( rsi1 <= 95.4883 )
									ret := 0.500000
								if( rsi1 > 95.4883 )
									ret := 1.000000 // buy
							if( VIM > 0.734415 )
								ret := 0.066667
						if( VIP > 1.33094 )
							ret := -0.181818
					if( VIP_VIM > 0.699327 )
						if( VIP_VIM <= 1.10632 )
							if( k <= 98.1884 )
								ret := 0.100000
							if( k > 98.1884 )
								if( d <= 93.3822 )
									ret := 0.222222
								if( d > 93.3822 )
									ret := -0.542969
						if( VIP_VIM > 1.10632 )
							if( k <= 99.2811 )
								ret := -0.909091 // sell
							if( k > 99.2811 )
								if( rsi1 <= 91.9028 )
									ret := -0.166667
								if( rsi1 > 91.9028 )
									ret := 0.812500 // buy
	
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
float op_operation = decision_tree_0_LYFT_1Min_93e22e16(d, d_k, smoothK_k, k, rsi1, smoothD_d, VIP, VIP_VIM, VIM)

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


