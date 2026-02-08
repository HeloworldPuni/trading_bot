//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: SNAP_1Hour_1WAV_e12afa2d Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Hour_1WAV_e12afa2d", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Hour_e12afa2d(esa, d_tci, tci, ci_wt2, wt2, d, ci, ap)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( d <= 0.218646 )
		if( ci <= 7.97751 )
			if( ci_wt2 <= 20.9967 )
				if( esa <= 9.2209 )
					if( tci <= -35.6183 )
						if( tci <= -44.1966 )
							ret := 0.070833
						if( tci > -44.1966 )
							ret := -0.451613
					if( tci > -35.6183 )
						if( ci_wt2 <= 2.31642 )
							ret := 0.237288
						if( ci_wt2 > 2.31642 )
							ret := 0.708333 // buy
				if( esa > 9.2209 )
					if( d_tci <= -46.4669 )
						if( ci_wt2 <= -83.7226 )
							ret := -0.224490
						if( ci_wt2 > -83.7226 )
							ret := 0.473171
					if( d_tci > -46.4669 )
						if( wt2 <= -31.4951 )
							ret := 0.138104
						if( wt2 > -31.4951 )
							ret := 0.022064
			if( ci_wt2 > 20.9967 )
				if( tci <= -40.652 )
					if( ap <= 17.2497 )
						if( tci <= -49.051 )
							ret := -0.050296
						if( tci > -49.051 )
							ret := -0.462745
					if( ap > 17.2497 )
						if( ci <= -1.54727 )
							ret := 0.851852 // buy
						if( ci > -1.54727 )
							ret := -0.333333
				if( tci > -40.652 )
					if( esa <= 10.6573 )
						if( wt2 <= -37.1988 )
							ret := 0.775862 // buy
						if( wt2 > -37.1988 )
							ret := 0.319149
					if( esa > 10.6573 )
						if( ci <= -17.7097 )
							ret := -1.000000 // sell
						if( ci > -17.7097 )
							ret := -0.114094
		if( ci > 7.97751 )
			if( esa <= 10.8482 )
				if( ap <= 9.8673 )
					if( tci <= 37.6997 )
						if( ci_wt2 <= -16.0538 )
							ret := -0.772727 // sell
						if( ci_wt2 > -16.0538 )
							ret := 0.060357
					if( tci > 37.6997 )
						if( ci_wt2 <= -11.6324 )
							ret := 0.290476
						if( ci_wt2 > -11.6324 )
							ret := -0.261290
				if( ap > 9.8673 )
					if( ci_wt2 <= 50.1495 )
						if( ci_wt2 <= 46.5459 )
							ret := 0.096305
						if( ci_wt2 > 46.5459 )
							ret := -0.649123
					if( ci_wt2 > 50.1495 )
						if( ci <= 108.454 )
							ret := 0.379705
						if( ci > 108.454 )
							ret := 0.044944
			if( esa > 10.8482 )
				if( tci <= 2.09963 )
					if( ci <= 10.334 )
						if( wt2 <= -47.2648 )
							ret := -1.000000 // sell
						if( wt2 > -47.2648 )
							ret := -0.500000
					if( ci > 10.334 )
						if( d <= 0.174717 )
							ret := -0.243619
						if( d > 0.174717 )
							ret := -0.486486
				if( tci > 2.09963 )
					if( d_tci <= -37.1568 )
						if( d_tci <= -48.2772 )
							ret := 0.034702
						if( d_tci > -48.2772 )
							ret := -0.253812
					if( d_tci > -37.1568 )
						if( d <= 0.062335 )
							ret := -0.123762
						if( d > 0.062335 )
							ret := 0.152416
	if( d > 0.218646 )
		if( wt2 <= -53.6308 )
			if( esa <= 18.2195 )
				if( tci <= -71.9363 )
					if( esa <= 15.3443 )
						if( d <= 0.420452 )
							ret := 0.750000 // buy
						if( d > 0.420452 )
							ret := -0.100000
					if( esa > 15.3443 )
						ret := -0.533333
				if( tci > -71.9363 )
					if( ci_wt2 <= -17.8147 )
						if( ap <= 12.727 )
							ret := 0.600000
						if( ap > 12.727 )
							ret := -0.322581
					if( ci_wt2 > -17.8147 )
						if( ap <= 10.2646 )
							ret := 0.000000
						if( ap > 10.2646 )
							ret := -0.695238
			if( esa > 18.2195 )
				if( ci_wt2 <= 14.6067 )
					if( tci <= -64.7086 )
						if( ci <= -119.064 )
							ret := 0.666667
						if( ci > -119.064 )
							ret := -0.057471
					if( tci > -64.7086 )
						if( tci <= -60.9924 )
							ret := 0.728571 // buy
						if( tci > -60.9924 )
							ret := 0.422907
				if( ci_wt2 > 14.6067 )
					if( ci <= 54.0586 )
						if( esa <= 36.9082 )
							ret := -0.360825
						if( esa > 36.9082 )
							ret := 0.028213
					if( ci > 54.0586 )
						if( tci <= -44.1259 )
							ret := 1.000000 // buy
						if( tci > -44.1259 )
							ret := 0.400000
		if( wt2 > -53.6308 )
			if( ci <= -36.1476 )
				if( ci <= -103.64 )
					if( tci <= -42.3336 )
						if( esa <= 41.8631 )
							ret := 0.614379
						if( esa > 41.8631 )
							ret := -0.100775
					if( tci > -42.3336 )
						if( tci <= 35.3542 )
							ret := -0.056761
						if( tci > 35.3542 )
							ret := -1.000000 // sell
				if( ci > -103.64 )
					if( d <= 0.337047 )
						if( ci_wt2 <= -116.775 )
							ret := 0.509091
						if( ci_wt2 > -116.775 )
							ret := -0.058896
					if( d > 0.337047 )
						if( ap <= 43.6908 )
							ret := -0.413831
						if( ap > 43.6908 )
							ret := -0.189218
			if( ci > -36.1476 )
				if( ci_wt2 <= -18.5187 )
					if( esa <= 70.9483 )
						if( d_tci <= -22.3149 )
							ret := 0.127747
						if( d_tci > -22.3149 )
							ret := 0.475676
					if( esa > 70.9483 )
						if( ci <= -33.4546 )
							ret := 1.000000 // buy
						if( ci > -33.4546 )
							ret := -0.413043
				if( ci_wt2 > -18.5187 )
					if( wt2 <= 45.573 )
						if( tci <= 44.7791 )
							ret := -0.046555
						if( tci > 44.7791 )
							ret := 0.419708
					if( wt2 > 45.573 )
						if( tci <= 48.6126 )
							ret := -0.735294 // sell
						if( tci > 48.6126 )
							ret := -0.156636
	
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
float op_operation = decision_tree_0_SNAP_1Hour_e12afa2d(esa, d_tci, tci, ci_wt2, wt2, d, ci, ap)

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


