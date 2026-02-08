//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: NVST_30Min_2BT0_48960afa Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_NVST_30Min_2BT0_48960afa", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_NVST_30Min_48960afa(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( ema13 <= 0.525524 )
		if( ema2 <= 44.8371 )
			if( ema3 <= 14.1794 )
				if( ema3 <= 12.3637 )
					if( ema2 <= 12.2324 )
						if( ema3 <= 12.2385 )
							ret := 0.916667 // buy
						if( ema3 > 12.2385 )
							ret := -0.428571
					if( ema2 > 12.2324 )
						if( bullPower <= 0.064149 )
							ret := 0.500000
						if( bullPower > 0.064149 )
							ret := -1.000000 // sell
				if( ema3 > 12.3637 )
					if( bbp <= 0.87776 )
						if( bullPower <= -0.158477 )
							ret := 0.722222 // buy
						if( bullPower > -0.158477 )
							ret := 0.989247 // buy
					if( bbp > 0.87776 )
						ret := 0.526316
			if( ema3 > 14.1794 )
				if( bbp <= -0.347754 )
					if( tema <= 14.1961 )
						ret := -1.000000 // sell
					if( tema > 14.1961 )
						if( ema12 <= -0.608227 )
							ret := 0.843750 // buy
						if( ema12 > -0.608227 )
							ret := 0.111899
				if( bbp > -0.347754 )
					if( bearPower <= 0.632173 )
						if( tema <= 44.7745 )
							ret := -0.007311
						if( tema > 44.7745 )
							ret := 0.750000 // buy
					if( bearPower > 0.632173 )
						if( bbm <= 0.427636 )
							ret := -0.972222 // sell
						if( bbm > 0.427636 )
							ret := 0.000000
		if( ema2 > 44.8371 )
			if( ema3 <= 45.2351 )
				if( bbp <= -0.331711 )
					if( bbp <= -1.42267 )
						ret := 0.000000
					if( bbp > -1.42267 )
						if( ema3 <= 45.2217 )
							ret := -1.000000 // sell
						if( ema3 > 45.2217 )
							ret := -0.600000
				if( bbp > -0.331711 )
					if( ema2 <= 45.1592 )
						if( bbm <= 0.115751 )
							ret := 0.142857
						if( bbm > 0.115751 )
							ret := -0.305556
					if( ema2 > 45.1592 )
						if( ema1 <= 45.4334 )
							ret := -0.827586 // sell
						if( ema1 > 45.4334 )
							ret := 1.000000 // buy
			if( ema3 > 45.2351 )
				if( ema13 <= -0.581564 )
					if( bbm <= 0.563402 )
						if( tema <= 44.9239 )
							ret := -0.411765
						if( tema > 44.9239 )
							ret := 0.107143
					if( bbm > 0.563402 )
						if( ema2 <= 46.2263 )
							ret := 0.000000
						if( ema2 > 46.2263 )
							ret := 0.958333 // buy
				if( ema13 > -0.581564 )
					if( ema2 <= 49.4696 )
						if( ema3 <= 49.1588 )
							ret := -0.225071
						if( ema3 > 49.1588 )
							ret := -0.780000 // sell
					if( ema2 > 49.4696 )
						if( ema3 <= 49.7948 )
							ret := 0.702128 // buy
						if( ema3 > 49.7948 )
							ret := -0.368421
	if( ema13 > 0.525524 )
		if( ema1 <= 35.8867 )
			if( ema2 <= 33.8193 )
				if( bullPower <= 0.566494 )
					if( tema <= 18.2674 )
						if( ema1 <= 17.4072 )
							ret := -0.333333
						if( ema1 > 17.4072 )
							ret := -1.000000 // sell
					if( tema > 18.2674 )
						if( tema <= 24.1602 )
							ret := 0.733333 // buy
						if( tema > 24.1602 )
							ret := -0.195652
				if( bullPower > 0.566494 )
					if( bbp <= 1.73229 )
						if( ema3 <= 12.2047 )
							ret := 1.000000 // buy
						if( ema3 > 12.2047 )
							ret := -0.666667
					if( bbp > 1.73229 )
						if( bearPower <= 0.765407 )
							ret := 0.875000 // buy
						if( bearPower > 0.765407 )
							ret := -0.360000
			if( ema2 > 33.8193 )
				if( bbp <= 0.10684 )
					ret := 0.000000
				if( bbp > 0.10684 )
					if( bbm <= 0.190829 )
						if( ema2 <= 34.0908 )
							ret := 0.000000
						if( ema2 > 34.0908 )
							ret := -0.800000 // sell
					if( bbm > 0.190829 )
						if( tema <= 34.8353 )
							ret := -0.600000
						if( tema > 34.8353 )
							ret := -0.986842 // sell
		if( ema1 > 35.8867 )
			if( ema2 <= 48.2452 )
				if( ema3 <= 35.8652 )
					ret := 1.000000 // buy
				if( ema3 > 35.8652 )
					if( tema <= 39.6435 )
						if( ema12 <= 0.434652 )
							ret := -0.539823
						if( ema12 > 0.434652 )
							ret := 0.062500
					if( tema > 39.6435 )
						if( bbp <= 2.03377 )
							ret := 0.013661
						if( bbp > 2.03377 )
							ret := -0.430233
			if( ema2 > 48.2452 )
				if( ema13 <= 0.717747 )
					if( ema13 <= 0.652562 )
						if( ema13 <= 0.649909 )
							ret := -0.843750 // sell
						if( ema13 > 0.649909 )
							ret := 0.000000
					if( ema13 > 0.652562 )
						ret := -1.000000 // sell
				if( ema13 > 0.717747 )
					ret := 0.000000
	
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
float op_operation = decision_tree_0_NVST_30Min_48960afa(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)

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


