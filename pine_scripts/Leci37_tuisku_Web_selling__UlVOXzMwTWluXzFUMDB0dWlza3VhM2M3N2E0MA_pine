//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: RUN_30Min_1T00_a3c77a40 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RUN_30Min_1T00_a3c77a40", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RUN_30Min_a3c77a40(ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( tema <= 4.90048 )
		if( tema <= 4.76262 )
			if( ema13 <= -0.137898 )
				if( ema2 <= 4.87696 )
					ret := -0.071429
				if( ema2 > 4.87696 )
					ret := 0.833333 // buy
			if( ema13 > -0.137898 )
				if( ema3 <= 4.83286 )
					if( ema12 <= 0.001954 )
						if( tema <= 4.61924 )
							ret := 0.666667
						if( tema > 4.61924 )
							ret := 0.967391 // buy
					if( ema12 > 0.001954 )
						ret := 0.583333
				if( ema3 > 4.83286 )
					if( ema2 <= 4.82827 )
						ret := 0.090909
					if( ema2 > 4.82827 )
						ret := 1.000000 // buy
		if( tema > 4.76262 )
			if( ema2 <= 4.78163 )
				if( ema13 <= 0.026176 )
					if( ema12 <= 0.013596 )
						ret := -0.875000 // sell
					if( ema12 > 0.013596 )
						ret := -1.000000 // sell
				if( ema13 > 0.026176 )
					ret := 0.500000
			if( ema2 > 4.78163 )
				if( ema13 <= -0.098405 )
					if( ema12 <= -0.061761 )
						ret := -0.277778
					if( ema12 > -0.061761 )
						ret := -0.923077 // sell
				if( ema13 > -0.098405 )
					if( ema1 <= 4.81332 )
						if( ema3 <= 4.82015 )
							ret := 0.523810
						if( ema3 > 4.82015 )
							ret := -0.437500
					if( ema1 > 4.81332 )
						if( tema <= 4.88701 )
							ret := 0.707006 // buy
						if( tema > 4.88701 )
							ret := 0.326531
	if( tema > 4.90048 )
		if( ema3 <= 24.1169 )
			if( tema <= 23.5828 )
				if( ema3 <= 5.38425 )
					if( ema3 <= 5.31737 )
						if( ema12 <= -0.028514 )
							ret := 0.423077
						if( ema12 > -0.028514 )
							ret := 0.005757
					if( ema3 > 5.31737 )
						if( tema <= 5.27463 )
							ret := 0.351064
						if( tema > 5.27463 )
							ret := 0.691176
				if( ema3 > 5.38425 )
					if( ema2 <= 5.59573 )
						if( ema3 <= 5.5751 )
							ret := -0.064870
						if( ema3 > 5.5751 )
							ret := -0.546667
					if( ema2 > 5.59573 )
						if( ema12 <= -0.57046 )
							ret := 0.419540
						if( ema12 > -0.57046 )
							ret := 0.009493
			if( tema > 23.5828 )
				if( tema <= 24.1609 )
					if( ema3 <= 22.9278 )
						if( ema2 <= 22.3965 )
							ret := 0.941176 // buy
						if( ema2 > 22.3965 )
							ret := -0.777778 // sell
					if( ema3 > 22.9278 )
						if( ema13 <= -0.104865 )
							ret := 0.195652
						if( ema13 > -0.104865 )
							ret := 0.634703
				if( tema > 24.1609 )
					if( ema3 <= 23.6662 )
						if( tema <= 24.2591 )
							ret := 0.241379
						if( tema > 24.2591 )
							ret := -0.500000
					if( ema3 > 23.6662 )
						if( ema12 <= 0.148027 )
							ret := -0.425000
						if( ema12 > 0.148027 )
							ret := 0.497238
		if( ema3 > 24.1169 )
			if( ema2 <= 24.4697 )
				if( tema <= 22.5222 )
					ret := 1.000000 // buy
				if( tema > 22.5222 )
					if( ema3 <= 24.2577 )
						if( ema2 <= 24.1711 )
							ret := -0.468254
						if( ema2 > 24.1711 )
							ret := 0.157480
					if( ema3 > 24.2577 )
						if( ema12 <= 0.096634 )
							ret := -0.454321
						if( ema12 > 0.096634 )
							ret := -0.862745 // sell
			if( ema2 > 24.4697 )
				if( ema13 <= 0.619143 )
					if( ema3 <= 93.301 )
						if( ema12 <= 0.042713 )
							ret := -0.026136
						if( ema12 > 0.042713 )
							ret := -0.124935
					if( ema3 > 93.301 )
						if( ema1 <= 95.1485 )
							ret := 0.711538 // buy
						if( ema1 > 95.1485 )
							ret := -0.153846
				if( ema13 > 0.619143 )
					if( ema12 <= 0.530372 )
						if( tema <= 62.8356 )
							ret := 0.221561
						if( tema > 62.8356 )
							ret := -0.065217
					if( ema12 > 0.530372 )
						if( ema2 <= 94.7333 )
							ret := -0.025959
						if( ema2 > 94.7333 )
							ret := -0.970588 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_RUN_30Min_a3c77a40(ema1, tema, ema12, ema2, ema3, ema13)

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


