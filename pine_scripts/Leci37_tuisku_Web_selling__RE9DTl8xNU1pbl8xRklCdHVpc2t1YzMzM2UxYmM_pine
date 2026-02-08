//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Fibonacci_Bollinger
// ID_model: DOCN_15Min_1FIB_c333e1bc Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOCN_15Min_1FIB_c333e1bc", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOCN_15Min_c333e1bc(upper_2, basis, lower_6, basis_minus, lower_5, upper_5, upper_4, basis_max, upper_6, upper_3, lower_2, upper_1, lower_4, lower_1, lower_3)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( upper_2 <= 32.1408 )
		if( upper_6 <= 32.2569 )
			if( upper_2 <= 29.9248 )
				if( lower_3 <= 27.3722 )
					if( lower_3 <= 19.9771 )
						if( lower_3 <= 19.1152 )
							ret := -0.056604
						if( lower_3 > 19.1152 )
							ret := 0.608491
					if( lower_3 > 19.9771 )
						if( lower_3 <= 23.1471 )
							ret := -0.148987
						if( lower_3 > 23.1471 )
							ret := 0.091074
				if( lower_3 > 27.3722 )
					if( upper_3 <= 30.0643 )
						if( upper_4 <= 29.5787 )
							ret := 0.000000
						if( upper_4 > 29.5787 )
							ret := 0.891089 // buy
					if( upper_3 > 30.0643 )
						if( upper_1 <= 29.604 )
							ret := 0.000000
						if( upper_1 > 29.604 )
							ret := 0.500000
			if( upper_2 > 29.9248 )
				if( basis_max <= -3.01745 )
					if( upper_4 <= 31.0247 )
						ret := 0.555556
					if( upper_4 > 31.0247 )
						ret := 1.000000 // buy
				if( basis_max > -3.01745 )
					if( lower_3 <= 29.7521 )
						if( upper_1 <= 29.9286 )
							ret := -0.380074
						if( upper_1 > 29.9286 )
							ret := -0.844444 // sell
					if( lower_3 > 29.7521 )
						if( upper_5 <= 31.6688 )
							ret := -0.056338
						if( upper_5 > 31.6688 )
							ret := 0.419355
		if( upper_6 > 32.2569 )
			if( lower_2 <= 27.5777 )
				if( lower_3 <= 26.8832 )
					if( lower_5 <= 25.0761 )
						if( lower_1 <= 27.4008 )
							ret := 1.000000 // buy
						if( lower_1 > 27.4008 )
							ret := -0.073604
					if( lower_5 > 25.0761 )
						if( lower_4 <= 26.1644 )
							ret := 0.682759
						if( lower_4 > 26.1644 )
							ret := -0.045455
				if( lower_3 > 26.8832 )
					if( upper_2 <= 30.4159 )
						if( basis_minus <= 3.69 )
							ret := 0.500000
						if( basis_minus > 3.69 )
							ret := -0.942308 // sell
					if( upper_2 > 30.4159 )
						if( upper_1 <= 30.3657 )
							ret := -0.047619
						if( upper_1 > 30.3657 )
							ret := -0.941176 // sell
			if( lower_2 > 27.5777 )
				if( upper_1 <= 31.8354 )
					if( lower_2 <= 27.7134 )
						if( basis <= 29.0461 )
							ret := 0.375000
						if( basis > 29.0461 )
							ret := 0.871429 // buy
					if( lower_2 > 27.7134 )
						if( lower_2 <= 28.356 )
							ret := 0.125000
						if( lower_2 > 28.356 )
							ret := 0.602500
				if( upper_1 > 31.8354 )
					if( upper_4 <= 32.5966 )
						ret := 0.214286
					if( upper_4 > 32.5966 )
						ret := -1.000000 // sell
	if( upper_2 > 32.1408 )
		if( basis <= 31.7711 )
			if( lower_3 <= 27.2603 )
				if( lower_1 <= 28.3589 )
					if( lower_5 <= 24.7883 )
						if( basis_max <= -6.81829 )
							ret := -0.625000
						if( basis_max > -6.81829 )
							ret := 0.285714
					if( lower_5 > 24.7883 )
						if( basis_minus <= 6.55655 )
							ret := -1.000000 // sell
						if( basis_minus > 6.55655 )
							ret := -0.666667
				if( lower_1 > 28.3589 )
					if( lower_5 <= 24.9142 )
						if( lower_4 <= 25.8541 )
							ret := 1.000000 // buy
						if( lower_4 > 25.8541 )
							ret := 0.562500
					if( lower_5 > 24.9142 )
						if( upper_3 <= 33.167 )
							ret := 1.000000 // buy
						if( upper_3 > 33.167 )
							ret := -0.134615
			if( lower_3 > 27.2603 )
				if( basis_minus <= 5.65399 )
					if( lower_2 <= 29.3178 )
						if( basis_max <= -5.4539 )
							ret := -0.206897
						if( basis_max > -5.4539 )
							ret := 0.369369
					if( lower_2 > 29.3178 )
						if( basis_minus <= 1.99421 )
							ret := 0.625000
						if( basis_minus > 1.99421 )
							ret := -0.473815
				if( basis_minus > 5.65399 )
					if( basis_minus <= 7.95635 )
						if( lower_2 <= 28.6068 )
							ret := -0.805882 // sell
						if( lower_2 > 28.6068 )
							ret := -0.472973
					if( basis_minus > 7.95635 )
						if( upper_4 <= 36.4516 )
							ret := 0.457143
						if( upper_4 > 36.4516 )
							ret := -0.857143 // sell
		if( basis > 31.7711 )
			if( lower_2 <= 31.2849 )
				if( upper_2 <= 35.5874 )
					if( basis <= 32.1747 )
						if( basis_max <= -2.78164 )
							ret := 0.210526
						if( basis_max > -2.78164 )
							ret := -0.557377
					if( basis > 32.1747 )
						if( lower_2 <= 31.1041 )
							ret := 0.397849
						if( lower_2 > 31.1041 )
							ret := 0.728972 // buy
				if( upper_2 > 35.5874 )
					if( lower_3 <= 30.4118 )
						if( lower_6 <= 25.9862 )
							ret := -0.190476
						if( lower_6 > 25.9862 )
							ret := 0.454545
					if( lower_3 > 30.4118 )
						if( upper_3 <= 36.2776 )
							ret := 0.333333
						if( upper_3 > 36.2776 )
							ret := -0.857143 // sell
			if( lower_2 > 31.2849 )
				if( lower_2 <= 31.5265 )
					if( lower_1 <= 31.6406 )
						if( upper_4 <= 33.5946 )
							ret := -0.692308
						if( upper_4 > 33.5946 )
							ret := 0.960000 // buy
					if( lower_1 > 31.6406 )
						if( upper_1 <= 33.3503 )
							ret := -0.804878 // sell
						if( upper_1 > 33.3503 )
							ret := -0.267148
				if( lower_2 > 31.5265 )
					if( upper_1 <= 32.4876 )
						ret := 1.000000 // buy
					if( upper_1 > 32.4876 )
						if( upper_6 <= 152.638 )
							ret := -0.020076
						if( upper_6 > 152.638 )
							ret := 0.620690
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Fibonacci_Bollinger 
//@version=5
//indicator shorttitle="FBB", title="Fibonacci Bollinger Bands", overlay=true)

// Inputs
length_FiboBB = input.int(200, minval=1)
src = input(hlc3, title="Source")
mult = input.float(3.0, minval=0.001, maxval=50)

// Calculations
basis = ta.vwma(src, length_FiboBB)
dev = mult * ta.stdev(src, length_FiboBB)

// Upper Bands
upper_1 = basis + (0.236 * dev)
upper_2 = basis + (0.382 * dev)
upper_3 = basis + (0.5 * dev)
upper_4 = basis + (0.618 * dev)
upper_5 = basis + (0.764 * dev)
upper_6 = basis + (1 * dev)

// Lower Bands
lower_1 = basis - (0.236 * dev)
lower_2 = basis - (0.382 * dev)
lower_3 = basis - (0.5 * dev)
lower_4 = basis - (0.618 * dev)
lower_5 = basis - (0.764 * dev)
lower_6 = basis - (1 * dev)

basis_minus = basis -lower_6
basis_max = basis -upper_6

// Plotting
plot(basis, color=color.fuchsia, linewidth=2)
plot(upper_1, color=color.white, linewidth=1, title="0.236")
plot(upper_2, color=color.white, linewidth=1, title="0.382")
plot(upper_3, color=color.white, linewidth=1, title="0.5")
plot(upper_4, color=color.white, linewidth=1, title="0.618")
plot(upper_5, color=color.white, linewidth=1, title="0.764")
plot(upper_6, color=color.red, linewidth=2, title="1")
plot(lower_1, color=color.white, linewidth=1, title="0.236")
plot(lower_2, color=color.white, linewidth=1, title="0.382")
plot(lower_3, color=color.white, linewidth=1, title="0.5")
plot(lower_4, color=color.white, linewidth=1, title="0.618")
plot(lower_5, color=color.white, linewidth=1, title="0.764")
plot(lower_6, color=color.green, linewidth=2, title="1")

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
float op_operation = decision_tree_0_DOCN_15Min_c333e1bc(upper_2, basis, lower_6, basis_minus, lower_5, upper_5, upper_4, basis_max, upper_6, upper_3, lower_2, upper_1, lower_4, lower_1, lower_3)

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


