//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: NVDA_1Hour_1T00_ac2c9d28 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_NVDA_1Hour_1T00_ac2c9d28", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_NVDA_1Hour_ac2c9d28(ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ema12 <= 2.2774 )
		if( tema <= 106.435 )
			if( ema2 <= 104.446 )
				if( ema12 <= 1.01785 )
					if( ema1 <= 100.342 )
						if( tema <= 97.6874 )
							ret := 1.000000 // buy
						if( tema > 97.6874 )
							ret := 0.892857 // buy
					if( ema1 > 100.342 )
						if( tema <= 102.105 )
							ret := 0.214286
						if( tema > 102.105 )
							ret := 0.821429 // buy
				if( ema12 > 1.01785 )
					ret := 0.285714
			if( ema2 > 104.446 )
				if( ema1 <= 105.929 )
					if( ema13 <= 0.093907 )
						if( ema3 <= 106.785 )
							ret := -0.700000 // sell
						if( ema3 > 106.785 )
							ret := 0.250000
					if( ema13 > 0.093907 )
						if( ema13 <= 0.773989 )
							ret := 0.923077 // buy
						if( ema13 > 0.773989 )
							ret := -0.916667 // sell
				if( ema1 > 105.929 )
					if( ema13 <= -5.50357 )
						ret := 0.100000
					if( ema13 > -5.50357 )
						if( ema3 <= 106.528 )
							ret := 1.000000 // buy
						if( ema3 > 106.528 )
							ret := 0.875000 // buy
		if( tema > 106.435 )
			if( ema13 <= -7.22782 )
				if( ema3 <= 290.916 )
					if( tema <= 167.662 )
						if( tema <= 141.011 )
							ret := 0.705882 // buy
						if( tema > 141.011 )
							ret := -0.766667 // sell
					if( tema > 167.662 )
						if( tema <= 222.757 )
							ret := 0.774566 // buy
						if( tema > 222.757 )
							ret := 0.408840
				if( ema3 > 290.916 )
					if( tema <= 297.077 )
						if( ema1 <= 284.858 )
							ret := 0.047619
						if( ema1 > 284.858 )
							ret := -0.593220
					if( tema > 297.077 )
						if( ema1 <= 406.789 )
							ret := 0.796296 // buy
						if( ema1 > 406.789 )
							ret := 0.020091
			if( ema13 > -7.22782 )
				if( ema12 <= -1.6509 )
					if( ema1 <= 259.115 )
						if( tema <= 248.626 )
							ret := -0.283798
						if( tema > 248.626 )
							ret := -0.898148 // sell
					if( ema1 > 259.115 )
						if( ema2 <= 564.946 )
							ret := -0.031432
						if( ema2 > 564.946 )
							ret := -0.366894
				if( ema12 > -1.6509 )
					if( ema1 <= 106.858 )
						if( ema13 <= 1.54306 )
							ret := -0.743590 // sell
						if( ema13 > 1.54306 )
							ret := -1.000000 // sell
					if( ema1 > 106.858 )
						if( ema1 <= 952.445 )
							ret := -0.006800
						if( ema1 > 952.445 )
							ret := -0.688889
	if( ema12 > 2.2774 )
		if( ema1 <= 250.881 )
			if( ema1 <= 229.623 )
				if( ema3 <= 221.712 )
					if( ema3 <= 146.793 )
						if( ema12 <= 2.37828 )
							ret := 0.583333
						if( ema12 > 2.37828 )
							ret := 0.860000 // buy
					if( ema3 > 146.793 )
						if( ema1 <= 165.109 )
							ret := -0.461538
						if( ema1 > 165.109 )
							ret := 0.393814
				if( ema3 > 221.712 )
					if( tema <= 232.851 )
						ret := -0.200000
					if( tema > 232.851 )
						ret := -0.764706 // sell
			if( ema1 > 229.623 )
				if( ema2 <= 234.449 )
					if( ema13 <= 5.80708 )
						if( ema1 <= 234.196 )
							ret := -0.363636
						if( ema1 > 234.196 )
							ret := 0.896552 // buy
					if( ema13 > 5.80708 )
						if( ema1 <= 234.094 )
							ret := 0.951613 // buy
						if( ema1 > 234.094 )
							ret := 0.695652
				if( ema2 > 234.449 )
					if( tema <= 249.563 )
						if( ema13 <= 7.23024 )
							ret := -0.500000
						if( ema13 > 7.23024 )
							ret := 0.000000
					if( tema > 249.563 )
						if( ema2 <= 244.138 )
							ret := 0.428571
						if( ema2 > 244.138 )
							ret := 0.911765 // buy
		if( ema1 > 250.881 )
			if( ema3 <= 571.94 )
				if( ema13 <= 5.98295 )
					if( ema12 <= 3.46292 )
						if( ema2 <= 559.223 )
							ret := 0.109023
						if( ema2 > 559.223 )
							ret := -0.588235
					if( ema12 > 3.46292 )
						if( ema12 <= 3.88446 )
							ret := 0.510870
						if( ema12 > 3.88446 )
							ret := 0.853659 // buy
				if( ema13 > 5.98295 )
					if( ema12 <= 3.12693 )
						if( ema2 <= 265.246 )
							ret := -0.882353 // sell
						if( ema2 > 265.246 )
							ret := -0.410256
					if( ema12 > 3.12693 )
						if( ema1 <= 255.908 )
							ret := -0.826087 // sell
						if( ema1 > 255.908 )
							ret := -0.064375
			if( ema3 > 571.94 )
				if( ema2 <= 1203.5 )
					if( ema3 <= 1028.79 )
						if( ema3 <= 884.873 )
							ret := 0.255910
						if( ema3 > 884.873 )
							ret := -0.167421
					if( ema3 > 1028.79 )
						if( tema <= 1134.16 )
							ret := 0.977778 // buy
						if( tema > 1134.16 )
							ret := 0.588235
				if( ema2 > 1203.5 )
					if( ema13 <= 23.1221 )
						ret := -1.000000 // sell
					if( ema13 > 23.1221 )
						ret := -0.857143 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_NVDA_1Hour_ac2c9d28(ema12, ema3, ema13, tema, ema1, ema2)

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


