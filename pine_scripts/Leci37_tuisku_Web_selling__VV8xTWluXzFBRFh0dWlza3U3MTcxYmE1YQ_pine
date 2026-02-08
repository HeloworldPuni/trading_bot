//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: ADX_and_DI
// ID_model: U_1Min_1ADX_7171ba5a Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_1ADX_7171ba5a", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_7171ba5a(directionalMovementPlus, directionalMovementMinus, trueRange, smoothedDirectionalMovementPlus, smoothedDirectionalMovementMinus, diPlus, diMinus, smoothedTrueRange, adx, dx)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=7, max_features=0.65, min_samples_leaf=4,min_samples_split=5, random_state=843828734)
	if( directionalMovementMinus <= 0.016432 )
		if( diPlus <= 53.4247 )
			if( adx <= 62.8565 )
				if( directionalMovementPlus <= 0.024315 )
					if( dx <= 70.2487 )
						if( diMinus <= 53.7081 )
							if( smoothedTrueRange <= 0.061388 )
								ret := -0.037045
							if( smoothedTrueRange > 0.061388 )
								ret := 0.073007
						if( diMinus > 53.7081 )
							if( directionalMovementMinus <= 0 )
								ret := 0.045879
							if( directionalMovementMinus > 0 )
								ret := 0.210117
					if( dx > 70.2487 )
						if( smoothedDirectionalMovementPlus <= 0.010354 )
							if( diMinus <= 71.1748 )
								ret := 0.017052
							if( diMinus > 71.1748 )
								ret := 0.555556
						if( smoothedDirectionalMovementPlus > 0.010354 )
							if( adx <= 36.5767 )
								ret := 0.566964
							if( adx > 36.5767 )
								ret := 0.123037
				if( directionalMovementPlus > 0.024315 )
					if( dx <= 26.6054 )
						if( diMinus <= 37.569 )
							if( diPlus <= 39.5133 )
								ret := -0.093340
							if( diPlus > 39.5133 )
								ret := -0.307823
						if( diMinus > 37.569 )
							if( adx <= 6.89157 )
								ret := 0.777778 // buy
							if( adx > 6.89157 )
								ret := -0.416555
					if( dx > 26.6054 )
						if( smoothedTrueRange <= 0.312733 )
							if( directionalMovementPlus <= 0.144237 )
								ret := 0.013935
							if( directionalMovementPlus > 0.144237 )
								ret := -0.566038
						if( smoothedTrueRange > 0.312733 )
							ret := 1.000000 // buy
			if( adx > 62.8565 )
				if( smoothedTrueRange <= 0.107695 )
					if( smoothedDirectionalMovementMinus <= 0.028554 )
						if( diMinus <= 14.3386 )
							if( diPlus <= 51.31 )
								ret := 0.245144
							if( diPlus > 51.31 )
								ret := -0.318584
						if( diMinus > 14.3386 )
							if( adx <= 71.714 )
								ret := 0.082754
							if( adx > 71.714 )
								ret := -0.112554
					if( smoothedDirectionalMovementMinus > 0.028554 )
						if( diPlus <= 9.8217 )
							if( diMinus <= 47.6827 )
								ret := 0.327586
							if( diMinus > 47.6827 )
								ret := 0.929412 // buy
						if( diPlus > 9.8217 )
							if( diMinus <= 38.9448 )
								ret := 0.875000 // buy
							if( diMinus > 38.9448 )
								ret := -0.150000
				if( smoothedTrueRange > 0.107695 )
					if( diMinus <= 31.31 )
						if( directionalMovementPlus <= 0.011146 )
							if( dx <= 61.0013 )
								ret := -0.640000
							if( dx > 61.0013 )
								ret := 0.533333
						if( directionalMovementPlus > 0.011146 )
							if( adx <= 63.6945 )
								ret := -0.250000
							if( adx > 63.6945 )
								ret := -0.909091 // sell
					if( diMinus > 31.31 )
						if( smoothedTrueRange <= 0.169943 )
							if( smoothedTrueRange <= 0.113066 )
								ret := -0.800000 // sell
							if( smoothedTrueRange > 0.113066 )
								ret := 0.246575
						if( smoothedTrueRange > 0.169943 )
							if( directionalMovementMinus <= 9.2e-05 )
								ret := -0.600000
							if( directionalMovementMinus > 9.2e-05 )
								ret := -1.000000 // sell
		if( diPlus > 53.4247 )
			if( trueRange <= 0.020105 )
				if( smoothedTrueRange <= 0.036785 )
					if( trueRange <= 0.010003 )
						if( dx <= 60.9693 )
							if( diMinus <= 43.0707 )
								ret := -0.141739
							if( diMinus > 43.0707 )
								ret := 0.232143
						if( dx > 60.9693 )
							if( diPlus <= 81.5631 )
								ret := 0.305195
							if( diPlus > 81.5631 )
								ret := -0.171429
					if( trueRange > 0.010003 )
						if( smoothedDirectionalMovementMinus <= 0.00093 )
							if( smoothedDirectionalMovementPlus <= 0.014464 )
								ret := -0.057143
							if( smoothedDirectionalMovementPlus > 0.014464 )
								ret := 1.000000 // buy
						if( smoothedDirectionalMovementMinus > 0.00093 )
							if( directionalMovementPlus <= 0.019654 )
								ret := -0.387019
							if( directionalMovementPlus > 0.019654 )
								ret := -0.094972
				if( smoothedTrueRange > 0.036785 )
					if( diPlus <= 56.29 )
						if( smoothedDirectionalMovementPlus <= 0.024104 )
							if( directionalMovementPlus <= 0.000222 )
								ret := -0.238095
							if( directionalMovementPlus > 0.000222 )
								ret := 0.363636
						if( smoothedDirectionalMovementPlus > 0.024104 )
							if( smoothedDirectionalMovementMinus <= 0.016264 )
								ret := -0.850000 // sell
							if( smoothedDirectionalMovementMinus > 0.016264 )
								ret := -0.250000
					if( diPlus > 56.29 )
						if( dx <= 50.294 )
							if( directionalMovementPlus <= 0.009691 )
								ret := 0.704762 // buy
							if( directionalMovementPlus > 0.009691 )
								ret := 0.111111
						if( dx > 50.294 )
							if( dx <= 59.1508 )
								ret := -0.774194 // sell
							if( dx > 59.1508 )
								ret := 0.472727
			if( trueRange > 0.020105 )
				if( adx <= 25.5431 )
					if( smoothedDirectionalMovementPlus <= 0.011659 )
						if( smoothedDirectionalMovementMinus <= 0.007854 )
							if( adx <= 11.716 )
								ret := 0.000000
							if( adx > 11.716 )
								ret := -0.486239
						if( smoothedDirectionalMovementMinus > 0.007854 )
							if( smoothedDirectionalMovementMinus <= 0.007903 )
								ret := 0.750000 // buy
							if( smoothedDirectionalMovementMinus > 0.007903 )
								ret := 0.000000
					if( smoothedDirectionalMovementPlus > 0.011659 )
						if( smoothedTrueRange <= 0.026387 )
							if( diMinus <= 37.4622 )
								ret := -0.793103 // sell
							if( diMinus > 37.4622 )
								ret := -0.414634
						if( smoothedTrueRange > 0.026387 )
							if( directionalMovementPlus <= 0.024031 )
								ret := -0.197674
							if( directionalMovementPlus > 0.024031 )
								ret := -0.536530
				if( adx > 25.5431 )
					if( diPlus <= 67.8354 )
						if( diPlus <= 67.5492 )
							if( dx <= 16.2598 )
								ret := -0.836735 // sell
							if( dx > 16.2598 )
								ret := -0.054191
						if( diPlus > 67.5492 )
							if( diMinus <= 19.7371 )
								ret := 0.500000
							if( diMinus > 19.7371 )
								ret := 1.000000 // buy
					if( diPlus > 67.8354 )
						if( directionalMovementMinus <= 0.00471 )
							if( directionalMovementPlus <= 0.11826 )
								ret := -0.700000 // sell
							if( directionalMovementPlus > 0.11826 )
								ret := 0.137931
						if( directionalMovementMinus > 0.00471 )
							if( smoothedTrueRange <= 0.039982 )
								ret := 0.850000 // buy
							if( smoothedTrueRange > 0.039982 )
								ret := -0.428571
	if( directionalMovementMinus > 0.016432 )
		if( diMinus <= 50.598 )
			if( diPlus <= 31.055 )
				if( adx <= 73.9077 )
					if( smoothedDirectionalMovementMinus <= 0.010938 )
						if( diPlus <= 1.99528 )
							if( adx <= 45.5092 )
								ret := -0.052632
							if( adx > 45.5092 )
								ret := 0.804348 // buy
						if( diPlus > 1.99528 )
							if( dx <= 16.1173 )
								ret := 0.045480
							if( dx > 16.1173 )
								ret := -0.091620
					if( smoothedDirectionalMovementMinus > 0.010938 )
						if( smoothedDirectionalMovementPlus <= 0.044243 )
							if( directionalMovementMinus <= 0.068586 )
								ret := 0.077660
							if( directionalMovementMinus > 0.068586 )
								ret := 0.213348
						if( smoothedDirectionalMovementPlus > 0.044243 )
							if( adx <= 19.018 )
								ret := 0.500000
							if( adx > 19.018 )
								ret := -0.619048
				if( adx > 73.9077 )
					if( diMinus <= 32.7417 )
						if( smoothedDirectionalMovementPlus <= 0.005394 )
							if( diPlus <= 2.12055 )
								ret := -1.000000 // sell
							if( diPlus > 2.12055 )
								ret := 0.000000
						if( smoothedDirectionalMovementPlus > 0.005394 )
							if( smoothedTrueRange <= 0.029043 )
								ret := -0.250000
							if( smoothedTrueRange > 0.029043 )
								ret := -0.980392 // sell
					if( diMinus > 32.7417 )
						if( diMinus <= 38.6426 )
							if( diMinus <= 35.0642 )
								ret := 0.000000
							if( diMinus > 35.0642 )
								ret := 0.833333 // buy
						if( diMinus > 38.6426 )
							if( directionalMovementMinus <= 0.035289 )
								ret := -0.647887
							if( directionalMovementMinus > 0.035289 )
								ret := 0.051282
			if( diPlus > 31.055 )
				if( dx <= 17.5597 )
					if( dx <= 14.2855 )
						if( dx <= 7.99518 )
							if( adx <= 20.9207 )
								ret := 0.198307
							if( adx > 20.9207 )
								ret := 0.431118
						if( dx > 7.99518 )
							if( diPlus <= 37.712 )
								ret := 0.294872
							if( diPlus > 37.712 )
								ret := -0.031716
					if( dx > 14.2855 )
						if( smoothedTrueRange <= 0.064938 )
							if( smoothedTrueRange <= 0.022976 )
								ret := 0.243902
							if( smoothedTrueRange > 0.022976 )
								ret := 0.620690
						if( smoothedTrueRange > 0.064938 )
							if( trueRange <= 0.116298 )
								ret := -0.750000 // sell
							if( trueRange > 0.116298 )
								ret := 0.500000
				if( dx > 17.5597 )
					if( dx <= 29.9686 )
						if( directionalMovementMinus <= 0.025925 )
							if( trueRange <= 0.060003 )
								ret := -0.104712
							if( trueRange > 0.060003 )
								ret := -0.696429
						if( directionalMovementMinus > 0.025925 )
							if( adx <= 31.2708 )
								ret := -0.057229
							if( adx > 31.2708 )
								ret := 0.275862
					if( dx > 29.9686 )
						if( diMinus <= 27.2143 )
							if( adx <= 55.8676 )
								ret := 0.045118
							if( adx > 55.8676 )
								ret := 0.291221
						if( diMinus > 27.2143 )
							if( smoothedDirectionalMovementMinus <= 0.008605 )
								ret := 0.288462
							if( smoothedDirectionalMovementMinus > 0.008605 )
								ret := 0.850575 // buy
		if( diMinus > 50.598 )
			if( dx <= 18.4087 )
				if( trueRange <= 0.041037 )
					if( adx <= 41.0516 )
						if( diMinus <= 52.3212 )
							if( adx <= 11.559 )
								ret := -0.500000
							if( adx > 11.559 )
								ret := 0.404762
						if( diMinus > 52.3212 )
							if( smoothedTrueRange <= 0.018764 )
								ret := 0.252747
							if( smoothedTrueRange > 0.018764 )
								ret := 0.798561 // buy
					if( adx > 41.0516 )
						ret := -0.625000
				if( trueRange > 0.041037 )
					if( adx <= 40.8964 )
						if( diMinus <= 53.1856 )
							if( directionalMovementPlus <= 0.003561 )
								ret := 0.745098 // buy
							if( directionalMovementPlus > 0.003561 )
								ret := 0.000000
						if( diMinus > 53.1856 )
							if( smoothedTrueRange <= 0.047425 )
								ret := 0.943089 // buy
							if( smoothedTrueRange > 0.047425 )
								ret := 0.625000
					if( adx > 40.8964 )
						if( smoothedDirectionalMovementPlus <= 0.010494 )
							ret := -1.000000 // sell
						if( smoothedDirectionalMovementPlus > 0.010494 )
							ret := 0.700000 // buy
			if( dx > 18.4087 )
				if( smoothedDirectionalMovementMinus <= 0.018157 )
					if( dx <= 99.8931 )
						if( directionalMovementMinus <= 0.020566 )
							if( adx <= 16.7438 )
								ret := -0.237288
							if( adx > 16.7438 )
								ret := 0.315534
						if( directionalMovementMinus > 0.020566 )
							if( smoothedDirectionalMovementPlus <= 0.001397 )
								ret := 0.101266
							if( smoothedDirectionalMovementPlus > 0.001397 )
								ret := 0.496422
					if( dx > 99.8931 )
						if( smoothedDirectionalMovementMinus <= 0.015174 )
							if( adx <= 58.9928 )
								ret := -0.833333 // sell
							if( adx > 58.9928 )
								ret := -1.000000 // sell
						if( smoothedDirectionalMovementMinus > 0.015174 )
							ret := 0.625000
				if( smoothedDirectionalMovementMinus > 0.018157 )
					if( diPlus <= 8.17902 )
						if( smoothedDirectionalMovementPlus <= 0.002579 )
							if( directionalMovementMinus <= 0.036842 )
								ret := -0.168539
							if( directionalMovementMinus > 0.036842 )
								ret := 0.277027
						if( smoothedDirectionalMovementPlus > 0.002579 )
							if( trueRange <= 0.139162 )
								ret := 0.887218 // buy
							if( trueRange > 0.139162 )
								ret := 0.038462
					if( diPlus > 8.17902 )
						if( adx <= 24.6071 )
							if( diPlus <= 26.2154 )
								ret := 0.532934
							if( diPlus > 26.2154 )
								ret := 0.189427
						if( adx > 24.6071 )
							if( adx <= 27.4633 )
								ret := -0.534091
							if( adx > 27.4633 )
								ret := 0.057052
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator ADX_and_DI 
//@version=5
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © BeikabuOyaji

//indicator "ADX and DI for v5", overlay=false)

// Input parameters
len = input(14, title="Length")
th = input(20, title="Threshold")

// Calculate True Range
trueRange = math.max(math.max(high - low, math.abs(high - nz(close[1]))), math.abs(low - nz(close[1])))

// Calculate Directional Movements
directionalMovementPlus = high - nz(high[1]) > nz(low[1]) - low ? math.max(high - nz(high[1]), 0) : 0
directionalMovementMinus = nz(low[1]) - low > high - nz(high[1]) ? math.max(nz(low[1]) - low, 0) : 0

// Initialize and calculate smoothed values
var float smoothedTrueRange = 0
var float smoothedDirectionalMovementPlus = 0
var float smoothedDirectionalMovementMinus = 0

smoothedTrueRange := nz(smoothedTrueRange[1]) - (nz(smoothedTrueRange[1]) / len) + trueRange
smoothedDirectionalMovementPlus := nz(smoothedDirectionalMovementPlus[1]) - (nz(smoothedDirectionalMovementPlus[1]) / len) + directionalMovementPlus
smoothedDirectionalMovementMinus := nz(smoothedDirectionalMovementMinus[1]) - (nz(smoothedDirectionalMovementMinus[1]) / len) + directionalMovementMinus

// Calculate DI+ and DI-
diPlus = (smoothedDirectionalMovementPlus / smoothedTrueRange) * 100
diMinus = (smoothedDirectionalMovementMinus / smoothedTrueRange) * 100

// Calculate DX and ADX
dx = math.abs(diPlus - diMinus) / (diPlus + diMinus) * 100
adx = ta.sma(dx, len)

// Plot DI+, DI-, and ADX
plot(diPlus, color=color.green, title="DI+")
plot(diMinus, color=color.red, title="DI-")
plot(adx, color=color.navy, title="ADX")

// Plot threshold line
hline(th, "Threshold", color=color.black)

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
float op_operation = decision_tree_0_U_1Min_7171ba5a(directionalMovementPlus, directionalMovementMinus, trueRange, smoothedDirectionalMovementPlus, smoothedDirectionalMovementMinus, diPlus, diMinus, smoothedTrueRange, adx, dx)

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


