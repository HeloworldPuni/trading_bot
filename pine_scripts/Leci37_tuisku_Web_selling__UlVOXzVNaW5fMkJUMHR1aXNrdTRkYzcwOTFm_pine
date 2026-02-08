//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: RUN_5Min_2BT0_4dc7091f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RUN_5Min_2BT0_4dc7091f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RUN_5Min_4dc7091f(bbm, bearPower, bbp, bullPower, BBPower_Color, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( bbp <= 0.001176 )
		if( ema3 <= 10.2129 )
			if( bearPower <= -0.256871 )
				if( bullPower <= -0.186927 )
					ret := -0.153846
				if( bullPower > -0.186927 )
					if( ema3 <= 9.56795 )
						if( bullPower <= -0.15941 )
							ret := -0.888889 // sell
						if( bullPower > -0.15941 )
							ret := -1.000000 // sell
					if( ema3 > 9.56795 )
						ret := -0.533333
			if( bearPower > -0.256871 )
				if( bullPower <= -0.027627 )
					if( bullPower <= -0.093189 )
						if( ema12 <= -0.11929 )
							ret := 0.708333 // buy
						if( ema12 > -0.11929 )
							ret := -0.341772
					if( bullPower > -0.093189 )
						if( ema2 <= 8.89783 )
							ret := 0.929412 // buy
						if( ema2 > 8.89783 )
							ret := 0.466448
				if( bullPower > -0.027627 )
					if( bbm <= 0.093036 )
						if( ema1 <= 10.0232 )
							ret := 0.053571
						if( ema1 > 10.0232 )
							ret := 0.420091
					if( bbm > 0.093036 )
						if( ema1 <= 10.0079 )
							ret := 0.676829
						if( ema1 > 10.0079 )
							ret := -0.266667
		if( ema3 > 10.2129 )
			if( bbm <= 0.024997 )
				if( bullPower <= -0.162699 )
					if( ema12 <= -0.161309 )
						if( ema2 <= 16.5799 )
							ret := 0.153846
						if( ema2 > 16.5799 )
							ret := -0.750000 // sell
					if( ema12 > -0.161309 )
						if( ema13 <= -0.107619 )
							ret := 0.824074 // buy
						if( ema13 > -0.107619 )
							ret := 0.434783
				if( bullPower > -0.162699 )
					if( ema1 <= 11.816 )
						if( ema1 <= 10.822 )
							ret := 0.113314
						if( ema1 > 10.822 )
							ret := 0.374080
					if( ema1 > 11.816 )
						if( ema12 <= 0.002678 )
							ret := 0.063608
						if( ema12 > 0.002678 )
							ret := 0.278861
			if( bbm > 0.024997 )
				if( ema3 <= 11.2822 )
					if( ema2 <= 11.1485 )
						if( ema1 <= 10.1036 )
							ret := -0.735849 // sell
						if( ema1 > 10.1036 )
							ret := -0.096070
					if( ema2 > 11.1485 )
						if( tema <= 11.0337 )
							ret := -0.275862
						if( tema > 11.0337 )
							ret := -0.840708 // sell
				if( ema3 > 11.2822 )
					if( tema <= 11.7189 )
						if( ema3 <= 11.8733 )
							ret := 0.195577
						if( ema3 > 11.8733 )
							ret := 0.658031
					if( tema > 11.7189 )
						if( tema <= 22.621 )
							ret := 0.003956
						if( tema > 22.621 )
							ret := -0.714286 // sell
	if( bbp > 0.001176 )
		if( bbm <= 0.029696 )
			if( bbp <= 0.093888 )
				if( ema13 <= 0.047205 )
					if( ema2 <= 11.4974 )
						if( bullPower <= 0.031632 )
							ret := -0.196816
						if( bullPower > 0.031632 )
							ret := -0.563694
					if( ema2 > 11.4974 )
						if( tema <= 17.2711 )
							ret := -0.121729
						if( tema > 17.2711 )
							ret := 0.068807
				if( ema13 > 0.047205 )
					if( ema2 <= 19.4389 )
						if( ema1 <= 11.6063 )
							ret := 0.418605
						if( ema1 > 11.6063 )
							ret := 0.179878
					if( ema2 > 19.4389 )
						if( bullPower <= 0.04409 )
							ret := -0.416667
						if( bullPower > 0.04409 )
							ret := 0.333333
			if( bbp > 0.093888 )
				if( bullPower <= 0.103116 )
					if( ema13 <= 0.126141 )
						if( ema13 <= 0.024429 )
							ret := -0.444169
						if( ema13 > 0.024429 )
							ret := -0.192699
					if( ema13 > 0.126141 )
						if( ema13 <= 0.202331 )
							ret := 0.366667
						if( ema13 > 0.202331 )
							ret := -0.260870
				if( bullPower > 0.103116 )
					if( ema2 <= 12.8574 )
						if( ema1 <= 10.3165 )
							ret := -0.282051
						if( ema1 > 10.3165 )
							ret := -0.755556 // sell
					if( ema2 > 12.8574 )
						if( ema1 <= 17.6979 )
							ret := -0.179739
						if( ema1 > 17.6979 )
							ret := -0.559322
		if( bbm > 0.029696 )
			if( tema <= 10.2464 )
				if( ema3 <= 10.0504 )
					if( ema3 <= 9.89808 )
						if( ema3 <= 9.75209 )
							ret := 0.099352
						if( ema3 > 9.75209 )
							ret := 0.662835
					if( ema3 > 9.89808 )
						if( ema12 <= 0.022638 )
							ret := 0.122807
						if( ema12 > 0.022638 )
							ret := -0.496241
				if( ema3 > 10.0504 )
					if( ema1 <= 10.2059 )
						if( bearPower <= -0.035963 )
							ret := -0.368421
						if( bearPower > -0.035963 )
							ret := 0.717593 // buy
					if( ema1 > 10.2059 )
						if( ema12 <= 0.01319 )
							ret := -0.181818
						if( ema12 > 0.01319 )
							ret := -0.928571 // sell
			if( tema > 10.2464 )
				if( ema1 <= 10.1708 )
					if( bearPower <= 0.318471 )
						if( bullPower <= 0.256186 )
							ret := -1.000000 // sell
						if( bullPower > 0.256186 )
							ret := -0.842105 // sell
					if( bearPower > 0.318471 )
						ret := -0.555556
				if( ema1 > 10.1708 )
					if( ema1 <= 23.1191 )
						if( ema13 <= 0.22936 )
							ret := -0.036394
						if( ema13 > 0.22936 )
							ret := 0.094285
					if( ema1 > 23.1191 )
						if( tema <= 23.7157 )
							ret := -1.000000 // sell
						if( tema > 23.7157 )
							ret := -0.200000
	
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
float op_operation = decision_tree_0_RUN_5Min_4dc7091f(bbm, bearPower, bbp, bullPower, BBPower_Color, ema1, tema, ema12, ema2, ema3, ema13)

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


