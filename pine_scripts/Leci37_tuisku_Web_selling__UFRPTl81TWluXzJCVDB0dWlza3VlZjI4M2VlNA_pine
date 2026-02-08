//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: PTON_5Min_2BT0_ef283ee4 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PTON_5Min_2BT0_ef283ee4", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PTON_5Min_ef283ee4(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( bearPower <= 0.005404 )
		if( bbm <= 0.008898 )
			if( bearPower <= -0.012143 )
				if( ema3 <= 3.58173 )
					if( bullPower <= -0.059731 )
						ret := -0.625000
					if( bullPower > -0.059731 )
						if( bbp <= -0.022592 )
							ret := 0.777778 // buy
						if( bbp > -0.022592 )
							ret := 0.333333
				if( ema3 > 3.58173 )
					if( bbp <= -0.064207 )
						if( tema <= 4.69164 )
							ret := 0.756272 // buy
						if( tema > 4.69164 )
							ret := 0.371002
					if( bbp > -0.064207 )
						if( ema12 <= -0.007726 )
							ret := 0.166295
						if( ema12 > -0.007726 )
							ret := 0.429293
			if( bearPower > -0.012143 )
				if( bullPower <= 0.000988 )
					if( ema3 <= 4.39992 )
						if( ema12 <= -0.002461 )
							ret := 0.169708
						if( ema12 > -0.002461 )
							ret := 0.437975
					if( ema3 > 4.39992 )
						if( bearPower <= -0.010162 )
							ret := -0.165323
						if( bearPower > -0.010162 )
							ret := 0.100000
				if( bullPower > 0.000988 )
					if( ema1 <= 3.08158 )
						if( ema3 <= 3.05034 )
							ret := 0.205882
						if( ema3 > 3.05034 )
							ret := 0.933333 // buy
					if( ema1 > 3.08158 )
						if( ema1 <= 5.52298 )
							ret := -0.162441
						if( ema1 > 5.52298 )
							ret := 0.147420
		if( bbm > 0.008898 )
			if( tema <= 2.94111 )
				if( ema2 <= 3.03228 )
					if( bearPower <= -0.009613 )
						if( ema13 <= -0.000789 )
							ret := 0.545082
						if( ema13 > -0.000789 )
							ret := 0.933333 // buy
					if( bearPower > -0.009613 )
						if( bbm <= 0.0275 )
							ret := -0.069444
						if( bbm > 0.0275 )
							ret := 0.952381 // buy
				if( ema2 > 3.03228 )
					ret := -0.666667
			if( tema > 2.94111 )
				if( bearPower <= -0.258342 )
					if( ema13 <= -0.47212 )
						if( bbp <= -0.490766 )
							ret := -1.000000 // sell
						if( bbp > -0.490766 )
							ret := -0.900000 // sell
					if( ema13 > -0.47212 )
						if( ema12 <= -0.093988 )
							ret := -0.103030
						if( ema12 > -0.093988 )
							ret := -0.720930 // sell
				if( bearPower > -0.258342 )
					if( tema <= 9.60906 )
						if( bbp <= 0.032476 )
							ret := 0.010474
						if( bbp > 0.032476 )
							ret := 0.108088
					if( tema > 9.60906 )
						if( ema3 <= 9.67588 )
							ret := -0.585526
						if( ema3 > 9.67588 )
							ret := 0.066667
	if( bearPower > 0.005404 )
		if( bbm <= 0.009765 )
			if( bullPower <= 0.042579 )
				if( ema13 <= 0.031463 )
					if( tema <= 4.01588 )
						if( ema12 <= 0.015584 )
							ret := -0.418564
						if( ema12 > 0.015584 )
							ret := 0.351852
					if( tema > 4.01588 )
						if( bullPower <= 0.026992 )
							ret := -0.137824
						if( bullPower > 0.026992 )
							ret := -0.389662
				if( ema13 > 0.031463 )
					if( bullPower <= 0.038778 )
						if( ema12 <= 0.014146 )
							ret := -0.619048
						if( ema12 > 0.014146 )
							ret := 0.187500
					if( bullPower > 0.038778 )
						if( ema2 <= 4.97948 )
							ret := -0.851852 // sell
						if( ema2 > 4.97948 )
							ret := -0.100000
			if( bullPower > 0.042579 )
				if( tema <= 4.85128 )
					if( tema <= 4.54594 )
						if( bbm <= 3e-06 )
							ret := -0.908046 // sell
						if( bbm > 3e-06 )
							ret := -1.000000 // sell
					if( tema > 4.54594 )
						if( ema12 <= 0.020706 )
							ret := -0.945946 // sell
						if( ema12 > 0.020706 )
							ret := -0.333333
				if( tema > 4.85128 )
					if( bullPower <= 0.063329 )
						if( ema1 <= 6.7295 )
							ret := 0.086957
						if( ema1 > 6.7295 )
							ret := -0.413793
					if( bullPower > 0.063329 )
						if( ema12 <= 0.081104 )
							ret := -0.874074 // sell
						if( ema12 > 0.081104 )
							ret := -0.312500
		if( bbm > 0.009765 )
			if( ema2 <= 9.56402 )
				if( ema2 <= 3.1428 )
					if( ema3 <= 3.03663 )
						if( tema <= 3.01499 )
							ret := 0.288591
						if( tema > 3.01499 )
							ret := -0.612245
					if( ema3 > 3.03663 )
						if( ema3 <= 3.08944 )
							ret := 0.604762
						if( ema3 > 3.08944 )
							ret := -0.007143
				if( ema2 > 3.1428 )
					if( ema3 <= 3.69898 )
						if( ema12 <= 0.025598 )
							ret := -0.099356
						if( ema12 > 0.025598 )
							ret := -0.752315 // sell
					if( ema3 > 3.69898 )
						if( ema13 <= 0.026159 )
							ret := -0.153490
						if( ema13 > 0.026159 )
							ret := -0.003360
			if( ema2 > 9.56402 )
				if( ema13 <= 0.150061 )
					if( ema13 <= 0.065819 )
						if( bullPower <= 0.037825 )
							ret := -0.272727
						if( bullPower > 0.037825 )
							ret := -0.737500 // sell
					if( ema13 > 0.065819 )
						if( ema3 <= 9.59121 )
							ret := 0.000000
						if( ema3 > 9.59121 )
							ret := -0.375000
				if( ema13 > 0.150061 )
					ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_PTON_5Min_ef283ee4(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)

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


