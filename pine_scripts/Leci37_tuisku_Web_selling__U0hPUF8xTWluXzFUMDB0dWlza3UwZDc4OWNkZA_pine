//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: SHOP_1Min_1T00_0d789cdd Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SHOP_1Min_1T00_0d789cdd", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SHOP_1Min_0d789cdd(ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.5,min_samples_leaf=4, random_state=843828734)
	if( ema12 <= -0.021183 )
		if( ema1 <= 81.0201 )
			if( ema13 <= -0.02573 )
				if( ema3 <= 49.5787 )
					ret := 1.000000 // buy
				if( ema3 > 49.5787 )
					if( ema3 <= 51.3918 )
						if( ema13 <= -0.17863 )
							if( ema2 <= 50.9598 )
								ret := -0.579439
							if( ema2 > 50.9598 )
								ret := -0.976744 // sell
						if( ema13 > -0.17863 )
							if( ema1 <= 50.1216 )
								ret := 1.000000 // buy
							if( ema1 > 50.1216 )
								ret := -0.812500 // sell
					if( ema3 > 51.3918 )
						if( ema3 <= 54.0463 )
							if( ema12 <= -0.069481 )
								ret := 0.603960
							if( ema12 > -0.069481 )
								ret := 0.032086
						if( ema3 > 54.0463 )
							if( ema13 <= -0.130472 )
								ret := -0.015426
							if( ema13 > -0.130472 )
								ret := 0.052519
			if( ema13 > -0.02573 )
				if( ema2 <= 63.2471 )
					if( ema1 <= 52.0431 )
						if( ema13 <= 0.013811 )
							ret := 1.000000 // buy
						if( ema13 > 0.013811 )
							ret := 0.750000 // buy
					if( ema1 > 52.0431 )
						if( ema1 <= 60.0338 )
							if( ema2 <= 56.9949 )
								ret := -0.448276
							if( ema2 > 56.9949 )
								ret := 0.211111
						if( ema1 > 60.0338 )
							if( ema13 <= -0.023603 )
								ret := 0.400000
							if( ema13 > -0.023603 )
								ret := -0.466667
				if( ema2 > 63.2471 )
					if( tema <= 63.795 )
						if( ema2 <= 63.7084 )
							if( ema3 <= 63.5999 )
								ret := 0.666667
							if( ema3 > 63.5999 )
								ret := -0.750000 // sell
						if( ema2 > 63.7084 )
							if( ema13 <= 0.040889 )
								ret := 1.000000 // buy
							if( ema13 > 0.040889 )
								ret := 0.750000 // buy
					if( tema > 63.795 )
						if( ema3 <= 66.162 )
							if( ema3 <= 65.8005 )
								ret := 0.176471
							if( ema3 > 65.8005 )
								ret := -0.818182 // sell
						if( ema3 > 66.162 )
							if( ema3 <= 68.8038 )
								ret := 0.523179
							if( ema3 > 68.8038 )
								ret := 0.319444
		if( ema1 > 81.0201 )
			if( ema3 <= 83.5161 )
				if( ema1 <= 81.5599 )
					if( ema2 <= 81.2032 )
						if( ema13 <= -0.051168 )
							ret := 0.000000
						if( ema13 > -0.051168 )
							ret := 1.000000 // buy
					if( ema2 > 81.2032 )
						if( ema12 <= -0.059572 )
							if( tema <= 80.9083 )
								ret := 0.500000
							if( tema > 80.9083 )
								ret := 0.986301 // buy
						if( ema12 > -0.059572 )
							if( ema2 <= 81.5296 )
								ret := 0.500000
							if( ema2 > 81.5296 )
								ret := 1.000000 // buy
				if( ema1 > 81.5599 )
					if( ema1 <= 82.1742 )
						if( ema2 <= 81.653 )
							ret := 0.200000
						if( ema2 > 81.653 )
							if( ema13 <= -0.297255 )
								ret := -0.500000
							if( ema13 > -0.297255 )
								ret := -1.000000 // sell
					if( ema1 > 82.1742 )
						if( ema3 <= 83.3078 )
							if( ema2 <= 83.1493 )
								ret := 0.414216
							if( ema2 > 83.1493 )
								ret := -0.078947
						if( ema3 > 83.3078 )
							if( ema2 <= 83.287 )
								ret := 1.000000 // buy
							if( ema2 > 83.287 )
								ret := 0.607843
			if( ema3 > 83.5161 )
				if( ema3 <= 83.5468 )
					if( ema1 <= 83.4516 )
						if( ema13 <= -0.122776 )
							ret := -1.000000 // sell
						if( ema13 > -0.122776 )
							if( ema2 <= 83.4929 )
								ret := 0.000000
							if( ema2 > 83.4929 )
								ret := -0.500000
					if( ema1 > 83.4516 )
						if( ema13 <= -0.072251 )
							ret := -0.750000 // sell
						if( ema13 > -0.072251 )
							ret := -1.000000 // sell
				if( ema3 > 83.5468 )
					if( ema3 <= 84.0417 )
						if( ema1 <= 83.7713 )
							if( tema <= 82.7968 )
								ret := 1.000000 // buy
							if( tema > 82.7968 )
								ret := -0.114035
						if( ema1 > 83.7713 )
							if( ema1 <= 83.8484 )
								ret := 0.562500
							if( ema1 > 83.8484 )
								ret := 0.133333
					if( ema3 > 84.0417 )
						if( ema1 <= 84.0168 )
							if( ema1 <= 84.0036 )
								ret := -0.500000
							if( ema1 > 84.0036 )
								ret := -1.000000 // sell
						if( ema1 > 84.0168 )
							if( ema2 <= 84.0783 )
								ret := -0.375000
							if( ema2 > 84.0783 )
								ret := 0.000000
	if( ema12 > -0.021183 )
		if( ema12 <= 0.100807 )
			if( ema3 <= 52.7384 )
				if( ema2 <= 49.072 )
					ret := -0.857143 // sell
				if( ema2 > 49.072 )
					if( ema13 <= -0.036582 )
						if( ema12 <= -0.006489 )
							if( ema3 <= 50.2025 )
								ret := 1.000000 // buy
							if( ema3 > 50.2025 )
								ret := 0.166667
						if( ema12 > -0.006489 )
							if( ema12 <= 0.000432 )
								ret := -0.272727
							if( ema12 > 0.000432 )
								ret := -1.000000 // sell
					if( ema13 > -0.036582 )
						if( ema13 <= 0.045667 )
							if( ema3 <= 52.1954 )
								ret := 0.885714 // buy
							if( ema3 > 52.1954 )
								ret := 0.521739
						if( ema13 > 0.045667 )
							if( tema <= 52.5766 )
								ret := 0.177778
							if( tema > 52.5766 )
								ret := 0.564103
			if( ema3 > 52.7384 )
				if( ema3 <= 62.4898 )
					if( tema <= 58.8716 )
						if( ema1 <= 54.8942 )
							if( ema12 <= 0.0683 )
								ret := -0.200000
							if( ema12 > 0.0683 )
								ret := 0.330000
						if( ema1 > 54.8942 )
							if( tema <= 56.0443 )
								ret := 0.934783 // buy
							if( tema > 56.0443 )
								ret := 0.024063
					if( tema > 58.8716 )
						if( ema1 <= 58.8988 )
							if( ema2 <= 58.8957 )
								ret := -0.394495
							if( ema2 > 58.8957 )
								ret := -0.820513 // sell
						if( ema1 > 58.8988 )
							if( ema13 <= -0.068964 )
								ret := 0.571429
							if( ema13 > -0.068964 )
								ret := -0.098827
				if( ema3 > 62.4898 )
					if( ema1 <= 62.716 )
						if( ema1 <= 62.4794 )
							ret := -1.000000 // sell
						if( ema1 > 62.4794 )
							if( tema <= 62.6636 )
								ret := 0.236264
							if( tema > 62.6636 )
								ret := 0.497006
					if( ema1 > 62.716 )
						if( ema2 <= 62.8088 )
							if( ema1 <= 62.8361 )
								ret := -0.297386
							if( ema1 > 62.8361 )
								ret := -0.853659 // sell
						if( ema2 > 62.8088 )
							if( ema3 <= 63.2899 )
								ret := 0.237695
							if( ema3 > 63.2899 )
								ret := -0.005088
		if( ema12 > 0.100807 )
			if( ema13 <= 2.30716 )
				if( ema3 <= 64.8497 )
					if( tema <= 62.5547 )
						if( ema3 <= 53.168 )
							if( ema13 <= 0.593694 )
								ret := -0.670588
							if( ema13 > 0.593694 )
								ret := 0.312500
						if( ema3 > 53.168 )
							if( ema3 <= 53.7222 )
								ret := 0.530612
							if( ema3 > 53.7222 )
								ret := -0.180905
					if( tema > 62.5547 )
						if( ema2 <= 62.8365 )
							if( tema <= 62.8627 )
								ret := -0.648649
							if( tema > 62.8627 )
								ret := -0.969072 // sell
						if( ema2 > 62.8365 )
							if( ema2 <= 62.9814 )
								ret := 0.916667 // buy
							if( ema2 > 62.9814 )
								ret := -0.314066
				if( ema3 > 64.8497 )
					if( ema2 <= 65.6451 )
						if( ema12 <= 0.122217 )
							if( ema1 <= 65.3851 )
								ret := -0.392857
							if( ema1 > 65.3851 )
								ret := 0.611111
						if( ema12 > 0.122217 )
							if( tema <= 66.42 )
								ret := 0.702128 // buy
							if( tema > 66.42 )
								ret := -0.428571
					if( ema2 > 65.6451 )
						if( ema12 <= 0.262298 )
							if( ema1 <= 66.0695 )
								ret := -0.645570
							if( ema1 > 66.0695 )
								ret := -0.040486
						if( ema12 > 0.262298 )
							if( ema12 <= 0.478214 )
								ret := -0.445820
							if( ema12 > 0.478214 )
								ret := 0.538462
			if( ema13 > 2.30716 )
				ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_SHOP_1Min_0d789cdd(ema1, tema, ema12, ema2, ema3, ema13)

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


