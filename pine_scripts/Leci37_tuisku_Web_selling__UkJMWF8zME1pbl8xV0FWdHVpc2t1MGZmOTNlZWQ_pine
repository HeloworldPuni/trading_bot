//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: RBLX_30Min_1WAV_0ff93eed Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RBLX_30Min_1WAV_0ff93eed", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RBLX_30Min_0ff93eed(ap, d_tci, ci, ci_wt2, tci, d, wt2, esa)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ap <= 40.6778 )
		if( ci_wt2 <= 82.7668 )
			if( d <= 1.51266 )
				if( tci <= -69.7852 )
					if( ap <= 40.3723 )
						if( d <= 1.2961 )
							ret := 0.524793
						if( d > 1.2961 )
							ret := -0.666667
					if( ap > 40.3723 )
						ret := -0.714286 // sell
				if( tci > -69.7852 )
					if( tci <= 12.7713 )
						if( ap <= 24.8224 )
							ret := 0.551724
						if( ap > 24.8224 )
							ret := 0.037411
					if( tci > 12.7713 )
						if( d_tci <= -55.7312 )
							ret := -0.002927
						if( d_tci > -55.7312 )
							ret := 0.161675
			if( d > 1.51266 )
				if( d_tci <= 80.1125 )
					if( ap <= 33.2019 )
						if( ap <= 28.4183 )
							ret := -0.375000
						if( ap > 28.4183 )
							ret := -0.924528 // sell
					if( ap > 33.2019 )
						ret := 0.100000
				if( d_tci > 80.1125 )
					ret := 0.636364
		if( ci_wt2 > 82.7668 )
			if( ap <= 39.575 )
				if( d_tci <= -52.5046 )
					if( wt2 <= 60.5926 )
						if( ci_wt2 <= 89.8714 )
							ret := 0.037037
						if( ci_wt2 > 89.8714 )
							ret := -0.637168
					if( wt2 > 60.5926 )
						ret := 0.538462
				if( d_tci > -52.5046 )
					if( ci <= 48.3392 )
						if( esa <= 36.2367 )
							ret := 0.691358
						if( esa > 36.2367 )
							ret := -0.222222
					if( ci > 48.3392 )
						if( ci_wt2 <= 93.5574 )
							ret := -0.338235
						if( ci_wt2 > 93.5574 )
							ret := 0.077266
			if( ap > 39.575 )
				if( wt2 <= -29.3511 )
					if( ci <= 81.242 )
						if( esa <= 39.8362 )
							ret := -0.615385
						if( esa > 39.8362 )
							ret := 0.150000
					if( ci > 81.242 )
						if( ci <= 127.424 )
							ret := 0.833333 // buy
						if( ci > 127.424 )
							ret := 0.400000
				if( wt2 > -29.3511 )
					if( d <= 0.145671 )
						if( ap <= 40.3904 )
							ret := -0.302326
						if( ap > 40.3904 )
							ret := 0.666667
					if( d > 0.145671 )
						if( ci_wt2 <= 86.2139 )
							ret := 0.076923
						if( ci_wt2 > 86.2139 )
							ret := -0.617486
	if( ap > 40.6778 )
		if( ci <= 48.7867 )
			if( ci <= -186.423 )
				if( ap <= 69.8869 )
					if( tci <= -46.3812 )
						if( ci_wt2 <= -183.925 )
							ret := -0.642857
						if( ci_wt2 > -183.925 )
							ret := 0.000000
					if( tci > -46.3812 )
						if( ci <= -196.671 )
							ret := -0.603448
						if( ci > -196.671 )
							ret := -0.975000 // sell
				if( ap > 69.8869 )
					if( ap <= 77.6021 )
						ret := 0.647059
					if( ap > 77.6021 )
						if( d_tci <= -11.0539 )
							ret := -1.000000 // sell
						if( d_tci > -11.0539 )
							ret := -0.285714
			if( ci > -186.423 )
				if( ap <= 123.203 )
					if( ap <= 117.03 )
						if( d_tci <= -48.5423 )
							ret := -0.227462
						if( d_tci > -48.5423 )
							ret := 0.002330
					if( ap > 117.03 )
						if( tci <= -20.6765 )
							ret := -0.942029 // sell
						if( tci > -20.6765 )
							ret := -0.125000
				if( ap > 123.203 )
					if( ci_wt2 <= -75.2676 )
						if( tci <= 32.0022 )
							ret := -1.000000 // sell
						if( tci > 32.0022 )
							ret := -0.666667
					if( ci_wt2 > -75.2676 )
						if( ci <= 45.836 )
							ret := 0.653409
						if( ci > 45.836 )
							ret := -0.275862
		if( ci > 48.7867 )
			if( wt2 <= -22.2631 )
				if( tci <= -36.9879 )
					if( d <= 0.833201 )
						if( esa <= 47.1776 )
							ret := 0.062500
						if( esa > 47.1776 )
							ret := 0.789474 // buy
					if( d > 0.833201 )
						ret := -0.375000
				if( tci > -36.9879 )
					if( ap <= 102.554 )
						if( wt2 <= -38.416 )
							ret := -0.140187
						if( wt2 > -38.416 )
							ret := -0.492063
					if( ap > 102.554 )
						ret := 0.529412
			if( wt2 > -22.2631 )
				if( d <= 0.247283 )
					if( tci <= 58.9853 )
						if( esa <= 86.7931 )
							ret := 0.036669
						if( esa > 86.7931 )
							ret := -0.607143
					if( tci > 58.9853 )
						if( ci_wt2 <= -3.17049 )
							ret := -0.050000
						if( ci_wt2 > -3.17049 )
							ret := -0.529412
				if( d > 0.247283 )
					if( ci <= 141.202 )
						if( ci_wt2 <= 75.4162 )
							ret := -0.114991
						if( ci_wt2 > 75.4162 )
							ret := -0.377914
					if( ci > 141.202 )
						if( d <= 0.661451 )
							ret := -0.151899
						if( d > 0.661451 )
							ret := 0.382979
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_RBLX_30Min_0ff93eed(ap, d_tci, ci, ci_wt2, tci, d, wt2, esa)

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


