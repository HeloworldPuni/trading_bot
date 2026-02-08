//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: ZI_5Min_2BT0_9dddb46b Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ZI_5Min_2BT0_9dddb46b", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ZI_5Min_9dddb46b(bbp, bullPower, BBPower_Color, bearPower, bbm, ema2, tema, ema12, ema3, ema1, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( bbp <= 0.366797 )
		if( bullPower <= -0.012286 )
			if( bbm <= 0.019877 )
				if( bearPower <= -0.078452 )
					if( ema1 <= 17.1847 )
						if( ema12 <= -0.088502 )
							ret := -0.284483
						if( ema12 > -0.088502 )
							ret := 0.524355
					if( ema1 > 17.1847 )
						if( ema1 <= 25.2181 )
							ret := 0.831034 // buy
						if( ema1 > 25.2181 )
							ret := 0.258621
				if( bearPower > -0.078452 )
					if( ema13 <= 0.013337 )
						if( ema13 <= -0.021747 )
							ret := 0.312092
						if( ema13 > -0.021747 )
							ret := 0.060998
					if( ema13 > 0.013337 )
						if( ema12 <= 0.048066 )
							ret := 0.607656
						if( ema12 > 0.048066 )
							ret := -0.600000
			if( bbm > 0.019877 )
				if( ema1 <= 8.64904 )
					if( bbm <= 0.105 )
						if( ema12 <= -0.033466 )
							ret := 0.982143 // buy
						if( ema12 > -0.033466 )
							ret := 0.629630
					if( bbm > 0.105 )
						ret := 0.294118
				if( ema1 > 8.64904 )
					if( tema <= 28.8688 )
						if( ema13 <= -0.076874 )
							ret := -0.061177
						if( ema13 > -0.076874 )
							ret := 0.057700
					if( tema > 28.8688 )
						if( bearPower <= -0.243695 )
							ret := -0.545455
						if( bearPower > -0.243695 )
							ret := -1.000000 // sell
		if( bullPower > -0.012286 )
			if( ema13 <= 0.02492 )
				if( bearPower <= 0.038688 )
					if( ema1 <= 8.64442 )
						if( tema <= 8.34583 )
							ret := 0.149351
						if( tema > 8.34583 )
							ret := 0.762376 // buy
					if( ema1 > 8.64442 )
						if( ema2 <= 8.93123 )
							ret := -0.505263
						if( ema2 > 8.93123 )
							ret := -0.047205
				if( bearPower > 0.038688 )
					if( ema12 <= 0.021452 )
						if( bullPower <= 0.142497 )
							ret := -0.608696
						if( bullPower > 0.142497 )
							ret := -0.048780
					if( ema12 > 0.021452 )
						if( bbp <= 0.159296 )
							ret := -0.419355
						if( bbp > 0.159296 )
							ret := 0.347826
			if( ema13 > 0.02492 )
				if( bbm <= 0.0014 )
					if( ema1 <= 23.4223 )
						if( bearPower <= 0.034451 )
							ret := -0.053812
						if( bearPower > 0.034451 )
							ret := -0.434164
					if( ema1 > 23.4223 )
						if( bearPower <= 0.053725 )
							ret := 0.958333 // buy
						if( bearPower > 0.053725 )
							ret := 0.319149
				if( bbm > 0.0014 )
					if( ema3 <= 8.52901 )
						if( ema13 <= 0.036156 )
							ret := 0.857143 // buy
						if( ema13 > 0.036156 )
							ret := -0.529412
					if( ema3 > 8.52901 )
						if( tema <= 9.22792 )
							ret := 0.594595
						if( tema > 9.22792 )
							ret := 0.049155
	if( bbp > 0.366797 )
		if( ema13 <= 0.15717 )
			if( ema2 <= 22.5961 )
				if( bearPower <= 0.18845 )
					if( tema <= 18.6368 )
						if( ema3 <= 15.7229 )
							ret := -0.804878 // sell
						if( ema3 > 15.7229 )
							ret := -0.136364
					if( tema > 18.6368 )
						if( ema13 <= 0.022809 )
							ret := -0.727273 // sell
						if( ema13 > 0.022809 )
							ret := -1.000000 // sell
				if( bearPower > 0.18845 )
					if( ema12 <= 0.100281 )
						if( tema <= 20.7692 )
							ret := -0.976608 // sell
						if( tema > 20.7692 )
							ret := -0.823529 // sell
					if( ema12 > 0.100281 )
						ret := -0.538462
			if( ema2 > 22.5961 )
				if( ema2 <= 24.2846 )
					ret := 0.541667
				if( ema2 > 24.2846 )
					if( ema2 <= 25.7985 )
						ret := -0.923077 // sell
					if( ema2 > 25.7985 )
						if( bearPower <= 0.216414 )
							ret := 0.111111
						if( bearPower > 0.216414 )
							ret := -0.642857
		if( ema13 > 0.15717 )
			if( ema3 <= 16.3792 )
				if( bullPower <= 0.32291 )
					if( bearPower <= 0.172879 )
						if( bbm <= 0.115115 )
							ret := 0.612245
						if( bbm > 0.115115 )
							ret := -0.625000
					if( bearPower > 0.172879 )
						if( bullPower <= 0.271075 )
							ret := -0.848485 // sell
						if( bullPower > 0.271075 )
							ret := 0.000000
				if( bullPower > 0.32291 )
					if( bearPower <= 0.451547 )
						if( ema1 <= 15.8151 )
							ret := 0.473684
						if( ema1 > 15.8151 )
							ret := 0.959184 // buy
					if( bearPower > 0.451547 )
						ret := 0.272727
			if( ema3 > 16.3792 )
				if( ema2 <= 22.9692 )
					if( ema12 <= 0.105013 )
						ret := 0.777778 // buy
					if( ema12 > 0.105013 )
						if( ema13 <= 0.825989 )
							ret := -0.595745
						if( ema13 > 0.825989 )
							ret := 0.666667
				if( ema2 > 22.9692 )
					if( bbp <= 0.80437 )
						if( ema2 <= 26.0997 )
							ret := 0.340708
						if( ema2 > 26.0997 )
							ret := -0.333333
					if( bbp > 0.80437 )
						if( ema1 <= 26.5085 )
							ret := -0.975000 // sell
						if( ema1 > 26.5085 )
							ret := 0.200000
	
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
float op_operation = decision_tree_0_ZI_5Min_9dddb46b(bbp, bullPower, BBPower_Color, bearPower, bbm, ema2, tema, ema12, ema3, ema1, ema13)

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


