//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Fibonacci_Bollinger
// ID_model: RUN_15Min_1FIB_785e7e2a Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RUN_15Min_1FIB_785e7e2a", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RUN_15Min_785e7e2a(basis, upper_2, upper_3, lower_2, lower_6, lower_1, basis_minus, lower_3, upper_6, lower_5, lower_4, upper_5, upper_4, basis_max, upper_1)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( upper_3 <= 12.1157 )
		if( upper_3 <= 11.9664 )
			if( upper_1 <= 11.7578 )
				if( basis <= 4.90005 )
					if( lower_4 <= 4.66373 )
						ret := -1.000000 // sell
					if( lower_4 > 4.66373 )
						ret := -0.888889 // sell
				if( basis > 4.90005 )
					if( lower_5 <= 9.89207 )
						if( lower_4 <= 9.96439 )
							if( basis <= 5.7257 )
								if( upper_5 <= 6.31284 )
									ret := 0.104999
								if( upper_5 > 6.31284 )
									ret := 0.813253 // buy
							if( basis > 5.7257 )
								if( lower_5 <= 8.58686 )
									ret := -0.019911
								if( lower_5 > 8.58686 )
									ret := 0.147714
						if( lower_4 > 9.96439 )
							if( lower_1 <= 10.508 )
								if( upper_2 <= 11.1093 )
									ret := -0.733333 // sell
								if( upper_2 > 11.1093 )
									ret := -1.000000 // sell
							if( lower_1 > 10.508 )
								ret := -0.111111
					if( lower_5 > 9.89207 )
						if( basis <= 10.5816 )
							if( upper_2 <= 10.7595 )
								ret := -0.900000 // sell
							if( upper_2 > 10.7595 )
								if( basis_minus <= 0.712838 )
									ret := 0.983051 // buy
								if( basis_minus > 0.712838 )
									ret := 0.485401
						if( basis > 10.5816 )
							if( lower_5 <= 9.93695 )
								if( basis_max <= -0.868999 )
									ret := -0.657143
								if( basis_max > -0.868999 )
									ret := -0.125000
							if( lower_5 > 9.93695 )
								if( upper_2 <= 11.8479 )
									ret := 0.239482
								if( upper_2 > 11.8479 )
									ret := -0.333333
			if( upper_1 > 11.7578 )
				ret := -1.000000 // sell
		if( upper_3 > 11.9664 )
			if( lower_5 <= 10.5867 )
				if( basis <= 11.4294 )
					if( upper_5 <= 12.6715 )
						if( upper_4 <= 12.2581 )
							if( lower_4 <= 9.91774 )
								ret := -0.071429
							if( lower_4 > 9.91774 )
								if( basis <= 11.3609 )
									ret := 1.000000 // buy
								if( basis > 11.3609 )
									ret := 0.000000
						if( upper_4 > 12.2581 )
							if( upper_2 <= 11.7668 )
								ret := 0.375000
							if( upper_2 > 11.7668 )
								if( lower_4 <= 9.91622 )
									ret := 1.000000 // buy
								if( lower_4 > 9.91622 )
									ret := 0.846154 // buy
					if( upper_5 > 12.6715 )
						if( basis <= 10.814 )
							if( basis <= 10.5702 )
								if( lower_6 <= 7.49717 )
									ret := 0.548387
								if( lower_6 > 7.49717 )
									ret := -0.848485 // sell
							if( basis > 10.5702 )
								if( basis <= 10.6014 )
									ret := 1.000000 // buy
								if( basis > 10.6014 )
									ret := 0.409091
						if( basis > 10.814 )
							if( upper_5 <= 12.7085 )
								ret := -0.105263
							if( upper_5 > 12.7085 )
								if( basis_minus <= 2.51768 )
									ret := -1.000000 // sell
								if( basis_minus > 2.51768 )
									ret := -0.800000 // sell
				if( basis > 11.4294 )
					if( upper_2 <= 11.8989 )
						if( lower_6 <= 10.3001 )
							if( basis <= 11.4566 )
								ret := -0.692308
							if( basis > 11.4566 )
								ret := -1.000000 // sell
						if( lower_6 > 10.3001 )
							ret := -0.416667
					if( upper_2 > 11.8989 )
						ret := -0.222222
			if( lower_5 > 10.5867 )
				if( upper_1 <= 11.7402 )
					if( basis_minus <= 0.989027 )
						if( lower_5 <= 10.757 )
							ret := 0.814815 // buy
						if( lower_5 > 10.757 )
							ret := 1.000000 // buy
					if( basis_minus > 0.989027 )
						if( lower_4 <= 10.78 )
							ret := 0.875000 // buy
						if( lower_4 > 10.78 )
							ret := 1.000000 // buy
				if( upper_1 > 11.7402 )
					if( upper_1 <= 11.7466 )
						if( lower_1 <= 11.2793 )
							ret := -0.583333
						if( lower_1 > 11.2793 )
							ret := -0.363636
					if( upper_1 > 11.7466 )
						if( upper_5 <= 12.2891 )
							if( basis <= 11.7252 )
								if( lower_2 <= 11.4263 )
									ret := 0.206897
								if( lower_2 > 11.4263 )
									ret := 1.000000 // buy
							if( basis > 11.7252 )
								if( basis_max <= -0.587067 )
									ret := -0.687500
								if( basis_max > -0.587067 )
									ret := 0.387097
						if( upper_5 > 12.2891 )
							if( upper_6 <= 12.6429 )
								if( upper_6 <= 12.6378 )
									ret := 0.537037
								if( upper_6 > 12.6378 )
									ret := 1.000000 // buy
							if( upper_6 > 12.6429 )
								ret := -0.250000
	if( upper_3 > 12.1157 )
		if( lower_4 <= 51.2461 )
			if( basis <= 52.7972 )
				if( upper_1 <= 11.9931 )
					if( upper_1 <= 11.9224 )
						if( lower_3 <= 10.8271 )
							if( lower_6 <= 7.40569 )
								if( lower_1 <= 9.02415 )
									ret := 0.733333 // buy
								if( lower_1 > 9.02415 )
									ret := -0.516393
							if( lower_6 > 7.40569 )
								if( lower_3 <= 9.50413 )
									ret := 0.429245
								if( lower_3 > 9.50413 )
									ret := -0.136164
						if( lower_3 > 10.8271 )
							if( upper_4 <= 12.2472 )
								if( lower_4 <= 11.2452 )
									ret := 0.133333
								if( lower_4 > 11.2452 )
									ret := 0.000000
							if( upper_4 > 12.2472 )
								if( lower_4 <= 10.9393 )
									ret := -0.727273 // sell
								if( lower_4 > 10.9393 )
									ret := -1.000000 // sell
					if( upper_1 > 11.9224 )
						if( lower_4 <= 10.5664 )
							if( upper_4 <= 13.043 )
								if( basis_max <= -1.67143 )
									ret := -0.864286 // sell
								if( basis_max > -1.67143 )
									ret := -0.500000
							if( upper_4 > 13.043 )
								if( upper_4 <= 13.066 )
									ret := 0.470588
								if( upper_4 > 13.066 )
									ret := -0.827586 // sell
						if( lower_4 > 10.5664 )
							if( lower_6 <= 10.9689 )
								if( lower_1 <= 11.2041 )
									ret := 0.777778 // buy
								if( lower_1 > 11.2041 )
									ret := 0.141176
							if( lower_6 > 10.9689 )
								if( lower_5 <= 11.2083 )
									ret := -0.818182 // sell
								if( lower_5 > 11.2083 )
									ret := -0.197183
				if( upper_1 > 11.9931 )
					if( upper_5 <= 61.0727 )
						if( basis_minus <= 0.602805 )
							if( lower_3 <= 13.4825 )
								if( upper_5 <= 14.1109 )
									ret := 0.213904
								if( upper_5 > 14.1109 )
									ret := 0.742424 // buy
							if( lower_3 > 13.4825 )
								if( lower_6 <= 14.3433 )
									ret := -0.198738
								if( lower_6 > 14.3433 )
									ret := 0.247734
						if( basis_minus > 0.602805 )
							if( upper_3 <= 57.6831 )
								if( upper_1 <= 12.2154 )
									ret := 0.141770
								if( upper_1 > 12.2154 )
									ret := -0.005834
							if( upper_3 > 57.6831 )
								if( upper_1 <= 55.2257 )
									ret := -0.940000 // sell
								if( upper_1 > 55.2257 )
									ret := -0.437500
					if( upper_5 > 61.0727 )
						if( upper_6 <= 63.9499 )
							ret := 1.000000 // buy
						if( upper_6 > 63.9499 )
							ret := 0.777778 // buy
			if( basis > 52.7972 )
				if( upper_1 <= 58.3743 )
					if( basis_max <= -8.18689 )
						if( basis_max <= -14.5297 )
							ret := -1.000000 // sell
						if( basis_max > -14.5297 )
							if( basis <= 52.8848 )
								if( basis_max <= -8.46795 )
									ret := -0.500000
								if( basis_max > -8.46795 )
									ret := 0.818182 // buy
							if( basis > 52.8848 )
								if( lower_3 <= 48.1828 )
									ret := 0.975610 // buy
								if( lower_3 > 48.1828 )
									ret := 0.635246
					if( basis_max > -8.18689 )
						if( lower_2 <= 52.1705 )
							if( upper_6 <= 56.6939 )
								if( upper_3 <= 54.6746 )
									ret := 0.500000
								if( upper_3 > 54.6746 )
									ret := -0.723404 // sell
							if( upper_6 > 56.6939 )
								if( lower_5 <= 50.2994 )
									ret := 0.267650
								if( lower_5 > 50.2994 )
									ret := 0.803571 // buy
						if( lower_2 > 52.1705 )
							if( basis_minus <= 7.15288 )
								if( lower_2 <= 52.4974 )
									ret := -0.248408
								if( lower_2 > 52.4974 )
									ret := 0.369231
							if( basis_minus > 7.15288 )
								if( upper_6 <= 62.8617 )
									ret := -0.777778 // sell
								if( upper_6 > 62.8617 )
									ret := 0.025000
				if( upper_1 > 58.3743 )
					if( lower_1 <= 54.0186 )
						if( basis_max <= -10.9067 )
							if( basis <= 55.4719 )
								if( upper_6 <= 71.7272 )
									ret := -1.000000 // sell
								if( upper_6 > 71.7272 )
									ret := -0.900000 // sell
							if( basis > 55.4719 )
								if( upper_4 <= 64.554 )
									ret := -0.851852 // sell
								if( upper_4 > 64.554 )
									ret := 0.415842
						if( basis_max > -10.9067 )
							if( basis <= 56.1527 )
								ret := 0.666667
							if( basis > 56.1527 )
								ret := 1.000000 // buy
					if( lower_1 > 54.0186 )
						if( upper_1 <= 59.3432 )
							if( lower_5 <= 49.5017 )
								if( basis_max <= -9.44275 )
									ret := -0.666667
								if( basis_max > -9.44275 )
									ret := -1.000000 // sell
							if( lower_5 > 49.5017 )
								ret := -0.285714
						if( upper_1 > 59.3432 )
							if( lower_6 <= 44.6468 )
								if( lower_5 <= 47.2404 )
									ret := -0.913043 // sell
								if( lower_5 > 47.2404 )
									ret := -0.647059
							if( lower_6 > 44.6468 )
								if( basis <= 57.2079 )
									ret := -0.368421
								if( basis > 57.2079 )
									ret := 0.447059
		if( lower_4 > 51.2461 )
			if( basis_minus <= 15.1607 )
				if( lower_2 <= 56.4151 )
					if( basis <= 58.0656 )
						if( basis <= 57.5323 )
							if( lower_4 <= 55.3291 )
								if( basis_minus <= 2.16694 )
									ret := 0.274390
								if( basis_minus > 2.16694 )
									ret := -0.133615
							if( lower_4 > 55.3291 )
								if( upper_2 <= 57.4149 )
									ret := -0.920000 // sell
								if( upper_2 > 57.4149 )
									ret := -0.266055
						if( basis > 57.5323 )
							if( upper_5 <= 62.7542 )
								if( basis_max <= -4.65449 )
									ret := 0.970588 // buy
								if( basis_max > -4.65449 )
									ret := 0.333333
							if( upper_5 > 62.7542 )
								if( upper_3 <= 61.1339 )
									ret := -0.636364
								if( upper_3 > 61.1339 )
									ret := 0.301205
					if( basis > 58.0656 )
						if( basis <= 58.4929 )
							if( lower_2 <= 55.4027 )
								if( lower_1 <= 56.425 )
									ret := -0.873016 // sell
								if( lower_1 > 56.425 )
									ret := -0.342105
							if( lower_2 > 55.4027 )
								ret := -1.000000 // sell
						if( basis > 58.4929 )
							if( upper_4 <= 64.4768 )
								if( upper_3 <= 62.8195 )
									ret := 0.054348
								if( upper_3 > 62.8195 )
									ret := -0.729730 // sell
							if( upper_4 > 64.4768 )
								if( basis_max <= -8.55612 )
									ret := 0.155963
								if( basis_max > -8.55612 )
									ret := -0.739130 // sell
				if( lower_2 > 56.4151 )
					if( lower_5 <= 55.3477 )
						if( basis_max <= -8.03228 )
							if( lower_2 <= 57.2361 )
								if( basis_max <= -8.25215 )
									ret := -0.061728
								if( basis_max > -8.25215 )
									ret := -0.972222 // sell
							if( lower_2 > 57.2361 )
								if( lower_1 <= 59.6934 )
									ret := 0.965517 // buy
								if( lower_1 > 59.6934 )
									ret := -0.259259
						if( basis_max > -8.03228 )
							if( lower_4 <= 55.8184 )
								if( upper_6 <= 63.3271 )
									ret := 0.645161
								if( upper_6 > 63.3271 )
									ret := 0.070175
							if( lower_4 > 55.8184 )
								if( lower_5 <= 55.1278 )
									ret := 0.104478
								if( lower_5 > 55.1278 )
									ret := 0.690141
					if( lower_5 > 55.3477 )
						if( upper_1 <= 60.5274 )
							if( lower_1 <= 57.2492 )
								if( basis_minus <= 2.29042 )
									ret := -0.162791
								if( basis_minus > 2.29042 )
									ret := 0.325000
							if( lower_1 > 57.2492 )
								if( upper_2 <= 61.0575 )
									ret := -0.392405
								if( upper_2 > 61.0575 )
									ret := -0.852941 // sell
						if( upper_1 > 60.5274 )
							if( upper_6 <= 65.149 )
								if( basis <= 59.587 )
									ret := 0.205128
								if( basis > 59.587 )
									ret := 0.695652
							if( upper_6 > 65.149 )
								if( upper_6 <= 103.661 )
									ret := -0.086734
								if( upper_6 > 103.661 )
									ret := 0.869565 // buy
			if( basis_minus > 15.1607 )
				if( upper_2 <= 96.2102 )
					if( lower_1 <= 68.6385 )
						if( basis_minus <= 15.8707 )
							if( upper_6 <= 86.624 )
								if( lower_1 <= 67.3304 )
									ret := 0.920000 // buy
								if( lower_1 > 67.3304 )
									ret := 0.300000
							if( upper_6 > 86.624 )
								ret := 1.000000 // buy
						if( basis_minus > 15.8707 )
							if( lower_3 <= 62.2487 )
								ret := 0.083333
							if( lower_3 > 62.2487 )
								if( lower_4 <= 61.9731 )
									ret := 1.000000 // buy
								if( lower_4 > 61.9731 )
									ret := 0.818182 // buy
					if( lower_1 > 68.6385 )
						if( upper_1 <= 78.5044 )
							if( lower_4 <= 63.5206 )
								if( basis_max <= -17.2158 )
									ret := 0.090909
								if( basis_max > -17.2158 )
									ret := -0.369565
							if( lower_4 > 63.5206 )
								ret := -1.000000 // sell
						if( upper_1 > 78.5044 )
							if( basis <= 78.6022 )
								if( lower_1 <= 74.449 )
									ret := 0.577236
								if( lower_1 > 74.449 )
									ret := 1.000000 // buy
							if( basis > 78.6022 )
								if( basis_minus <= 26.0317 )
									ret := 0.372263
								if( basis_minus > 26.0317 )
									ret := -0.513514
				if( upper_2 > 96.2102 )
					if( upper_3 <= 98.928 )
						if( basis <= 89.1396 )
							ret := 0.375000
						if( basis > 89.1396 )
							ret := -1.000000 // sell
					if( upper_3 > 98.928 )
						ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Fibonacci_Bollinger 
//@version=5
//indicator shorttitle="FBB", title="Fibonacci Bollinger Bands", overlay=true)

// Inputs
length_FiboBB = input.int(200, minval=1)
src = input(hlc3, title="Source")
mult = input.float(3.0, minval=0.001, maxval=50)

// Calculations
basis = ta.vwma(src, length_FiboBB)
dev = mult * ta.stdev(src, length_FiboBB)

// Upper Bands
upper_1 = basis + (0.236 * dev)
upper_2 = basis + (0.382 * dev)
upper_3 = basis + (0.5 * dev)
upper_4 = basis + (0.618 * dev)
upper_5 = basis + (0.764 * dev)
upper_6 = basis + (1 * dev)

// Lower Bands
lower_1 = basis - (0.236 * dev)
lower_2 = basis - (0.382 * dev)
lower_3 = basis - (0.5 * dev)
lower_4 = basis - (0.618 * dev)
lower_5 = basis - (0.764 * dev)
lower_6 = basis - (1 * dev)

basis_minus = basis -lower_6
basis_max = basis -upper_6

// Plotting
plot(basis, color=color.fuchsia, linewidth=2)
plot(upper_1, color=color.white, linewidth=1, title="0.236")
plot(upper_2, color=color.white, linewidth=1, title="0.382")
plot(upper_3, color=color.white, linewidth=1, title="0.5")
plot(upper_4, color=color.white, linewidth=1, title="0.618")
plot(upper_5, color=color.white, linewidth=1, title="0.764")
plot(upper_6, color=color.red, linewidth=2, title="1")
plot(lower_1, color=color.white, linewidth=1, title="0.236")
plot(lower_2, color=color.white, linewidth=1, title="0.382")
plot(lower_3, color=color.white, linewidth=1, title="0.5")
plot(lower_4, color=color.white, linewidth=1, title="0.618")
plot(lower_5, color=color.white, linewidth=1, title="0.764")
plot(lower_6, color=color.green, linewidth=2, title="1")

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
float op_operation = decision_tree_0_RUN_15Min_785e7e2a(basis, upper_2, upper_3, lower_2, lower_6, lower_1, basis_minus, lower_3, upper_6, lower_5, lower_4, upper_5, upper_4, basis_max, upper_1)

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


