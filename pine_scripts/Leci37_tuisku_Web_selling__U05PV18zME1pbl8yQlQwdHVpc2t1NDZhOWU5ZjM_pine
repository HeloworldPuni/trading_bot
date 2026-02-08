//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: SNOW_30Min_2BT0_46a9e9f3 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNOW_30Min_2BT0_46a9e9f3", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNOW_30Min_46a9e9f3(bbm, bearPower, bbp, bullPower, BBPower_Color, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( tema <= 113.567 )
		if( tema <= 109.848 )
			if( bearPower <= -0.33173 )
				if( tema <= 109.496 )
					if( bbm <= 0.427867 )
						if( ema1 <= 108.008 )
							ret := 1.000000 // buy
						if( ema1 > 108.008 )
							ret := 0.000000
					if( bbm > 0.427867 )
						if( tema <= 108.121 )
							ret := 0.222222
						if( tema > 108.121 )
							ret := 0.851852 // buy
				if( tema > 109.496 )
					if( ema2 <= 109.917 )
						ret := 0.000000
					if( ema2 > 109.917 )
						if( bearPower <= -1.12896 )
							ret := 0.500000
						if( bearPower > -1.12896 )
							ret := 1.000000 // buy
			if( bearPower > -0.33173 )
				if( ema1 <= 109.712 )
					ret := 0.000000
				if( ema1 > 109.712 )
					ret := 0.250000
		if( tema > 109.848 )
			if( tema <= 111.728 )
				if( ema1 <= 111.353 )
					if( ema1 <= 110.987 )
						if( bullPower <= 0.651604 )
							ret := 0.180180
						if( bullPower > 0.651604 )
							ret := -0.486486
					if( ema1 > 110.987 )
						if( ema12 <= 0.327805 )
							ret := 0.680000
						if( ema12 > 0.327805 )
							ret := -1.000000 // sell
				if( ema1 > 111.353 )
					if( bbp <= 1.70843 )
						if( bbm <= 0.4925 )
							ret := 0.000000
						if( bbm > 0.4925 )
							ret := -0.629630
					if( bbp > 1.70843 )
						ret := 1.000000 // buy
			if( tema > 111.728 )
				if( bullPower <= -3.24275 )
					ret := -0.700000 // sell
				if( bullPower > -3.24275 )
					if( ema13 <= -0.834954 )
						if( ema1 <= 114.607 )
							ret := 0.924528 // buy
						if( ema1 > 114.607 )
							ret := 0.666667
					if( ema13 > -0.834954 )
						if( bbm <= 1.96502 )
							ret := 0.406667
						if( bbm > 1.96502 )
							ret := -0.750000 // sell
	if( tema > 113.567 )
		if( bullPower <= -0.300071 )
			if( ema1 <= 267.887 )
				if( tema <= 227.737 )
					if( tema <= 123.339 )
						if( tema <= 121.71 )
							ret := 0.013793
						if( tema > 121.71 )
							ret := -0.702479 // sell
					if( tema > 123.339 )
						if( ema2 <= 143.742 )
							ret := 0.228829
						if( ema2 > 143.742 )
							ret := 0.018673
				if( tema > 227.737 )
					if( bbp <= -16.5693 )
						if( bbm <= 4.22588 )
							ret := 0.833333 // buy
						if( bbm > 4.22588 )
							ret := 1.000000 // buy
					if( bbp > -16.5693 )
						if( tema <= 262.188 )
							ret := 0.228341
						if( tema > 262.188 )
							ret := 0.620482
			if( ema1 > 267.887 )
				if( tema <= 280.612 )
					if( ema12 <= -1.69868 )
						if( bbm <= 8.92436 )
							ret := -0.641667
						if( bbm > 8.92436 )
							ret := 1.000000 // buy
					if( ema12 > -1.69868 )
						if( ema1 <= 280.091 )
							ret := 0.174419
						if( ema1 > 280.091 )
							ret := -0.786885 // sell
				if( tema > 280.612 )
					if( ema1 <= 367.131 )
						if( bbm <= 1.60634 )
							ret := 0.161589
						if( bbm > 1.60634 )
							ret := -0.057836
					if( ema1 > 367.131 )
						if( bbp <= -26.3354 )
							ret := 0.923077 // buy
						if( bbp > -26.3354 )
							ret := -0.510309
		if( bullPower > -0.300071 )
			if( ema3 <= 128.713 )
				if( ema3 <= 115.247 )
					if( bearPower <= 1.03415 )
						if( ema1 <= 114.491 )
							ret := -0.158103
						if( ema1 > 114.491 )
							ret := -0.733333 // sell
					if( bearPower > 1.03415 )
						if( ema13 <= 1.16671 )
							ret := 0.000000
						if( ema13 > 1.16671 )
							ret := 0.592593
				if( ema3 > 115.247 )
					if( ema13 <= 1.57012 )
						if( ema13 <= -0.310418 )
							ret := 0.103093
						if( ema13 > -0.310418 )
							ret := 0.454068
					if( ema13 > 1.57012 )
						if( tema <= 119.89 )
							ret := 0.500000
						if( tema > 119.89 )
							ret := -0.336634
			if( ema3 > 128.713 )
				if( ema13 <= 1.73576 )
					if( ema1 <= 133.913 )
						if( bearPower <= -1.21703 )
							ret := 0.141026
						if( bearPower > -1.21703 )
							ret := -0.416667
					if( ema1 > 133.913 )
						if( tema <= 135.438 )
							ret := 0.520635
						if( tema > 135.438 )
							ret := -0.072889
				if( ema13 > 1.73576 )
					if( ema2 <= 267.184 )
						if( bullPower <= 11.6237 )
							ret := 0.105070
						if( bullPower > 11.6237 )
							ret := -0.642857
					if( ema2 > 267.184 )
						if( ema3 <= 268.099 )
							ret := -0.709677 // sell
						if( ema3 > 268.099 )
							ret := -0.037886
	
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
float op_operation = decision_tree_0_SNOW_30Min_46a9e9f3(bbm, bearPower, bbp, bullPower, BBPower_Color, ema1, tema, ema12, ema2, ema3, ema13)

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


