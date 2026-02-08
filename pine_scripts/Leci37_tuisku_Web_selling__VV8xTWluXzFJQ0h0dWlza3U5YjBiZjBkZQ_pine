//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ichimoku_Cloud
// ID_model: U_1Min_1ICH_9b0bf0de Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_1ICH_9b0bf0de", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_9b0bf0de(senkou_span_a_displaced, cross_dn_tenkan_kinjunInt, kinjun_sen, chinkou_span, senkou_span_b_displaced, basis_minus, senkou_span_b, senkou_span_a, cross_up_tenkan_kinjunInt, tenkan_sen, basis_max)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( senkou_span_a <= 13.7096 )
		if( senkou_span_b <= 14.1021 )
			if( senkou_span_a_displaced <= 13.3475 )
				ret := 0.000000
			if( senkou_span_a_displaced > 13.3475 )
				if( senkou_span_a <= 13.6887 )
					if( senkou_span_a <= 13.5924 )
						if( tenkan_sen <= 13.3814 )
							if( tenkan_sen <= 13.3552 )
								if( basis_max <= 0.082772 )
									ret := 1.000000 // buy
								if( basis_max > 0.082772 )
									ret := 0.750000 // buy
							if( tenkan_sen > 13.3552 )
								ret := -0.166667
						if( tenkan_sen > 13.3814 )
							ret := 1.000000 // buy
					if( senkou_span_a > 13.5924 )
						if( chinkou_span <= 13.8888 )
							ret := -0.600000
						if( chinkou_span > 13.8888 )
							if( tenkan_sen <= 13.7027 )
								if( senkou_span_a <= 13.6367 )
									ret := 0.666667
								if( senkou_span_a > 13.6367 )
									ret := 1.000000 // buy
							if( tenkan_sen > 13.7027 )
								ret := 0.142857
				if( senkou_span_a > 13.6887 )
					if( senkou_span_a_displaced <= 13.8848 )
						ret := 1.000000 // buy
					if( senkou_span_a_displaced > 13.8848 )
						ret := 0.750000 // buy
		if( senkou_span_b > 14.1021 )
			ret := -1.000000 // sell
	if( senkou_span_a > 13.7096 )
		if( chinkou_span <= 16.2076 )
			if( senkou_span_a <= 16.1503 )
				if( chinkou_span <= 16.0213 )
					if( tenkan_sen <= 15.9551 )
						if( chinkou_span <= 15.8821 )
							if( senkou_span_a_displaced <= 15.8112 )
								if( basis_max <= 0.010316 )
									ret := 0.018996
								if( basis_max > 0.010316 )
									ret := 0.191054
							if( senkou_span_a_displaced > 15.8112 )
								if( tenkan_sen <= 15.8918 )
									ret := -0.155514
								if( tenkan_sen > 15.8918 )
									ret := -0.476190
						if( chinkou_span > 15.8821 )
							if( tenkan_sen <= 15.8133 )
								if( senkou_span_a_displaced <= 15.6995 )
									ret := 0.402597
								if( senkou_span_a_displaced > 15.6995 )
									ret := 0.852459 // buy
							if( tenkan_sen > 15.8133 )
								if( chinkou_span <= 15.97 )
									ret := 0.106267
								if( chinkou_span > 15.97 )
									ret := 0.490000
					if( tenkan_sen > 15.9551 )
						if( chinkou_span <= 15.8697 )
							if( senkou_span_a <= 16.0773 )
								if( tenkan_sen <= 15.9703 )
									ret := -0.274510
								if( tenkan_sen > 15.9703 )
									ret := -0.841026 // sell
							if( senkou_span_a > 16.0773 )
								if( senkou_span_b <= 16.2266 )
									ret := -0.045455
								if( senkou_span_b > 16.2266 )
									ret := -1.000000 // sell
						if( chinkou_span > 15.8697 )
							if( basis_minus <= -0.128665 )
								if( chinkou_span <= 15.9137 )
									ret := 1.000000 // buy
								if( chinkou_span > 15.9137 )
									ret := 0.250000
							if( basis_minus > -0.128665 )
								if( basis_minus <= -0.007207 )
									ret := -0.148825
								if( basis_minus > -0.007207 )
									ret := -0.392157
				if( chinkou_span > 16.0213 )
					if( tenkan_sen <= 16.0551 )
						if( senkou_span_a_displaced <= 14.178 )
							if( senkou_span_a <= 15.3313 )
								if( kinjun_sen <= 14.9463 )
									ret := 1.000000 // buy
								if( kinjun_sen > 14.9463 )
									ret := 0.750000 // buy
							if( senkou_span_a > 15.3313 )
								ret := -1.000000 // sell
						if( senkou_span_a_displaced > 14.178 )
							if( kinjun_sen <= 16.1278 )
								if( chinkou_span <= 16.1146 )
									ret := 0.347880
								if( chinkou_span > 16.1146 )
									ret := 0.552817
							if( kinjun_sen > 16.1278 )
								if( chinkou_span <= 16.1825 )
									ret := 0.250000
								if( chinkou_span > 16.1825 )
									ret := -0.875000 // sell
					if( tenkan_sen > 16.0551 )
						if( senkou_span_a_displaced <= 15.8956 )
							if( kinjun_sen <= 15.8517 )
								if( chinkou_span <= 16.1818 )
									ret := -0.833333 // sell
								if( chinkou_span > 16.1818 )
									ret := 0.000000
							if( kinjun_sen > 15.8517 )
								if( basis_max <= -0.03495 )
									ret := 0.851351 // buy
								if( basis_max > -0.03495 )
									ret := -0.272727
						if( senkou_span_a_displaced > 15.8956 )
							if( basis_max <= -0.016335 )
								if( senkou_span_b_displaced <= 16.1887 )
									ret := -0.601852
								if( senkou_span_b_displaced > 16.1887 )
									ret := 0.423077
							if( basis_max > -0.016335 )
								if( chinkou_span <= 16.1601 )
									ret := 0.043796
								if( chinkou_span > 16.1601 )
									ret := 0.383721
			if( senkou_span_a > 16.1503 )
				if( basis_max <= 0.032475 )
					if( basis_minus <= -0.164049 )
						if( basis_max <= -0.032552 )
							ret := 1.000000 // buy
						if( basis_max > -0.032552 )
							ret := 0.500000
					if( basis_minus > -0.164049 )
						if( basis_max <= -0.024988 )
							if( senkou_span_a_displaced <= 15.8414 )
								ret := 0.166667
							if( senkou_span_a_displaced > 15.8414 )
								if( chinkou_span <= 16.1642 )
									ret := -0.879699 // sell
								if( chinkou_span > 16.1642 )
									ret := -0.527778
						if( basis_max > -0.024988 )
							if( kinjun_sen <= 16.3332 )
								if( tenkan_sen <= 16.312 )
									ret := -0.334996
								if( tenkan_sen > 16.312 )
									ret := 0.129032
							if( kinjun_sen > 16.3332 )
								if( cross_up_tenkan_kinjunInt <= 0.5 )
									ret := -0.657692
								if( cross_up_tenkan_kinjunInt > 0.5 )
									ret := 1.000000 // buy
				if( basis_max > 0.032475 )
					if( senkou_span_b <= 16.3201 )
						if( senkou_span_b <= 16.1655 )
							if( senkou_span_b_displaced <= 15.975 )
								ret := -0.750000 // sell
							if( senkou_span_b_displaced > 15.975 )
								ret := -1.000000 // sell
						if( senkou_span_b > 16.1655 )
							if( basis_max <= 0.043039 )
								if( senkou_span_a_displaced <= 16.3925 )
									ret := 0.212121
								if( senkou_span_a_displaced > 16.3925 )
									ret := -0.833333 // sell
							if( basis_max > 0.043039 )
								if( basis_max <= 0.071238 )
									ret := 0.847826 // buy
								if( basis_max > 0.071238 )
									ret := -0.250000
					if( senkou_span_b > 16.3201 )
						if( basis_max <= 0.087456 )
							if( basis_minus <= -0.113075 )
								if( chinkou_span <= 16.1664 )
									ret := 0.200000
								if( chinkou_span > 16.1664 )
									ret := 0.666667
							if( basis_minus > -0.113075 )
								if( basis_minus <= -0.100555 )
									ret := -0.842105 // sell
								if( basis_minus > -0.100555 )
									ret := -0.448276
						if( basis_max > 0.087456 )
							ret := -1.000000 // sell
		if( chinkou_span > 16.2076 )
			if( tenkan_sen <= 16.2324 )
				if( tenkan_sen <= 16.11 )
					if( kinjun_sen <= 16.0706 )
						if( senkou_span_b_displaced <= 16.2025 )
							if( tenkan_sen <= 15.7767 )
								if( basis_max <= -0.063175 )
									ret := 0.000000
								if( basis_max > -0.063175 )
									ret := 0.978022 // buy
							if( tenkan_sen > 15.7767 )
								if( senkou_span_a <= 15.8758 )
									ret := 0.170732
								if( senkou_span_a > 15.8758 )
									ret := 0.688776
						if( senkou_span_b_displaced > 16.2025 )
							if( senkou_span_b_displaced <= 16.2248 )
								ret := -1.000000 // sell
							if( senkou_span_b_displaced > 16.2248 )
								ret := -0.500000
					if( kinjun_sen > 16.0706 )
						if( basis_max <= 0.089625 )
							if( chinkou_span <= 16.2299 )
								if( basis_max <= 0.029912 )
									ret := 0.000000
								if( basis_max > 0.029912 )
									ret := 0.916667 // buy
							if( chinkou_span > 16.2299 )
								if( tenkan_sen <= 16.1046 )
									ret := 0.928105 // buy
								if( tenkan_sen > 16.1046 )
									ret := 0.777778 // buy
						if( basis_max > 0.089625 )
							ret := -0.200000
				if( tenkan_sen > 16.11 )
					if( senkou_span_b_displaced <= 15.2975 )
						if( basis_minus <= 0.3225 )
							if( basis_max <= -0.167154 )
								ret := -0.666667
							if( basis_max > -0.167154 )
								ret := -1.000000 // sell
						if( basis_minus > 0.3225 )
							ret := 0.166667
					if( senkou_span_b_displaced > 15.2975 )
						if( chinkou_span <= 16.2684 )
							if( senkou_span_b_displaced <= 16.2915 )
								if( basis_max <= 0.038375 )
									ret := 0.181818
								if( basis_max > 0.038375 )
									ret := -0.750000 // sell
							if( senkou_span_b_displaced > 16.2915 )
								if( tenkan_sen <= 16.1593 )
									ret := 0.333333
								if( tenkan_sen > 16.1593 )
									ret := 0.797753 // buy
						if( chinkou_span > 16.2684 )
							if( senkou_span_a_displaced <= 16.241 )
								if( senkou_span_a_displaced <= 15.9518 )
									ret := 1.000000 // buy
								if( senkou_span_a_displaced > 15.9518 )
									ret := 0.628180
							if( senkou_span_a_displaced > 16.241 )
								if( senkou_span_b_displaced <= 16.3114 )
									ret := -0.035714
								if( senkou_span_b_displaced > 16.3114 )
									ret := 0.649485
			if( tenkan_sen > 16.2324 )
				if( chinkou_span <= 16.3454 )
					if( tenkan_sen <= 16.3613 )
						if( basis_max <= 0.036691 )
							if( tenkan_sen <= 16.3215 )
								if( basis_max <= 0.028232 )
									ret := 0.000000
								if( basis_max > 0.028232 )
									ret := 0.585366
							if( tenkan_sen > 16.3215 )
								if( kinjun_sen <= 16.3648 )
									ret := -0.269542
								if( kinjun_sen > 16.3648 )
									ret := 0.188976
						if( basis_max > 0.036691 )
							if( senkou_span_a_displaced <= 16.5625 )
								if( kinjun_sen <= 16.3813 )
									ret := 0.444444
								if( kinjun_sen > 16.3813 )
									ret := 0.000000
							if( senkou_span_a_displaced > 16.5625 )
								if( basis_max <= 0.042789 )
									ret := 0.833333 // buy
								if( basis_max > 0.042789 )
									ret := 1.000000 // buy
					if( tenkan_sen > 16.3613 )
						if( kinjun_sen <= 16.4714 )
							if( senkou_span_a_displaced <= 16.4665 )
								if( basis_minus <= 0.035335 )
									ret := -0.366102
								if( basis_minus > 0.035335 )
									ret := -0.688889
							if( senkou_span_a_displaced > 16.4665 )
								if( senkou_span_a <= 16.4616 )
									ret := 0.020833
								if( senkou_span_a > 16.4616 )
									ret := -0.526316
						if( kinjun_sen > 16.4714 )
							if( senkou_span_a <= 16.6143 )
								if( senkou_span_a_displaced <= 16.6477 )
									ret := -0.619632
								if( senkou_span_a_displaced > 16.6477 )
									ret := -0.941176 // sell
							if( senkou_span_a > 16.6143 )
								if( senkou_span_a_displaced <= 16.9319 )
									ret := 0.000000
								if( senkou_span_a_displaced > 16.9319 )
									ret := -0.750000 // sell
				if( chinkou_span > 16.3454 )
					if( senkou_span_b <= 16.4924 )
						if( chinkou_span <= 16.4833 )
							if( tenkan_sen <= 16.3294 )
								if( senkou_span_b <= 16.1994 )
									ret := 0.791667 // buy
								if( senkou_span_b > 16.1994 )
									ret := 0.372751
							if( tenkan_sen > 16.3294 )
								if( basis_minus <= 0.117856 )
									ret := 0.008274
								if( basis_minus > 0.117856 )
									ret := -0.886792 // sell
						if( chinkou_span > 16.4833 )
							if( senkou_span_b <= 16.4313 )
								if( senkou_span_b <= 16.4 )
									ret := 0.460916
								if( senkou_span_b > 16.4 )
									ret := 0.072727
							if( senkou_span_b > 16.4313 )
								if( chinkou_span <= 16.9175 )
									ret := 0.551313
								if( chinkou_span > 16.9175 )
									ret := 0.875000 // buy
					if( senkou_span_b > 16.4924 )
						if( chinkou_span <= 16.6198 )
							if( tenkan_sen <= 16.6013 )
								if( chinkou_span <= 16.4862 )
									ret := -0.240175
								if( chinkou_span > 16.4862 )
									ret := 0.158273
							if( tenkan_sen > 16.6013 )
								if( kinjun_sen <= 16.7975 )
									ret := -0.349708
								if( kinjun_sen > 16.7975 )
									ret := -0.713262 // sell
						if( chinkou_span > 16.6198 )
							if( senkou_span_a <= 16.7075 )
								if( chinkou_span <= 16.7127 )
									ret := 0.137632
								if( chinkou_span > 16.7127 )
									ret := 0.463946
							if( senkou_span_a > 16.7075 )
								if( basis_max <= 0.031753 )
									ret := 0.030711
								if( basis_max > 0.031753 )
									ret := 0.174805
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Ichimoku_Cloud 
//@version=5
//indicator "Ichimoku Cloud", overlay=true)

// Input parameters for the Ichimoku Cloud
turning_periods = input.int(9, title="Tenkan-Sen Period")
standard_periods = input.int(26, title="Kinjun-Sen Period")
leading_span2_periods = input.int(52, title="Senkou Span B Period")
displacement = input.int(26, title="Displacement")

show_tenkan_sen = input.bool(true, title="Show Tenkan-Sen")
show_kinjun_sen = input.bool(true, title="Show Kinjun-Sen")
show_chinkou_span = input.bool(true, title="Show Chinkou Span")
show_cloud = input.bool(true, title="Show Cloud")
show_crosses = input.bool(false, title="Show Crosses")

// Donchian channel calculation
donchian(highs, lows, length) =>
    (ta.highest(highs, length) + ta.lowest(lows, length)) / 2

// Ichimoku calculations
tenkan_sen = donchian(high, low, turning_periods)
kinjun_sen = donchian(high, low, standard_periods)
senkou_span_a = (tenkan_sen + kinjun_sen) / 2
senkou_span_b = donchian(high, low, leading_span2_periods)

// Displaced Senkou Spans
senkou_span_a_displaced = senkou_span_a[displacement]
senkou_span_b_displaced = senkou_span_b[displacement]

// Chinkou Span
chinkou_span = close[displacement]

// Crosses
cross_up_tenkan_kinjun = ta.crossover(tenkan_sen, kinjun_sen)
cross_dn_tenkan_kinjun = ta.crossunder(tenkan_sen, kinjun_sen)
cross_up_tenkan_kinjunInt = cross_up_tenkan_kinjun ? 1 : 0  // Bool to int
cross_dn_tenkan_kinjunInt = cross_dn_tenkan_kinjun ? 1 : 0  // Bool to int

basis_minus = senkou_span_a - senkou_span_b
basis_max = senkou_span_a - tenkan_sen

// Plotting
plot(show_tenkan_sen ? tenkan_sen : na, color=color.lime, title="Tenkan-Sen", linewidth=1)
plot(show_kinjun_sen ? kinjun_sen : na, color=color.fuchsia, title="Kinjun-Sen", linewidth=1)
plot(show_chinkou_span ? chinkou_span : na, color=color.aqua, title="Chinkou Span", linewidth=1, offset=-displacement)

// Plot the Senkou Span lines and store the plot references
senkou_span_a_plot = plot(show_cloud ? senkou_span_a_displaced : na, color=color.green, title="Senkou Span A", linewidth=1)
senkou_span_b_plot = plot(show_cloud ? senkou_span_b_displaced : na, color=color.red, title="Senkou Span B", linewidth=1)

// Cloud filling
fill(senkou_span_a_plot, senkou_span_b_plot, color=color.new(color.lime, 90), title="Bullish Cloud", transp=70, fillgaps=true)
fill(senkou_span_a_plot, senkou_span_b_plot, color=color.new(color.red, 90), title="Bearish Cloud", transp=70, fillgaps=true)

plotshape(series=(show_crosses and cross_up_tenkan_kinjun) ? close : na, location=location.belowbar, color=color.yellow, style=shape.triangleup, size=size.small, title="Cross Up Tenkan Kinjun")
plotshape(series=(show_crosses and cross_dn_tenkan_kinjun) ? close : na, location=location.abovebar, color=color.yellow, style=shape.triangledown, size=size.small, title="Cross Down Tenkan Kinjun")

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
float op_operation = decision_tree_0_U_1Min_9b0bf0de(senkou_span_a_displaced, cross_dn_tenkan_kinjunInt, kinjun_sen, chinkou_span, senkou_span_b_displaced, basis_minus, senkou_span_b, senkou_span_a, cross_up_tenkan_kinjunInt, tenkan_sen, basis_max)

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


