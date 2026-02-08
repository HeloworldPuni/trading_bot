//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: TWLO_5Min_1WAV_bf22e336 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TWLO_5Min_1WAV_bf22e336", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TWLO_5Min_bf22e336(ap, d_tci, ci, ci_wt2, tci, d, wt2, esa)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ci_wt2 <= 77.5444 )
		if( ci_wt2 <= -149.088 )
			if( ap <= 61.1353 )
				if( d <= 0.080154 )
					if( ci <= -143.956 )
						if( ci_wt2 <= -181.464 )
							ret := 0.567568
						if( ci_wt2 > -181.464 )
							ret := -0.049180
					if( ci > -143.956 )
						if( d_tci <= -18.5846 )
							ret := 0.250000
						if( d_tci > -18.5846 )
							ret := -0.687500
				if( d > 0.080154 )
					if( esa <= 61.5315 )
						if( ap <= 49.2001 )
							ret := -0.166667
						if( ap > 49.2001 )
							ret := 0.750594 // buy
					if( esa > 61.5315 )
						if( ap <= 60.8811 )
							ret := -0.800000 // sell
						if( ap > 60.8811 )
							ret := 0.600000
			if( ap > 61.1353 )
				if( ci_wt2 <= -209.188 )
					if( ci_wt2 <= -248.356 )
						if( d_tci <= 10.5079 )
							ret := 0.650000
						if( d_tci > 10.5079 )
							ret := 0.111111
					if( ci_wt2 > -248.356 )
						if( ci_wt2 <= -219.848 )
							ret := 1.000000 // buy
						if( ci_wt2 > -219.848 )
							ret := 0.777778 // buy
				if( ci_wt2 > -209.188 )
					if( d_tci <= -26.0735 )
						if( ci_wt2 <= -165.66 )
							ret := 0.921875 // buy
						if( ci_wt2 > -165.66 )
							ret := -0.260870
					if( d_tci > -26.0735 )
						if( wt2 <= 39.7976 )
							ret := 0.015528
						if( wt2 > 39.7976 )
							ret := -0.823529 // sell
		if( ci_wt2 > -149.088 )
			if( ap <= 57.0204 )
				if( d <= 0.076248 )
					if( ap <= 55.0888 )
						if( ci_wt2 <= 50.8805 )
							ret := -0.037563
						if( ci_wt2 > 50.8805 )
							ret := -0.405594
					if( ap > 55.0888 )
						if( esa <= 55.7221 )
							ret := 0.209581
						if( esa > 55.7221 )
							ret := 0.013333
				if( d > 0.076248 )
					if( ci_wt2 <= -6.21848 )
						if( d_tci <= 55.1723 )
							ret := 0.172526
						if( d_tci > 55.1723 )
							ret := 0.523909
					if( ci_wt2 > -6.21848 )
						if( d_tci <= 74.7398 )
							ret := 0.067393
						if( d_tci > 74.7398 )
							ret := -0.846154 // sell
			if( ap > 57.0204 )
				if( ci_wt2 <= -15.0099 )
					if( wt2 <= 79.532 )
						if( wt2 <= -43.8214 )
							ret := -0.067458
						if( wt2 > -43.8214 )
							ret := 0.062949
					if( wt2 > 79.532 )
						if( ap <= 65.3221 )
							ret := -1.000000 // sell
						if( ap > 65.3221 )
							ret := 0.363636
				if( ci_wt2 > -15.0099 )
					if( d <= 0.56165 )
						if( ci_wt2 <= -12.2058 )
							ret := -0.261941
						if( ci_wt2 > -12.2058 )
							ret := -0.024075
					if( d > 0.56165 )
						if( ap <= 60.11 )
							ret := 0.084337
						if( ap > 60.11 )
							ret := -0.503788
	if( ci_wt2 > 77.5444 )
		if( ci_wt2 <= 216.831 )
			if( ci <= 53.2305 )
				if( ap <= 50.511 )
					if( d <= 0.112306 )
						ret := -1.000000 // sell
					if( d > 0.112306 )
						ret := -0.545455
				if( ap > 50.511 )
					if( wt2 <= -51.2003 )
						if( wt2 <= -66.1116 )
							ret := 0.545455
						if( wt2 > -66.1116 )
							ret := -0.212871
					if( wt2 > -51.2003 )
						if( wt2 <= -45.7132 )
							ret := 0.576389
						if( wt2 > -45.7132 )
							ret := 0.035461
			if( ci > 53.2305 )
				if( d_tci <= 7.23372 )
					if( tci <= -1.06915 )
						if( ci_wt2 <= 163.23 )
							ret := 0.002268
						if( ci_wt2 > 163.23 )
							ret := 0.600000
					if( tci > -1.06915 )
						if( ap <= 56.7432 )
							ret := -0.344765
						if( ap > 56.7432 )
							ret := -0.150848
				if( d_tci > 7.23372 )
					if( ci <= 128.614 )
						if( d <= 0.074017 )
							ret := 0.002646
						if( d > 0.074017 )
							ret := -0.311713
					if( ci > 128.614 )
						if( d <= 0.051142 )
							ret := 0.117647
						if( d > 0.051142 )
							ret := -0.757732 // sell
		if( ci_wt2 > 216.831 )
			if( ci <= 235.102 )
				if( esa <= 62.0962 )
					if( ci <= 221.634 )
						if( d <= 0.10612 )
							ret := -0.666667
						if( d > 0.10612 )
							ret := -1.000000 // sell
					if( ci > 221.634 )
						ret := -0.307692
				if( esa > 62.0962 )
					if( esa <= 64.523 )
						ret := 0.615385
					if( esa > 64.523 )
						ret := -0.421053
			if( ci > 235.102 )
				if( d <= 0.135433 )
					ret := -0.583333
				if( d > 0.135433 )
					if( esa <= 58.5033 )
						ret := -0.777778 // sell
					if( esa > 58.5033 )
						ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_TWLO_5Min_bf22e336(ap, d_tci, ci, ci_wt2, tci, d, wt2, esa)

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


