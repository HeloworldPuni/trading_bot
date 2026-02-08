//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: RUN_15Min_2ST0_7976ca3f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RUN_15Min_2ST0_7976ca3f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RUN_15Min_7976ca3f(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( ema1 <= 14.4765 )
		if( d <= 99.6469 )
			if( ema1 <= 5.0463 )
				if( ema2 <= 4.716 )
					ret := 0.937500 // buy
				if( ema2 > 4.716 )
					if( ema12 <= 0.032302 )
						if( k <= 17.4378 )
							if( smoothD_d <= -2.30629 )
								ret := 0.800000 // buy
							if( smoothD_d > -2.30629 )
								if( ema13 <= 0.007297 )
									ret := -0.104478
								if( ema13 > 0.007297 )
									ret := 0.562500
						if( k > 17.4378 )
							if( rsi1 <= 45.7206 )
								if( smoothD_d <= 28.0408 )
									ret := 0.237288
								if( smoothD_d > 28.0408 )
									ret := 0.604762
							if( rsi1 > 45.7206 )
								if( k <= 40.2659 )
									ret := -0.196078
								if( k > 40.2659 )
									ret := 0.235602
					if( ema12 > 0.032302 )
						if( smoothD_d <= 89.8798 )
							if( k <= 78.1759 )
								ret := -0.538462
							if( k > 78.1759 )
								if( ema3 <= 4.86031 )
									ret := -0.888889 // sell
								if( ema3 > 4.86031 )
									ret := -1.000000 // sell
						if( smoothD_d > 89.8798 )
							ret := 0.076923
			if( ema1 > 5.0463 )
				if( smoothD_d <= 87.6704 )
					if( d <= 0.810584 )
						if( d <= 0.788477 )
							if( ema12 <= -0.063575 )
								if( k <= 0.021109 )
									ret := -0.273292
								if( k > 0.021109 )
									ret := 0.281106
							if( ema12 > -0.063575 )
								if( ema13 <= 0.258748 )
									ret := 0.430712
								if( ema13 > 0.258748 )
									ret := -0.846154 // sell
						if( d > 0.788477 )
							if( ema12 <= -0.093894 )
								ret := 0.777778 // buy
							if( ema12 > -0.093894 )
								ret := 0.928571 // buy
					if( d > 0.810584 )
						if( ema13 <= -0.421685 )
							if( rsi1 <= 5.42431 )
								if( smoothK_k <= -1.99152 )
									ret := -0.846154 // sell
								if( smoothK_k > -1.99152 )
									ret := -1.000000 // sell
							if( rsi1 > 5.42431 )
								if( k <= 27.9375 )
									ret := 0.486804
								if( k > 27.9375 )
									ret := 0.120690
						if( ema13 > -0.421685 )
							if( ema12 <= -0.134072 )
								if( d <= 19.9 )
									ret := -0.214286
								if( d > 19.9 )
									ret := 0.147583
							if( ema12 > -0.134072 )
								if( ema12 <= 0.333847 )
									ret := 0.029948
								if( ema12 > 0.333847 )
									ret := -0.750000 // sell
				if( smoothD_d > 87.6704 )
					if( tema <= 10.752 )
						if( d <= 92.8944 )
							if( ema3 <= 6.34427 )
								if( d_k <= -7.7676 )
									ret := 0.300000
								if( d_k > -7.7676 )
									ret := -0.459330
							if( ema3 > 6.34427 )
								if( d_k <= 1.66174 )
									ret := 0.250000
								if( d_k > 1.66174 )
									ret := -0.316547
						if( d > 92.8944 )
							if( tema <= 6.01147 )
								if( ema3 <= 5.08385 )
									ret := 0.761905 // buy
								if( ema3 > 5.08385 )
									ret := -0.104308
							if( tema > 6.01147 )
								if( smoothD_d <= 95.9557 )
									ret := 0.287762
								if( smoothD_d > 95.9557 )
									ret := -0.089286
					if( tema > 10.752 )
						if( ema12 <= -0.075816 )
							if( k <= 87.1211 )
								ret := -0.416667
							if( k > 87.1211 )
								if( k <= 96.0045 )
									ret := -0.978723 // sell
								if( k > 96.0045 )
									ret := -0.729167 // sell
						if( ema12 > -0.075816 )
							if( rsi1 <= 63.7354 )
								if( ema13 <= 0.210921 )
									ret := 0.131793
								if( ema13 > 0.210921 )
									ret := -0.823529 // sell
							if( rsi1 > 63.7354 )
								if( ema3 <= 10.6335 )
									ret := -0.615942
								if( ema3 > 10.6335 )
									ret := -0.194978
		if( d > 99.6469 )
			if( ema3 <= 6.36826 )
				if( tema <= 5.14274 )
					ret := -0.294118
				if( tema > 5.14274 )
					if( ema3 <= 5.2166 )
						if( tema <= 5.29896 )
							ret := 0.600000
						if( tema > 5.29896 )
							ret := 1.000000 // buy
					if( ema3 > 5.2166 )
						if( k <= 99.9297 )
							if( ema13 <= 0.09286 )
								if( d <= 99.7566 )
									ret := 0.333333
								if( d > 99.7566 )
									ret := 0.928571 // buy
							if( ema13 > 0.09286 )
								ret := -0.636364
						if( k > 99.9297 )
							if( ema13 <= 0.019138 )
								ret := 0.157895
							if( ema13 > 0.019138 )
								if( ema12 <= 0.025628 )
									ret := 0.538462
								if( ema12 > 0.025628 )
									ret := 0.895522 // buy
			if( ema3 > 6.36826 )
				if( d_k <= 0.164896 )
					if( smoothK_k <= 96.9347 )
						if( ema3 <= 10.7092 )
							ret := -0.071429
						if( ema3 > 10.7092 )
							if( ema12 <= 0.05544 )
								ret := 0.421053
							if( ema12 > 0.05544 )
								if( ema1 <= 12.1689 )
									ret := 0.913043 // buy
								if( ema1 > 12.1689 )
									ret := 0.708333 // buy
					if( smoothK_k > 96.9347 )
						if( rsi1 <= 69.1815 )
							if( rsi1 <= 64.0737 )
								if( ema3 <= 10.0788 )
									ret := 0.416667
								if( ema3 > 10.0788 )
									ret := -0.047619
							if( rsi1 > 64.0737 )
								if( d <= 99.9964 )
									ret := 0.444444
								if( d > 99.9964 )
									ret := 0.928571 // buy
						if( rsi1 > 69.1815 )
							if( ema12 <= 0.28519 )
								if( d_k <= -0.002919 )
									ret := -0.375000
								if( d_k > -0.002919 )
									ret := -0.051724
							if( ema12 > 0.28519 )
								ret := 0.777778 // buy
				if( d_k > 0.164896 )
					if( ema2 <= 8.16423 )
						ret := -0.818182 // sell
					if( ema2 > 8.16423 )
						if( ema13 <= 0.183082 )
							if( k <= 99.375 )
								ret := 0.466667
							if( k > 99.375 )
								ret := 0.100000
						if( ema13 > 0.183082 )
							ret := -0.555556
	if( ema1 > 14.4765 )
		if( smoothK_k <= 19.0624 )
			if( ema13 <= 1.1358 )
				if( tema <= 19.1104 )
					if( ema1 <= 15.0243 )
						if( ema12 <= 0.139595 )
							if( ema2 <= 14.5552 )
								if( smoothD_d <= 6.38451 )
									ret := 0.555556
								if( smoothD_d > 6.38451 )
									ret := 0.017544
							if( ema2 > 14.5552 )
								if( d <= 6.94101 )
									ret := 0.016077
								if( d > 6.94101 )
									ret := -0.269725
						if( ema12 > 0.139595 )
							ret := 0.888889 // buy
					if( ema1 > 15.0243 )
						if( ema13 <= -0.79275 )
							if( d_k <= -2.5754 )
								if( d <= 10.5951 )
									ret := 0.466667
								if( d > 10.5951 )
									ret := -1.000000 // sell
							if( d_k > -2.5754 )
								if( ema3 <= 18.5178 )
									ret := 1.000000 // buy
								if( ema3 > 18.5178 )
									ret := 0.564103
						if( ema13 > -0.79275 )
							if( smoothD_d <= 1.51735 )
								if( k <= 0.778046 )
									ret := 0.227528
								if( k > 0.778046 )
									ret := -0.142681
							if( smoothD_d > 1.51735 )
								if( rsi1 <= 30.6851 )
									ret := 0.257143
								if( rsi1 > 30.6851 )
									ret := 0.100583
				if( tema > 19.1104 )
					if( ema13 <= -1.96364 )
						if( d_k <= -1.15839 )
							if( d <= 8.2142 )
								if( d_k <= -1.80439 )
									ret := 0.416667
								if( d_k > -1.80439 )
									ret := -0.666667
							if( d > 8.2142 )
								ret := -0.882353 // sell
						if( d_k > -1.15839 )
							if( tema <= 78.2974 )
								if( ema3 <= 51.8358 )
									ret := 0.000000
								if( ema3 > 51.8358 )
									ret := 0.789474 // buy
							if( tema > 78.2974 )
								ret := -0.357143
					if( ema13 > -1.96364 )
						if( ema13 <= -0.351414 )
							if( smoothD_d <= 4.74081 )
								if( rsi1 <= 22.2659 )
									ret := 0.022117
								if( rsi1 > 22.2659 )
									ret := -0.227582
							if( smoothD_d > 4.74081 )
								if( k <= 1.78369 )
									ret := 0.465517
								if( k > 1.78369 )
									ret := 0.001456
						if( ema13 > -0.351414 )
							if( tema <= 28.5997 )
								if( ema12 <= 0.084954 )
									ret := -0.044402
								if( ema12 > 0.084954 )
									ret := -0.292735
							if( tema > 28.5997 )
								if( d_k <= 7.0686 )
									ret := 0.160108
								if( d_k > 7.0686 )
									ret := -0.010254
			if( ema13 > 1.1358 )
				if( d_k <= 18.9033 )
					if( ema3 <= 35.1446 )
						ret := 1.000000 // buy
					if( ema3 > 35.1446 )
						if( ema2 <= 76.898 )
							if( ema13 <= 1.35711 )
								ret := -0.545455
							if( ema13 > 1.35711 )
								ret := 0.210526
						if( ema2 > 76.898 )
							if( tema <= 81.2433 )
								ret := 1.000000 // buy
							if( tema > 81.2433 )
								ret := 0.818182 // buy
				if( d_k > 18.9033 )
					ret := -0.285714
		if( smoothK_k > 19.0624 )
			if( ema3 <= 38.9017 )
				if( ema13 <= 0.74049 )
					if( ema2 <= 31.7013 )
						if( d <= 61.2058 )
							if( ema1 <= 24.7554 )
								if( tema <= 23.8566 )
									ret := -0.065115
								if( tema > 23.8566 )
									ret := 0.174419
							if( ema1 > 24.7554 )
								if( ema3 <= 29.4167 )
									ret := -0.250265
								if( ema3 > 29.4167 )
									ret := -0.018750
						if( d > 61.2058 )
							if( ema13 <= -0.074349 )
								if( ema12 <= -0.243331 )
									ret := 0.582822
								if( ema12 > -0.243331 )
									ret := 0.076518
							if( ema13 > -0.074349 )
								if( d_k <= 16.8181 )
									ret := -0.053352
								if( d_k > 16.8181 )
									ret := 0.184466
					if( ema2 > 31.7013 )
						if( ema12 <= 0.126456 )
							if( k <= 25.7812 )
								if( d <= 21.8034 )
									ret := -0.623529
								if( d > 21.8034 )
									ret := -0.330357
							if( k > 25.7812 )
								if( d_k <= 17.3181 )
									ret := -0.130153
								if( d_k > 17.3181 )
									ret := 0.504065
						if( ema12 > 0.126456 )
							if( k <= 99.3051 )
								if( ema12 <= 0.205228 )
									ret := -0.347932
								if( ema12 > 0.205228 )
									ret := -0.561062
							if( k > 99.3051 )
								if( tema <= 33.9267 )
									ret := -0.485714
								if( tema > 33.9267 )
									ret := 0.280000
				if( ema13 > 0.74049 )
					if( ema1 <= 29.1076 )
						if( ema1 <= 28.349 )
							if( d <= 36.8076 )
								if( ema12 <= 0.577705 )
									ret := 0.294118
								if( ema12 > 0.577705 )
									ret := -0.809524 // sell
							if( d > 36.8076 )
								if( rsi1 <= 93.3583 )
									ret := 0.382436
								if( rsi1 > 93.3583 )
									ret := -0.404762
						if( ema1 > 28.349 )
							if( d_k <= -0.144117 )
								ret := 0.750000 // buy
							if( d_k > -0.144117 )
								ret := 1.000000 // buy
					if( ema1 > 29.1076 )
						if( d_k <= 5.68752 )
							if( smoothK_k <= 88.3883 )
								if( k <= 60.7776 )
									ret := 0.909091 // buy
								if( k > 60.7776 )
									ret := -0.378947
							if( smoothK_k > 88.3883 )
								if( d_k <= 0.456274 )
									ret := 0.145161
								if( d_k > 0.456274 )
									ret := 0.805970 // buy
						if( d_k > 5.68752 )
							if( d_k <= 13.1767 )
								if( smoothK_k <= 60.5909 )
									ret := -0.500000
								if( smoothK_k > 60.5909 )
									ret := -0.838235 // sell
							if( d_k > 13.1767 )
								if( d <= 73.9006 )
									ret := -0.409091
								if( d > 73.9006 )
									ret := 0.466667
			if( ema3 > 38.9017 )
				if( d_k <= 16.9677 )
					if( tema <= 51.9139 )
						if( d <= 77.7829 )
							if( ema13 <= -0.97835 )
								if( k <= 49.8919 )
									ret := 0.507538
								if( k > 49.8919 )
									ret := -0.137931
							if( ema13 > -0.97835 )
								if( smoothK_k <= 24.1494 )
									ret := 0.219672
								if( smoothK_k > 24.1494 )
									ret := -0.046538
						if( d > 77.7829 )
							if( ema12 <= -0.049513 )
								if( ema3 <= 47.5364 )
									ret := 0.172000
								if( ema3 > 47.5364 )
									ret := 0.652381
							if( ema12 > -0.049513 )
								if( ema1 <= 44.3554 )
									ret := 0.286479
								if( ema1 > 44.3554 )
									ret := -0.005055
					if( tema > 51.9139 )
						if( rsi1 <= 44.0934 )
							if( tema <= 90.998 )
								if( ema12 <= -0.603179 )
									ret := -0.003390
								if( ema12 > -0.603179 )
									ret := -0.267136
							if( tema > 90.998 )
								ret := 0.842105 // buy
						if( rsi1 > 44.0934 )
							if( ema13 <= 0.897999 )
								if( smoothD_d <= 63.4 )
									ret := 0.101819
								if( smoothD_d > 63.4 )
									ret := -0.087653
							if( ema13 > 0.897999 )
								if( smoothD_d <= 95.1703 )
									ret := -0.161062
								if( smoothD_d > 95.1703 )
									ret := -0.584416
				if( d_k > 16.9677 )
					if( ema1 <= 56.8816 )
						if( smoothD_d <= 63.4124 )
							if( ema13 <= -0.347713 )
								if( k <= 33.174 )
									ret := 0.020408
								if( k > 33.174 )
									ret := -0.500000
							if( ema13 > -0.347713 )
								if( ema12 <= 0.015226 )
									ret := 0.440994
								if( ema12 > 0.015226 )
									ret := 0.188235
						if( smoothD_d > 63.4124 )
							if( ema2 <= 42.7792 )
								if( ema3 <= 41.011 )
									ret := 0.294118
								if( ema3 > 41.011 )
									ret := -0.250000
							if( ema2 > 42.7792 )
								if( d <= 78.1358 )
									ret := 0.414414
								if( d > 78.1358 )
									ret := 0.712329 // buy
					if( ema1 > 56.8816 )
						if( smoothD_d <= 77.6884 )
							if( ema12 <= -0.156527 )
								if( ema13 <= -0.473926 )
									ret := -0.030303
								if( ema13 > -0.473926 )
									ret := 0.653846
							if( ema12 > -0.156527 )
								if( rsi1 <= 73.2929 )
									ret := -0.128342
								if( rsi1 > 73.2929 )
									ret := 0.916667 // buy
						if( smoothD_d > 77.6884 )
							if( ema2 <= 61.6848 )
								ret := -0.750000 // sell
							if( ema2 > 61.6848 )
								ret := -0.300000
	
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
float op_operation = decision_tree_0_RUN_15Min_7976ca3f(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)

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


