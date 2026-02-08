//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: DBX_30Min_2BT0_11c47d22 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DBX_30Min_2BT0_11c47d22", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DBX_30Min_11c47d22(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( bullPower <= -0.028195 )
		if( bbm <= 0.074786 )
			if( bullPower <= -0.264048 )
				if( bbp <= -0.75294 )
					if( ema12 <= -0.247629 )
						if( ema13 <= -0.416229 )
							ret := 0.619048
						if( ema13 > -0.416229 )
							ret := -0.333333
					if( ema12 > -0.247629 )
						if( bbm <= 0.039756 )
							ret := 0.905579 // buy
						if( bbm > 0.039756 )
							ret := 0.600000
				if( bbp > -0.75294 )
					if( ema1 <= 21.3367 )
						if( bbm <= 0.03227 )
							ret := -0.184211
						if( bbm > 0.03227 )
							ret := 0.769231 // buy
					if( ema1 > 21.3367 )
						if( ema13 <= -0.360072 )
							ret := 0.169492
						if( ema13 > -0.360072 )
							ret := 0.669202
			if( bullPower > -0.264048 )
				if( ema13 <= -0.056039 )
					if( bearPower <= -0.146793 )
						if( ema13 <= -0.218586 )
							ret := 0.088406
						if( ema13 > -0.218586 )
							ret := 0.377168
					if( bearPower > -0.146793 )
						if( tema <= 29.9963 )
							ret := 0.031012
						if( tema > 29.9963 )
							ret := 0.479730
				if( ema13 > -0.056039 )
					if( bearPower <= -0.118686 )
						if( bullPower <= -0.118061 )
							ret := 0.744382 // buy
						if( bullPower > -0.118061 )
							ret := 0.458333
					if( bearPower > -0.118686 )
						if( ema2 <= 23.4637 )
							ret := 0.419223
						if( ema2 > 23.4637 )
							ret := 0.085903
		if( bbm > 0.074786 )
			if( ema12 <= -0.840614 )
				if( ema13 <= -1.74477 )
					ret := -1.000000 // sell
				if( ema13 > -1.74477 )
					ret := -0.888889 // sell
			if( ema12 > -0.840614 )
				if( tema <= 19.7164 )
					if( ema12 <= -0.161898 )
						if( bullPower <= -0.317652 )
							ret := 0.742515 // buy
						if( bullPower > -0.317652 )
							ret := 0.407407
					if( ema12 > -0.161898 )
						if( bullPower <= -0.10147 )
							ret := -0.071685
						if( bullPower > -0.10147 )
							ret := 0.239521
				if( tema > 19.7164 )
					if( tema <= 32.4471 )
						if( bullPower <= -0.408351 )
							ret := 0.257194
						if( bullPower > -0.408351 )
							ret := 0.033485
					if( tema > 32.4471 )
						if( ema3 <= 36.2335 )
							ret := -0.672566
						if( ema3 > 36.2335 )
							ret := 0.264706
	if( bullPower > -0.028195 )
		if( tema <= 22.7182 )
			if( bearPower <= 0.143281 )
				if( ema13 <= 0.297277 )
					if( ema2 <= 22.8276 )
						if( ema2 <= 16.1598 )
							ret := 0.672727
						if( ema2 > 16.1598 )
							ret := 0.008127
					if( ema2 > 22.8276 )
						if( bbm <= 0.36073 )
							ret := 0.562500
						if( bbm > 0.36073 )
							ret := 1.000000 // buy
				if( ema13 > 0.297277 )
					if( bearPower <= 0.099397 )
						if( ema3 <= 21.1332 )
							ret := 0.843137 // buy
						if( ema3 > 21.1332 )
							ret := 0.072727
					if( bearPower > 0.099397 )
						if( ema1 <= 22.0256 )
							ret := -0.230769
						if( ema1 > 22.0256 )
							ret := 0.818182 // buy
			if( bearPower > 0.143281 )
				if( tema <= 21.3435 )
					if( ema3 <= 20.907 )
						if( bbm <= 0.078668 )
							ret := -0.458763
						if( bbm > 0.078668 )
							ret := -0.163235
					if( ema3 > 20.907 )
						if( tema <= 21.2579 )
							ret := -0.959184 // sell
						if( tema > 21.2579 )
							ret := -0.090909
				if( tema > 21.3435 )
					if( bbp <= 0.381728 )
						if( ema2 <= 21.7565 )
							ret := 0.323529
						if( ema2 > 21.7565 )
							ret := -0.912500 // sell
					if( bbp > 0.381728 )
						if( bearPower <= 0.323241 )
							ret := 0.241147
						if( bearPower > 0.323241 )
							ret := -0.220588
		if( tema > 22.7182 )
			if( ema2 <= 32.4184 )
				if( bbp <= 0.309885 )
					if( ema13 <= 0.051819 )
						if( ema1 <= 22.8241 )
							ret := -0.659483
						if( ema1 > 22.8241 )
							ret := -0.094898
					if( ema13 > 0.051819 )
						if( tema <= 26.9923 )
							ret := -0.065439
						if( tema > 26.9923 )
							ret := 0.109489
				if( bbp > 0.309885 )
					if( ema2 <= 22.1888 )
						if( ema13 <= 0.862483 )
							ret := 0.829787 // buy
						if( ema13 > 0.862483 )
							ret := 0.090909
					if( ema2 > 22.1888 )
						if( ema12 <= 0.063051 )
							ret := -0.381643
						if( ema12 > 0.063051 )
							ret := -0.161430
			if( ema2 > 32.4184 )
				if( ema13 <= 1.03975 )
					if( bbp <= 0.371108 )
						if( ema3 <= 41.2531 )
							ret := -0.319489
						if( ema3 > 41.2531 )
							ret := -1.000000 // sell
					if( bbp > 0.371108 )
						if( ema3 <= 36.2525 )
							ret := -0.862319 // sell
						if( ema3 > 36.2525 )
							ret := -0.451613
				if( ema13 > 1.03975 )
					if( tema <= 42.4963 )
						if( tema <= 35.9013 )
							ret := -0.705882 // sell
						if( tema > 35.9013 )
							ret := 0.754098 // buy
					if( tema > 42.4963 )
						ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0


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
float op_operation = decision_tree_0_DBX_30Min_11c47d22(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)

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


