//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ichimoku_Cloud
// ID_model: TSLA_1Min_1ICH_0d6b1ffa Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TSLA_1Min_1ICH_0d6b1ffa", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TSLA_1Min_0d6b1ffa(senkou_span_a_displaced, cross_dn_tenkan_kinjunInt, kinjun_sen, chinkou_span, senkou_span_b_displaced, basis_minus, senkou_span_b, senkou_span_a, cross_up_tenkan_kinjunInt, tenkan_sen, basis_max)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=0.7, min_samples_leaf=7,min_samples_split=10, random_state=843828734)
	if( senkou_span_a_displaced <= 259.251 )
		if( basis_minus <= -2.01866 )
			if( chinkou_span <= 252.656 )
				if( senkou_span_b_displaced <= 224.94 )
					if( kinjun_sen <= 141.199 )
						if( basis_max <= 0.07414 )
							if( basis_minus <= -2.60136 )
								ret := -1.000000 // sell
							if( basis_minus > -2.60136 )
								ret := -0.818182 // sell
						if( basis_max > 0.07414 )
							ret := 0.300000
					if( kinjun_sen > 141.199 )
						if( basis_minus <= -2.73749 )
							if( basis_max <= -0.120642 )
								ret := -0.187500
							if( basis_max > -0.120642 )
								if( chinkou_span <= 177.725 )
									ret := 0.052632
								if( chinkou_span > 177.725 )
									ret := 0.811159 // buy
						if( basis_minus > -2.73749 )
							if( basis_minus <= -2.58201 )
								if( basis_minus <= -2.71609 )
									ret := 0.294118
								if( basis_minus > -2.71609 )
									ret := -0.773585 // sell
							if( basis_minus > -2.58201 )
								if( chinkou_span <= 219.01 )
									ret := 0.322581
								if( chinkou_span > 219.01 )
									ret := 0.711111 // buy
				if( senkou_span_b_displaced > 224.94 )
					if( senkou_span_a_displaced <= 229.54 )
						if( senkou_span_b_displaced <= 230.606 )
							if( basis_minus <= -2.24478 )
								if( basis_minus <= -4.57387 )
									ret := -0.468750
								if( basis_minus > -4.57387 )
									ret := -0.921569 // sell
							if( basis_minus > -2.24478 )
								if( chinkou_span <= 224.267 )
									ret := -0.750000 // sell
								if( chinkou_span > 224.267 )
									ret := -0.083333
						if( senkou_span_b_displaced > 230.606 )
							ret := 0.214286
					if( senkou_span_a_displaced > 229.54 )
						if( kinjun_sen <= 242.706 )
							if( basis_max <= 1.13058 )
								if( chinkou_span <= 229.179 )
									ret := 0.345455
								if( chinkou_span > 229.179 )
									ret := 0.842105 // buy
							if( basis_max > 1.13058 )
								if( basis_max <= 2.98017 )
									ret := -0.212766
								if( basis_max > 2.98017 )
									ret := 0.511628
						if( kinjun_sen > 242.706 )
							if( chinkou_span <= 245.418 )
								if( kinjun_sen <= 248.327 )
									ret := -0.597938
								if( kinjun_sen > 248.327 )
									ret := 0.800000 // buy
							if( chinkou_span > 245.418 )
								if( kinjun_sen <= 251.933 )
									ret := 0.242424
								if( kinjun_sen > 251.933 )
									ret := -0.636364
			if( chinkou_span > 252.656 )
				if( basis_max <= 0.241372 )
					ret := 0.416667
				if( basis_max > 0.241372 )
					if( basis_minus <= -2.99102 )
						ret := 0.777778 // buy
					if( basis_minus > -2.99102 )
						if( senkou_span_b <= 255.723 )
							if( chinkou_span <= 253.381 )
								ret := 0.928571 // buy
							if( chinkou_span > 253.381 )
								ret := 1.000000 // buy
						if( senkou_span_b > 255.723 )
							ret := 0.833333 // buy
		if( basis_minus > -2.01866 )
			if( chinkou_span <= 261.63 )
				if( basis_max <= -2.02504 )
					if( basis_minus <= 4.2025 )
						if( basis_max <= -3.31078 )
							if( basis_max <= -3.46565 )
								if( senkou_span_b <= 153.029 )
									ret := -0.055556
								if( senkou_span_b > 153.029 )
									ret := 0.840000 // buy
							if( basis_max > -3.46565 )
								ret := -0.777778 // sell
						if( basis_max > -3.31078 )
							if( basis_max <= -2.83824 )
								ret := 1.000000 // buy
							if( basis_max > -2.83824 )
								if( basis_max <= -2.56449 )
									ret := 0.352941
								if( basis_max > -2.56449 )
									ret := 0.723404 // buy
					if( basis_minus > 4.2025 )
						ret := -0.866667 // sell
				if( basis_max > -2.02504 )
					if( basis_minus <= 6.33919 )
						if( chinkou_span <= 176.547 )
							if( senkou_span_b <= 176.413 )
								if( basis_minus <= -0.243444 )
									ret := 0.144369
								if( basis_minus > -0.243444 )
									ret := 0.008024
							if( senkou_span_b > 176.413 )
								if( kinjun_sen <= 177.081 )
									ret := -0.283802
								if( kinjun_sen > 177.081 )
									ret := -0.680743
						if( chinkou_span > 176.547 )
							if( senkou_span_a <= 176.877 )
								if( tenkan_sen <= 175.816 )
									ret := 0.784270 // buy
								if( tenkan_sen > 175.816 )
									ret := 0.413727
							if( senkou_span_a > 176.877 )
								if( kinjun_sen <= 178.517 )
									ret := 0.148811
								if( kinjun_sen > 178.517 )
									ret := 0.045127
					if( basis_minus > 6.33919 )
						if( senkou_span_b_displaced <= 153.101 )
							ret := 0.000000
						if( senkou_span_b_displaced > 153.101 )
							if( senkou_span_a_displaced <= 214.955 )
								if( tenkan_sen <= 190.29 )
									ret := 0.955556 // buy
								if( tenkan_sen > 190.29 )
									ret := 0.071429
							if( senkou_span_a_displaced > 214.955 )
								ret := 1.000000 // buy
			if( chinkou_span > 261.63 )
				if( basis_max <= -1.09766 )
					ret := -0.866667 // sell
				if( basis_max > -1.09766 )
					if( kinjun_sen <= 261.547 )
						if( basis_minus <= 0.152169 )
							if( chinkou_span <= 263.1 )
								ret := -0.187500
							if( chinkou_span > 263.1 )
								if( chinkou_span <= 263.896 )
									ret := 1.000000 // buy
								if( chinkou_span > 263.896 )
									ret := 0.727273 // buy
						if( basis_minus > 0.152169 )
							if( senkou_span_a_displaced <= 257.75 )
								if( basis_max <= -0.884169 )
									ret := 0.600000
								if( basis_max > -0.884169 )
									ret := 0.888889 // buy
							if( senkou_span_a_displaced > 257.75 )
								if( chinkou_span <= 261.806 )
									ret := 0.782609 // buy
								if( chinkou_span > 261.806 )
									ret := 0.946309 // buy
					if( kinjun_sen > 261.547 )
						ret := -0.250000
	if( senkou_span_a_displaced > 259.251 )
		if( senkou_span_a <= 256.508 )
			if( senkou_span_a <= 249.545 )
				ret := 0.142857
			if( senkou_span_a > 249.545 )
				if( chinkou_span <= 246.577 )
					ret := -0.727273 // sell
				if( chinkou_span > 246.577 )
					if( basis_minus <= -3.04239 )
						ret := -0.777778 // sell
					if( basis_minus > -3.04239 )
						if( chinkou_span <= 253.352 )
							ret := -1.000000 // sell
						if( chinkou_span > 253.352 )
							ret := -0.909091 // sell
		if( senkou_span_a > 256.508 )
			if( chinkou_span <= 257.682 )
				if( kinjun_sen <= 263.591 )
					if( kinjun_sen <= 260.687 )
						if( basis_max <= 0.514636 )
							if( tenkan_sen <= 259.448 )
								if( senkou_span_a_displaced <= 259.367 )
									ret := 0.111111
								if( senkou_span_a_displaced > 259.367 )
									ret := -0.840000 // sell
							if( tenkan_sen > 259.448 )
								ret := -0.176471
						if( basis_max > 0.514636 )
							if( basis_minus <= -1.41375 )
								ret := -0.384615
							if( basis_minus > -1.41375 )
								ret := 0.761905 // buy
					if( kinjun_sen > 260.687 )
						if( chinkou_span <= 254.386 )
							ret := -1.000000 // sell
						if( chinkou_span > 254.386 )
							if( senkou_span_b_displaced <= 262.61 )
								ret := -0.789474 // sell
							if( senkou_span_b_displaced > 262.61 )
								ret := -0.500000
				if( kinjun_sen > 263.591 )
					ret := 0.470588
			if( chinkou_span > 257.682 )
				if( basis_max <= 0.255492 )
					if( chinkou_span <= 262.832 )
						if( senkou_span_b <= 262.918 )
							if( chinkou_span <= 260.276 )
								if( senkou_span_b <= 258.028 )
									ret := 0.880000 // buy
								if( senkou_span_b > 258.028 )
									ret := -0.277603
							if( chinkou_span > 260.276 )
								if( senkou_span_a <= 260.309 )
									ret := 0.559633
								if( senkou_span_a > 260.309 )
									ret := -0.025890
						if( senkou_span_b > 262.918 )
							if( senkou_span_a <= 262.872 )
								if( chinkou_span <= 262.641 )
									ret := 0.170213
								if( chinkou_span > 262.641 )
									ret := -0.882353 // sell
							if( senkou_span_a > 262.872 )
								if( chinkou_span <= 260.788 )
									ret := -0.185185
								if( chinkou_span > 260.788 )
									ret := -0.817757 // sell
					if( chinkou_span > 262.832 )
						if( kinjun_sen <= 263.317 )
							if( tenkan_sen <= 262.417 )
								if( senkou_span_b <= 261.668 )
									ret := 0.055556
								if( senkou_span_b > 261.668 )
									ret := 0.795620 // buy
							if( tenkan_sen > 262.417 )
								if( kinjun_sen <= 262.818 )
									ret := 0.055118
								if( kinjun_sen > 262.818 )
									ret := 0.369369
						if( kinjun_sen > 263.317 )
							if( basis_minus <= 1.40217 )
								if( kinjun_sen <= 264.445 )
									ret := -0.210059
								if( kinjun_sen > 264.445 )
									ret := 0.150794
							if( basis_minus > 1.40217 )
								if( kinjun_sen <= 263.411 )
									ret := 0.666667
								if( kinjun_sen > 263.411 )
									ret := -0.884615 // sell
				if( basis_max > 0.255492 )
					if( chinkou_span <= 260.035 )
						if( senkou_span_a <= 261.099 )
							if( kinjun_sen <= 257.992 )
								ret := 1.000000 // buy
							if( kinjun_sen > 257.992 )
								if( kinjun_sen <= 259.977 )
									ret := -0.400000
								if( kinjun_sen > 259.977 )
									ret := 0.471910
						if( senkou_span_a > 261.099 )
							if( basis_max <= 0.394208 )
								if( senkou_span_b <= 262.389 )
									ret := -1.000000 // sell
								if( senkou_span_b > 262.389 )
									ret := -0.818182 // sell
							if( basis_max > 0.394208 )
								if( senkou_span_a_displaced <= 263.174 )
									ret := 0.076923
								if( senkou_span_a_displaced > 263.174 )
									ret := -0.450000
					if( chinkou_span > 260.035 )
						if( chinkou_span <= 260.741 )
							if( senkou_span_a <= 262.364 )
								if( basis_max <= 0.307886 )
									ret := 0.909091 // buy
								if( basis_max > 0.307886 )
									ret := 1.000000 // buy
							if( senkou_span_a > 262.364 )
								ret := 0.769231 // buy
						if( chinkou_span > 260.741 )
							if( senkou_span_a_displaced <= 266.604 )
								if( senkou_span_b_displaced <= 265.086 )
									ret := 0.373239
								if( senkou_span_b_displaced > 265.086 )
									ret := -0.607143
							if( senkou_span_a_displaced > 266.604 )
								if( basis_max <= 0.4548 )
									ret := 0.500000
								if( basis_max > 0.4548 )
									ret := 0.921053 // buy
	
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
float op_operation = decision_tree_0_TSLA_1Min_0d6b1ffa(senkou_span_a_displaced, cross_dn_tenkan_kinjunInt, kinjun_sen, chinkou_span, senkou_span_b_displaced, basis_minus, senkou_span_b, senkou_span_a, cross_up_tenkan_kinjunInt, tenkan_sen, basis_max)

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


