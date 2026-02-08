//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: DOCN_5Min_1T00_45ad0c97 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOCN_5Min_1T00_45ad0c97", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOCN_5Min_45ad0c97(ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( tema <= 49.1119 )
		if( ema2 <= 32.3646 )
			if( ema13 <= 0.152639 )
				if( ema12 <= -0.01324 )
					if( ema13 <= -0.275972 )
						if( ema13 <= -1.04809 )
							ret := 0.780488 // buy
						if( ema13 > -1.04809 )
							ret := -0.202312
					if( ema13 > -0.275972 )
						if( ema12 <= -0.063846 )
							ret := 0.249868
						if( ema12 > -0.063846 )
							ret := 0.086361
				if( ema12 > -0.01324 )
					if( ema1 <= 31.8311 )
						if( ema2 <= 31.6897 )
							ret := -0.097338
						if( ema2 > 31.6897 )
							ret := -0.828125 // sell
					if( ema1 > 31.8311 )
						if( ema13 <= 0.037861 )
							ret := 0.514286
						if( ema13 > 0.037861 )
							ret := 0.149390
			if( ema13 > 0.152639 )
				if( tema <= 22.3314 )
					if( tema <= 20.8977 )
						ret := 0.714286 // buy
					if( tema > 20.8977 )
						if( ema13 <= 0.162674 )
							ret := 0.375000
						if( ema13 > 0.162674 )
							ret := -0.718310 // sell
				if( tema > 22.3314 )
					if( ema2 <= 32.3176 )
						if( ema1 <= 23.9564 )
							ret := 0.653333
						if( ema1 > 23.9564 )
							ret := 0.213183
					if( ema2 > 32.3176 )
						if( ema13 <= 0.274793 )
							ret := -0.870968 // sell
						if( ema13 > 0.274793 )
							ret := 0.250000
		if( ema2 > 32.3646 )
			if( ema12 <= -0.068542 )
				if( tema <= 32.1223 )
					if( tema <= 31.757 )
						ret := 0.333333
					if( tema > 31.757 )
						if( ema3 <= 32.5136 )
							ret := -0.200000
						if( ema3 > 32.5136 )
							ret := -0.811881 // sell
				if( tema > 32.1223 )
					if( ema13 <= -0.731765 )
						if( ema1 <= 36.2048 )
							ret := 0.631579
						if( ema1 > 36.2048 )
							ret := -0.481884
					if( ema13 > -0.731765 )
						if( ema2 <= 48.2887 )
							ret := 0.081136
						if( ema2 > 48.2887 )
							ret := 0.406780
			if( ema12 > -0.068542 )
				if( ema13 <= 0.381577 )
					if( ema3 <= 44.9333 )
						if( ema3 <= 32.3249 )
							ret := -0.592105
						if( ema3 > 32.3249 )
							ret := -0.033615
					if( ema3 > 44.9333 )
						if( ema1 <= 45.6892 )
							ret := 0.706522 // buy
						if( ema1 > 45.6892 )
							ret := 0.032006
				if( ema13 > 0.381577 )
					if( ema13 <= 0.552305 )
						if( ema12 <= 0.134813 )
							ret := 0.928571 // buy
						if( ema12 > 0.134813 )
							ret := -0.324004
					if( ema13 > 0.552305 )
						if( tema <= 44.9688 )
							ret := 0.145188
						if( tema > 44.9688 )
							ret := -0.876923 // sell
	if( tema > 49.1119 )
		if( ema2 <= 49.5293 )
			if( ema3 <= 49.0989 )
				if( ema12 <= 0.119187 )
					if( ema3 <= 48.9603 )
						ret := 1.000000 // buy
					if( ema3 > 48.9603 )
						if( ema12 <= 0.090735 )
							ret := 0.812500 // buy
						if( ema12 > 0.090735 )
							ret := 0.416667
				if( ema12 > 0.119187 )
					if( ema3 <= 48.7581 )
						if( ema12 <= 0.263429 )
							ret := -0.733333 // sell
						if( ema12 > 0.263429 )
							ret := -0.928571 // sell
					if( ema3 > 48.7581 )
						if( ema1 <= 49.324 )
							ret := 0.000000
						if( ema1 > 49.324 )
							ret := -1.000000 // sell
			if( ema3 > 49.0989 )
				if( ema1 <= 49.3493 )
					if( ema2 <= 49.1586 )
						if( ema3 <= 49.1337 )
							ret := -0.714286 // sell
						if( ema3 > 49.1337 )
							ret := -1.000000 // sell
					if( ema2 > 49.1586 )
						if( ema3 <= 49.2604 )
							ret := -0.236842
						if( ema3 > 49.2604 )
							ret := -0.952381 // sell
				if( ema1 > 49.3493 )
					if( tema <= 49.4807 )
						ret := -1.000000 // sell
					if( tema > 49.4807 )
						if( ema3 <= 49.282 )
							ret := -0.818182 // sell
						if( ema3 > 49.282 )
							ret := -1.000000 // sell
		if( ema2 > 49.5293 )
			if( ema3 <= 50.492 )
				if( tema <= 49.6402 )
					if( ema1 <= 49.5414 )
						ret := 0.111111
					if( ema1 > 49.5414 )
						if( ema12 <= -0.114127 )
							ret := 0.388889
						if( ema12 > -0.114127 )
							ret := 1.000000 // buy
				if( tema > 49.6402 )
					if( ema12 <= -0.011681 )
						if( ema3 <= 49.9951 )
							ret := -0.866667 // sell
						if( ema3 > 49.9951 )
							ret := -0.333333
					if( ema12 > -0.011681 )
						if( ema3 <= 50.1228 )
							ret := -0.092593
						if( ema3 > 50.1228 )
							ret := 0.727273 // buy
			if( ema3 > 50.492 )
				if( ema2 <= 50.8916 )
					ret := -0.600000
				if( ema2 > 50.8916 )
					ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

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
float op_operation = decision_tree_0_DOCN_5Min_45ad0c97(ema12, ema3, ema13, tema, ema1, ema2)

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


