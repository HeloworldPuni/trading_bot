//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: ETHUSDT_1Hour_1WAV_bc9a4cc6 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ETHUSDT_1Hour_1WAV_bc9a4cc6", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ETHUSDT_1Hour_bc9a4cc6(d, esa, d_tci, ci_wt2, wt2, ci, ap, tci)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( d_tci <= -21.5443 )
		if( esa <= 1817.55 )
			if( d <= 1.69894 )
				if( ci <= 122.489 )
					if( d <= 1.10601 )
						if( ap <= 282.559 )
							ret := 0.014493
						if( ap > 282.559 )
							ret := 0.444444
					if( d > 1.10601 )
						if( ap <= 385.34 )
							ret := -0.213095
						if( ap > 385.34 )
							ret := 0.180952
				if( ci > 122.489 )
					if( ap <= 244.895 )
						if( ci_wt2 <= 111.505 )
							ret := 0.727273 // buy
						if( ci_wt2 > 111.505 )
							ret := 0.277778
					if( ap > 244.895 )
						if( esa <= 272.958 )
							ret := -0.882353 // sell
						if( esa > 272.958 )
							ret := 0.419355
			if( d > 1.69894 )
				if( ci_wt2 <= -15.5056 )
					if( ci_wt2 <= -46.1398 )
						if( esa <= 155.011 )
							ret := -0.727273 // sell
						if( esa > 155.011 )
							ret := 0.179641
					if( ci_wt2 > -46.1398 )
						if( d <= 3.56993 )
							ret := 0.183983
						if( d > 3.56993 )
							ret := 0.457328
				if( ci_wt2 > -15.5056 )
					if( ci_wt2 <= 52.3418 )
						if( d <= 2.95328 )
							ret := 0.272938
						if( d > 2.95328 )
							ret := 0.012279
					if( ci_wt2 > 52.3418 )
						if( ap <= 224.406 )
							ret := -0.256757
						if( ap > 224.406 )
							ret := 0.304448
		if( esa > 1817.55 )
			if( ap <= 4419.82 )
				if( ci <= 183.312 )
					if( d <= 15.6351 )
						if( esa <= 2238.22 )
							ret := -0.071429
						if( esa > 2238.22 )
							ret := 0.156433
					if( d > 15.6351 )
						if( ap <= 2585.74 )
							ret := 0.076237
						if( ap > 2585.74 )
							ret := -0.175014
				if( ci > 183.312 )
					if( ci_wt2 <= 171.439 )
						if( d_tci <= -49.7342 )
							ret := 0.142857
						if( d_tci > -49.7342 )
							ret := 0.792453 // buy
					if( ci_wt2 > 171.439 )
						ret := -0.111111
			if( ap > 4419.82 )
				if( ap <= 4717.99 )
					if( wt2 <= 52.2987 )
						ret := 0.000000
					if( wt2 > 52.2987 )
						if( esa <= 4443.42 )
							ret := 0.733333 // buy
						if( esa > 4443.42 )
							ret := 1.000000 // buy
				if( ap > 4717.99 )
					ret := 0.000000
	if( d_tci > -21.5443 )
		if( ap <= 1069.3 )
			if( esa <= 711.844 )
				if( esa <= 383.125 )
					if( esa <= 248.741 )
						if( ap <= 230.206 )
							ret := 0.056440
						if( ap > 230.206 )
							ret := -0.237401
					if( esa > 248.741 )
						if( ci_wt2 <= 117.87 )
							ret := 0.148192
						if( ci_wt2 > 117.87 )
							ret := 0.758621 // buy
				if( esa > 383.125 )
					if( d <= 5.66206 )
						if( wt2 <= -24.4341 )
							ret := -0.392308
						if( wt2 > -24.4341 )
							ret := -0.054383
					if( d > 5.66206 )
						if( d_tci <= 2.15804 )
							ret := -0.411765
						if( d_tci > 2.15804 )
							ret := 0.269521
			if( esa > 711.844 )
				if( ci_wt2 <= 21.9237 )
					if( ci <= -141.261 )
						ret := -0.357143
					if( ci > -141.261 )
						if( ap <= 1049.6 )
							ret := 0.810036 // buy
						if( ap > 1049.6 )
							ret := 0.444444
				if( ci_wt2 > 21.9237 )
					if( esa <= 1007.88 )
						if( esa <= 992.564 )
							ret := 0.228916
						if( esa > 992.564 )
							ret := -1.000000 // sell
					if( esa > 1007.88 )
						if( d <= 19.0387 )
							ret := 0.170213
						if( d > 19.0387 )
							ret := 0.923077 // buy
		if( ap > 1069.3 )
			if( ap <= 4324.8 )
				if( esa <= 4321.66 )
					if( esa <= 4285.57 )
						if( ci_wt2 <= 66.9473 )
							ret := -0.060137
						if( ci_wt2 > 66.9473 )
							ret := 0.014456
					if( esa > 4285.57 )
						if( ap <= 4261.97 )
							ret := -0.517241
						if( ap > 4261.97 )
							ret := 0.791667 // buy
				if( esa > 4321.66 )
					if( ap <= 4294.81 )
						if( d_tci <= 109.352 )
							ret := -1.000000 // sell
						if( d_tci > 109.352 )
							ret := -0.769231 // sell
					if( ap > 4294.81 )
						if( d_tci <= 40.2097 )
							ret := -0.785714 // sell
						if( d_tci > 40.2097 )
							ret := -0.500000
			if( ap > 4324.8 )
				if( wt2 <= -24.1753 )
					if( ci <= 4.42347 )
						if( wt2 <= -39.7128 )
							ret := 0.833333 // buy
						if( wt2 > -39.7128 )
							ret := 0.470588
					if( ci > 4.42347 )
						if( esa <= 4641.87 )
							ret := -0.232558
						if( esa > 4641.87 )
							ret := 1.000000 // buy
				if( wt2 > -24.1753 )
					if( d_tci <= -2.12867 )
						if( esa <= 4703.93 )
							ret := -0.045455
						if( esa > 4703.93 )
							ret := -0.716981 // sell
					if( d_tci > -2.12867 )
						if( ap <= 4479.49 )
							ret := -0.770270 // sell
						if( ap > 4479.49 )
							ret := -0.300000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_ETHUSDT_1Hour_bc9a4cc6(d, esa, d_tci, ci_wt2, wt2, ci, ap, tci)

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


