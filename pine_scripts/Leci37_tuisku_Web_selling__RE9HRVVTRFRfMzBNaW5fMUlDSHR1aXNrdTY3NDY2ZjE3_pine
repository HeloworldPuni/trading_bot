//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ichimoku_Cloud
// ID_model: DOGEUSDT_30Min_1ICH_67466f17 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOGEUSDT_30Min_1ICH_67466f17", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOGEUSDT_30Min_67466f17(senkou_span_a, basis_minus, chinkou_span, senkou_span_a_displaced, kinjun_sen, senkou_span_b_displaced, cross_up_tenkan_kinjunInt, senkou_span_b, cross_dn_tenkan_kinjunInt, tenkan_sen, basis_max)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.5,min_samples_leaf=4, random_state=843828734)
	if( senkou_span_a <= 0.078492 )
		if( chinkou_span <= 0.0768 )
			if( tenkan_sen <= 0.07072 )
				if( basis_max <= 0.000184 )
					if( basis_minus <= 0.001393 )
						if( senkou_span_b_displaced <= 0.063255 )
							if( chinkou_span <= 0.063198 )
								ret := 0.018606
							if( chinkou_span > 0.063198 )
								ret := 0.366760
						if( senkou_span_b_displaced > 0.063255 )
							if( tenkan_sen <= 0.070451 )
								ret := -0.041593
							if( tenkan_sen > 0.070451 )
								ret := 0.318548
					if( basis_minus > 0.001393 )
						if( chinkou_span <= 0.06949 )
							if( tenkan_sen <= 0.058617 )
								ret := -0.004024
							if( tenkan_sen > 0.058617 )
								ret := -0.625000
						if( chinkou_span > 0.06949 )
							if( basis_minus <= 0.002232 )
								ret := -0.219512
							if( basis_minus > 0.002232 )
								ret := 0.970149 // buy
				if( basis_max > 0.000184 )
					if( senkou_span_b_displaced <= 0.009687 )
						ret := 1.000000 // buy
					if( senkou_span_b_displaced > 0.009687 )
						if( senkou_span_a <= 0.070437 )
							if( senkou_span_b_displaced <= 0.010248 )
								ret := -0.935484 // sell
							if( senkou_span_b_displaced > 0.010248 )
								ret := 0.111960
						if( senkou_span_a > 0.070437 )
							if( senkou_span_a_displaced <= 0.072824 )
								ret := 0.618090
							if( senkou_span_a_displaced > 0.072824 )
								ret := 0.048544
			if( tenkan_sen > 0.07072 )
				if( tenkan_sen <= 0.07564 )
					if( chinkou_span <= 0.072159 )
						if( senkou_span_a_displaced <= 0.067724 )
							if( chinkou_span <= 0.070953 )
								ret := -0.466667
							if( chinkou_span > 0.070953 )
								ret := 0.714286 // buy
						if( senkou_span_a_displaced > 0.067724 )
							if( chinkou_span <= 0.069794 )
								ret := -0.614108
							if( chinkou_span > 0.069794 )
								ret := -0.295070
					if( chinkou_span > 0.072159 )
						if( senkou_span_a <= 0.073636 )
							if( basis_max <= 0.000491 )
								ret := 0.189349
							if( basis_max > 0.000491 )
								ret := 0.830769 // buy
						if( senkou_span_a > 0.073636 )
							if( senkou_span_b_displaced <= 0.079465 )
								ret := -0.026017
							if( senkou_span_b_displaced > 0.079465 )
								ret := 0.620000
				if( tenkan_sen > 0.07564 )
					if( basis_max <= 0.000306 )
						if( senkou_span_b <= 0.075634 )
							if( kinjun_sen <= 0.076434 )
								ret := -0.306189
							if( kinjun_sen > 0.076434 )
								ret := 0.652174
						if( senkou_span_b > 0.075634 )
							if( chinkou_span <= 0.07538 )
								ret := -0.593846
							if( chinkou_span > 0.07538 )
								ret := -0.262222
					if( basis_max > 0.000306 )
						if( senkou_span_a_displaced <= 0.075835 )
							if( senkou_span_b_displaced <= 0.069599 )
								ret := -0.250000
							if( senkou_span_b_displaced > 0.069599 )
								ret := 1.000000 // buy
						if( senkou_span_a_displaced > 0.075835 )
							if( senkou_span_b_displaced <= 0.075971 )
								ret := -0.875000 // sell
							if( senkou_span_b_displaced > 0.075971 )
								ret := 0.200000
		if( chinkou_span > 0.0768 )
			if( tenkan_sen <= 0.074846 )
				if( basis_minus <= 0.000739 )
					if( senkou_span_a <= 0.073232 )
						if( senkou_span_a <= 0.071018 )
							if( senkou_span_a_displaced <= 0.072635 )
								ret := 1.000000 // buy
							if( senkou_span_a_displaced > 0.072635 )
								ret := 0.500000
						if( senkou_span_a > 0.071018 )
							ret := 1.000000 // buy
					if( senkou_span_a > 0.073232 )
						if( senkou_span_b_displaced <= 0.072431 )
							if( senkou_span_b_displaced <= 0.072075 )
								ret := -0.111111
							if( senkou_span_b_displaced > 0.072075 )
								ret := 0.454545
						if( senkou_span_b_displaced > 0.072431 )
							if( senkou_span_a_displaced <= 0.074006 )
								ret := 0.962963 // buy
							if( senkou_span_a_displaced > 0.074006 )
								ret := 0.757895 // buy
				if( basis_minus > 0.000739 )
					if( senkou_span_b_displaced <= 0.061985 )
						if( basis_max <= 0.000282 )
							if( basis_minus <= 0.002214 )
								ret := 1.000000 // buy
							if( basis_minus > 0.002214 )
								ret := -0.400000
						if( basis_max > 0.000282 )
							if( senkou_span_a <= 0.071462 )
								ret := -1.000000 // sell
							if( senkou_span_a > 0.071462 )
								ret := -0.600000
					if( senkou_span_b_displaced > 0.061985 )
						if( senkou_span_a_displaced <= 0.067341 )
							if( basis_minus <= 0.002286 )
								ret := 0.500000
							if( basis_minus > 0.002286 )
								ret := 0.978261 // buy
						if( senkou_span_a_displaced > 0.067341 )
							if( kinjun_sen <= 0.073875 )
								ret := 0.112903
							if( kinjun_sen > 0.073875 )
								ret := 0.742424 // buy
			if( tenkan_sen > 0.074846 )
				if( senkou_span_b_displaced <= 0.071495 )
					if( basis_minus <= 0.000403 )
						ret := 1.000000 // buy
					if( basis_minus > 0.000403 )
						if( kinjun_sen <= 0.073283 )
							ret := 1.000000 // buy
						if( kinjun_sen > 0.073283 )
							if( senkou_span_b <= 0.07472 )
								ret := -0.878049 // sell
							if( senkou_span_b > 0.07472 )
								ret := 0.500000
				if( senkou_span_b_displaced > 0.071495 )
					if( chinkou_span <= 0.078974 )
						if( basis_max <= 0.001087 )
							if( senkou_span_a_displaced <= 0.074629 )
								ret := 0.512195
							if( senkou_span_a_displaced > 0.074629 )
								ret := 0.081409
						if( basis_max > 0.001087 )
							if( chinkou_span <= 0.077452 )
								ret := 0.750000 // buy
							if( chinkou_span > 0.077452 )
								ret := 0.960000 // buy
					if( chinkou_span > 0.078974 )
						if( tenkan_sen <= 0.076699 )
							if( senkou_span_a <= 0.075356 )
								ret := -0.230769
							if( senkou_span_a > 0.075356 )
								ret := 0.764706 // buy
						if( tenkan_sen > 0.076699 )
							if( kinjun_sen <= 0.07654 )
								ret := -0.107143
							if( kinjun_sen > 0.07654 )
								ret := 0.487616
	if( senkou_span_a > 0.078492 )
		if( chinkou_span <= 0.080007 )
			if( tenkan_sen <= 0.080483 )
				if( senkou_span_b <= 0.077675 )
					if( basis_max <= -0.000231 )
						if( senkou_span_b_displaced <= 0.074054 )
							if( senkou_span_b <= 0.07704 )
								ret := -1.000000 // sell
							if( senkou_span_b > 0.07704 )
								ret := -0.600000
						if( senkou_span_b_displaced > 0.074054 )
							if( senkou_span_a <= 0.079282 )
								ret := 0.875000 // buy
							if( senkou_span_a > 0.079282 )
								ret := 0.333333
					if( basis_max > -0.000231 )
						if( senkou_span_a <= 0.079637 )
							ret := 1.000000 // buy
						if( senkou_span_a > 0.079637 )
							ret := 0.571429
				if( senkou_span_b > 0.077675 )
					if( chinkou_span <= 0.077947 )
						if( senkou_span_a_displaced <= 0.078222 )
							if( kinjun_sen <= 0.079573 )
								ret := -0.450000
							if( kinjun_sen > 0.079573 )
								ret := 0.708333 // buy
						if( senkou_span_a_displaced > 0.078222 )
							if( basis_max <= 4.5e-05 )
								ret := -0.349515
							if( basis_max > 4.5e-05 )
								ret := -0.690236
					if( chinkou_span > 0.077947 )
						if( senkou_span_a_displaced <= 0.077563 )
							if( chinkou_span <= 0.078456 )
								ret := -0.181818
							if( chinkou_span > 0.078456 )
								ret := -0.775281 // sell
						if( senkou_span_a_displaced > 0.077563 )
							if( kinjun_sen <= 0.078832 )
								ret := 0.052023
							if( kinjun_sen > 0.078832 )
								ret := -0.153538
			if( tenkan_sen > 0.080483 )
				if( senkou_span_a <= 0.098856 )
					if( basis_minus <= -0.01015 )
						ret := 1.000000 // buy
					if( basis_minus > -0.01015 )
						if( tenkan_sen <= 0.085298 )
							if( basis_minus <= -0.002132 )
								ret := 0.191489
							if( basis_minus > -0.002132 )
								ret := -0.607595
						if( tenkan_sen > 0.085298 )
							if( senkou_span_b <= 0.090225 )
								ret := -0.750000 // sell
							if( senkou_span_b > 0.090225 )
								ret := -0.971831 // sell
				if( senkou_span_a > 0.098856 )
					ret := 1.000000 // buy
		if( chinkou_span > 0.080007 )
			if( tenkan_sen <= 0.083101 )
				if( senkou_span_b_displaced <= 0.073995 )
					if( senkou_span_a <= 0.080444 )
						ret := -0.750000 // sell
					if( senkou_span_a > 0.080444 )
						ret := -1.000000 // sell
				if( senkou_span_b_displaced > 0.073995 )
					if( senkou_span_a_displaced <= 0.079789 )
						if( tenkan_sen <= 0.081909 )
							if( basis_minus <= 0.00217 )
								ret := 0.300188
							if( basis_minus > 0.00217 )
								ret := -0.722222 // sell
						if( tenkan_sen > 0.081909 )
							if( chinkou_span <= 0.081538 )
								ret := 0.555556
							if( chinkou_span > 0.081538 )
								ret := 0.970000 // buy
					if( senkou_span_a_displaced > 0.079789 )
						if( chinkou_span <= 0.08363 )
							if( tenkan_sen <= 0.080848 )
								ret := 0.235000
							if( tenkan_sen > 0.080848 )
								ret := -0.041757
						if( chinkou_span > 0.08363 )
							if( chinkou_span <= 0.091814 )
								ret := 0.542929
							if( chinkou_span > 0.091814 )
								ret := -0.904762 // sell
			if( tenkan_sen > 0.083101 )
				if( basis_max <= 0.037229 )
					if( basis_minus <= 0.02134 )
						if( basis_max <= -0.013131 )
							if( senkou_span_b <= 0.502773 )
								ret := -0.467742
							if( senkou_span_b > 0.502773 )
								ret := -0.919355 // sell
						if( basis_max > -0.013131 )
							if( chinkou_span <= 0.084269 )
								ret := -0.405769
							if( chinkou_span > 0.084269 )
								ret := -0.009787
					if( basis_minus > 0.02134 )
						if( basis_minus <= 0.041697 )
							if( senkou_span_a_displaced <= 0.317014 )
								ret := 0.654709
							if( senkou_span_a_displaced > 0.317014 )
								ret := 0.173171
						if( basis_minus > 0.041697 )
							if( kinjun_sen <= 0.595879 )
								ret := 0.073620
							if( kinjun_sen > 0.595879 )
								ret := -0.453608
				if( basis_max > 0.037229 )
					ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_DOGEUSDT_30Min_67466f17(senkou_span_a, basis_minus, chinkou_span, senkou_span_a_displaced, kinjun_sen, senkou_span_b_displaced, cross_up_tenkan_kinjunInt, senkou_span_b, cross_dn_tenkan_kinjunInt, tenkan_sen, basis_max)

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


