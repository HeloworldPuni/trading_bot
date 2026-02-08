//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: ADSK_1Min_1WAV_4fcbe029 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ADSK_1Min_1WAV_4fcbe029", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ADSK_1Min_4fcbe029(tci, ci, d_tci, esa, d, ci_wt2, wt2, ap)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ci_wt2 <= -24.5331 )
		if( ci <= -118.934 )
			if( ci <= -193.155 )
				if( ci <= -233.498 )
					if( ci <= -264.171 )
						if( wt2 <= -27.0821 )
							ret := 0.090909
						if( wt2 > -27.0821 )
							ret := 1.000000 // buy
					if( ci > -264.171 )
						if( ci <= -247.196 )
							ret := -0.866667 // sell
						if( ci > -247.196 )
							ret := -0.071429
				if( ci > -233.498 )
					if( tci <= -0.024322 )
						if( d <= 0.15091 )
							ret := 0.603774
						if( d > 0.15091 )
							ret := 0.958333 // buy
					if( tci > -0.024322 )
						ret := 0.333333
			if( ci > -193.155 )
				if( esa <= 246.322 )
					if( ci_wt2 <= -143.375 )
						if( esa <= 212.689 )
							ret := -0.644444
						if( esa > 212.689 )
							ret := 0.129979
					if( ci_wt2 > -143.375 )
						if( ap <= 207.557 )
							ret := -0.212766
						if( ap > 207.557 )
							ret := 0.332120
				if( esa > 246.322 )
					if( wt2 <= 26.7814 )
						if( wt2 <= -51.7871 )
							ret := 0.538462
						if( wt2 > -51.7871 )
							ret := -0.046460
					if( wt2 > 26.7814 )
						if( tci <= 25.2558 )
							ret := 0.603774
						if( tci > 25.2558 )
							ret := 0.153846
		if( ci > -118.934 )
			if( esa <= 254.104 )
				if( d <= 0.702432 )
					if( wt2 <= 59.192 )
						if( ap <= 237.969 )
							ret := 0.039291
						if( ap > 237.969 )
							ret := 0.114492
					if( wt2 > 59.192 )
						if( ap <= 242.483 )
							ret := 0.049020
						if( ap > 242.483 )
							ret := -0.370229
				if( d > 0.702432 )
					if( wt2 <= 57.0113 )
						if( wt2 <= 51.784 )
							ret := 0.413502
						if( wt2 > 51.784 )
							ret := -0.666667
					if( wt2 > 57.0113 )
						if( ci <= 32.6881 )
							ret := 0.941176 // buy
						if( ci > 32.6881 )
							ret := 0.421053
			if( esa > 254.104 )
				if( ci_wt2 <= -102.859 )
					if( wt2 <= -6.76058 )
						if( ci <= -115.317 )
							ret := -0.692308
						if( ci > -115.317 )
							ret := -1.000000 // sell
					if( wt2 > -6.76058 )
						if( ci <= -99.0838 )
							ret := 0.074286
						if( ci > -99.0838 )
							ret := 0.334254
				if( ci_wt2 > -102.859 )
					if( ci <= 17.8688 )
						if( esa <= 270.367 )
							ret := -0.085081
						if( esa > 270.367 )
							ret := 0.111708
					if( ci > 17.8688 )
						if( ap <= 256.306 )
							ret := 0.169811
						if( ap > 256.306 )
							ret := -0.455285
	if( ci_wt2 > -24.5331 )
		if( ci_wt2 <= 104.345 )
			if( esa <= 242.664 )
				if( d_tci <= 67.4539 )
					if( ap <= 238.555 )
						if( esa <= 215.281 )
							ret := 0.061681
						if( esa > 215.281 )
							ret := -0.049336
					if( ap > 238.555 )
						if( d <= 0.246097 )
							ret := 0.009375
						if( d > 0.246097 )
							ret := 0.239691
				if( d_tci > 67.4539 )
					if( ci_wt2 <= 46.4028 )
						if( ap <= 241.643 )
							ret := 0.609272
						if( ap > 241.643 )
							ret := -0.487805
					if( ci_wt2 > 46.4028 )
						if( esa <= 208.971 )
							ret := -0.461538
						if( esa > 208.971 )
							ret := -0.909091 // sell
			if( esa > 242.664 )
				if( d <= 0.189048 )
					if( esa <= 265.709 )
						if( tci <= -34.112 )
							ret := -0.219574
						if( tci > -34.112 )
							ret := -0.044282
					if( esa > 265.709 )
						if( ci <= 122.885 )
							ret := 0.098186
						if( ci > 122.885 )
							ret := 0.626667
				if( d > 0.189048 )
					if( ap <= 269.314 )
						if( esa <= 246.967 )
							ret := -0.180029
						if( esa > 246.967 )
							ret := -0.037235
					if( ap > 269.314 )
						if( ci <= 91.1877 )
							ret := -0.364415
						if( ci > 91.1877 )
							ret := 0.152381
		if( ci_wt2 > 104.345 )
			if( ci <= 38.3061 )
				if( d <= 1.44107 )
					ret := -1.000000 // sell
				if( d > 1.44107 )
					ret := -0.900000 // sell
			if( ci > 38.3061 )
				if( esa <= 266.62 )
					if( ci <= 231.743 )
						if( ci_wt2 <= 108.389 )
							ret := -0.374150
						if( ci_wt2 > 108.389 )
							ret := -0.130202
					if( ci > 231.743 )
						if( tci <= 51.5617 )
							ret := -0.802632 // sell
						if( tci > 51.5617 )
							ret := 0.363636
				if( esa > 266.62 )
					if( ci <= 98.1513 )
						if( wt2 <= -19.8736 )
							ret := 0.226190
						if( wt2 > -19.8736 )
							ret := 0.870968 // buy
					if( ci > 98.1513 )
						if( ci <= 110.184 )
							ret := -0.647059
						if( ci > 110.184 )
							ret := 0.064516
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Wave_Trend_Calculation 
//@version=5
//indicator "WaveTrend [LazyBear]", shorttitle="WT_LB", overlay=false)

n1 = input.int(10, title="Channel Length")
n2 = input.int(21, title="Average Length")
obLevel1 = input.float(60, title="Over Bought Level 1")
obLevel2 = input.float(53, title="Over Bought Level 2")
osLevel1 = input.float(-60, title="Over Sold Level 1")
osLevel2 = input.float(-53, title="Over Sold Level 2")

ap = hlc3
esa = ta.ema(ap, n1)
d = ta.ema(math.abs(ap - esa), n1)
ci = (ap - esa) / (0.015 * d)
tci = ta.ema(ci, n2)

wt1 = tci
wt2 = ta.sma(wt1, 4)

d_tci = d-tci
ci_wt2 = ci - wt2

plot(0, color=color.gray)
plot(obLevel1, color=color.red)
plot(osLevel1, color=color.green)
plot(obLevel2, color=color.red, linewidth=2, style=plot.style_line, title="OB Level 2 (Dashed)", color=color.red)
plot(osLevel2, color=color.green, linewidth=2, style=plot.style_line, title="OS Level 2 (Dashed)", color=color.green)

plot(wt1, color=color.green, title="WT1")
plot(wt2, color=color.red, title="WT2", style=plot.style_line, linewidth=1)
plot(wt1 - wt2, color=color.new(color.blue, 80), title="WT1-WT2", style=plot.style_area)

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
float op_operation = decision_tree_0_ADSK_1Min_4fcbe029(tci, ci, d_tci, esa, d, ci_wt2, wt2, ap)

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


